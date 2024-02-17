import os
import time
from inspect import isclass
from typing import Any, Callable, Optional, Union
from warnings import warn

import arrow
from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated, get_args, get_origin

FORBID_EXTRA_RESULT_FIELDS = os.environ.get("RHINO_SDK_FORBID_EXTRA_RESULT_FIELDS", "").lower() in {
    "1",
    "on",
    "true",
}

RESULT_DATACLASS_EXTRA = "forbid" if FORBID_EXTRA_RESULT_FIELDS else "ignore"


class AliasResponse:
    """
    @autoapi False
    Placeholder interface for a raw_response to ensure backwards compatibility if a user uses unsupported internal methods
    """

    def __init__(self, dataclass):
        self.dataclass = dataclass

    @property
    def content(self):
        raise NotImplementedError  # TODO: No good way of handling this

    @property
    def status_code(self):
        return 200  # TODO: Placeholder

    def json(self):
        return self.dataclass.model_dump_json()

    def text(self):
        return self.json()


class RhinoBaseModel(BaseModel):
    session: Annotated[Any, Field(exclude=True)] = None
    _persisted: bool = False

    def __init__(self, **data):
        self._handle_aliases(data)
        self._handle_uids(data)
        self._handle_models(data)
        self._handle_hidden(data)
        super().__init__(**data)

    def __str__(self):
        return f"{self.__class__.__name__} {super(RhinoBaseModel, self).__str__()}"

    model_config = ConfigDict(extra=RESULT_DATACLASS_EXTRA)

    def dict(self, *args, **kwargs):
        """
        Return a dictionary representation of the data class.
        See https://docs.pydantic.dev/latest/concepts/serialization/#modelmodel_dump for available arguments
        """
        return self.model_dump(*args, **kwargs)

    def to_dict(self, *args, **kwargs):
        """
        @autoapi False

        In the event users are used to pandas
        """
        return self.dict(*args, **kwargs)

    def json(self, *args, **kwargs):
        """
        @autoapi False

        Pydantic is deprecating the name but the old name is much clearer
        """
        # TODO: Need to reverse the uids
        return self.model_dump_json(*args, **kwargs)

    def _handle_uids(self, data):
        """
        Remap backend uid results to uid parameter
        """

        for field_name, field_attr in self.model_fields.items():
            if data.get(field_name, None) is not None:  # User passed in or already converted
                continue
            # TODO: Change existing annotations to be explicit instead of implicit so we can check on the type declaration instead of it
            # being name based
            if field_name != field_attr.alias:
                old_key = field_attr.alias
            elif field_name.endswith("_uids"):
                old_key = field_name[:-5]
            elif field_name.endswith("_uid"):
                old_key = field_name[:-4]
            else:
                continue
            value = data.get(old_key, None)
            # Check for V2 UID And Name
            if isinstance(value, list) and len(value) and isinstance(value[0], dict):
                data[field_name] = [uid_and_name["uid"] for uid_and_name in value]
                if field_name != field_attr.alias:
                    data[field_attr.alias] = data[field_name]
                    if RESULT_DATACLASS_EXTRA == "forbid":
                        data.pop(field_name, None)
            elif isinstance(value, dict):
                data[field_name] = value["uid"]
                if field_name != field_attr.alias:
                    data[field_attr.alias] = data[field_name]
                    if RESULT_DATACLASS_EXTRA == "forbid":
                        data.pop(field_name, None)
            elif value is not None:
                if RESULT_DATACLASS_EXTRA == "forbid" and field_attr.alias != field_name:
                    # Under Strict CI Mode in Pydantic V2 need to assign to alias
                    data[field_attr.alias] = value
                    data.pop(field_name, None)
                else:
                    data[field_name] = value

    def _handle_models(self, data):
        """
        Add the session variable to any child models
        """
        # TODO Replace the detection of this to use UIDField or something of that nature.
        session = getattr(self, "session", data.get("session"))
        for field, field_attr in self.model_fields.items():
            field_type = field_attr.annotation
            # With type annotations there can be many wrapping types and there's
            # no convenience get_actual_base_class function so we need
            # to get the actual base class
            field_types = []
            pending_evaluation = [field_type]
            while pending_evaluation:
                _current_field_type = pending_evaluation.pop()
                origin = get_origin(_current_field_type)
                if origin == Union:
                    pending_evaluation.extend(get_args(_current_field_type))
                elif origin == list:
                    pending_evaluation.append(get_args(_current_field_type)[0])
                else:
                    field_types.append(_current_field_type)
            for _field_type in field_types:
                if isclass(_field_type) and issubclass(_field_type, RhinoBaseModel):
                    value = data.get(field, None)
                    if isinstance(value, list):
                        for entry in value:
                            if isinstance(entry, dict):
                                entry["session"] = session
                        break
                    elif isinstance(value, dict):
                        data[field]["session"] = session
                        break

    def _handle_aliases(self, data):
        for field_name, field_attr in self.model_fields.items():
            if field_attr.alias is not None and field_name != field_attr.alias:
                if field_name in data:
                    data[field_attr.alias] = data.get(field_name, None)
                if RESULT_DATACLASS_EXTRA == "forbid":
                    # Need to remove unaliased kwarg due to pydantic
                    data.pop(field_name, None)

    def _handle_hidden(self, data):
        """
        Remove any explicitly hidden fields from the constructor of the pydantic model
        in order to not fail the Extra forbidden check.
        """
        for field_name in getattr(self.__class__, "__hidden__", []):
            if field_name in data:
                data.pop(field_name, None)

    def raw_response(self):
        warn(
            f"The SDK method you called now returns a {self.__class__.__name__} dataclass. Please update your code to use the dataclass instead. You can directly access fields on the return result, or call .dict() for a similar interface"
        )
        return AliasResponse(self)

    def _wait_for_completion(
        self,
        name: str,
        is_complete: bool,
        query_function: Callable,
        validation_function: Callable,
        timeout_seconds: int = 500,
        poll_frequency: int = 10,
        print_progress: bool = True,
        is_successful: Callable = lambda result: True,
        on_success: Callable = lambda result: print("Done"),
        on_failure: Callable = lambda result: print("Finished with errors"),
    ):
        """
        @autoapi False

        Reusable code for waiting for pending operations to complete
        :param name: Name of the operation
        :param is_complete: Whether or not the object has finished
        :param query_function: lamnda(self) -> dataclass What SDK function to call to check
        :param validation_function: lambda(old_object, new_object) -> bool whether to break checking
        :param timeout_seconds: Timeout in total seconds
        :param poll_frequency: Frequency to poll
        :param print_progress: Show progress to users
        :param is_successful: lambda(result) -> bool Whether the operation was successful
        :param on_success: lambda(result) -> None What to do on success
        :param on_failure: lambda(result) -> None What to do on failure
        :return: dataclass
        """
        if is_complete:
            return self
        start_time = arrow.utcnow()
        timeout_time = start_time.shift(seconds=timeout_seconds)
        while arrow.utcnow() < timeout_time:
            try:
                new_result = query_function(self)
                if validation_function(self, new_result):
                    if is_successful(new_result):
                        on_success(new_result)
                    else:
                        on_failure(new_result)
                    return new_result
            except Exception as e:
                raise Exception(f"Exception in wait_for_completion() calling get_status(): {e}")
            if print_progress:
                time_eclipsed = arrow.utcnow().humanize(
                    start_time, granularity=["hour", "minute", "second"], only_distance=True
                )
                print(f"Waiting for {name} to complete ({time_eclipsed})")
            if poll_frequency:
                time.sleep(poll_frequency)
        raise Exception(f"Timeout waiting for {name} to complete")

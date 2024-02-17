import json
import logging
from abc import ABC
from collections import OrderedDict
from enum import Enum
from typing import Any, Dict, List, Optional, Union
from warnings import warn

from pydantic import BaseModel

from rhino_health.lib.metrics.filter_variable import (
    FilterBetweenRange,
    FilterType,
    FilterVariableTypeOrColumnName,
)


class DataFilter(BaseModel):
    """
    A filter to be applied on the entire Dataset
    """

    filter_column: str
    """The column in the remote dataset df to check against"""
    filter_value: Union[Any, FilterBetweenRange]
    """The value to match against or a FilterBetweenRange if filter_type is FilterType.BETWEEN"""
    filter_type: Optional[FilterType] = FilterType.EQUAL
    """The type of filtering to perform. Defaults to FilterType.EQUAL"""
    filter_dataset: Optional[str] = None
    """The dataset to perform the filter on if there are multiple datasets for Federated Join. If unspecified will be all datasets"""


class GroupingData(BaseModel):
    """
    Configuration for grouping metric results

    See Also
    --------
    pandas.groupby : Implementation used for grouping. `See documentation <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html>`_
    """

    groupings: List[str] = []
    """
    A list of columns to group metric results by
    """
    dropna: Optional[bool] = True
    """
    Should na values be dropped if in a grouping key
    """


MetricResultDataType = Dict[str, Any]
"""
Dict[str, Any]
"""


class MetricResponse(BaseModel):
    """
    Standardized response from querying metrics against a Dataset
    """

    output: MetricResultDataType  # if group_by is specified in the arguments, is a map of group: output
    metric_configuration_dict: Optional[Dict[str, Any]] = None

    def __init__(self, **data):
        status = data.get("status", None)
        if status == "error":
            data["output"] = {"error": data["data"]}
        else:
            if isinstance(data["output"], str):
                data["output"] = json.loads(data["output"])
            if list(data["output"].keys()) == ["null"]:
                data["output"] = data["output"]["null"]
        if "metric_configuration_dict" not in data:
            data["metric_configuration_dict"] = None
        super(MetricResponse, self).__init__(**data)


class KaplanMeierMetricResponse(MetricResponse):
    time_variable: str
    event_variable: str

    def __init__(self, **data):
        arguments = json.loads(data["metric_configuration_dict"]["arguments"])
        data["time_variable"] = arguments["time_variable"]
        data["event_variable"] = arguments["event_variable"]
        super().__init__(**data)

    def surv_func_right_model(self, group=None):
        """
        Creates a survival function model for the metric response
        """
        try:
            import statsmodels.api as sm
        except ImportError:
            raise ImportError(
                "Package statsmodels is not installed. Use the survival and time vectors in KaplanMeierMetricResponse.output "
                "to manually create a survival function model using statsmodels.SurvFuncRight."
            )
        events_vector = self.output[group] if group else self.output
        return sm.SurvfuncRight(
            events_vector[self.time_variable], events_vector[self.event_variable]
        )


class TwoByTwoTableMetricResponse(MetricResponse):
    def as_table(self):
        """
        Display the 2X2 table metric response as a dict representing a table. Use pd.DataFrame(as_table_result)
        to visualize the table.
        The data provided should represent a 2X2 table meaning the
        dict is of length 4, the keys should be tuples of length 2 representing the possible combination of values.
        The "detected" values are the columns and the "exposed" values are the rows.
        If the data is boolean, the table order is (true, false) for both columns and rows.
        If not, the order is alphabetical.
        """
        table_data = self.output.get("two_by_two_table")
        if not table_data:
            # As grouped two by two tables are a less common use case, and as it results in an unkNown number of tables,
            # we do not support the multiple tables output - the user can manually access the output and
            # create the desired table.
            raise ValueError(
                "Can not visualize table for grouped results. To solve this, "
                "remove the group_by argument from the metric configuration or manually access "
                "MetricResponse.output for retrieving the table data."
            )
        if not any(
            isinstance(key, str) and isinstance(value, (int, dict))
            for key, value in table_data.items()
        ):
            raise ValueError("MetricResponse is not representing a table")

        table_as_dict = TwoByTwoTableMetricResponse.get_ordered_dict_table(table_data)

        return table_as_dict

    @staticmethod
    def get_ordered_dict_table(table_data: dict):
        """
        Returns the table data as an ordered dict representing a table.
        The data provided should represent a 2X2 table meaning the
        dict is of length 4, the keys should be tuples of length 2 representing the possible combination of values.
        The "detected" values are the columns and the "exposed" values are the rows.
        If the data is boolean, the table order is (true, false) for both columns and rows.
        If not, the order is alphabetical.
        """

        def get_table_headers_from_data():
            col_values, row_values = set(), set()
            for key in table_data:
                col_value, row_value = eval(key)
                col_values.add(col_value)
                row_values.add(row_value)

            return sorted(col_values, reverse=all(isinstance(v, bool) for v in col_values)), sorted(
                row_values, reverse=all(isinstance(v, bool) for v in row_values)
            )

        col_headers, row_headers = get_table_headers_from_data()
        table_as_dict: OrderedDict = OrderedDict(
            [(str(col), OrderedDict({str(row): 0 for row in row_headers})) for col in col_headers]
        )

        for key, value in table_data.items():
            col_value, row_value = eval(key)
            table_as_dict[str(col_value)][str(row_value)] = value.get("count")

        return table_as_dict


class BaseMetric(BaseModel):
    """
    Parameters available for every metric
    """

    data_filters: Optional[List[DataFilter]] = []  # We will filter in the order passed in
    group_by: Optional[GroupingData] = None
    timeout_seconds: Optional[
        float
    ] = 600.0  # Metric calculations that take longer than this time will timeout
    count_variable_name: str = "variable"

    @classmethod
    def metric_name(cls):
        """
        @autoapi False
        Each metric should define this so the backend cloud knows how to handle things.
        """
        raise NotImplementedError

    def data(self):
        data = {
            "metric": self.metric_name(),
            "arguments": self.json(exclude_none=True, exclude={"timeout_seconds"}),
        }
        if self.timeout_seconds is not None:
            data["timeout_seconds"] = self.timeout_seconds
        return data

    @property
    def metric_response(self):
        return MetricResponse


class AggregatableMetric(BaseMetric, ABC):
    """
    @autoapi False
    """

    @property
    def supports_custom_aggregation(self):
        """
        @autoapi False
        """
        return True


class JoinMode(str, Enum):
    """
    @autoapi True
    """

    INTERSECTION = "intersection"
    """
    @autoapi True Return values where the indentifiers are found in both the filter and query datasets.
    """
    UNION = "union"
    """
    @autoapi True Returns values where rows with the same identifiers are deduplicated.
    """


class JoinableMetric(AggregatableMetric, ABC):
    """
    @autoapi False
    """

    join_mode: Optional[JoinMode] = None
    """
    @autoapi True The mode to perform an optional Federated Join in. Defaults to intersection if join_field, query_datasets, or filter_datasets are defined
    """
    join_field: Optional[FilterVariableTypeOrColumnName] = None
    """
    @autoapi True A field to perform a join on if performing a Federated Join. This filter_variable will be performed on the filter_dataset(s)
    """
    query_datasets: Optional[List[str]] = None
    """
    @autoapi False A list of Datasets to get data from. Used for Federated Join. Currently only supports 1 dataset for Intersection Mode. Supports any number of datasets for Union mode. The order of datasets determines the selection order in Intersection mode. Data from earlier datasets has will be used over later datasets.
    """
    filter_datasets: Optional[List[str]] = None
    """
    @autoapi False A list of datasets to perform the join filter logic against. Used for Federated Join Intersection. Currently only supports 1 dataset.
    """

    def __init__(self, **data):
        # Handle optional join_mode fields based on user input
        join_field = data.get("join_field")
        query_datasets = data.get("query_datasets")
        filter_datasets = data.get("filter_datasets")
        join_mode = data.get("join_mode")
        if any([x is not None for x in [join_field, query_datasets, filter_datasets, join_mode]]):
            # Cannot do the following check with the desired interface alias
            # if not query_datasets:
            #     raise ValueError("data_datasets cannot be empty for a Federated Join. Either remove all Join fields or provide a dataset UID")
            # if not filter_datasets:
            #     raise ValueError("filter_datasets cannot be empty for a Federated Join. Either remove all Join fields or provide a dataset UID")
            if not join_field:
                raise ValueError(
                    "The join_field cannot be empty when attempting a Federated Join. Either remove all Join fields or provide a join field"
                )
            if not join_mode:
                data["join_mode"] = JoinMode.INTERSECTION
        super().__init__(**data)

import json
from itertools import chain
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional

from funcy import compact

if TYPE_CHECKING:
    from rhino_health.lib.rhino_session import RhinoSession

from rhino_health.lib.metrics.base_metric import BaseMetric, MetricResponse


def get_cloud_aggregated_metric_data(
    session: "RhinoSession",
    dataset_uids: List[str],
    metric_configuration: BaseMetric,
    aggregation_method_override: Optional[Callable] = None,
) -> MetricResponse:
    metric_configuration_dict = metric_configuration.data()
    timeout_seconds = metric_configuration_dict.pop("timeout_seconds", None)
    override_aggregation_method = True if aggregation_method_override else False
    metric_response = session.post(
        f"/projects/calculate_aggregate_metric/",
        data={
            "dataset_uids": dataset_uids,
            "metric_configuration": json.dumps(metric_configuration_dict),
            "timeout_seconds": timeout_seconds,
            "override_aggregation_method": override_aggregation_method,
        },
    )
    parsed_response = metric_response.raw_response.json()
    response_status = parsed_response.pop("status")
    response_data = parsed_response.pop("data", None)
    response_output = parsed_response.pop("output", None)

    if override_aggregation_method:
        response_output = custom_metric_aggregator(
            metric_configuration.metric_name(),
            response_output,
            aggregation_method_override,
            metric_configuration.group_by,
            metric_configuration.count_variable_name,
        )

    if parsed_response:
        raise ValueError(f"Unexpected fields in response: {', '.join(parsed_response.keys())}")
    return metric_configuration.metric_response(
        status=response_status,
        data=response_data,
        output=response_output,
        metric_configuration_dict=metric_configuration_dict,
    )


def custom_metric_aggregator(
    metric_name: str,
    metric_results: List[Dict[str, Any]],
    aggregation_method: Callable,
    group_by: Optional[str] = None,
    count_variable: str = "variable",
) -> Dict[str, Any]:
    """
    Aggregates the results from the individual datasets into one.
    """
    if group_by is None:
        return aggregation_method(metric_name, metric_results, count_variable=count_variable)
    else:
        groups = set(chain.from_iterable(metric_result.keys() for metric_result in metric_results))
        grouped_results = {}
        for group in groups:
            group_result = compact(
                [metric_result.get(group, None) for metric_result in metric_results]
            )
            grouped_results[group] = aggregation_method(
                metric_name, group_result, count_variable=count_variable
            )
        return grouped_results

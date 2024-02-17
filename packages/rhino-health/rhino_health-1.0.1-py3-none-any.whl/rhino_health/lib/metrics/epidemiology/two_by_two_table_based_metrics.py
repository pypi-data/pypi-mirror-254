from abc import ABC

from rhino_health.lib.metrics.base_metric import (
    AggregatableMetric,
    BaseMetric,
    TwoByTwoTableMetricResponse,
)
from rhino_health.lib.metrics.filter_variable import FilterVariableTypeOrColumnName


class TwoByTwoTableBasedMetric(AggregatableMetric, ABC):
    """
    Abstract class for metrics that are based on a two by two table
    """

    variable: FilterVariableTypeOrColumnName
    detected_column_name: FilterVariableTypeOrColumnName
    exposed_column_name: FilterVariableTypeOrColumnName

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.group_by:
            if (
                self.detected_column_name in self.group_by.groupings
                or self.exposed_column_name in self.group_by.groupings
            ):
                raise ValueError("Can not group by detected_column_name or exposed_column_name")

    @property
    def supports_custom_aggregation(self):
        """
        @autoapi False
        """
        return False


class TwoByTwoTable(TwoByTwoTableBasedMetric):
    """
    Returns the two by two table of entries for a specified VARIABLE
    """

    @classmethod
    def metric_name(cls):
        return "two_by_two_table"

    @property
    def metric_response(self):
        """
        Returns the response class for the metric
        """
        return TwoByTwoTableMetricResponse


class OddsRatio(TwoByTwoTableBasedMetric):
    """
    Returns the odds ratio of entries for a specified VARIABLE
    """

    @classmethod
    def metric_name(cls):
        return "odds_ratio"


class Odds(AggregatableMetric):
    """
    Returns the odds of entries for a specified VARIABLE where the odd is calculated by the ratio of the number of true
     occurrences to the number of false occurrences.
    """

    variable: FilterVariableTypeOrColumnName
    column_name: FilterVariableTypeOrColumnName

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def metric_name(cls):
        return "odds"

    @property
    def supports_custom_aggregation(self):
        """
        @autoapi False
        """
        return False


class Risk(TwoByTwoTableBasedMetric):
    """
    Returns the risk of entries for a specified VARIABLE
    """

    @classmethod
    def metric_name(cls):
        return "risk"


class RiskRatio(TwoByTwoTableBasedMetric):
    """
    Returns the risk ratio of entries for a specified VARIABLE
    """

    @classmethod
    def metric_name(cls):
        return "risk_ratio"

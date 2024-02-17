from rhino_health.lib.metrics.base_metric import (
    AggregatableMetric,
    BaseMetric,
    KaplanMeierMetricResponse,
)
from rhino_health.lib.metrics.filter_variable import FilterVariableTypeOrColumnName


class ChiSquare(AggregatableMetric):
    """
    A metric that calculates the Chi-Square test for multiple Datasets.
    """

    variable: FilterVariableTypeOrColumnName
    variable_1: FilterVariableTypeOrColumnName  # TODO: better names
    variable_2: FilterVariableTypeOrColumnName

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.group_by:
            if (
                self.variable_1 in self.group_by.groupings
                or self.variable_2 in self.group_by.groupings
            ):
                raise ValueError(
                    "Can not group by the given metric variables (variable_1, variable_2)"
                )

    @classmethod
    def metric_name(cls):
        return "chi_square"

    @property
    def supports_custom_aggregation(self):
        return False


class TTest(AggregatableMetric):
    """
    A metric that calculates the T test for multiple Datasets.
    The methods used is the Welch's t-test (equal or unequal sample sizes, unequal variances).
    """

    numeric_variable: FilterVariableTypeOrColumnName
    categorical_variable: FilterVariableTypeOrColumnName  # TODO: better names

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.group_by:
            if (
                self.numeric_variable in self.group_by.groupings
                or self.categorical_variable in self.group_by.groupings
            ):
                raise ValueError(
                    "Can not group by the given metric variables (numeric_variable, categorical_variable)"
                )

    @classmethod
    def metric_name(cls):
        return "t_test"

    @property
    def supports_custom_aggregation(self):
        return False


class OneWayANOVA(AggregatableMetric):
    """
    A metric that calculates the T test for multiple Datasets.
    If the numeric variable data column has nans, they will be ignored.
    """

    variable: FilterVariableTypeOrColumnName  # Used as an identifier for the count calculation
    numeric_variable: FilterVariableTypeOrColumnName
    categorical_variable: FilterVariableTypeOrColumnName

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.group_by:
            if (
                self.numeric_variable in self.group_by.groupings
                or self.categorical_variable in self.group_by.groupings
            ):
                raise ValueError(
                    "Can not group by the given metric variables (numeric_variable, categorical_variable)"
                )

    @classmethod
    def metric_name(cls):
        return "one_way_ANOVA"

    @property
    def supports_custom_aggregation(self):
        return False

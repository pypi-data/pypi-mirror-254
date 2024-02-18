from dataclasses import dataclass
from decimal import Decimal

from scipy.stats import rv_continuous, rv_discrete


@dataclass(frozen=True)
class FormForecast:
    """
    A forecast of a horse's form rating for a given set of conditions
    """

    probability_distribution: rv_discrete | rv_continuous
    solidity: Decimal

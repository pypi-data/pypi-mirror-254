from decimal import Decimal

from scipy.stats import triang

from analysis.forecasting.forecast_strategies.form_forecast_strategy import (
    FormForecastStrategy,
)
from analysis.forecasting.form_forecast import FormForecast
from analysis.horse import Horse
from analysis.race_conditions import RaceConditions


class MinModeMaxTriangular(FormForecastStrategy):
    def __call__(self, horse: Horse, _race_conditions: RaceConditions) -> FormForecast:
        rated_performances = [
            p.form_rating for p in horse.performances if p.form_rating
        ]

        min_rating = min(rated_performances)
        max_rating = max(rated_performances)
        mode_rating = sum(rated_performances) / len(horse.performances)

        loc = min_rating
        scale = max_rating - min_rating
        c = (mode_rating - min_rating) / scale

        probability_distribution = triang(c, loc, scale)
        solidity = Decimal(1.0)
        return FormForecast(probability_distribution, solidity)

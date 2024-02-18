from analysis import Horse, RaceConditions
from analysis.forecasting.forecast_strategies import FormForecastStrategy
from analysis.forecasting.form_forecast import FormForecast


class FormForecaster:
    def __init__(self, strategy: FormForecastStrategy):
        self.strategy = strategy

    def forecast(
        self,
        horse: Horse,
        race_conditions: RaceConditions,
    ) -> FormForecast:
        return self.strategy(horse, race_conditions)

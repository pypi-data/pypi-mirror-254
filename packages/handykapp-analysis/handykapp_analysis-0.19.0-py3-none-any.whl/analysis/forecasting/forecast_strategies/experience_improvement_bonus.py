from decimal import Decimal

from .form_prediction_factor import FormPredictionFactor


class ExperienceImprovementBonus(FormPredictionFactor):
    def _calc(self) -> Decimal:
        perfs = self.horse.performances

        if not perfs:
            return Decimal(0)

        return Decimal(max(6 - len(perfs), 0) ** 3 / 10)

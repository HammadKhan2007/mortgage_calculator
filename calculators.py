"""Mortgage calculator implementations."""

from abc import ABC, abstractmethod

from .models import AmortizationSummary, MortgageInputs


class MortgageCalculator(ABC):
    """Base class for mortgage calculators."""

    payments_per_year = 12

    def __init__(self, inputs: MortgageInputs) -> None:
        self.inputs = inputs

    @abstractmethod
    def monthly_payment(self) -> float:
        """Return the required recurring payment."""

    def summary(self) -> AmortizationSummary:
        """Return payment and interest totals for the full loan term."""
        number_of_payments = self.inputs.term_years * self.payments_per_year
        payment = self.monthly_payment()
        total_paid = payment * number_of_payments
        return AmortizationSummary(
            monthly_payment=payment,
            total_paid=total_paid,
            total_interest=total_paid - self.inputs.principal,
            number_of_payments=number_of_payments,
        )


class FixedRateMortgageCalculator(MortgageCalculator):
    """Calculate payments for a fixed-rate, fully amortizing mortgage."""

    def monthly_payment(self) -> float:
        """Return the monthly payment using the standard amortization formula."""
        principal = self.inputs.principal
        monthly_rate = (
            self.inputs.annual_interest_rate / 100 / self.payments_per_year
        )
        number_of_payments = self.inputs.term_years * self.payments_per_year

        if monthly_rate == 0:
            return principal / number_of_payments

        rate_factor = (1 + monthly_rate) ** number_of_payments
        return principal * monthly_rate * rate_factor / (rate_factor - 1)

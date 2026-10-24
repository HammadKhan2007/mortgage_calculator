"""Data models used by mortgage calculators."""

from dataclasses import dataclass


@dataclass(frozen=True)
class MortgageInputs:
    """Validated inputs for a mortgage calculation."""

    principal: float
    annual_interest_rate: float
    term_years: int

    def __post_init__(self) -> None:
        if self.principal <= 0:
            raise ValueError("principal must be greater than zero")
        if self.annual_interest_rate < 0:
            raise ValueError("annual_interest_rate cannot be negative")
        if self.term_years <= 0:
            raise ValueError("term_years must be greater than zero")


@dataclass(frozen=True)
class AmortizationSummary:
    """The main outputs of an amortizing loan calculation."""

    monthly_payment: float
    total_paid: float
    total_interest: float
    number_of_payments: int

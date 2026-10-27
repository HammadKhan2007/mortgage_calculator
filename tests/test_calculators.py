import pytest

from mortgage_calculator import FixedRateMortgageCalculator, MortgageInputs


def test_fixed_rate_payment_matches_known_example() -> None:
    calculator = FixedRateMortgageCalculator(
        MortgageInputs(principal=300_000, annual_interest_rate=6.5, term_years=30)
    )

    assert calculator.monthly_payment() == pytest.approx(1_896.20, abs=0.01)


def test_zero_interest_is_split_evenly_across_payments() -> None:
    calculator = FixedRateMortgageCalculator(
        MortgageInputs(principal=120_000, annual_interest_rate=0, term_years=10)
    )

    assert calculator.monthly_payment() == pytest.approx(1_000)


def test_summary_contains_total_interest() -> None:
    calculator = FixedRateMortgageCalculator(
        MortgageInputs(principal=100_000, annual_interest_rate=5, term_years=1)
    )

    summary = calculator.summary()

    assert summary.number_of_payments == 12
    assert summary.total_paid == pytest.approx(summary.monthly_payment * 12)
    assert summary.total_interest == pytest.approx(
        summary.total_paid - calculator.inputs.principal
    )


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("principal", 0, "principal"),
        ("principal", -1, "principal"),
        ("annual_interest_rate", -0.1, "annual_interest_rate"),
        ("term_years", 0, "term_years"),
    ],
)
def test_invalid_inputs_raise_value_error(
    field: str, value: float, message: str
) -> None:
    values = {
        "principal": 100_000,
        "annual_interest_rate": 5,
        "term_years": 30,
    }
    values[field] = value

    with pytest.raises(ValueError, match=message):
        MortgageInputs(**values)

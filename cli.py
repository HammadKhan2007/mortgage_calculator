"""Command-line interface for the mortgage calculator."""

import argparse

from .calculators import FixedRateMortgageCalculator
from .models import MortgageInputs


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Calculate fixed-rate mortgage costs.")
    parser.add_argument("--principal", type=float, required=True)
    parser.add_argument(
        "--annual-rate",
        type=float,
        required=True,
        help="Annual interest rate as a percentage, such as 6.5.",
    )
    parser.add_argument("--term-years", type=int, required=True)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    inputs = MortgageInputs(
        principal=args.principal,
        annual_interest_rate=args.annual_rate,
        term_years=args.term_years,
    )
    summary = FixedRateMortgageCalculator(inputs).summary()

    print(f"Monthly payment: ${summary.monthly_payment:,.2f}")
    print(f"Total paid:      ${summary.total_paid:,.2f}")
    print(f"Total interest:  ${summary.total_interest:,.2f}")
    print(f"Payments:        {summary.number_of_payments}")


if __name__ == "__main__":
    main()

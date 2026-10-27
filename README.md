# Mortgage Calculator

A modular Python mortgage calculator demonstrating:

- Separation of input models, calculation logic, and the command-line interface.
- Inheritance through an abstract `MortgageCalculator` base class.
- DRY summary logic shared by calculator implementations.
- Input validation and automated tests with `pytest`.

## Setup

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

python -m pip install -e ".[dev]"
```

## Run

```bash
python -m mortgage_calculator.cli --principal 300000 --annual-rate 6.5 --term-years 30
```

Example output:

```text
Monthly payment: $1,896.20
Total paid:      $682,633.47
Total interest:  $382,633.47
Payments:        360
```

The annual interest rate is entered as a percentage. The calculator assumes monthly
payments and a fully amortizing fixed-rate loan.

## Test

```bash
pytest
```

"""Labs 13-14: check the fictional Meridian mandate. Standard library only.

Weights are percentages; money inputs are USD millions.
Run: python mandate.py
"""

from math import isclose, isfinite


HOLDINGS = [
    {"name": "Cash", "issuer": "none", "days": 0, "reserve": True},
    {"name": "Treasury bills", "issuer": "U.S. Treasury", "days": 1, "reserve": True},
    {"name": "Treasury 10-year note", "issuer": "U.S. Treasury", "days": 1, "reserve": True},
    {"name": "Global equity index fund", "issuer": "diversified fund", "days": 2, "reserve": False},
    {"name": "Investment-grade bond fund", "issuer": "diversified fund", "days": 3, "reserve": False},
    {"name": "Private real estate fund", "issuer": "diversified fund", "days": 90, "reserve": False},
    {"name": "Acme Corp bonds", "issuer": "Acme Corp", "days": 4, "reserve": False},
    {"name": "Acme Corp stock", "issuer": "Acme Corp", "days": 1, "reserve": False},
]
# Weights follow HOLDINGS order.
CANDIDATES = {
    "A": [2, 2, 10, 60, 26, 0, 0, 0],
    "B": [1, 0, 0, 55, 20, 15, 5, 4],
    "C": [1, 1, 0, 70, 20, 0, 0, 8],
    # AI-proposed attack: all cash passes these checks, but exposes S2/S10.
    "D": [100, 0, 0, 0, 0, 0, 0, 0],
    # Lab 14 benchmark: 40% IG bonds, 60% global equity.
    "E": [0, 0, 0, 60, 40, 0, 0, 0],
}
RESERVE_SIZE = 100.0
QUARTERLY_DISTRIBUTION = 0.75
QUARTERS_TO_COVER = 4
LIQUIDITY_WINDOW = 5
MINIMUM_LIQUID_SHARE = 90.0
ISSUER_LIMIT = 8.0
EXEMPT_ISSUERS = {"none", "U.S. Treasury", "diversified fund"}


def reserve_minimum():
    if not isfinite(RESERVE_SIZE) or RESERVE_SIZE <= 0:
        raise ValueError("Reserve size must be finite and positive.")
    return 100 * QUARTERS_TO_COVER * QUARTERLY_DISTRIBUTION / RESERVE_SIZE


def company_exposures(weights):
    totals = {}
    for holding, weight in zip(HOLDINGS, weights):
        issuer = holding["issuer"]
        if issuer not in EXEMPT_ISSUERS:
            totals[issuer] = totals.get(issuer, 0.0) + weight
    return totals


def check_candidate(weights):
    if len(weights) != len(HOLDINGS) or any(not isfinite(w) for w in weights):
        raise ValueError("Provide one finite weight per holding.")
    total = sum(weights)
    lowest = min(weights)
    reserve = sum(w for h, w in zip(HOLDINGS, weights) if h["reserve"])
    liquid = sum(w for h, w in zip(HOLDINGS, weights) if h["days"] <= LIQUIDITY_WINDOW)
    largest = max(company_exposures(weights).values(), default=0.0)
    minimum = reserve_minimum()
    return [
        ("Weights sum to 100", total, isclose(total, 100.0, rel_tol=0, abs_tol=1e-9)),
        ("Long-only (lowest weight)", lowest, lowest >= 0),
        (f"Reserve >= {minimum:.1f}%", reserve, reserve >= minimum),
        (f"Redeemable in {LIQUIDITY_WINDOW} days >= {MINIMUM_LIQUID_SHARE:.1f}%",
         liquid, liquid >= MINIMUM_LIQUID_SHARE),
        (f"Largest single company <= {ISSUER_LIMIT:.1f}%", largest, largest <= ISSUER_LIMIT),
    ]


def main():
    print(f"Reserve minimum: {reserve_minimum():.1f}% of the portfolio")
    for name, weights in CANDIDATES.items():
        print(f"\nCandidate {name}")
        checks = check_candidate(weights)
        for label, value, passed in checks:
            print(f"{label}: {value:.1f} {'pass' if passed else 'FAIL'}")
        print("Calendar-year loss: requires CIO clarification")
        failures = sum(not passed for _, _, passed in checks)
        print("passes every checkable rule" if not failures else f"fails {failures} rule(s)")
    print("\nScope: these are allocation checks, not a complete suitability verdict.")
    print("Turnover, rebalancing, costs, and performance need additional data.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        raise SystemExit(f"Refusing to run: {error}") from error

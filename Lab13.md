# Lab 13 - Meridian mandate defense

Prepared for late submission. This is retrospective work; no earlier completion
is claimed. Candidate E is a later Lab 14 extension; A-D are the Lab 13 candidates.

## Question
Which candidates does the Meridian mandate permit, and what must the CIO answer
before optimization?

## Statement sorting

| Statement | Case wording (condensed) | Your type and reason |
|---|---|---|
| S1 | Seven-year horizon; annual rebalancing | Hard constraint: sets the planning horizon and required rebalancing schedule, although a single holdings snapshot cannot verify compliance over time. |
| S2 | CPI + 4% annually, net of costs, over rolling five years | Objective: defines the desired net real return and evaluation period, rather than a guaranteed outcome. |
| S3 | $0.75m quarterly payouts; twelve months in cash/daily-liquid government securities | Hard constraint: requires four quarterly payouts, or $3m, in eligible reserves, equal to 3% of the $100m portfolio. |
| S4 | Benchmark 60% global equity, 40% US IG bonds | Preference (benchmark reference): specifies the comparison allocation, not a requirement to hold those exact weights. |
| S5 | Long-only; no borrowing, shorts, derivatives | Hard constraint: explicitly prohibits leverage, negative holdings, and derivatives; the permitted holdings and weight checks implement the static allocation portion. |
| S6 | Single issuer maximum 8%; stated exemptions apply | Hard constraint: caps combined exposure to each nonexempt company at 8%, so Acme bonds and stock must be added together. |
| S7 | Annual turnover at most 25% absent committee approval | Hard constraint with an approval exception: turnover above 25% requires committee permission; testing it needs trading history, not just current weights. |
| S8 | At least 90% redeemable within five business days | Hard constraint: requires the sum of weights redeemable within the stated window to be at least 90%. |
| S9 | No calendar-year loss greater than 10%; no measure/breach rule | Unverifiable promise as stated: current holdings cannot guarantee a future loss ceiling; the CIO must clarify the operational risk measure and breach response. |
| S10 | No stated preferences or pilot optimization objective | Missing: the mandate provides neither additional preferences nor the tradeoff the optimizer should prioritize, so these cannot be invented. |

## Checker
File: [mandate.py](mandate.py). Standard library only.
Run `python mandate.py` from this folder.
On this computer, `.venv\Scripts\python.exe mandate.py` uses the existing environment.

Reserve minimum is computed as 4 x 0.75 / 100 x 100 = 3.0%.
The company exposure calculation combines Acme bonds and stock.
S9 is printed as requiring CIO clarification; it is never tested.
The static holdings checker does not certify turnover or future performance.

### Executed technical verification - October 20, 2026
All five measured values matched the handout for A, B, and C.
A passes; B fails three rules; C fails one.
The negative-cash probe changed A to cash -2 and equity 64: total 100.0,
lowest -2.0, reserve 10.0, liquid 100.0, company 0.0. Only long-only failed.
The probe used a copy; saved A remains unchanged.
D passes every checkable rule. Lab 14 E fails only reserve (0.0%).
These checks were executed with AI assistance, not as a claimed student exercise.

## AI-proposed attack (authorized AI step)
Candidate D: 100% cash. It passes the five numerical checks.
It exposes S2 (whether the return objective can be supported) and S10 (the
unresolved optimization tradeoff). Lab 13 provides no cash return or CPI forecast,
so a numeric return failure is not established. The CIO could reject an allocation
that provides no demonstrated path to the stated objective.

### Two-sentence judgment
The objection holds as a suitability concern: 100% cash passes the allocation
checks but does not demonstrate a credible path to the required real return.
S2 supplies the return objective, while S10 leaves the tradeoff unresolved; without
cash-return and inflation assumptions, this is not proof of a numerical return failure.

### Skeptical-colleague role
Counterargument: cash protects liquidity, so why reject a portfolio that passes
every test? Response: S3 and S8 specify minimum liquidity, not the entire investment
purpose; S2 still requires evaluating the portfolio against the real-return
objective. S4 is a comparison benchmark, so deviating from 60/40 is not itself a
hard-rule violation. This is a written skeptical review, not a claimed partner exchange.

## One question for the CIO
When pursuing CPI + 4% conflicts with avoiding a calendar-year loss above 10%,
which priority should govern the pilot: pursue the return objective subject to
an agreed measurable downside-risk policy, or prioritize capital preservation
and accept that the return objective may not be met?

If capital preservation governs, the design would favor more cash and government
securities and explicitly revisit the return objective. If the CIO prioritizes
the return objective and accepts defined downside risk, the design could consider
more growth exposure while preserving the reserve, liquidity, issuer, and other
hard limits. No allocation should be optimized until the CIO operationalizes S9
with a risk measure, acceptable threshold or probability, and breach response;
volatility alone does not guarantee the stated loss ceiling.

## IPS learning and reflection
An investment policy statement is a written agreement defining the portfolio's
purpose, objectives, constraints, responsibilities, and review rules. It gives
decision-makers a consistent basis for choosing and monitoring investments.

Objectives describe the outcomes sought; constraints bound the acceptable choices.
A feasible allocation satisfies the operational constraints, but feasibility alone
does not establish that it is likely to achieve the objective or suit the client.

For Meridian, S1 supplies the horizon and rebalancing policy; S2 the return
objective; S3 the spending and reserve policy; S4 the performance benchmark;
S5 permitted investment practices; S6 concentration limits; S7 turnover and
exception governance; and S8 liquidity. S9 needs an operational risk policy,
and S10 identifies missing preferences and an optimization priority.

Passing the checker can still be unsuitable because it tests only the supplied
static allocation rules. It does not forecast net real returns, guarantee losses,
or verify annual turnover and rebalancing from a single snapshot. Candidate D
illustrates the gap between numerical compliance and a supported investment plan.

Classification ambiguity for reflection: S4 is the least straightforward fit
within the provided categories. A benchmark is a performance reference rather
than a required allocation or an ordinary discretionary preference. The table
uses "preference (benchmark reference)" to preserve that distinction; imposing
60/40 as a hard constraint would add a requirement the CIO did not state.

## Project 2 follow-on (separate from this common-case checkout)
The student's own client has not yet been specified. A separate mandate will need
that client's objective, hard constraints, and one unresolved client question;
Meridian's facts are not assumed to describe that client.

## Ownership and checkout
Review the written judgments before submission. Code-quiz practice remains pending.
Publish this file and mandate.py to your own GitHub repository; paste their
individual links in the Lab 13 quiz. No GitHub publication is claimed here.

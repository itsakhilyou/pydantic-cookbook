# Finance starter — example output

Agent output from `starters/finance_research.py` (Finance Research API).

- **Verified:** 2026-08-19
- **Model:** `openrouter:deepseek/deepseek-v4-flash-0731`
- **Surface:** `YouResearch` (`finance_research`, `finance_effort='deep'`)
- **Wall time:** ~4 min
- **Tool calls:** 2 `finance_research`, then synthesis

---

# DESK NOTE — Private Credit: Entering 2026, the Silence Is the Signal
**For PMs | Credit Strategy | Not investment advice**

## The one-line call
Private credit is not (yet) in a casualty-wave bankruptcy — the stress is being *held* inside the system through PIK amendments, distressed exchanges, and delayed marks. The investment question entering 2026 is not "will there be defaults" but "who holds the losses once marks catch up to cash-flow reality."

---

## 1. Size & growth — big, but the number depends on who's counting
- **FSB (regulatory, narrow):** $1.5–2.0T B2B nonbank lending at end-2024, ~$1T in the US — comparable to institutional leveraged loans (~$1.5–1.7T) and public HY (~$2T). *(FSB May 2026)*
- **Fed (vehicle-based, broad):** $1.34T US / ~$2T global by 2024-Q2; BDC assets $134B (2020) → **$375B (2024)**. *(Fed Notes, 23 May 2025)*
- **AIMA/ACC:** **$3.5T global AUM** as of 9 Dec 2025 — a *broader* measure that includes commitments/structure. *(AIMA)*

⚠️ Flag: these are **not one comparable time series**. Exact size is contested; treat growth as "rapid double-digit," not a precise $ figure.

## 2. Stress signals — defaults are high *if you count them honestly*
- **Fitch US private-credit default rate: record 6.0%** (12-mo to Apr 2026), up from 5.7% in March; 9.2% (2025) vs 8.1% (2024) on Fitch's monitored sample. *(Fitch)*
- **Moody's:** just **1.6–4.7% for 2025** — definitional difference. Distressed restructurings ~65% of defaults. *(Moody's)*
- **Lincoln (the "shadow default" indicator):** **11%** of borrowers on PIK; **6.4%** carrying "bad PIK" (introduced *after* origination) vs **2.5% in Q4 2021**; bad-PIK LTV up from **39.4% at inception → 76.1%** in Q4 2025. *(Lincoln)*

The gap between 1.6% and 9.2% isn't a contradiction — it's the whole point. Amend-and-extend, PIK amendments and distressed exchanges keep a loan's *nominal* value intact while cash economics deteriorate.

## 3. Valuation / mark transparency — the core amplifier
- IMF & FSB both find private marks are quarterly, model-based, discretionary, and show **smaller markdowns than credit quality justifies**. *(IMF GFSR Ch.2; FSB)*
- **Confirmation is arriving in listed vehicles:** avg BDC NAV **-2.0% in Q1 2026** (-2.5%/share) as spreads widened, software valuations fell, non-accruals rose. *(Fitch BDC, 18 Jun 2026)*
- **Fund liquidity is cracking:** Q1-2026 redemptions across 17 direct-lending vehicles = **$19.5B**, only **$10.4B (53%)** paid; 9 vehicles hit withdrawal caps. **Blue Owl limited redemptions** at two funds after unprecedented requests (Apr 2026). *(BI; Bloomberg)*
- Why it matters: **stale NAVs → first-mover incentive** — LPs redeem before marks catch up to market-clearing. This is the FSB's specific warning.

## 4. Credit deterioration & emblematic names
- **Pluralsight (2024):** $1.3B debt-for-equity; lenders (incl. Blue Owl, Ares, Golub, Oaktree, BlackRock) took 100% ownership + $250M new capital. *(Goodwin)*
- **Mitel (2025):** Ch. 11 on 9 Mar 2025, ~$1.3B debt; cut $1.15B; completed 20 Jun 2025. *(Reuters/Mitel)*
- **Envision Healthcare (2023):** KKR-owned; cut **>$7B** debt, split in two. *(Reuters)* — the early-cycle template.
- **First Brands Group (Ch. 11, Sep 2025):** **$6.1B** debt incl. ~$5.3B term loans; 20 BDCs had held its 2027 loans. *(PitchBook/9fin)* — an underwriting/collateral-verification case.
- **Tricolor Holdings (subprime auto, Sep 2025):** **JPMorgan $170M** charge-off, **Fifth Third $178M** impairment; noteholders (>$230M) sued over red flags. *(Reuters)* — **collateral-fraud/operational risk** in warehouse/ABS lending.

## 5. Systemic interconnections — the transmission map
- **Banks:** only ~**$56B** loans to private-credit vehicles (5% of US industry) at 2024-Q4 — but the FSB's broader tally is ~**$220B** drawn+undrawn fund credit lines. Exposure is **nonlinear**: funds draw facilities *precisely when* portfolio stress, margin pressure and redemptions rise. *(Fed; FSB)*
- **Basel channel:** BDC borrowing-base and fund-portfolio facilities are **economically NAV/asset-backed** — banks can get lower risk weights (equity tranches often 30–40%), making facilities look safe singly while embedding correlated underlying exposure. *(FSB)*
- **Private-credit CLOs:** ~**$155B** outstanding (Oct 2025), ~16% of the $977B US CLO market — but collateral has more CCC, weaker recoveries, less transparency, though senior tranches benefit from higher equity subordination. *(FSB)*
- **Insurers/PE-owned reinsurers:** exposure via asset-intensive, funded-reinsurance structures and **private ratings** used for regulatory capital. Concentrated, less-visible pockets. *(FSB; Chicago Fed)*
- **Retail/semi-liquid:** perpetual non-traded BDCs — illiquid loans vs periodic redemption = the emerging run-risk locus. *(IMF)*

## 6. Shift to asset-backed finance (ABF) — opportunity, now with underwriting tail risk
- Volumes are rising across consumer/autos/equipment/CRE whole loans, receivables, royalties — a genuine diversifier vs sponsor cash-flow lending (bankruptcy-remote collateral). *(Brookfield; CNBC, 2 Dec 2025)*
- But it swaps single-company EBITDA risk for **collateral-performance, servicer, fraud, advance-rate, prepayment and appraisal risk**. **Tricolor** is the cautionary case; **First Brands** flagged originator/verification discipline. Intense inflows are compressing ABF standards. *(CNBC; Reuters)*
- **NAV lending** adds a **second layer of leverage** above operating-company debt (can force asset sales/capital calls if valuations fall). *(FSB)*

## 7. Pricing hasn't repriced — that's the tell
- US direct loans: **SOFR + 450–550 bp**, OID only ~**1.0–1.5%** — ~**50 bp tighter than 12–18 months ago**, despite rising PIK/defaults. Thin cushion. *(StepStone 2H25)*
- Covenant-lite ≈ **70%** of new private loans (2024) vs 91% of outstanding leveraged loans — less early-intervention ability. *(Lincoln; note lower in PC CLOs per FSB)*

---

## What to watch next
1. **Cash interest coverage + PIK toggles + non-accruals + covenant amendments** — not headline "default rates." Watch the bad-PIK share creep (currently 6.4% and rising).
2. **Loan-level mark evidence** — valuation date, comparables, discount-rate moves, realized vs unrealized PIK, sponsor support. Trust NAV stability less, portfolio construction more.
3. **Layer-by-layer leverage map** — borrower → BDC/fund → subscription/NAV/warehouse → PC-CLO → insurer/reinsurer balance sheet. Who lends at each layer, on what collateral, and what triggers a draw.
4. **Redemption pressure in semi-liquid funds** — the 53% payout ratio and Blue Owl caps are the advance warning of a liquidity event. If more vehicles hit withdrawal caps, expect orderly-sale NAV marks to gap down.
5. **ABF concentration** — single-originator, servicer, consumer-cohort or CRE-geography exposure; verify collateral and cash-flow controls, not just LTV.
6. **Recovery values** — observed losses are low largely because recoveries *haven't been crystallized* (deferrals/extensions). Assume current recovery data understate eventual loss severity.

**Bottom line for positioning:** the marginal risk is not principal loss in the next quarter — it's **late and correlated recognition** meeting **redemption-driven forced marks**. Favor transparency (managed accounts, loan-level data) over braided NAV; favor well-subordinated PC-CLO seniors over unsubordinated equity layers; stress-test every ABF book for the single-originator/servicer failure case; and treat any fund-liquidity event as a *portfolio-wide* mark signal, not a single-name story.

⚠️ **Data caveats:** Market size, default rates (1.6–9.7% dependent on definition/sample), and covenant/PIK shares (some estimates unaudited, e.g., the 70% cov-lite and 11% PIK figures are market estimates) are contested. The FSB itself calls the sector "data-poor and untested by a prolonged downturn." Treat precise numbers as directional, dated figures (mostly late-2025 to mid-2026) rather than audited fact.

*Sources: FSB Report on Vulnerabilities in Private Credit (6 May 2026); Fed Notes (23 May 2025); IMF GFSR Ch.2 (Apr 2024); AIMA (9 Dec 2025); Fitch (18 May 2026; 3 Jun 2026; 18 Jun 2026); Moody's; Lincoln International; StepStone 2H25; Reuters; Bloomberg; PitchBook; 9fin; Goodwin; Business Insider; CNBC; Brookfield; Chicago Fed.*

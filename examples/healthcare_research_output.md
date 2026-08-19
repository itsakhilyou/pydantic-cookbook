# Healthcare starter — example output

Agent output from `starters/healthcare_research.py` (Research API).

- **Verified:** 2026-08-19
- **Model:** `openrouter:deepseek/deepseek-v4-flash-0731`
- **Surface:** `YouResearch` (`research`), with an `output_schema`, `boost_domains` (CDC, WHO, clinical journals), and `country='us'`
- **Wall time:** ~1.5 min
- **Tool calls:** 1 `research` + 1 `answer`, then synthesis

---

Here is a clinically oriented summary of the current U.S. *Candida auris* situation, drawn from the CDC's latest surveillance and guidance with dates attached.

## Case counts and geographic spread
- **Clinical cases (CDC tracking page, as of March 3, 2026):** 6,304 clinical cases in calendar year **2024**; the 2025 total fell to an estimated **4,290** clinical cases. Note the figures differ because they come from different CDC reporting layers — the 2024 number is the completed case-based total, while 2025 reflects the live tracking table prior to full case reconciliation ([CDC Tracking C. auris](https://www.cdc.gov/candida-auris/tracking-c-auris/index.html); [Becker's Hospital Review](https://www.beckershospitalreview.com/quality/public-health/c-auris-clinical-cases-by-state-2026/)).
- **CDC case-based surveillance analysis (specimens 2022–2024, analysis finalized Feb 20, 2026):** 13,507 clinical cases total (2,882 in 2022; 4,428 in 2023; 6,197 in 2024) and 27,853 **screening/colonization** detections (6,226 in 2022; 9,195 in 2023; 12,432 in 2024). Cases continue to rise each year, though the *rate* of increase has slowed since 2022 ([MMWR Surveillance Summary](https://www.cdc.gov/mmwr/volumes/75/ss/ss7504a1.htm?s_cid=ss7504a1_w)).
- **Geographic spread:** Ongoing transmission is concentrated in the **West, Southeast, and Midwest** AR Laboratory Network regions, with spread into new areas; some regions continue to have unremitting transmission ([MMWR](https://www.cdc.gov/mmwr/volumes/75/ss/ss7504a1.htm)). Press reporting in mid-2026 describes detection in roughly **23–27 states**, with notable current screening burdens in Texas (~715 screening cases) and Michigan (~518) ([USA Today](https://www.usatoday.com/story/news/health/2026/08/06/deadly-drug-resistant-fungus-spreading-see-map/91198651007/); [Newsweek](https://www.newsweek.com/candida-auris-map-outbreak-fungus-superbug-states-12310310)). The "states affected" figure varies by whether clinical plus screening detections are counted together.

## Resistance epidemiology
- Based on **8,033 isolates collected 2022–2023** (CDC analysis): **>95% resistant to fluconazole**, **~15% resistant to amphotericin B**, **~1% resistant to echinocandins**, and **<1% pan-resistant** (resistant to all three major classes). Most U.S. strains remain echinocandin-susceptible, but echinocandin-resistant and pan-resistant cases are rising ([MMWR Surveillance Summary](https://www.cdc.gov/mmwr/volumes/75/ss/ss7504a1.htm); [CDC Clinical Care](https://www.cdc.gov/candida-auris/hcp/clinical-care/)).

## First-line treatment selection
- **Adults and children >2 months:** start an **echinocandin** — anidulafungin, caspofungin, or micafungin — as initial therapy.
- **Treat only clinical infection**, not colonization or positive screening results without symptoms.
- **Infants <2 months:** initial therapy is **amphotericin B deoxycholate 1 mg/kg/day**; liposomal amphotericin B 5 mg/kg/day may be considered if unresponsive. Echinocandins may be used cautiously in exceptional cases if CNS involvement is excluded.
- **Echinocandin-resistant or non-improving cases:** consider **liposomal amphotericin B**; **investigational agents** may be considered for pan-resistant infection. This is CDC guidance, not a randomized-trial-level recommendation ([CDC Clinical Care](https://www.cdc.gov/candida-auris/hcp/clinical-care/)).

## Infection control and containment (CDC)
- **Hand hygiene:** alcohol-based hand sanitizer routinely when hands not visibly soiled; soap and water if visibly soiled.
- **Isolation:** single rooms when possible; **Contact Precautions** in acute care and LTACHs; Contact Precautions or **Enhanced Barrier Precautions** in nursing homes/SNFs depending on setting; cohorting when needed; gowns and gloves with proper donning/doffing.
- **Environmental disinfection:** clean/disinfect rooms at least daily and at discharge/transfer; use **EPA-registered disinfectants effective against C. auris (EPA List P)** — many common hospital disinfectants and quaternary-ammonium–only products are **not** effective. Disinfect shared/mobile equipment after each use.
- **Screening:** screen high-risk patients and epidemiologic contacts, especially in high-burden or transmission settings.
- **Interfacility communication:** relay C. auris status during transfers. CDC does **not** recommend routine re-screening to discontinue precautions, because colonization can persist for months or indefinitely ([CDC Infection Control](https://www.cdc.gov/candida-auris/hcp/infection-control/index.html); [CDC Screening](https://www.cdc.gov/candida-auris/hcp/screening-hcp/index.html)).

## Interpretation and caveats
The epidemiology is well-established and consistently reported by CDC surveillance, but two figures should be read with care: the **2025 total (4,290) is a running tracker number, not a finalized annual count**, and the **"23–27 states"** figure mixes clinical and screening detection and reflects press interpretation rather than a single CDC metric. Resistance data are from 2022–2023 isolates; more recent echinocandin and pan-resistance trends may be under-reported. Treatment and infection-control recommendations are CDC expert guidance based on observational data and emerging resistance surveillance, not on large controlled efficacy trials.

**Key current dates:** CDC tracking page current as of **2026-03-03**; case-based surveillance dataset finalized **2026-02-20**; press reporting on state spread from **August 2026**.

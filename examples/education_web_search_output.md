# Education starter — example output

Agent output from `starters/education_web_search.py` (Web Search API).

- **Verified:** 2026-08-19
- **Model:** `openrouter:deepseek/deepseek-v4-flash-0731`
- **Surface:** `YouSearch` (`web_search` + `get_page`), with `boost_domains` (RAND, NCES, OECD, Pew, EdWeek), `exclude_domains` (aggregators), and `country='us'`
- **Wall time:** ~2.5 min
- **Tool calls:** 11 `web_search` + 3 `get_page`, then synthesis

---

Based on my research across RAND, the Learning Policy Institute (LPI), OECD/TALIS, Pew Research Center, NCES, and Gallup, here is a synthesis of the current evidence for your briefing.

---

# K-12 Teacher Burnout and Retention: Evidence Brief

## 1. Burnout rates: still elevated, and still worse than the broader workforce

The single most reliable trend series is RAND's **State of the American Teacher** survey (nationally representative, ~1,000–2,300 public-school teachers per year since 2021). Teachers have reported worse well-being than comparable working adults **on every indicator, every year since 2021**.

**Reported burnout** (share reporting burnout in RAND's series):
- 2023: 56% (teachers) vs. 35% (similar working adults)
- 2024: 60% vs. 33%
- 2025: 53% vs. 39%
- 2026: 57% vs. 36%
*Source: https://www.rand.org/pubs/commentary/2026/08/the-state-of-public-education-in-2026-in-five-charts.html*

**Frequent job-related stress** followed a similar pattern, spiking at 73–78% in 2021–22, easing to ~55–62% through 2024–26, versus roughly 33–41% for comparable adults. Teacher depression symptoms (~17–19%) also run roughly double the comparable-adult rate. Even in the "good" years, approximately **6 in 10 teachers report burnout or frequent stress** — consistently about 1.5–2x the rate of similar professionals. *(RAND 2026 charts, above; https://www.rand.org/pubs/research_reports/RRA1108-12.html)*

**Reference points from other surveys:**
- **Pew Research Center (2024, n=2,531):** 54% of teachers say it's difficult to achieve work-life balance; 84% say there isn't enough time in the regular workday to get everything done. *(https://www.pewresearch.org/social-trends/2024/04/04/whats-it-like-to-be-a-teacher-in-america-today/)*
- **Intentions to leave:** 16% of teachers reported intentions to leave in 2024–25; that rose to **18% in 2026**, and only one in four said they planned to stay in the profession as long as they were able *(RAND)*.
- Top stressors: **managing student behavior**, **low pay**, and **working too many hours** *(RAND 2025–26)*.

## 2. Weekly workload: ~53 hours, with ~12–15 hours of uncompensated work

- **RAND 2024:** Teachers reported working **about 53 hours/week vs. 44 for comparable working adults** (9 hours more). Contracts required a 38-hour week, so teachers logged roughly **11.6 uncompensated hours per week** on average. Only ~41–46% of teachers were satisfied with their total hours (vs. ~68% of comparable adults). *(https://www.rand.org/pubs/research_reports/RRA1108-12.html)*
- **NCES data** put the average US teacher week at **53.3 hours against a 38.2-hour contract** — a ~15-hour gap. *(Cited in https://www.tutero.com/au/blog/how-many-hours-do-teachers-work)*
- Because actual teaching is only ~43% of the week, the load is heaviest from **lesson planning, grading, and administrative work**. *(OECD TALIS 2024)* — this is the workload dimension that AI tools can most directly address (see Section 5).

**Bottom line:** This is not primarily a "hours above 53" problem; it is that a large share of those hours are on top of a 38-hour contract, not paid, and consumed by non-instructional tasks.

## 3. Turnover: stabilizing after the pandemic peak, but still elevated — and early-career attrition is the most expensive slice

**National turnover trend (RAND American School District Panel, district-reported resignation/retirement rates):**
- Pre-pandemic: **5.7%**
- 2021–22 pandemic peak: **10.0%**
- 2022–23: 9.1% → 2023–24: 7.2% → **2024–25: 6.7%**
- Urban districts remain elevated at **11.1% in 2024–25** (vs. 5.9% suburban, 6.6% rural).
*Source: https://www.rand.org/pubs/research_reports/RRA4737-1.html*

**Early-career attrition — the core retention cost:**
- **7–15% of US public school teachers leave within their first two years; by the end of year five, 44–55% of new teachers have left** (NCES, cited in the global retention survey). *(https://www.azcentral.com/press-release/story/105804/new-global-survey-reveals-the-hidden-drivers-of-teacher-retention-and-what-it-means-for-school-budgets/)*
- **OECD/TALIS 2024:** 6.5% of fully qualified teachers left the profession in 2022/23; across 7 systems, **16–68% of resigning teachers had fewer than five years' experience**; 1 in 5 teachers under 30 intend to leave within five years. *(https://www.oecd.org/en/publications/2025/09/education-at-a-glance-2025_c58fc9ae/full-report/how-severe-are-teacher-shortages-across-countries_781f4a97.html)*

**Cost:**
- **LPI:** Replacing a single teacher costs districts roughly **$12,000–$25,000** (recruitment, hiring, onboarding; some estimates range $11,860–$25,000). *(https://www.devlinpeck.com/content/teacher-shortage-by-state; https://www.azcentral.com/press-release/story/105804/)*
- **Attrition drives ~90% of annual teacher demand**, and ~74% of leavers move or leave voluntarily for reasons other than retirement — making retention the single biggest lever on the shortage. *(LPI, An Overview of Teacher Shortages: 2026, via https://www.devlinpeck.com/content/teacher-shortage-by-state)*
- The national shortage now stands at ~**425,000 teaching positions unfilled or filled by non-fully-certified teachers (~1 in 8)** — a rise for the third consecutive year. *(LPI 2026)*

## 4. Protective factors — what the evidence best supports

The most consistent finding across RAND, LPI, and the OECD reviews is that retention is driven **mostly by conditions inside the school organization**, not individual resilience alone:

- **School leadership / support** is the single most influential mutable factor. LPI found the predicted probability of teacher turnover falls from **18.7% to 9.0%** when comparing teachers reporting low vs. high leadership effectiveness and support — a halving of turnover risk. *(Cited in https://www.everydayprincipal.com/post/before-you-ask-teachers-to-do-more-the-leadership-case-for-a-schoolwide-friction-audit; supported by https://ifp.nyu.edu/2026/meta-analyses-systematic-reviews/rev3-70182/)*
- **Mentoring and structured induction** are among the best-evidenced early-career interventions: high-quality mentoring improves retention, teacher effectiveness, and job satisfaction, especially in the first three years when attrition peaks. *(OECD TALIS 2024, https://www.oecd.org/en/publications/2025/10/results-from-talis-2024_28fbde1d/full-report/developing-teacher-expertise_f95ff343.html; https://www.mdpi.com/2227-7102/16/8/1204)*
- **Preparation quality:** New teachers with little or no preservice preparation are ~**2.5x more likely to leave after one year** than well-prepared peers (LPI 2016, cited in Arizona retention reporting). *(https://www.eastvalleytribune.com/state-s-teacher-turnover-outpaces-nation/article_ff1ff290-73ef-55f9-9f85-b663ca5adc42.html)*
- **Professional community, autonomy, and a positive school climate** (feeling respected and valued) correlate consistently with persistence; relatedness and connectedness buffer early-career teachers.
- **Self-efficacy** is a genuine protective factor, but the evidence indicates it operates **indirectly — through work meaning and resilience** — and explains only a modest share of well-being, so it can't substitute for fixing organizational conditions. *(https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2026.1872336/full)*
- **Pay:** Adequacy of pay matters (teachers report ~$16k below what they consider adequate), but compensation functions as a necessary-but-not-sufficient factor; the Arizona exit-survey work shows burnout (~74% citing it) and leadership/respect often rank alongside or above salary as stated reasons for leaving.

Caution on interpretation: the "soft" factors (respect, leadership, mentorship) are **well-established in the literature**, whereas the AI time-saving results are newer and mixed (Section 5).

## 5. AI-assisted workload reduction — promising on time savings, but with important caveats

**What supports the hype:**
- **Gallup (2025, with the Walton Family Foundation):** Teachers who use AI at least **weekly save about 5.9 hours/week** (~6 weeks of time per school year); those using it only monthly save about **2.9 hours/week** — *frequency drives the return*. Roughly **3 in 10 teachers** already use AI weekly. *(Summarized at https://www.taskade.com/blog/ai-tools-teachers and https://programs.com/resources/ai-education-statistics/)*
- The biggest time wins align directly with the workload data above: **lesson planning (37% of users cite as top use), worksheet/resource creation (33%), differentiation (28%), admin/paperwork (28%), assessments (25%), and grading (16%)**. *(Gallup, via https://ghost.thirdrocktechkno.com/how-ai-reduces-teacher-workload-gcc-schools/)*
- **McKinsey** estimates AI could automate **20–40% of teachers' administrative tasks** — the current 5.9-hr savings (~11–13% of the 53-hr week) suggests the ceiling is higher than what's been captured so far.
- Because 70% of non-teaching time goes to grading, planning, and admin, AI targets exactly the burden that drives burnout and that RAND identifies as a "working too many hours" stressor.

**What warrants caution — this is still an emerging evidence base:**
- The Gallup figures are **self-reported time savings from a private polling firm**, not causal proof of reduced burnout or improved retention. No rigorous study yet links AI adoption directly to lower burnout or turnover.
- **One of the first randomized classroom trials (Sungu et al., Wharton/Penn, ~193 teachers, ~2,800 students in Turkey, spring 2025; draft only, not yet peer-reviewed)** found that giving teachers an AI teaching assistant **did not improve average achievement and actually reduced students' intrinsic motivation**; for weaker teachers, student achievement and confidence declined. The authors warn that teachers can use AI "as a crutch," losing their personal voice. The practical lesson: AI is best used as a **first-draft tool the teacher reviews, adapts, and makes their own** — not a "generate and copy-paste" machine. *(https://www.wgauradio.com/news/teachers-save-time/3VO3NU5PIYYWLNWK34ZEPBSHMU/)*
- **Equity and policy gaps:** teachers in higher-need schools are less likely to receive AI guidance; lack of policy and role clarity correlates with higher burnout. Surfacing AI without training, privacy guardrails, or review workflows risks widening inequalities and quality gaps.

## 6. What the evidence backs most strongly — recommended priorities

Ranked by depth of evidence:

1. **Strengthen school leadership and supportive working conditions.** This is the single best-evidenced and most cost-effective retention lever (turnover probability roughly halves with strong leadership support). Protect planning time, improve behavior-management support (the #1 stressor), and give teachers a real voice.

2. **Invest in structured early-career induction and high-quality mentoring** (especially years 1–3). This targets the highest-attrition, most expensive window and is supported by OECD, LPI, and systematic reviews. Quality matters — mentoring must have trained mentors, release time, and real observation/feedback, not just a checklist.

3. **Improve compensation adequacy and teaching quality preparation.** Teachers see pay as inadequate, and weakly-prepared novices are ~2.5x more likely to leave. Compensation should be sustainable base-pay progression (not one-off bonuses), paired with residency-type preparation.

4. **Treat workload — not just hours — as the problem.** The evidence points to cutting non-instructional load (planning, grading, admin) rather than adding more; reducing admin and providing high-quality shared resources frees roughly 3+ hours/week per teacher (Grattan Institute data).

5. **Approach AI-assisted workload reduction as a promising but early-stage tool.** Pilot it in high-load, low-risk tasks (lesson prep, worksheet/differentiation drafting, report-comment and parent-message drafting), measure *hours saved* and *teacher experience* in your own school, require teacher review of all output, and pair it with training and data-privacy guardrails. Do **not** treat the Gallup number or the Turkey trial as settled proof of burnout or retention gains — it is too early, and an unguided rollout can degrade quality, especially for weaker instructors.

---

**Key sources**
- RAND turnover trends: https://www.rand.org/pubs/research_reports/RRA4737-1.html
- RAND well-being series (2026): https://www.rand.org/pubs/commentary/2026/08/the-state-of-public-education-in-2026-in-five-charts.html
- RAND workload/pay (2024): https://www.rand.org/pubs/research_reports/RRA1108-12.html
- RAND State of the American Teacher 2025: https://www.rand.org/pubs/research_reports/RRA1108-16.html
- Pew: https://www.pewresearch.org/social-trends/2024/04/04/whats-it-like-to-be-a-teacher-in-america-today/
- OECD Education at a Glance 2025 (attrition & early career): https://www.oecd.org/en/publications/2025/09/education-at-a-glance-2025_c58fc9ae/full-report/how-severe-are-teacher-shortages-across-countries_781f4a97.html
- OECD TALIS 2024 (mentoring/induction): https://www.oecd.org/en/publications/2025/10/results-from-talis-2024_28fbde1d/full-report/developing-teacher-expertise_f95ff343.html
- LPI shortage overview / cost: https://www.devlinpeck.com/content/teacher-shortage-by-state and https://learningpolicyinstitute.org/topic/teacher-recruitment-retention-and-shortages
- Gallup AI time savings: https://programs.com/resources/ai-education-statistics/ and https://www.taskade.com/blog/ai-tools-teachers
- Randomized AI classroom trial (Hechinger/UPenn): https://www.wgauradio.com/news/teachers-save-time/3VO3NU5PIYYWLNWK34ZEPBSHMU/

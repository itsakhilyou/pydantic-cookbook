.PHONY: install smoke run-health run-edu run-finance run-deal

install:
	pip install -r requirements.txt

# Construct every agent without making network calls. Verifies imports,
# capability wiring, and the deal-desk subagent roster before you spend tokens.
# Needs keys present in .env (the OpenRouter provider checks OPENROUTER_API_KEY
# exists at construction time; it does not call the network).
smoke:
	python -c "import deal_desk, starters.healthcare_research as h, starters.education_web_search as e, starters.finance_research as f; \
	print('starters constructed:', h.agent.name or 'healthcare', e.agent.name or 'education', f.agent.name or 'finance'); \
	print('deal_desk specialists:', deal_desk.market_analyst.name, deal_desk.finance_analyst.name, deal_desk.risk_analyst.name); \
	print('deal_desk output_type:', deal_desk.DueDiligenceMemo.__name__); \
	print('LLM_MODEL:', deal_desk.MODEL); \
	assert {deal_desk.market_analyst.name, deal_desk.finance_analyst.name, deal_desk.risk_analyst.name} == {'market_analyst','finance_analyst','risk_analyst'}; \
	assert deal_desk.MODEL.startswith('openrouter:'), deal_desk.MODEL; \
	print('SMOKE OK')"

run-health:
	python starters/healthcare_research.py

run-edu:
	python starters/education_web_search.py

run-finance:
	python starters/finance_research.py

run-deal:
	python deal_desk.py

from crewai import Agent

iqvia_agent = Agent(
    name="IQVIA Agent",
    goal="Analyze market data",
    role="Market Analyst",
    backstory="You are an expert market analyst specializing in pharmaceutical market data analysis."
)
exim_agent = Agent(
    name="EXIM Agent",
    goal="Analyze trade flows",
    role="Trade Analyst",
    backstory="You are a trade analyst expert in analyzing import-export data for pharmaceutical products."
)
patent_agent = Agent(
    name="Patent Agent",
    goal="Analyze IP filings",
    role="Patent Analyst",
    backstory="You are a patent analyst specialized in intellectual property and patent filings analysis."
)
clinical_agent = Agent(
    name="Clinical Trials Agent",
    goal="Analyze trial pipelines",
    role="Clinical Analyst",
    backstory="You are a clinical analyst expert in analyzing clinical trial data and pipelines."
)
internal_agent = Agent(
    name="Internal Agent",
    goal="Summarize internal documents",
    role="Knowledge Analyst",
    backstory="You are a knowledge analyst specialized in summarizing and extracting insights from internal documents."
)
web_agent = Agent(
    name="Web Agent",
    goal="Search real-time publications",
    role="Web Researcher",
    backstory="You are a web researcher expert in finding and analyzing real-time publications and web sources."
)
report_agent = Agent(
    name="Report Agent",
    goal="Generate PDF summary",
    role="Report Designer",
    backstory="You are a report designer specialized in creating comprehensive PDF reports from analyzed data."
)
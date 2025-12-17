# Pharmaceutical Intelligence Platform

**Agentic AI Solution for Pharmaceutical Research and Portfolio Planning**

This platform uses AI agents to analyze multiple data sources and provide comprehensive pharmaceutical intelligence:

## Features

- **Market Intelligence**: IQVIA data analysis
- **Trade Analysis**: EXIM data insights
- **Patent Landscapes**: USPTO patent analysis
- **Clinical Trials**: ClinicalTrials.gov data
- **Internal Documents**: PDF document analysis
- **Web Intelligence**: Real-time web research
  
## Project Structure

pharmaceutical-intelligence-platform/
├── app.py                    ◄─── Main Gradio Application

├── main.py                   ◄─── Alternative Entry Point

├── requirements.txt          ◄─── Dependencies

├── README.md                 ◄─── Documentation

├── .env.example              ◄─── Environment Template

│

├── agents/                   ◄─── Agent Implementation Layer

│   ├── __init__.py

│   ├── master_agent.py       ◄─── LangGraph Orchestrator

│   ├── query_parser.py       ◄─── NLP Processing

│   ├── crewai_agents.py      ◄─── CrewAI Definitions

│   ├── worker_agents.py      ◄─── Alternative Implementation

│   ├── iqvia_agent.py        ◄─── Market Intelligence

│   ├── exim_agent.py         ◄─── Trade Analysis

│   ├── patent_agent.py       ◄─── IP Landscape

│   ├── clinical_agent.py     ◄─── Clinical Trials

│   ├── internal_agent.py     ◄─── PDF Processing

│   ├── web_agent.py          ◄─── Web Intelligence

│   └── report_agent.py       ◄─── PDF Generation

│

├── mock_data/                ◄─── Data Sources Layer

│   ├── iqvia_mock.json       ◄─── Market Data

│   ├── exim_mock.json        ◄─── Trade Data

│   ├── patent_mock.json      ◄─── Patent Data

│   ├── clinical_mock.json    ◄─── Clinical Data

│   ├── web_search_mock.json  ◄─── Web Data

│   ├── internal_mock.pdf     ◄─── Sample Document

│   └── synthetic_queries.json◄─── Example Queries

│

├── reports/                  ◄─── Output Storage

│   └── *.pdf                 ◄─── Generated Reports

│

├── uploads/                  ◄─── User File Storage

│   └── *.pdf                 ◄─── User Documents

│

└── .gradio/                  ◄─── Gradio Configuration
  

## How to Use

1. Enter your pharmaceutical research query
2. Optionally upload internal documents (PDF)
3. Click "Run Analysis" to get comprehensive insights
4. Download the generated PDF report

## Example Queries

- "Which respiratory diseases show low competition but high patient burden in India?"
- "Analyze market opportunity for repurposing metformin for cancer treatment"
- "What are the patent expiry timelines for statin drugs?"
- "Find clinical trials for diabetes drugs in Phase 3"

## Architecture

The platform uses a multi-agent architecture with:
- **Master Agent**: Query parsing and orchestration
- **Worker Agents**: Specialized data gathering from different sources
- **Report Generator**: Comprehensive PDF report creation

## Requirements

See `requirements.txt` for the complete list of dependencies.

## License


MIT License




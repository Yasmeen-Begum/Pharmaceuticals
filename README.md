---
title: Pharmaceutical Intelligence Platform
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: mit
---

# Pharmaceutical Intelligence Platform

**Agentic AI Solution for Pharmaceutical Research and Portfolio Planning**

This platform uses AI agents to analyze multiple data sources and provide comprehensive pharmaceutical intelligence for drug repurposing research, reducing research time from 2-3 months to hours.

## Features

- **Market Intelligence**: IQVIA data analysis with market size, CAGR trends, and competitor insights
- **Trade Analysis**: EXIM data insights for API/formulation trade flows and sourcing opportunities
- **Patent Landscapes**: USPTO patent analysis with active patents, expiry timelines, and FTO flags
- **Clinical Trials**: ClinicalTrials.gov data with trial pipeline information and sponsor profiles
- **Internal Documents**: PDF document analysis and summarization of strategy documents
- **Web Intelligence**: Real-time web research for guidelines, publications, and market signals

## Project Structure

```
pharmaceutical-intelligence-platform/
├── app.py                    # Main Gradio Application
├── main.py                   # Alternative Entry Point
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
├── .env.example              # Environment Template
│
├── agents/                   # Agent Implementation Layer
│   ├── __init__.py
│   ├── master_agent.py       # LangGraph Orchestrator
│   ├── query_parser.py       # NLP Processing
│   ├── crewai_agents.py      # CrewAI Definitions
│   ├── worker_agents.py      # Alternative Implementation
│   ├── iqvia_agent.py        # Market Intelligence
│   ├── exim_agent.py         # Trade Analysis
│   ├── patent_agent.py       # IP Landscape
│   ├── clinical_agent.py     # Clinical Trials
│   ├── internal_agent.py     # PDF Processing
│   ├── web_agent.py          # Web Intelligence
│   └── report_agent.py       # PDF Generation
│
├── mock_data/                # Data Sources Layer
│   ├── iqvia_mock.json       # Market Data
│   ├── exim_mock.json        # Trade Data
│   ├── patent_mock.json      # Patent Data
│   ├── clinical_mock.json    # Clinical Data
│   ├── web_search_mock.json  # Web Data
│   ├── internal_mock.pdf     # Sample Document
│   └── synthetic_queries.json # Example Queries
│
├── reports/                  # Output Storage
│   └── *.pdf                 # Generated Reports
│
├── uploads/                  # User File Storage
│   └── *.pdf                 # User Documents
│
└── .gradio/                  # Gradio Configuration
    └── certificate.pem       # SSL Certificate
```

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pharmaceutical-intelligence-platform.git
cd pharmaceutical-intelligence-platform
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

**Option A: Main Application**
```bash
python app.py
```

**Option B: Alternative Entry Point**
```bash
python main.py
```

The application will start on `http://localhost:7860`

## Environment Setup (Optional)

If you plan to integrate with real APIs in the future:

1. Copy the environment template:
```bash
cp .env.example .env
```

2. Edit `.env` file with your API keys:
```bash
# Future API integrations
OPENAI_API_KEY=your_openai_api_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=pharmaceutical-ai
```

**Note**: Current implementation uses mock data and doesn't require API keys.

## Deployment

### Hugging Face Spaces Deployment

1. **Create a new Space on Hugging Face:**
   - Go to [Hugging Face Spaces](https://huggingface.co/spaces)
   - Click "Create new Space"
   - Choose "Gradio" as the SDK
   - Set Space name: `pharmaceutical-intelligence-platform`

2. **Upload your files:**
   ```bash
   git clone https://huggingface.co/spaces/your-username/pharmaceutical-intelligence-platform
   cd pharmaceutical-intelligence-platform
   
   # Copy all project files
   cp -r /path/to/your/project/* .
   
   # Commit and push
   git add .
   git commit -m "Initial deployment"
   git push
   ```

3. **Configure Space settings:**
   - Ensure `app_file: app.py` is set in README.md frontmatter
   - Space will automatically build and deploy
   - Access your deployed app at: `https://huggingface.co/spaces/your-username/pharmaceutical-intelligence-platform`

### Local Development

For development with auto-reload:
```bash
python app.py
```

The app supports:
- Hot reload during development
- File upload for internal documents
- PDF report generation and download
- Example query templates

## How to Use

1. **Enter Research Query**: Type your pharmaceutical research question
2. **Upload Documents** (Optional): Add internal PDFs for analysis
3. **Run Analysis**: Click "Run Analysis" to process your query
4. **Download Report**: Get comprehensive PDF report with insights

## Example Queries

- "Which respiratory diseases show low competition but high patient burden in India?"
- "Analyze market opportunity for repurposing metformin for cancer treatment"
- "What are the patent expiry timelines for statin drugs?"
- "Find clinical trials for diabetes drugs in Phase 3"
- "Analyze trade flows for paracetamol API"
- "What are the unmet needs in cardiovascular therapy area?"
- "Search for repurposing opportunities for aspirin"
- "Analyze FTO risks for developing a new formulation of ibuprofen"

## Architecture

### Multi-Agent System
- **Master Agent (LangGraph)**: Query parsing, task orchestration, and workflow management
- **Worker Agents (CrewAI)**: Specialized data gathering from different sources
- **Report Generator**: Comprehensive PDF report creation with FPDF

### Technology Stack
- **Framework**: Python + LangGraph + CrewAI
- **UI**: Gradio
- **Data Processing**: Pandas, NumPy
- **PDF Generation**: FPDF
- **File Processing**: PyPDF2
- **Mock Data**: JSON files (no external API dependencies)

### Data Flow
1. User query → Master Agent → Query Parser
2. Task decomposition → Worker Agent routing
3. Parallel data gathering → State aggregation
4. Report synthesis → PDF generation
5. Download delivery

## Dependencies

Key requirements from `requirements.txt`:
- `gradio>=4.0.0` - Web interface
- `langgraph` - Agent orchestration
- `langchain` - LLM framework
- `langchain-community` - Community integrations
- `crewai` - Multi-agent framework
- `fpdf` - PDF generation
- `PyPDF2` - PDF processing
- `pandas` - Data manipulation
- `requests` - HTTP requests

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support

For issues and questions:
- Create an issue on GitHub
- Check existing documentation
- Review example queries for usage patterns
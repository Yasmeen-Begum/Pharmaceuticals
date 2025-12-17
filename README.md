---
title: Pharmaceutical Intelligence Platform
emoji: 🧬
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: mit
---

# 🧬 Pharmaceutical Intelligence Platform

**Agentic AI Solution for Pharmaceutical Research and Portfolio Planning**

This platform uses AI agents to analyze multiple data sources and provide comprehensive pharmaceutical intelligence:

## Features

- 📊 **Market Intelligence**: IQVIA data analysis
- 🌍 **Trade Analysis**: EXIM data insights
- 📜 **Patent Landscapes**: USPTO patent analysis
- 🔬 **Clinical Trials**: ClinicalTrials.gov data
- 📄 **Internal Documents**: PDF document analysis
- 🌐 **Web Intelligence**: Real-time web research

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
import gradio as gr
import os
import sys
from datetime import datetime

# Add agents directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "agents"))

from agents.master_agent import app as langgraph_app

# Create uploads directory
os.makedirs("uploads", exist_ok=True)

def run_agentic_ai(query: str, uploaded_file: gr.File = None):
    """Main function to run the agentic AI pipeline"""
    if not query or query.strip() == "":
        return "Please enter a research query to analyze.", None
        
    try:
        # Prepare state
        state = {
            "query": query.strip(),
            "molecule": "",
            "disease": "",
            "therapy_area": "",
            "query_type": "",
            "uploaded_file_path": None,
            "subtasks": [],
            "completed_tasks": [],
            "iqvia": {},
            "exim": {},
            "patent": {},
            "clinical": {},
            "internal": {},
            "web": {},
            "report_path": "",
            "summary": ""
        }
        
        # Handle file upload
        if uploaded_file and hasattr(uploaded_file, 'name'):
            state["uploaded_file_path"] = uploaded_file.name
        
        # Run the graph
        print(f"Processing query: {query}")
        result = langgraph_app.invoke(state)
        print(f"Analysis completed. Result keys: {list(result.keys())}")
        
        # Generate response
        report_path = result.get("report_path", "")
        
        # Create summary
        summary_parts = []
        
        # Process each agent result
        agents = [
            ("iqvia", "Market Analysis"),
            ("exim", "Trade Analysis"), 
            ("patent", "Patent Analysis"),
            ("clinical", "Clinical Trials"),
            ("internal", "Internal Docs"),
            ("web", "Web Intelligence")
        ]
        
        for agent_key, agent_name in agents:
            agent_data = result.get(agent_key, {})
            if isinstance(agent_data, dict):
                if "summary" in agent_data and agent_data["summary"]:
                    summary_text = agent_data["summary"]
                    if agent_key == "internal":
                        summary_text = summary_text[:200] + "..." if len(summary_text) > 200 else summary_text
                    summary_parts.append(f"{agent_name}: {summary_text}")
                elif "status" in agent_data:
                    summary_parts.append(f"{agent_name}: {agent_data['status'].title()}")
                else:
                    summary_parts.append(f"{agent_name}: Completed")
            else:
                summary_parts.append(f"{agent_name}: Completed")
        
        # Combine summary
        if summary_parts:
            summary = "\n\n".join(summary_parts)
        else:
            summary = "Analysis completed successfully."
            
        # Add report info
        if report_path and os.path.exists(report_path):
            summary += f"\n\nReport generated: {os.path.basename(report_path)}"
            return summary, report_path
        else:
            summary += "\n\nReport generation completed."
            return summary, None
        
    except ImportError as e:
        error_msg = f"Missing dependency: {str(e)}\nPlease install required packages: pip install -r requirements.txt"
        return error_msg, None
    except Exception as e:
        import traceback
        error_msg = f"Analysis Error: {str(e)}\n\nPlease try again or contact support if the issue persists."
        print(f"Full error traceback: {traceback.format_exc()}")
        return error_msg, None

# Example queries
example_queries = [
    "Which respiratory diseases show low competition but high patient burden in India?",
    "Analyze market opportunity for repurposing metformin for cancer treatment",
    "What are the patent expiry timelines for statin drugs?",
    "Find clinical trials for diabetes drugs in Phase 3",
    "Analyze trade flows for paracetamol API",
    "What are the unmet needs in cardiovascular therapy area?",
    "Search for repurposing opportunities for aspirin",
    "Analyze FTO risks for developing a new formulation of ibuprofen",
    "What are the market trends for oncology drugs in India?",
    "Find opportunities for developing extended-release formulations"
]

# Create Gradio interface
with gr.Blocks(title="Pharmaceutical Agentic AI", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # Pharmaceutical Intelligence Platform
    
    **Agentic AI Solution for Pharmaceutical Research and Portfolio Planning**
    
    This platform uses AI agents to analyze:
    - Market intelligence (IQVIA data)
    - Trade flows (EXIM data)
    - Patent landscapes (USPTO data)
    - Clinical trials (ClinicalTrials.gov)
    - Internal documents
    - Web intelligence
    
    Enter your query or select an example below.
    """)
    
    with gr.Row():
        with gr.Column(scale=2):
            query_input = gr.Textbox(
                label="Enter your research query",
                placeholder="e.g., Which respiratory diseases show low competition but high patient burden in India?",
                lines=3
            )
            
            file_upload = gr.File(
                label="Upload internal document (optional)",
                file_types=[".pdf"]
            )
            
            submit_btn = gr.Button("Run Analysis", variant="primary", size="lg")
        
        with gr.Column(scale=1):
            gr.Markdown("### Example Queries")
            examples = gr.Examples(
                examples=example_queries,
                inputs=query_input
            )
    
    with gr.Row():
        output_text = gr.Textbox(
            label="Analysis Results",
            lines=15,
            interactive=False
        )
        
        report_download = gr.File(
            label="Download Report",
            visible=True
        )
    
    submit_btn.click(
        fn=run_agentic_ai,
        inputs=[query_input, file_upload],
        outputs=[output_text, report_download]
    )
    
   

if __name__ == "__main__":
    # For Hugging Face Spaces, use default settings
    demo.launch()
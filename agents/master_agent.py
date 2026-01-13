import sys
import os
# Ensure parent directory is in path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from langgraph.graph import StateGraph, END
from typing import TypedDict, Any
from agents.query_parser import QueryParser
from agents.iqvia_agent import fetch_iqvia_data
from agents.exim_agent import fetch_exim_data
from agents.patent_agent import fetch_patent_data
from agents.clinical_agent import fetch_clinical_trials
from agents.internal_agent import summarize_internal_docs
from agents.web_agent import perform_web_search
from agents.report_agent import generate_pdf_report

class State(TypedDict):
    query: str
    molecule: str
    disease: str
    therapy_area: str
    query_type: str
    uploaded_file_path: str
    subtasks: list
    completed_tasks: list
    iqvia: dict
    exim: dict
    patent: dict
    clinical: dict
    internal: dict
    web: dict
    report_path: str
    summary: str

def master_orchestrator(state: State) -> State:
    """Master Agent: Parses query and determines workflow"""
    query = state.get("query", "")
    
    # Parse query
    parser = QueryParser()
    parsed = parser.parse_query(query)
    
    # Update state with parsed information
    state.update(parsed)
    
    # Ensure molecule is set - use therapy_area, disease, or query snippet
    if not state.get("molecule") or state.get("molecule") == "None":
        if state.get("therapy_area"):
            state["molecule"] = state["therapy_area"].title()
        elif state.get("disease"):
            state["molecule"] = state["disease"].title()
        else:
            # Use first meaningful words from query
            query_words = query.split()[:3]
            state["molecule"] = " ".join([w for w in query_words if w.lower() not in ['which', 'what', 'where', 'when', 'how', 'the', 'are', 'for', 'and', 'but']])[:30]
    
    # Determine which agents to activate
    subtasks = parser.decompose_query(parsed)
    state["subtasks"] = subtasks
    state["completed_tasks"] = []
    
    return state

def route_after_master(state: State) -> str:
    """Route to first agent after master orchestration"""
    subtasks = state.get("subtasks", [])
    if subtasks:
        return subtasks[0]
    return "report"

def route_after_agent(state: State) -> str:
    """Route to next agent or report"""
    subtasks = state.get("subtasks", [])
    completed = state.get("completed_tasks", [])
    
    # Find next uncompleted task
    for task in subtasks:
        if task not in completed:
            # Mark as completed
            if task not in completed:
                completed.append(task)
                state["completed_tasks"] = completed
            return task
    
    return "report"

# Create graph
graph = StateGraph(State)

# Add nodes
graph.add_node("master", master_orchestrator)
graph.add_node("iqvia", fetch_iqvia_data)
graph.add_node("exim", fetch_exim_data)
graph.add_node("patent", fetch_patent_data)
graph.add_node("clinical", fetch_clinical_trials)
graph.add_node("internal", summarize_internal_docs)
graph.add_node("web", perform_web_search)
graph.add_node("report", generate_pdf_report)

# Set entry point
graph.set_entry_point("master")

# Route from master to first agent
graph.add_conditional_edges(
    "master",
    route_after_master,
    {
        "iqvia": "iqvia",
        "exim": "exim",
        "patent": "patent",
        "clinical": "clinical",
        "internal": "internal",
        "web": "web",
        "report": "report"
    }
)

# Add conditional edges from each agent to next or report
for agent_name in ["iqvia", "exim", "patent", "clinical", "internal", "web"]:
    graph.add_conditional_edges(
        agent_name,
        route_after_agent,
        {
            "iqvia": "iqvia",
            "exim": "exim",
            "patent": "patent",
            "clinical": "clinical",
            "internal": "internal",
            "web": "web",
            "report": "report"
        }
    )

# Report always ends
graph.add_edge("report", END)

# Compile app
app = graph.compile()

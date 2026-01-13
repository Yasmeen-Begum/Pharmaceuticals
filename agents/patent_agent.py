import json
import os
from typing import Dict, Any
from datetime import datetime, timedelta

def fetch_patent_data(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Patent Landscape Agent: Searches for active patents, expiry timelines, FTO flags
    """
    molecule = state.get("molecule", "")
    therapy_area = state.get("therapy_area", "")
    query = state.get("query", "")
    
    search_key = molecule or therapy_area or query
    search_key_lower = search_key.lower() if search_key else ""
    
    mock_file = os.path.join("mock_data", "patent_mock.json")
    
    try:
        with open(mock_file, 'r') as f:
            data = json.load(f)
        
        # Try exact match first, then case-insensitive
        result = None
        for key in data.keys():
            if key.lower() == search_key_lower:
                result = data[key]
                break
        
        if not result:
            result = {
                "active_patents": [],
                "patent_expiry_timeline": [],
                "freedom_to_operate": "unknown",
                "fto_risks": [],
                "innovation_trends": [],
                "key_patents": [],
                "competitive_filings": {}
            }
        
        # Calculate FTO status
        fto_status = result.get("freedom_to_operate", "unknown")
        if result.get("active_patents"):
            fto_status = "restricted" if len(result["active_patents"]) > 0 else "clear"
        
        output = {
            "status": "success",
            "data": result,
            "summary": f"Patent analysis for {search_key}: {len(result.get('active_patents', []))} active patents, "
                      f"FTO status: {fto_status}. "
                      f"Key expiries: {len(result.get('patent_expiry_timeline', []))} patents expiring soon."
        }
        
    except FileNotFoundError:
        output = {
            "status": "error",
            "data": {},
            "summary": "Patent mock data file not found"
        }
    except Exception as e:
        output = {
            "status": "error",
            "data": {},
            "summary": f"Error fetching patent data: {str(e)}"
        }
    
    return {**state, "patent": output}

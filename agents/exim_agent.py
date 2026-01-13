import json
import os
from typing import Dict, Any

def fetch_exim_data(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    EXIM Trends Agent: Extracts export-import data for APIs/formulations
    """
    molecule = state.get("molecule", "")
    api_name = state.get("api_name", "")
    query = state.get("query", "")
    
    search_key = api_name or molecule or query
    
    mock_file = os.path.join("mock_data", "exim_mock.json")
    
    try:
        with open(mock_file, 'r') as f:
            data = json.load(f)
        
        result = data.get(search_key, {
            "export_volume_kg": 0,
            "import_volume_kg": 0,
            "net_trade_balance": 0,
            "top_export_destinations": [],
            "top_import_sources": [],
            "trade_trend": "stable",
            "api_availability": "unknown",
            "formulation_trade": {}
        })
        
        output = {
            "status": "success",
            "data": result,
            "summary": f"Trade analysis for {search_key}: Export {result.get('export_volume_kg', 0)}kg, "
                      f"Import {result.get('import_volume_kg', 0)}kg. "
                      f"Top destinations: {', '.join(result.get('top_export_destinations', [])[:3])}"
        }
        
    except FileNotFoundError:
        output = {
            "status": "error",
            "data": {},
            "summary": "EXIM mock data file not found"
        }
    except Exception as e:
        output = {
            "status": "error",
            "data": {},
            "summary": f"Error fetching EXIM data: {str(e)}"
        }
    
    return {**state, "exim": output}
import json
import os
from typing import Dict, Any

def fetch_iqvia_data(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    IQVIA Insights Agent: Fetches market size, growth, competitor data
    """
    query = state.get("query", "")
    molecule = state.get("molecule", "")
    therapy_area = state.get("therapy_area", "")
    disease = state.get("disease", "")
    
    # Determine search key
    search_key = molecule or therapy_area or disease or query
    
    mock_file = os.path.join("mock_data", "iqvia_mock.json")
    
    try:
        with open(mock_file, 'r') as f:
            data = json.load(f)
        
        # Try to find matching data (case-insensitive)
        result = None
        search_keys = [molecule, therapy_area, disease, query]
        for key in search_keys:
            if key:
                # Try exact match
                if key in data:
                    result = data[key]
                    break
                # Try case-insensitive match
                key_lower = key.lower()
                for data_key in data.keys():
                    if data_key.lower() == key_lower:
                        result = data[data_key]
                        break
                if result:
                    break
        
        if not result:
            # Default structure
            result = {
                "market_size_millions_usd": 0,
                "growth_rate_cagr_percent": 0,
                "competitors": [],
                "therapy_area": therapy_area or "Unknown",
                "market_trend": "stable",
                "volume_shifts": {},
                "geographic_distribution": {}
            }
        
        # Format output
        output = {
            "status": "success",
            "data": result,
            "summary": f"Market analysis for {search_key}: Market size ${result.get('market_size_millions_usd', 0)}M, "
                      f"Growth rate {result.get('growth_rate_cagr_percent', 0)}% CAGR, "
                      f"{len(result.get('competitors', []))} major competitors identified."
        }
        
    except FileNotFoundError:
        output = {
            "status": "error",
            "data": {},
            "summary": "IQVIA mock data file not found"
        }
    except Exception as e:
        output = {
            "status": "error",
            "data": {},
            "summary": f"Error fetching IQVIA data: {str(e)}"
        }
    
    return {**state, "iqvia": output}
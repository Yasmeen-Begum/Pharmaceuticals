import json
import os
from typing import Dict, Any

def fetch_clinical_trials(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Clinical Trials Agent: Fetches trial pipeline data
    """
    molecule = state.get("molecule", "")
    disease = state.get("disease", "")
    therapy_area = state.get("therapy_area", "")
    query = state.get("query", "")
    
    search_key = molecule or disease or therapy_area or query
    search_key_lower = search_key.lower() if search_key else ""
    
    mock_file = os.path.join("mock_data", "clinical_mock.json")
    
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
                "ongoing_trials": [],
                "completed_trials": [],
                "sponsors": [],
                "trial_phases": {
                    "phase_1": 0,
                    "phase_2": 0,
                    "phase_3": 0,
                    "phase_4": 0
                },
                "completion_dates": [],
                "trial_status": "unknown",
                "key_trials": []
            }
        
        total_trials = len(result.get("ongoing_trials", []))
        phase_3_trials = result.get("trial_phases", {}).get("phase_3", 0)
        
        output = {
            "status": "success",
            "data": result,
            "summary": f"Clinical trials for {search_key}: {total_trials} ongoing trials, "
                      f"{phase_3_trials} in Phase 3. "
                      f"Key sponsors: {', '.join(result.get('sponsors', [])[:3])}"
        }
        
    except FileNotFoundError:
        output = {
            "status": "error",
            "data": {},
            "summary": "Clinical trials mock data file not found"
        }
    except Exception as e:
        output = {
            "status": "error",
            "data": {},
            "summary": f"Error fetching clinical trials data: {str(e)}"
        }
    
    return {**state, "clinical": output}

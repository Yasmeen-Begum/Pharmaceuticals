import json
import os
from typing import Dict, Any

def perform_web_search(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Web Intelligence Agent: Performs real-time web search simulation
    """
    query = state.get("query", "")
    molecule = state.get("molecule", "")
    disease = state.get("disease", "")
    therapy_area = state.get("therapy_area", "")
    
    search_key = query or molecule or disease or therapy_area
    
    mock_file = os.path.join("mock_data", "web_search_mock.json")
    
    try:
        if os.path.exists(mock_file):
            with open(mock_file, 'r') as f:
                data = json.load(f)
            result = data.get(search_key, {})
        else:
            result = {}
        
        # Default structure if not found
        if not result:
            result = {
                "guidelines": [
                    f"Clinical guidelines for {search_key}",
                    f"Treatment protocols for {search_key}"
                ],
                "publications": [
                    f"Recent study: {search_key} efficacy",
                    f"Review article: {search_key} mechanism of action"
                ],
                "news": [
                    f"Latest news on {search_key}",
                    f"Industry updates: {search_key}"
                ],
                "forums": [
                    f"Patient discussion: {search_key}",
                    f"Healthcare provider insights: {search_key}"
                ],
                "real_world_evidence": []
            }
        
        # Create summary
        total_results = (
            len(result.get("guidelines", [])) +
            len(result.get("publications", [])) +
            len(result.get("news", [])) +
            len(result.get("forums", []))
        )
        
        output = {
            "status": "success",
            "data": result,
            "summary": f"Web search for {search_key}: Found {total_results} relevant results including "
                      f"{len(result.get('guidelines', []))} guidelines, "
                      f"{len(result.get('publications', []))} publications, "
                      f"{len(result.get('news', []))} news articles."
        }
        
    except Exception as e:
        output = {
            "status": "error",
            "data": {},
            "summary": f"Error performing web search: {str(e)}"
        }
    
    return {**state, "web": output}
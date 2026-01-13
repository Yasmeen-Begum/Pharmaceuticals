import re
from typing import Dict, List, Any

class QueryParser:
    """Parse user queries and extract key entities"""
    
    @staticmethod
    def parse_query(query: str) -> Dict[str, Any]:
        """Extract molecule, disease, therapy area, and other entities from query"""
        query_lower = query.lower()
        
        # Extract molecule names (common patterns)
        molecule_patterns = [
            r'\b([A-Z][a-z]+(?:[A-Z][a-z]+)*)\b',  # Capitalized words
            r'molecule[:\s]+([A-Za-z0-9-]+)',
            r'drug[:\s]+([A-Za-z0-9-]+)',
            r'compound[:\s]+([A-Za-z0-9-]+)'
        ]
        
        # Extract disease/therapy area
        disease_keywords = ['disease', 'indication', 'therapy', 'condition', 'disorder']
        therapy_areas = ['respiratory', 'cardiovascular', 'oncology', 'diabetes', 
                        'neurology', 'infectious', 'autoimmune', 'gastrointestinal']
        
        parsed = {
            "original_query": query,
            "molecule": None,
            "disease": None,
            "therapy_area": None,
            "query_type": "general",
            "entities": []
        }
        
        # Extract therapy area
        for area in therapy_areas:
            if area in query_lower:
                parsed["therapy_area"] = area
                # If no molecule found, use therapy area as molecule identifier
                if not parsed["molecule"]:
                    parsed["molecule"] = area.title()
                break
        
        # Extract disease/indication
        for keyword in disease_keywords:
            if keyword in query_lower:
                # Try to extract what comes after the keyword
                pattern = f'{keyword}[:\\s]+([A-Za-z\\s]+)'
                match = re.search(pattern, query_lower)
                if match:
                    disease_name = match.group(1).strip()
                    parsed["disease"] = disease_name
                    # If no molecule found, use disease as molecule identifier
                    if not parsed["molecule"]:
                        parsed["molecule"] = disease_name.title()
        
        # If still no molecule, try to extract from common drug names in query
        if not parsed["molecule"]:
            common_drugs = ['metformin', 'aspirin', 'paracetamol', 'ibuprofen', 'atorvastatin', 
                          'rosuvastatin', 'albuterol', 'salmeterol', 'insulin', 'warfarin']
            for drug in common_drugs:
                if drug in query_lower:
                    parsed["molecule"] = drug.title()
                    break
        
        # If still no molecule, use therapy area or first meaningful word from query
        if not parsed["molecule"]:
            if parsed["therapy_area"]:
                parsed["molecule"] = parsed["therapy_area"].title()
            else:
                # Extract first meaningful capitalized word or therapy-related term
                words = query.split()
                for word in words:
                    if word[0].isupper() and len(word) > 3 and word.lower() not in ['which', 'what', 'where', 'when', 'how', 'the', 'are', 'for', 'and', 'but']:
                        parsed["molecule"] = word
                        break
        
        # Determine query type (check opportunity first as it's most comprehensive)
        if "repurposing" in query_lower or "unmet" in query_lower or "opportunity" in query_lower:
            parsed["query_type"] = "opportunity_analysis"
        elif "market" in query_lower or "sales" in query_lower or "iqvia" in query_lower:
            parsed["query_type"] = "market_analysis"
        elif "patent" in query_lower or "ip" in query_lower or "freedom" in query_lower or "fto" in query_lower:
            parsed["query_type"] = "patent_analysis"
        elif "trial" in query_lower or "clinical" in query_lower:
            parsed["query_type"] = "clinical_analysis"
        elif "trade" in query_lower or "export" in query_lower or "import" in query_lower or "exim" in query_lower:
            parsed["query_type"] = "trade_analysis"
        
        return parsed
    
    @staticmethod
    def decompose_query(parsed_query: Dict[str, Any]) -> List[str]:
        """Break down query into subtasks for worker agents"""
        subtasks = []
        query_type = parsed_query["query_type"]
        
        if query_type == "opportunity_analysis" or query_type == "general":
            # Full analysis pipeline
            subtasks = [
                "iqvia", "exim", "patent", "clinical", "internal", "web"
            ]
        elif query_type == "market_analysis":
            subtasks = ["iqvia", "exim", "web"]
        elif query_type == "patent_analysis":
            subtasks = ["patent", "clinical", "web"]
        elif query_type == "clinical_analysis":
            subtasks = ["clinical", "patent", "web"]
        elif query_type == "trade_analysis":
            subtasks = ["exim", "iqvia"]
        
        return subtasks


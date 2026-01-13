from PyPDF2 import PdfReader
import os
from typing import Dict, Any

def summarize_internal_docs(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Internal Knowledge Agent: Retrieves and summarizes internal documents
    """
    uploaded_file = state.get("uploaded_file_path")
    query = state.get("query", "")
    molecule = state.get("molecule", "")
    
    # Determine which PDF to use
    if uploaded_file and os.path.exists(uploaded_file):
        pdf_path = uploaded_file
        source = "uploaded"
    else:
        pdf_path = os.path.join("mock_data", "internal_mock.pdf")
        source = "default"
    
    try:
        if os.path.exists(pdf_path):
            reader = PdfReader(pdf_path)
            full_text = ""
            
            # Extract text from all pages
            for page_num, page in enumerate(reader.pages):
                try:
                    page_text = page.extract_text()
                    full_text += f"\n--- Page {page_num + 1} ---\n{page_text}"
                except:
                    continue
            
            # Create summary (first 2000 chars + key sections)
            summary = full_text[:2000]
            
            # Try to extract key sections
            key_sections = []
            if "strategy" in full_text.lower():
                key_sections.append("Strategy discussion found")
            if "market" in full_text.lower():
                key_sections.append("Market insights found")
            if "clinical" in full_text.lower():
                key_sections.append("Clinical data found")
            
            output = {
                "status": "success",
                "source": source,
                "summary": summary,
                "key_sections": key_sections,
                "total_pages": len(reader.pages),
                "full_text_length": len(full_text)
            }
        else:
            output = {
                "status": "error",
                "summary": f"PDF file not found: {pdf_path}",
                "key_sections": []
            }
            
    except Exception as e:
        output = {
            "status": "error",
            "summary": f"Error reading PDF: {str(e)}",
            "key_sections": []
        }
    
    return {**state, "internal": output}
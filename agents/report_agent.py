from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import os
from datetime import datetime
from typing import Dict, Any

def generate_pdf_report(state: Dict[str, Any]) -> Dict[str, Any]:
    """Generate PDF report using ReportLab"""
    try:
        os.makedirs("reports", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        molecule = state.get("molecule", "") or state.get("therapy_area", "") or state.get("disease", "") or "Query"
        molecule = molecule.title() if molecule else "Query"
        molecule_clean = molecule.replace(' ', '_').replace('/', '_')[:30]
        filename = f"reports/pharma_intelligence_report_{molecule_clean}_{timestamp}.pdf"

        # Create PDF document
        doc = SimpleDocTemplate(filename, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        # Title
        title = Paragraph("Pharmaceutical Intelligence Report", styles['Title'])
        story.append(title)
        story.append(Spacer(1, 12))

        # Metadata
        meta_info = f"""
        <b>Generated:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br/>
        <b>Query:</b> {state.get('query', 'N/A')}<br/>
        <b>Molecule/Therapy Area:</b> {molecule}<br/>
        """
        story.append(Paragraph(meta_info, styles['Normal']))
        story.append(Spacer(1, 12))

        # Executive Summary
        story.append(Paragraph("Executive Summary", styles['Heading1']))
        summary_text = f"This report provides comprehensive intelligence on {molecule} across market dynamics, trade flows, patent landscape, clinical development, internal insights, and web intelligence."
        story.append(Paragraph(summary_text, styles['Normal']))
        story.append(Spacer(1, 12))

        # Sections
        sections = [
            ("IQVIA Market Intelligence", state.get("iqvia", {})),
            ("EXIM Trade Analysis", state.get("exim", {})),
            ("Patent Landscape", state.get("patent", {})),
            ("Clinical Trials Pipeline", state.get("clinical", {})),
            ("Internal Document Summary", state.get("internal", {})),
            ("Web Intelligence", state.get("web", {}))
        ]

        for section_name, section_data in sections:
            story.append(Paragraph(section_name, styles['Heading2']))
            
            if isinstance(section_data, dict) and section_data:
                if "summary" in section_data:
                    summary_text = section_data["summary"][:500] + "..." if len(section_data["summary"]) > 500 else section_data["summary"]
                    story.append(Paragraph(f"<b>Summary:</b> {summary_text}", styles['Normal']))
                
                # Add other data
                for key, value in section_data.items():
                    if key not in ["summary", "status"] and value:
                        if isinstance(value, (str, int, float)):
                            story.append(Paragraph(f"<b>{key.replace('_', ' ').title()}:</b> {str(value)[:200]}", styles['Normal']))
                        elif isinstance(value, list) and value:
                            items = ", ".join([str(item)[:50] for item in value[:5]])
                            story.append(Paragraph(f"<b>{key.replace('_', ' ').title()}:</b> {items}", styles['Normal']))
            else:
                story.append(Paragraph("No data available for this section.", styles['Normal']))
            
            story.append(Spacer(1, 12))

        # Build PDF
        doc.build(story)
        
        return {**state, "report_path": filename}
        
    except Exception as e:
        print(f"Error generating PDF: {str(e)}")
        # Return a simple text summary instead
        summary = f"Analysis completed for: {state.get('query', 'N/A')}\n"
        summary += f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        summary += "PDF generation failed, but analysis was successful."
        
        return {**state, "report_path": "", "summary": summary}
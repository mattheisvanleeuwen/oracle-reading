"""
Oracle PDF Generator - Creates beautifully formatted PDF reports.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Frame
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import datetime
from io import BytesIO


def create_oracle_pdf(reading_data, output_path=None):
    """
    Create a professionally formatted PDF report for an oracle reading.
    
    Args:
        reading_data: Dictionary with reading information from oracle_core.generate_reading_data()
        output_path: Path to save PDF (optional, returns BytesIO if None)
    
    Returns:
        BytesIO object if output_path is None, otherwise None
    """
    # Create buffer or file
    if output_path is None:
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter,
                               leftMargin=0.75*inch, rightMargin=0.75*inch,
                               topMargin=0.75*inch, bottomMargin=0.75*inch)
    else:
        doc = SimpleDocTemplate(str(output_path), pagesize=letter,
                               leftMargin=0.75*inch, rightMargin=0.75*inch,
                               topMargin=0.75*inch, bottomMargin=0.75*inch)
    
    # Build content
    story = []
    
    # Custom styles
    styles = getSampleStyleSheet()
    
    # Title style (large, centered)
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2C1810'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Subtitle style
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#5D4E37'),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Large symbol style
    symbol_style = ParagraphStyle(
        'SymbolStyle',
        parent=styles['Normal'],
        fontSize=36,
        textColor=colors.HexColor('#8B4513'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    # Hexagram title style
    hex_title_style = ParagraphStyle(
        'HexagramTitle',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=colors.HexColor('#2C1810'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Section header style
    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading3'],
        fontSize=14,
        textColor=colors.HexColor('#5D4E37'),
        spaceAfter=8,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    # Body text style - simple and clean
    body_style = ParagraphStyle(
        'BodyText',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.black,
        spaceAfter=8,
        alignment=TA_LEFT,
        leading=14
    )
    
    # Small text style
    small_style = ParagraphStyle(
        'SmallText',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#666666'),
        spaceAfter=4,
        alignment=TA_CENTER
    )
    
    # ========================================================================
    # PAGE 1: THE READING
    # ========================================================================
    
    # Title
    story.append(Paragraph("Oracle Reading", title_style))
    
    # User name if provided
    if reading_data.get("user_name"):
        story.append(Paragraph(f"Reading for {reading_data['user_name']}", subtitle_style))
    
    # Timestamp
    timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    story.append(Paragraph(timestamp, small_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Hexagram symbols and title
    hex_num = reading_data['hexagram']['number']
    hex_title = reading_data['hexagram']['title']
    lower_sym = reading_data['lower_trigram']['symbol']
    upper_sym = reading_data['upper_trigram']['symbol']
    
    # Large trigram symbols
    symbols_text = f"{upper_sym}<br/>{lower_sym}"
    story.append(Paragraph(symbols_text, symbol_style))
    
    # Hexagram info
    story.append(Paragraph(f"Hexagram {hex_num}: {hex_title}", hex_title_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Structure info
    structure_text = f"""
    <b>Upper Trigram (Outer/Strategy):</b> {upper_sym} {reading_data['upper_trigram']['name']} 
    — flavored by {reading_data['rune2']['name']} {reading_data['rune2']['symbol']}<br/>
    <b>Lower Trigram (Inner/Foundation):</b> {lower_sym} {reading_data['lower_trigram']['name']} 
    — flavored by {reading_data['rune1']['name']} {reading_data['rune1']['symbol']}
    """
    story.append(Paragraph(structure_text, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Two-column rune display - use oracle interpretations only (not full content)
    rune1_header = f"<b>Rune 1: {reading_data['rune1']['name']} {reading_data['rune1']['symbol']}</b><br/>(The Root)"
    rune2_header = f"<b>Rune 2: {reading_data['rune2']['name']} {reading_data['rune2']['symbol']}</b><br/>(The Context)"
    
    rune_table_data = [
        [Paragraph(rune1_header, section_style), Paragraph(rune2_header, section_style)],
        [Paragraph(reading_data['rune1']['oracle'], body_style), Paragraph(reading_data['rune2']['oracle'], body_style)]
    ]
    
    rune_table = Table(rune_table_data, colWidths=[3.25*inch, 3.25*inch])
    rune_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    
    story.append(rune_table)
    story.append(Spacer(1, 0.15*inch))
    
    # Hexagram content section
    story.append(Paragraph(f"The Hexagram: {hex_title}", section_style))
    
    # Include COMPLETE hexagram text - split into paragraphs for better formatting
    hex_paragraphs = reading_data['hexagram']['content'].split('\n\n')
    for para in hex_paragraphs:
        if para.strip() and not para.strip().startswith('#'):
            story.append(Paragraph(para.strip(), body_style))
    
    # Page break
    story.append(PageBreak())
    
    # ========================================================================
    # PAGE 2: THE INTERPRETATION
    # ========================================================================
    
    # Title
    story.append(Paragraph("Oracle Interpretation", title_style))
    
    # User name if provided
    if reading_data.get("user_name"):
        story.append(Paragraph(f"Interpretation for {reading_data['user_name']}", subtitle_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    # Hexagram symbols display
    symbols_text = f"{upper_sym}<br/>{lower_sym}"
    story.append(Paragraph(symbols_text, symbol_style))
    
    # Use AI interpretation if available, otherwise template interpretation
    interpretation_text = reading_data.get('ai_interpretation') or reading_data.get('narrative_interpretation', '')
    story.append(Paragraph(interpretation_text, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Quick Reference Box
    story.append(Paragraph("Quick Reference", section_style))
    ref_data = [
        ['Hexagram:', f"{hex_num} - {hex_title}"],
        ['Lower Trigram (Inner):', f"{lower_sym} {reading_data['lower_trigram']['name']} via {reading_data['rune1']['name']} {reading_data['rune1']['symbol']}"],
        ['Upper Trigram (Outer):', f"{upper_sym} {reading_data['upper_trigram']['name']} via {reading_data['rune2']['name']} {reading_data['rune2']['symbol']}"],
        ['Reading Date:', datetime.now().strftime("%B %d, %Y")]
    ]
    
    ref_table = Table(ref_data, colWidths=[1.5*inch, 5*inch])
    ref_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F5F5DC')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2C1810')),
        ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#D3D3D3')),
    ]))
    
    story.append(ref_table)
    
    # Build PDF
    doc.build(story)
    
    # Return buffer if no output path
    if output_path is None:
        buffer.seek(0)
        return buffer
    
    return None



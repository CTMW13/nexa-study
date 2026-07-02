import html
import re
from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def get_document_title(text):
    lines = text.splitlines()

    for line in lines:
        line = line.strip()

        if line.startswith("# "):
            title = line[2:].strip()
            break
    else:
        title = "Nexa Study Revision Pack"

    if not title:
        title = "Nexa Study Revision Pack"

    return title


def make_safe_filename(text):
    title = get_document_title(text)

    title = title.lower()
    title = re.sub(r"[^a-z0-9]+", "_", title)
    title = title.strip("_")

    if not title:
        title = "nexa_study_revision_pack"

    return title


def register_pdf_fonts():
    font_name = "Helvetica"
    bold_font_name = "Helvetica-Bold"

    try:
        pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
        pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))
        font_name = "Arial"
        bold_font_name = "Arial-Bold"
    except Exception:
        pass

    return font_name, bold_font_name


def flashcards_to_pdf(flashcards, pdf_title):
    """
    Creates a simple flashcard PDF with one card per page.
    """

    buffer = BytesIO()

    font_name, bold_font_name = register_pdf_fonts()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title=f"{pdf_title} Flashcards",
        author="Nexa Study",
        subject="AI-generated flashcards",
        creator="Nexa Study",
    )

    title_style = ParagraphStyle(
        name="FlashcardTitle",
        fontName=bold_font_name,
        fontSize=18,
        leading=22,
        spaceAfter=16,
        textColor=colors.HexColor("#1E3A5F"),
    )

    label_style = ParagraphStyle(
        name="FlashcardLabel",
        fontName=bold_font_name,
        fontSize=12,
        leading=16,
        spaceAfter=6,
        textColor=colors.HexColor("#C96A43"),
    )

    body_style = ParagraphStyle(
        name="FlashcardBody",
        fontName=font_name,
        fontSize=13,
        leading=18,
        spaceAfter=14,
        textColor=colors.HexColor("#334155"),
    )

    story = []

    for index, card in enumerate(flashcards, start=1):
        story.append(Paragraph(f"Flashcard {index}", title_style))
        story.append(Paragraph("Front", label_style))
        story.append(Paragraph(html.escape(card["front"]), body_style))
        story.append(Spacer(1, 14))
        story.append(Paragraph("Back", label_style))
        story.append(Paragraph(html.escape(card["back"]), body_style))

        if index != len(flashcards):
            story.append(PageBreak())

    doc.build(story)

    pdf_data = buffer.getvalue()
    buffer.close()

    return pdf_data


def convert_markdown_to_pdf(markdown_text, pdf_title):
    buffer = BytesIO()

    font_name, bold_font_name = register_pdf_fonts()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title=pdf_title,
        author="Nexa Study",
        subject="AI-generated STEM revision pack",
        creator="Nexa Study",
    )

    normal_style = ParagraphStyle(
        name="NormalText",
        fontName=font_name,
        fontSize=10.5,
        leading=15,
        spaceAfter=7,
    )

    table_style_text = ParagraphStyle(
        name="TableText",
        fontName=font_name,
        fontSize=9.5,
        leading=12,
    )

    heading1_style = ParagraphStyle(
        name="Heading1",
        fontName=bold_font_name,
        fontSize=20,
        leading=24,
        spaceBefore=8,
        spaceAfter=12,
    )

    heading2_style = ParagraphStyle(
        name="Heading2",
        fontName=bold_font_name,
        fontSize=15,
        leading=19,
        spaceBefore=10,
        spaceAfter=8,
    )

    heading3_style = ParagraphStyle(
        name="Heading3",
        fontName=bold_font_name,
        fontSize=12.5,
        leading=16,
        spaceBefore=8,
        spaceAfter=6,
    )

    quote_style = ParagraphStyle(
        name="Quote",
        fontName=font_name,
        fontSize=10,
        leading=14,
        leftIndent=14,
        spaceBefore=6,
        spaceAfter=8,
    )

    story = []

    def clean_inline_formatting(text):
        text = html.escape(text)
        text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
        return text

    def is_table_separator(line):
        stripped = line.strip()

        if not stripped.startswith("|"):
            return False

        content = stripped.replace("|", "").replace("-", "").replace(":", "").strip()
        return content == ""

    def parse_table_row(line):
        return [cell.strip() for cell in line.strip().strip("|").split("|")]

    def make_pdf_table(table_data):
        if not table_data:
            return None

        column_count = len(table_data[0])
        usable_width = A4[0] - (4 * cm)
        column_width = usable_width / column_count
        column_widths = [column_width] * column_count

        table = Table(
            table_data,
            hAlign="LEFT",
            colWidths=column_widths,
            repeatRows=1,
        )

        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                    ("TOPPADDING", (0, 0), (-1, -1), 6),
                    ("LEFTPADDING", (0, 0), (-1, -1), 6),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ]
            )
        )

        return table

    lines = markdown_text.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        if not line:
            story.append(Spacer(1, 6))
            i += 1
            continue

        if line.startswith("|") and i + 1 < len(lines) and is_table_separator(lines[i + 1]):
            table_data = []

            header_cells = parse_table_row(line)
            table_data.append(
                [
                    Paragraph(f"<b>{clean_inline_formatting(cell)}</b>", table_style_text)
                    for cell in header_cells
                ]
            )

            i += 2

            while i < len(lines) and lines[i].strip().startswith("|"):
                row_cells = parse_table_row(lines[i])

                while len(row_cells) < len(header_cells):
                    row_cells.append("")

                row_cells = row_cells[: len(header_cells)]

                table_data.append(
                    [
                        Paragraph(clean_inline_formatting(cell), table_style_text)
                        for cell in row_cells
                    ]
                )

                i += 1

            pdf_table = make_pdf_table(table_data)

            if pdf_table:
                story.append(pdf_table)
                story.append(Spacer(1, 10))

            continue

        if line.startswith("# "):
            story.append(Paragraph(clean_inline_formatting(line[2:]), heading1_style))

        elif line.startswith("## "):
            story.append(Paragraph(clean_inline_formatting(line[3:]), heading2_style))

        elif line.startswith("### "):
            story.append(Paragraph(clean_inline_formatting(line[4:]), heading3_style))

        elif line.startswith("- "):
            story.append(Paragraph(clean_inline_formatting("• " + line[2:]), normal_style))

        elif line.startswith("* "):
            story.append(Paragraph(clean_inline_formatting("• " + line[2:]), normal_style))

        elif line.startswith("> "):
            story.append(Paragraph(clean_inline_formatting(line[2:]), quote_style))

        else:
            story.append(Paragraph(clean_inline_formatting(line), normal_style))

        i += 1

    doc.build(story)

    pdf_data = buffer.getvalue()
    buffer.close()

    return pdf_data

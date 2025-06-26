
#
# utils/pdf_generator.py

# from fpdf import FPDF
# import os
# from textwrap import wrap

# class StylishPDF(FPDF):
#     def header(self):
#         self.set_font("Helvetica", "B", 16)
#         self.set_text_color(0, 102, 204)  # blue
#         self.cell(0, 10, "Enhanced Pitch Deck by PitchPal-AI", ln=True, align="C")
#         self.ln(5)
#         self.set_draw_color(0, 102, 204)
#         self.set_line_width(0.5)
#         self.line(10, self.get_y(), 200, self.get_y())  # horizontal line
#         self.ln(10)

#     def footer(self):
#         self.set_y(-15)
#         self.set_font("Helvetica", "I", 10)
#         self.set_text_color(150)  # grey
#         self.cell(0, 10, "Developed by Aryan Patel - PitchPal-AI", 0, 0, "C")

# def generate_pitch_pdf(text):
#     if hasattr(text, "output"):
#         text = text.output

#     if not isinstance(text, str):
#         raise ValueError("generate_pitch_pdf() expected a string, got: " + str(type(text)))

#     pdf = StylishPDF()
#     pdf.add_page()

#     pdf.set_font("Helvetica", "", 12)
#     pdf.set_text_color(30)  # dark gray

#     lines = text.split("\n")
#     for line in lines:
#         wrapped = wrap(line, width=90)
#         for wrap_line in wrapped:
#             pdf.cell(0, 10, wrap_line, ln=True)

#     output_path = "outputs/improved_pitch.pdf"
#     os.makedirs(os.path.dirname(output_path), exist_ok=True)
#     pdf.output(output_path)
#     return output_path
# utils/pdf_generator.py


from fpdf import FPDF
import os
from textwrap import wrap

class StylishPDF(FPDF):
    def header(self):
        # Add small circular logo
        try:
            self.image("images/logo.png", x=10, y=8, w=15, h=15)
        except Exception:
            pass  # Don't break if logo not found

        # Header Title
        self.set_xy(30, 10)
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(0, 102, 204)
        self.cell(0, 10, "Enhanced Pitch Deck by PitchPal-AI", ln=True, align="C")

        self.set_draw_color(0, 102, 204)
        self.set_line_width(0.5)
        self.line(10, self.get_y() + 5, 200, self.get_y() + 5)
        self.ln(12)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 10)
        self.set_text_color(150)
        self.cell(0, 10, "Developed by Aryan Patel - PitchPal-AI", 0, 0, "C")

def sanitize_text(text):
    replacements = {
        "™": "(TM)", "’": "'", "“": '"', "”": '"',
        "–": "-", "—": "-", "•": "-", "‘": "'", "…": "...",
        "🚀": "", "📄": "", "🎯": "", "📬": "", "📧": "",
        "✅": "", "🔍": "", "📥": "", "📢": "",
        "📊": "", "🧠": "", "✨": "", "📈": "", "🔬": "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text.encode("latin-1", "ignore").decode("latin-1")

def apply_styles(line):
    bold_keywords = ["traction", "team", "market", "problem", "solution", "ask", "funding", "revenue", "business model"]
    line_lower = line.lower()
    for word in bold_keywords:
        if word in line_lower:
            if word in ["problem", "market", "solution", "traction"]:
                return ("B", (0, 102, 0))  # Green bold
            elif word in ["ask", "funding", "revenue"]:
                return ("BI", (255, 102, 0))  # Orange bold italic
            else:
                return ("B", (50, 50, 50))  # Default bold
    return ("", (30, 30, 30))  # Default style

def generate_pitch_pdf(input_text):
    if hasattr(input_text, "output"):
        input_text = input_text.output

    if not isinstance(input_text, str):
        raise ValueError("generate_pitch_pdf() expected a string, got: " + str(type(input_text)))

    text = sanitize_text(input_text)
    pdf = StylishPDF()
    pdf.add_page()

    lines = text.split("\n")
    for line in lines:
        style, color = apply_styles(line)

        if line.strip().endswith(":"):
            pdf.set_font("Helvetica", "B", 13)
            pdf.set_text_color(0, 51, 102)
        else:
            pdf.set_font("Helvetica", style, 12)
            pdf.set_text_color(*color)

        wrapped = wrap(line, width=90)
        for wrap_line in wrapped:
            pdf.cell(0, 10, wrap_line, ln=True)

    output_path = "outputs/improved_pitch.pdf"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf.output(output_path)
    return output_path

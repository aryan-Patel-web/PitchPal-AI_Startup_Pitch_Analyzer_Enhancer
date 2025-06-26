# streamlit_app.py

import os
import logging
import warnings
import streamlit as st
from dotenv import load_dotenv
import fitz  # PyMuPDF

from crewai import Crew
from tasks.pitch_tasks import get_tasks
from utils.pdf_generator import generate_pitch_pdf
from utils.email_sender import send_email
# from utils.whatsapp_sender import send_whatsapp
from utils.whatsapp_sender import send_whatsapp_with_pdf


# 🔇 Suppress noisy logs
logging.getLogger("langchain").setLevel(logging.ERROR)
logging.getLogger("httpx").setLevel(logging.WARNING)
warnings.filterwarnings("ignore")

# 🔐 Load environment variables
load_dotenv()

# 🎨 Streamlit UI Setup
st.set_page_config(page_title="PitchPal-AI", layout="centered", page_icon="🚀")
st.title("🚀 PitchPal-AI")
st.caption("Your AI Co-Founder for crafting pitch-perfect decks 🎯")

# 📥 Inputs
st.subheader("📥 Upload Your Pitch")
pitch_text = st.text_area("Paste your pitch transcript or summary here (optional):")
pdf_file = st.file_uploader("Or upload your pitch deck (PDF only)", type="pdf")
domain = st.selectbox("🏷️ Select Your Startup Domain", [
    "FinTech",         # Finance tech
    "HealthTech",      # Healthcare tech
    "EdTech",          # Education tech
    "AgriTech",        # Agriculture + AI, smart farming
    "LegalTech",       # Law and legal automation
    "PropTech",        # Real estate technology
    "ClimateTech",     # Sustainability, climate action
    "RetailTech",      # Smart shopping, retail automation
    "GovTech",         # Government, civic tech
    "TravelTech",      # Tourism, mobility, booking
    "FoodTech",        # Food innovation, delivery
    "InsurTech",       # Insurance innovations
    "Cybersecurity",   # Digital safety & protection
    "Gaming",          # Game development, e-sports
    "AI/ML Tools"      # AI platforms, ML-powered products
])

email = st.text_input("📧 Enter your email (required to receive improved pitch deck)")
submit = st.button("🔍 Analyze & Rewrite My Pitch")

# 📄 Extract text from uploaded PDF
def extract_text_from_pdf(uploaded_pdf):
    try:
        with fitz.open(stream=uploaded_pdf.read(), filetype="pdf") as doc:
            return "\n\n".join([page.get_text("text") for page in doc]).strip()
    except Exception as e:
        st.error("❌ Failed to extract text from the PDF.")
        st.exception(e)
        return ""

# 🧠 Main Logic
if submit:
    if not email:
        st.error("📧 Please provide a valid email address.")
    elif not pitch_text.strip() and not pdf_file:
        st.error("❌ Please paste a pitch or upload a PDF file.")
    else:
        with st.spinner("🔎 Analyzing your pitch... Please wait."):
            try:
                # Extract text
                input_text = pitch_text.strip() or extract_text_from_pdf(pdf_file)
                if not input_text:
                    st.error("❌ No valid pitch content found.")
                    st.stop()

                # Get tasks + run CrewAI
                tasks = get_tasks(input_text, domain)
                crew = Crew(agents=[t.agent for t in tasks], tasks=tasks)
                result_obj = crew.kickoff()
                result = getattr(result_obj, "output", str(result_obj))

                if not isinstance(result, str):
                    raise ValueError("⚠️ Unexpected CrewAI result format.")

                # Show output
                st.success("✅ Pitch analyzed and rewritten!")
                st.markdown("### 📝 Rewritten Pitch")
                st.code(result.strip(), language="markdown")

                # Generate PDF
                pdf_path = generate_pitch_pdf(result)
                with open(pdf_path, "rb") as f:
                    st.download_button(
                        label="⬇️ Download Enhanced Pitch Deck (PDF)",
                        data=f,
                        file_name="PitchPal_Enhanced_Deck.pdf",
                        mime="application/pdf"
                    )

                # Send via email + WhatsApp
                send_email("📄 Your Enhanced Pitch from PitchPal-AI", result, email, attachments=[pdf_path])
                send_whatsapp_with_pdf("📢 Your enhanced pitch deck is ready!",pdf_path)
                st.success(f"📬 Pitch deck sent to {email} and your WhatsApp!")

            except Exception as e:
                st.error("🚨 Something went wrong during analysis.")
                st.exception(e)

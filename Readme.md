# 🚀 PitchPal-AI: Startup Pitch Analyzer & Enhancer

PitchPal-AI is your AI co-founder that reviews and rewrites startup pitch decks with investor-ready precision. It uses CrewAI agents to analyze your pitch, offer domain-specific advice, and generate a professional PDF—all sent to your email and WhatsApp instantly.

---

## 🌟 Features

- 📥 Upload text or PDF pitch (5–7 pages)
- 🧠 CrewAI-powered agents (Pitch Analyst, Domain Advisor, Rewriter)
- 📊 Enhances your pitch with stylish layout and formatting
- 📤 Sends the enhanced pitch deck via email & WhatsApp
- 🎨 Generates downloadable PDF with formatting, logo, and headings
- 🌐 Cloudinary upload for WhatsApp sharing

---

## 🎯 Benefits

- Save time creating investor-ready pitch decks
- Style + structure improves pitch clarity & impact
- Get feedback tailored to **your startup domain**
- Impress VCs with standout, modern decks

---

## 🗂️ Project Structure

PitchPal-AI/
│
├── streamlit_app.py # Main Streamlit UI
├── agents/
│ ├── pitch_analyst.py
│ ├── domain_advisor.py
│ └── rewriter_agent.py
├── tasks/
│ └── pitch_tasks.py
├── utils/
│ ├── pdf_generator.py
│ ├── pdf_reader.py
│ ├── email_sender.py
│ ├── whatsapp_sender.py
│ └── cloudinary_uploader.py
├── images/
│ └── logo.png
├── outputs/
│ └── improved_pitch.pdf
├── .env
└── requirements.txt

yaml
Copy
Edit

---

## ⚙️ Requirements

```bash
pip install -r requirements.txt

streamlit
crewai
langchain
langchain-groq
fpdf
python-dotenv
PyMuPDF
twilio
cloudinary
openai  # If fallback needed
email-validator
requests


Your .env should contain:
env

TWILIO_ACCOUNT_SID=...
TWILIO_AUTH_TOKEN=...
TWILIO_FROM=whatsapp:+1415XXXXXXX
TWILIO_TO=whatsapp:+91YOUR_NUMBER
SENDER_EMAIL=you@example.com
SENDER_PASSWORD=yourpassword
CLOUDINARY_CLOUD_NAME=...
CLOUDINARY_API_KEY=...
CLOUDINARY_API_SECRET=...


💡 Example Usage

Upload a pitch PDF (e.g., NeuroBoost_PitchDeck.pdf) or paste raw text, select HealthTech, enter your email, and click Analyze & Rewrite.
PitchPal-AI will generate a styled PDF and send it to your email + WhatsApp.


👨‍💻 Author

Aryan Patel
📧 [YourEmail@example.com]
🌐 Built with ❤️ using Python, Streamlit, CrewAI, LangChain, Groq, AstraDB


Demo Pitch Decks Included

1. SmartAgro AI – Investor Pitch Deck
Domain: AgriTech / AI

Overview: SmartAgro AI leverages machine learning and IoT to revolutionize crop intelligence and optimize yield forecasting for precision farming.

Demo File: SmartAgro AI Investor Pitch Deck.pdf

Prompt Example:

Build me an investor pitch deck for "SmartAgro AI", an agriculture-focused AI startup that uses predictive analytics, remote sensing, and machine learning to help farmers maximize crop yields.


2. NeuroBoost – Pitch Deck

Domain: HealthTech / NeuroTech

Overview: NeuroBoost creates wearable neurostimulation headbands to enhance mental performance, backed by AI-powered brainwave data analytics.

Demo File: NeuroBoost Pitch Deck.pdf

Prompt Example:

Create a pitch deck for "NeuroBoost", a neurotech company that offers wearable devices to improve memory, focus, and cognitive health using brainwave-synced stimulation and AI analytics.



🚧 Future Features (Planned)

🧠 Voice-based pitch analysis (via Whisper)

🌍 Multi-language pitch support

🗃️ Save pitch history per user (via Firebase or Supabase)

📊 Auto-slide generator from pitch content (PPTX output)

📈 VC-readiness scoring based on market benchmarks


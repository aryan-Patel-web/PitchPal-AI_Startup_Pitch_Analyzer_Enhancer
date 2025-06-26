# main.py - Run the pitch processing pipeline without UI
from tasks.pitch_tasks import get_tasks
from crewai import Crew
from utils.pdf_generator import generate_pitch_pdf
from utils.email_sender import send_email
from utils.whatsapp_sender import send_whatsapp

pitch_text = "We are building a mental health app using AI for teens."
domain = "HealthTech"
email = "founder@example.com"

# Setup tasks and crew
tasks = get_tasks(pitch_text, domain)
crew = Crew(agents=[t.agent for t in tasks], tasks=tasks)
result = crew.run()

print("=== Rewritten Pitch ===")
print(result)

# Save output
pdf_file = generate_pitch_pdf(result)
send_email("Your AI Rewritten Pitch", result, email, attachments=[pdf_file])
send_whatsapp(f"Your rewritten pitch is ready. Check your email or download: {pdf_file}")

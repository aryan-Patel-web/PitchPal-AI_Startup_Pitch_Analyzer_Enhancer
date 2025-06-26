# utils/whatsapp_sender.py

import os
from dotenv import load_dotenv
from twilio.rest import Client
import cloudinary
import cloudinary.uploader

# Load environment variables
load_dotenv()

# Configure Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

def upload_pdf_to_cloudinary(file_path):
    """
    Uploads the PDF to Cloudinary (as raw file) and returns its public URL.
    """
    try:
        response = cloudinary.uploader.upload(
            file_path,
            resource_type="raw",  # Required for non-image files like PDF
            use_filename=True,
            unique_filename=False,
            overwrite=True
        )
        return response["secure_url"]
    except Exception as e:
        print("❌ Cloudinary upload failed:", e)
        return None

def send_whatsapp_with_pdf(message_body, file_path):
    """
    Uploads a PDF to Cloudinary, then sends the download link via WhatsApp.
    """
    try:
        # Upload PDF and get URL
        pdf_url = upload_pdf_to_cloudinary(file_path)
        if not pdf_url:
            return "❌ Failed to upload PDF to Cloudinary."

        # Compose Twilio client
        client = Client(
            os.getenv("TWILIO_ACCOUNT_SID"),
            os.getenv("TWILIO_AUTH_TOKEN")
        )
        from_whatsapp = f"whatsapp:{os.getenv('TWILIO_FROM')}"
        to_whatsapp = f"whatsapp:{os.getenv('TWILIO_TO')}"  # Update or make dynamic if needed

        # Send WhatsApp message with link
        message = client.messages.create(
            body=f"{message_body}\n\n📄 Download your pitch deck: {pdf_url}",
            from_=from_whatsapp,
            to=to_whatsapp
        )
        return "✅ WhatsApp message with PDF sent successfully!"

    except Exception as e:
        return f"❌ WhatsApp Error: {e}"

import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.utils import timezone

def generate_qr_code(course_name):
    # Create a unique value for the QR code
    qr_data = f"{course_name}|{timezone.now()}"
    
    # Generate QR code
    qr = qrcode.make(qr_data)
    
    # Save to a BytesIO object
    buffer = BytesIO()
    qr.save(buffer, format='PNG')
    buffer.seek(0)
    
    return ContentFile(buffer.read(), name=f"{course_name}_qr.png") 
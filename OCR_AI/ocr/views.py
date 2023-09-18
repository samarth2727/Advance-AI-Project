import pytesseract
from pdf2image import convert_from_bytes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
# Create your views here.
# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def perform_ocr(request):
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        pdf_file = request.FILES['pdf_file'].read()

        # Convert the PDF to images (one image per page)
        images = convert_from_bytes(pdf_file)

        extracted_text = []

        # Perform OCR on each page
        for img in images:
            text = pytesseract.image_to_string(img)
            extracted_text.append(text)

        # Combine the extracted text from different pages with newlines
        combined_text = '\n'.join(extracted_text)

        # Return the extracted text as JSON with proper newlines
        return JsonResponse({'extracted_text': combined_text})

    return JsonResponse({'error': 'Invalid request'}, status=400)
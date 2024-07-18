import os
import shutil
import base64
import tempfile
from django.shortcuts import render
from django.http import HttpResponseServerError
from .forms import UploadImageForm
from gradio_client import Client, handle_file
from PIL import Image
import httpx

# Initialize the Gradio client with the correct endpoint URL
client = Client("https://eswarkarthikk-object-detection.hf.space")

def compress_image(image_file, max_bytes=2 * 1024 * 1024):
    """Compress image to fit within the specified byte size."""
    img = Image.open(image_file)
    
    # Ensure the image is in RGB format
    img = img.convert('RGB')
    
    buffer = tempfile.SpooledTemporaryFile(max_size=max_bytes)
    
    # Save the image with reduced quality to fit within the byte limit
    img.save(buffer, format='JPEG', quality=85)
    
    # Rewind the buffer to the beginning
    buffer.seek(0)
    
    return buffer

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Get the uploaded image file
                image_file = request.FILES['image']

                # Compress the image before sending to the API
                compressed_image_buffer = compress_image(image_file)

                # Convert the original image to base64
                original_image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

                # Example using gradio_client to predict with local file
                with httpx.Client(timeout=30) as http_client:  # Set a longer timeout if needed
                    result = client.predict(image=handle_file(compressed_image_buffer))

                # Check if the result is a file path
                if isinstance(result, str) and os.path.isfile(result):
                    # Read the predicted image and convert to base64
                    with open(result, 'rb') as img_file:
                        predicted_image_base64 = base64.b64encode(img_file.read()).decode('utf-8')

                    # Pass the base64 encoded images to the template
                    return render(request, 'index.html', {
                        'original_image_base64': original_image_base64,
                        'predicted_image_base64': predicted_image_base64
                    })
                else:
                    raise ValueError("Unexpected response format from Gradio API")

            except Exception as e:
                return HttpResponseServerError(f"Error: {str(e)}")

    else:
        form = UploadImageForm()

    return render(request, 'index.html', {'form': form})

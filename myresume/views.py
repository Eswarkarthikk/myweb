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

def resize_image(image_path, size=(224, 224)):
    with Image.open(image_path) as img:
        img = img.resize(size)
        resized_image_path = f"{os.path.splitext(image_path)[0]}_resized.jpg"
        img.save(resized_image_path)
    return resized_image_path

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Get the uploaded image file
                image_file = request.FILES['image']

                # Save the uploaded image to a temporary file
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    for chunk in image_file.chunks():
                        temp_file.write(chunk)
                    temp_file_path = temp_file.name

                # Resize the image before sending to the API
                resized_image_path = resize_image(temp_file_path)

                # Convert the original image to base64
                with open(temp_file_path, 'rb') as img_file:
                    original_image_base64 = base64.b64encode(img_file.read()).decode('utf-8')

                # Example using gradio_client to predict with local file
                with httpx.Client(timeout=60) as http_client:  # Set a longer timeout
                    result = client.predict(image=handle_file(resized_image_path))

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

            finally:
                # Clean up the temporary files
                os.remove(temp_file_path)
                os.remove(resized_image_path)

    else:
        form = UploadImageForm()

    return render(request, 'index.html', {'form': form})

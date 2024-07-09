import os
import shutil
import base64
from django.shortcuts import render
from django.http import HttpResponseServerError
from .forms import UploadImageForm
from gradio_client import Client, handle_file

# Initialize the Gradio client with the correct endpoint URL
client = Client("https://eswarkarthikk-object-detection.hf.space")

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Ensure a temporary directory exists for storing the image
                temp_dir = 'temp_images'
                if os.path.exists(temp_dir):
                    # Clear the temporary directory
                    shutil.rmtree(temp_dir)
                os.makedirs(temp_dir)

                # Get the uploaded image file
                image_file = request.FILES['image']

                # Save the uploaded image temporarily
                temp_file_path = os.path.join(temp_dir, image_file.name)
                with open(temp_file_path, 'wb') as temp_file:
                    for chunk in image_file.chunks():
                        temp_file.write(chunk)

                # Convert the original image to base64
                with open(temp_file_path, 'rb') as img_file:
                    original_image_base64 = base64.b64encode(img_file.read()).decode('utf-8')

                # Example using gradio_client to predict with local file
                result = client.predict(image=handle_file(temp_file_path))

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

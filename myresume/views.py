import os
import base64
import tempfile
from django.shortcuts import render
from django.http import HttpResponseServerError
from .forms import UploadImageForm
from gradio_client import Client, handle_file



def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        # Initialize the Gradio client with the correct endpoint URL
        client = Client("https://eswarkarthikk-object-detection.hf.space")
        if form.is_valid():
            try:
                # Create a temporary file to store the uploaded image
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    # Write the uploaded image data to the temporary file
                    for chunk in request.FILES['image'].chunks():
                        temp_file.write(chunk)

                # Get the path of the temporary file
                temp_file_path = temp_file.name

                # Example using gradio_client to predict with local file
                result = client.predict(image=handle_file(temp_file_path))

                # Check if the result is a file path
                if isinstance(result, str) and os.path.isfile(result):
                    # Read the predicted image and convert to base64
                    with open(result, 'rb') as img_file:
                        predicted_image_base64 = base64.b64encode(img_file.read()).decode('utf-8')

                    # Convert the original image to base64 for display
                    with open(temp_file_path, 'rb') as img_file:
                        original_image_base64 = base64.b64encode(img_file.read()).decode('utf-8')

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
                # Clean up: Delete the temporary file after processing
                if os.path.exists(temp_file_path):
                    os.remove(temp_file_path)

    else:
        form = UploadImageForm()

    return render(request, 'index.html', {'form': form})

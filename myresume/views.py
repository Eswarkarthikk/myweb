from django.shortcuts import render
from django.http import HttpResponseServerError
def mainpage(request):
    return render(request, 'homepage.html')

def projects1(request):
    return render(request, 'projects.html')
def projects2(request):
    return render(request, 'apps.html')
def experience1(request):
    return render(request, 'Experience.html')
def experience2(request):
    return render(request, 'intern.html')
def experience3(request):
    return render(request, 'experience2.html')
def aboutme(request):
    return render(request,'me.html')
def certifications(request):
    return render(request,'certifications.html')
# views.py
from django.shortcuts import render

def projects3(request):
    # Define the data directly as a list of dictionaries
    projects = [
        {
            'section title': 'Object detection',
            'title': 'Object Detection using Faster RCNN',
            'description': 'This is a deep learning project developed in region-based convolutional network. This model is trained on Pascal VOC 2012 dataset; it can predict 20 classes that are: aeroplane, bicycle, bird, boat, bottle, bus, car, cat, chair, cow, dining table, dog, horse, motorbike, person, potted plant, sheep, sofa, train, tv/monitor. This model is deployed on Hugging Face and by using its API, I have deployed another one so you can visit directly on my web. Please feel free to go through my GitHub repo.',
            'image_link': 'https://i.ibb.co/37jf8hb/image.png',
            'github_link': 'https://github.com/Eswarkarthikk/Ml-projects-/blob/main/r-cnn.ipynb',
            'weblink': 'https://objectdetection-weld.vercel.app/',
            'hugging_face_link': 'https://eswarkarthikk-object-detection.hf.space'
        },
        {
            'section title': '',
            'title': 'Project Two',
            'description': 'This is a description for Project Two.',
            'image_link': 'https://example.com/image2.jpg',
            'github_link': 'https://github.com/user/project2',
            'weblink': 'https://example.com/test2',
            'hugging_face_link': 'https://huggingface.co/user/project2'
        },
        {
            'section title': '',
            'title': 'Project Three',
            'description': 'This is a description for Project Three.',
            'image_link': 'https://example.com/image3.jpg',
            'github_link': 'https://github.com/user/project3',
            'weblink': 'https://example.com/test3',
            'hugging_face_link': 'https://huggingface.co/user/project3'
        },
        {
            'section title': '',
            'title': 'Project Four',
            'description': 'This is a description for Project Four.',
            'image_link': 'https://example.com/image4.jpg',
            'github_link': 'https://github.com/user/project4',
            'weblink': 'https://example.com/test4',
            'hugging_face_link': 'https://huggingface.co/user/project4'
        }
    ]
    
    # Render the template with the projects data
    return render(request, 'mlprojects.html', {'projects': projects})

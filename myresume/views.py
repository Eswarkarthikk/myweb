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

import pandas as pd
from django.shortcuts import render

def projects3(request):
    data = {
        'section title':[
            'Object detection',
            ''
        ],
        'title': [
            'Object Detection using Faster RCNN',
            'Project Two',
            'Project Three',
            'Project Four'
        ],
        'description': [
            'This is a deep learning project developed in reigion based convolutional network. This model is trained on Pascal Voc 2012 dataset it can predict 20 classes that are | aeroplane | bicycle | bird | boat | bottle | bus | car | cat | chair | cow | dining table | dog | horse | motorbike | person | potted plant | sheep | sofa | train | tv/monitor |....This model is deployed in Hugging face and by using its api i have deployed another one so you can visit directly in my web . please feel free to go through my git repo.',
            'This is a description for Project Two.',
            'This is a description for Project Three.',
            'This is a description for Project Four.'
        ],

        'image_link': [
            'https://i.ibb.co/37jf8hb/image.png',
            'https://example.com/image2.jpg',
            'https://example.com/image3.jpg',
            'https://example.com/image4.jpg'
        ],
        'github_link': [
            'https://github.com/Eswarkarthikk/Ml-projects-/blob/main/r-cnn.ipynb',
            'https://github.com/user/project2',
            'https://github.com/user/project3',
            'https://github.com/user/project4'
        ],
        'weblink': [
            'https://objectdetection-weld.vercel.app/',
            'https://example.com/test2',
            'https://example.com/test3',
            'https://example.com/test4'
        ],
        'hugging_face_link': [
            'https://eswarkarthikk-object-detection.hf.space',
            'https://huggingface.co/user/project2',
            'https://huggingface.co/user/project3',
            'https://huggingface.co/user/project4'
        ]
    }
    
    df = pd.DataFrame(data)
    
    # Convert DataFrame to a list of dictionaries
    projects = df.to_dict(orient='records')
    
    # Render the template with the projects data
    return render(request, 'mlprojects.html', {'projects': projects})
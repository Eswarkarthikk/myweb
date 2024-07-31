from django.shortcuts import render
from django.http import HttpResponseServerError
def mainpage(request):
    return render(request, 'homepage.html')

def projects1(request):
    projects = [
        {
            "main_title": "Resucraft",
            "description": "Resucraft is a full-stack web development project designed to create various resumes online by simply filling out a form. Users can update, delete, and create resumes through our web application, which utilizes Django for the backend and PostgreSQL for storing user data and login information. Our team dedicated significant time to this project, with my contributions including leading the design of the Django framework, managing integration, establishing database connectivity, and conducting project testing. I developed code for models and views, enabling users to edit and add information, while Srikar assisted with database management and contributed to the login and signup pages. Vivek focused on creating an interactive UI for various pages, and Bhavani designed some templates.",
            "image": "https://i.ibb.co/DYLJ17j/image.png",
            "git_link": "https://github.com/Eswarkarthikk/Resucraft",
            "weblink": "https://resucraft.vercel.app/",
             "snapshots": [
                
                "https://i.ibb.co/n35vB1Q/Screenshot-2024-07-21-205437.png",
                "https://i.ibb.co/Jv0h0cF/Screenshot-2024-07-21-205425.png",
                "https://i.ibb.co/p4K0kM6/Screenshot-2024-07-21-205518.png",
                "https://i.ibb.co/G2vsVcp/Screenshot-2024-07-21-205919.png",
                "https://i.ibb.co/wQqNFM7/Screenshot-2024-07-21-205901.png",
                "https://i.ibb.co/grxK58F/Screenshot-2024-07-21-205849.png",
                "https://i.ibb.co/3vSPqZL/Screenshot-2024-07-21-205827.png",
                "https://i.ibb.co/StzgPhG/Screenshot-2024-07-21-205815.png",
                "https://i.ibb.co/7pGmYZq/Screenshot-2024-07-21-205759.png",
                "https://i.ibb.co/425MY5V/Screenshot-2024-07-21-205750.png",
                "https://i.ibb.co/99GVY2k/Screenshot-2024-07-21-205736.png",
                "https://i.ibb.co/K9VHhbD/Screenshot-2024-07-21-205726.png",
                "https://i.ibb.co/hx6P5nZ/Screenshot-2024-07-21-205717.png",
                "https://i.ibb.co/q0PKKQ2/Screenshot-2024-07-21-205656.png",
                "https://i.ibb.co/2N6HXLQ/Screenshot-2024-07-21-205645.png",
                "https://i.ibb.co/5jh7Vmg/Screenshot-2024-07-21-205552.png",
                "https://i.ibb.co/WF5rR12/Screenshot-2024-07-21-205543.png",
                "https://i.ibb.co/3rbp6tJ/Screenshot-2024-07-21-205531.png",
                "https://i.ibb.co/WcZjY7Z/Screenshot-2024-07-21-205454.png",
                "https://i.ibb.co/D5QTLc0/Screenshot-2024-07-21-205406.png",
                "https://i.ibb.co/Tt28dJv/Screenshot-2024-07-21-205355.png",
                "https://i.ibb.co/YQXrB8Q/Screenshot-2024-07-21-205341.png",
                "https://i.ibb.co/r5Vcck0/Screenshot-2024-07-21-205313.png",
                "https://i.ibb.co/ZSZ22Sp/Screenshot-2024-07-21-205936.png",
            ]
        },
        {
            "main_title": "Project Title 2",
            "description": "Description for project 2.",
            "image": "https://example.com/main-image2.jpg",
            "git_link": "https://github.com/username/project2",
            "weblink": "https://example.com/project2",
            "snapshots": [
                "https://example.com/snapshot4.jpg",
                "https://example.com/snapshot5.jpg",
                "https://example.com/snapshot6.jpg",
            ]
        },
        {
            "main_title": "Project Title 3",
            "description": "Description for project 3.",
            "image": "https://example.com/main-image3.jpg",
            "git_link": "https://github.com/username/project3",
            "weblink": "https://example.com/project3",
            "snapshots": [
                "https://example.com/snapshot7.jpg",
                "https://example.com/snapshot8.jpg",
                "https://example.com/snapshot9.jpg",
            ]
        },
        # Add more projects as needed
    ]

   
    return render(request, 'projects.html',{'projects': projects})
def projects2(request):
    projects = [
        {
            "main_title": "Results Scraping",
            "description": "Result Pages is another web scraping project I created to scrape results from the JNTUGV website, which is built on React. I utilized Selenium and automation to extract data for all users and save it in a CSV file. Although it is not deployed due to the limitations of scraping codes in online applications, I am looking forward to releasing an app for this project.",
            "image": "https://i.ibb.co/DYLJ17j/image.png",
            "git_link": "https://github.com/Eswarkarthikk/results/tree/main/Results",
            "weblink": "https://github.com/Eswarkarthikk/results",
            "snapshots": [
                "https://i.ibb.co/QCkKs0V/Screenshot-2024-07-21-204233.png",
                "https://i.ibb.co/bQCzBsT/Screenshot-2024-07-21-204144.png",
                "https://i.ibb.co/pW2m5m0/Screenshot-2024-07-21-204126.png",
                "https://i.ibb.co/cgcXT5m/Screenshot-2024-07-21-204112.png",
                "https://i.ibb.co/5rrMjn1/Screenshot-2024-07-21-204101.png",
                "https://i.ibb.co/frwgCYW/Screenshot-2024-07-21-204050.png",
                "https://i.ibb.co/S7zSpZV/Screenshot-2024-07-21-202622.png",
                "https://i.ibb.co/S7sCdL5/Screenshot-2024-07-21-204642.png",
                "https://i.ibb.co/31z7rSK/Screenshot-2024-07-21-204629.png",
                "https://i.ibb.co/JRMSQs6/Screenshot-2024-07-21-204609.png",
                "https://i.ibb.co/CHcDGGB/Screenshot-2024-07-21-204245.png",
            ]
        },
        {
            "main_title": "Project Title 2",
            "description": "Description for project 2.",
            "image": "https://example.com/main-image2.jpg",
            "git_link": "https://github.com/username/project2",
            "weblink": "https://example.com/project2",
            "snapshots": [
                "https://example.com/snapshot4.jpg",
                "https://example.com/snapshot5.jpg",
                "https://example.com/snapshot6.jpg",
            ]
        },
        {
            "main_title": "Project Title 3",
            "description": "Description for project 3.",
            "image": "https://example.com/main-image3.jpg",
            "git_link": "https://github.com/username/project3",
            "weblink": "https://example.com/project3",
            "snapshots": [
                "https://example.com/snapshot7.jpg",
                "https://example.com/snapshot8.jpg",
                "https://example.com/snapshot9.jpg",
            ]
        },
        # Add more projects as needed
    ]

   
    return render(request, 'apps.html',{'projects': projects})
def experience1(request):

    images = [
        "https://i.ibb.co/CwPwVmP/20221208-112555-AMBy-GPSMap-Camera.jpg",
        "https://i.ibb.co/bbpDyCP/20221208-110937-AMBy-GPSMap-Camera.jpg",
        "https://i.ibb.co/Jk5cyy1/20221208-104050am-By-GPSMap-Camera.jpg",
        "https://i.ibb.co/Hhyg2PP/20221208-104034-AMBy-GPSMap-Camera.jpg",
        "https://i.ibb.co/qJXN87m/20221208-103952-AMBy-GPSMap-Camera.jpg",
        "https://i.ibb.co/RH9GGH4/20221208-103942-AMBy-GPSMap-Camera.jpg",
        "https://i.ibb.co/c1YwVYS/20221208-103927-AMBy-GPSMap-Camera.jpg",
        "https://i.ibb.co/V2ZMS1G/20221208-102308-AMBy-GPSMap-Camera.jpg",
        "https://i.ibb.co/z6z15sP/20221208-102306-AMBy-GPSMap-Camera.jpg",
        "https://i.ibb.co/QKVzZtf/20221208-102241-AMBy-GPSMap-Camera.jpg",
        "https://i.ibb.co/gr3Sp3W/20221208-102059-AMBy-GPSMap-Camera.jpg",
        "https://i.ibb.co/884ktr9/20221208-101156-AMBy-GPSMap-Camera.jpg",
        "https://i.ibb.co/tcr8Psk/20221208-100312am-By-GPSMap-Camera.jpg",
        "https://i.ibb.co/MGKkyg2/20221208-95629am-By-GPSMap-Camera.jpg",
        "https://i.ibb.co/9ZBRQVj/20221208-95524am-By-GPSMap-Camera.jpg",
        "https://i.ibb.co/x3Psx3G/20221208-95109am-By-GPSMap-Camera.jpg",
        "https://i.ibb.co/vd22DVw/20221208-95056am-By-GPSMap-Camera.jpg",
        "https://i.ibb.co/djPDgtP/20221208-94643am-By-GPSMap-Camera.jpg",
        "https://i.ibb.co/s5cCGC2/IMG20221208093639.jpg",
        "https://i.ibb.co/QkrzXpk/1670774555199.jpg",
        "https://i.ibb.co/GvD7QDB/1670774555234.jpg",
        "https://i.ibb.co/rZj0qcC/1670774554878.jpg",
        "https://i.ibb.co/YhXj5pQ/20221208-112603-AMBy-GPSMap-Camera.jpg"
    ]
    items = [
        {
            "main_title": "Main Title 1",
            "sub_title": "Sub Title 1",
            "image": "https://i.ibb.co/CwPwVmP/20221208-112555-AMBy-GPSMap-Camera.jpg",
            "description": "Description for the first image."
        },
        {
            "main_title": "Main Title 2",
            "sub_title": "Sub Title 2",
            "image": "https://i.ibb.co/bbpDyCP/20221208-110937-AMBy-GPSMap-Camera.jpg",
            "description": "Description for the second image."
        },
        {
            "main_title": "Main Title 3",
            "sub_title": "Sub Title 3",
            "image": "https://i.ibb.co/Jk5cyy1/20221208-104050am-By-GPSMap-Camera.jpg",
            "description": "Description for the third image."
        },
        {
            "main_title": "Main Title 4",
            "sub_title": "Sub Title 4",
            "image": "https://i.ibb.co/Hhyg2PP/20221208-104034-AMBy-GPSMap-Camera.jpg",
            "description": "Description for the fourth image."
        },
        {
            "main_title": "Main Title 5",
            "sub_title": "Sub Title 5",
            "image": "https://i.ibb.co/qJXN87m/20221208-103952-AMBy-GPSMap-Camera.jpg",
            "description": "Description for the fifth image."
        }
    ]

    return render(request , 'Experience.html' , { 'images' : images,'items':items})
    
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
            'sectiontitle': 'Object Detection',
            'title': 'Object Detection using Faster RCNN',
            'description': 'This is a deep learning project developed in region-based convolutional network. This model is trained on Pascal VOC 2012 dataset; it can predict 20 classes that are: aeroplane, bicycle, bird, boat, bottle, bus, car, cat, chair, cow, dining table, dog, horse, motorbike, person, potted plant, sheep, sofa, train, tv/monitor. This model is deployed on Hugging Face and by using its API, I have deployed another one so you can visit directly on my web. Please feel free to go through my GitHub repo.',
            'image_link': 'https://i.ibb.co/qJHQ2cM/image.png',
            'github_link': 'https://github.com/Eswarkarthikk/Ml-projects-/blob/main/r-cnn.ipynb',
            'weblink': 'https://objectdetection-weld.vercel.app/',
            'hugging_face_link': 'https://eswarkarthikk-object-detection.hf.space'
        },
        {
            'sectiontitle': '',
            'title': 'Project Two',
            'description': 'This is a description for Project Two.',
            'image_link': 'https://example.com/image2.jpg',
            'github_link': 'https://github.com/user/project2',
            'weblink': 'https://example.com/test2',
            'hugging_face_link': 'https://huggingface.co/user/project2'
        },
        {
            'sectiontitle': '',
            'title': 'Project Three',
            'description': 'This is a description for Project Three.',
            'image_link': 'https://example.com/image3.jpg',
            'github_link': 'https://github.com/user/project3',
            'weblink': 'https://example.com/test3',
            'hugging_face_link': 'https://huggingface.co/user/project3'
        },
        {
            'sectiontitle': '',
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

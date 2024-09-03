from django.shortcuts import render
from django.http import HttpResponseServerError
def mainpage(request):
    return render(request, 'homepage.html')

def projects1(request):
    projects = [
        {
            "main_title": "Resucraft",
            "description": "Resucraft is a full-stack web development project designed to create various resumes online by simply filling out a form. Users can update, delete, and create resumes through our web application, which utilizes Django for the backend and PostgreSQL for storing user data and login information. Our team dedicated significant time to this project, with my contributions including leading the design of the Django framework, managing integration, establishing database connectivity, and conducting project testing. I developed code for models and views, enabling users to edit and add information, while Srikar assisted with database management and contributed to the login and signup pages. Vivek focused on creating an interactive UI for various pages, and Bhavani designed some templates.",
            "image": "https://i.ibb.co/Tbwt72K/image.png",
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
            "main_title": "SENTIMAP",
            "description": "Sentimap is a web scraping project developed during the Smart India Hackathon. It takes a YouTube video link as input, scrapes all the comments, and analyzes them using NLP to provide various insights about the video. Additionally, it utilizes public data to make predictions for elections and detects vulgar messages in the comments.",
            "image": "https://i.ibb.co/dbLRWwJ/image.png",
            "git_link": "https://github.com/Eswarkarthikk/Sentimap/tree/main/SENTIMAP",
            "weblink": "https://github.com/Eswarkarthikk/Sentimap",
            "snapshots": [
                "https://i.ibb.co/cvfqT0L/55f9bcdb-8fc1-499d-bfe8-3d44faa22e12-4.jpg",
                "https://i.ibb.co/fC27KKs/55f9bcdb-8fc1-499d-bfe8-3d44faa22e12-3.jpg",
                "https://i.ibb.co/YczK9QY/55f9bcdb-8fc1-499d-bfe8-3d44faa22e12-2.jpg",
                "https://i.ibb.co/0G04tpn/55f9bcdb-8fc1-499d-bfe8-3d44faa22e12-1.jpg",
                "https://i.ibb.co/82CXVpj/55f9bcdb-8fc1-499d-bfe8-3d44faa22e12-0.jpg",
                "https://i.ibb.co/zXP4xJ1/Picture8.png",
                "https://i.ibb.co/QjCcwMq/Picture7.png",
                "https://i.ibb.co/gM101dt/Picture6.png",
                "https://i.ibb.co/t3DnyCZ/Picture5.png",
                "https://i.ibb.co/GC5ctpL/Picture4.png",
                "https://i.ibb.co/8XBXKYR/Picture3.png",
                "https://i.ibb.co/cyBWBCY/Picture2.png",
                "https://i.ibb.co/zXP4xJ1/Picture8.png",
                "https://i.ibb.co/Wns9VTc/55f9bcdb-8fc1-499d-bfe8-3d44faa22e12-6.jpg",
                "https://i.ibb.co/3mBdRWv/55f9bcdb-8fc1-499d-bfe8-3d44faa22e12-5.jpg",
            ]
        },
        {
            "main_title": "Random Gallery",
            "description": " It is a React-based website that I built to understand how React works. I have successfully deployed it on GitHub. To create this project, I used an API to fetch images and incorporated a search bar functionality, allowing users to retrieve pictures based on their input. This project helped me gain practical experience in working with React and integrating external APIs to enhance the user experience.",
            "image": "https://i.ibb.co/dGCQt4B/image.png",
            "git_link": "https://github.com/Eswarkarthikk/RandomGallery",
            "weblink": "https://eswarkarthikk.github.io/RandomGallery/",
            "snapshots": [
                "https://i.ibb.co/D56jnqN/Screenshot-2024-08-01-230433.png",
                "https://i.ibb.co/ScmVrnL/Screenshot-2024-08-01-230451.png",
                "https://i.ibb.co/MVM1rhL/Screenshot-2024-08-01-230538.png",
                "https://i.ibb.co/SdqhMYD/Screenshot-2024-08-01-230555.png",
                
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
            "main_title": "E - Library ",
            "description": "Library Management is a project me and my team harsha,amar,bhavani and sushma developed using pure HTML during my second year of studying web development. This project helped me grasp fundamental HTML concepts and understand how to structure a web application effectively. It served as a solid foundation for my future endeavors in web development, introducing me to essential coding practices and the importance of clean, semantic markup.",
            "image":"https://i.ibb.co/s9zPgS6/Screenshot-2024-07-21-200544.png",
            "git_link": "https://github.com/username/project2",
            "weblink": "https://example.com/project2",
             "snapshots": [
                "https://i.ibb.co/K0Wh4Pp/Screenshot-2024-07-21-200700.png",
                "https://i.ibb.co/3FM3268/Screenshot-2024-07-21-200638.png",
                "https://i.ibb.co/GPTrYBX/Screenshot-2024-07-21-200627.png",
                "https://i.ibb.co/VwkLFY5/Screenshot-2024-07-21-200610.png",
                "https://i.ibb.co/fFwtNjL/Screenshot-2024-07-21-200556.png",
                "https://i.ibb.co/ZXbLDC4/Screenshot-2024-07-21-200923.png",
                "https://i.ibb.co/D4BTBQZ/Screenshot-2024-07-21-200908.png",
                "https://i.ibb.co/jRXshq9/Screenshot-2024-07-21-200846.png",
                "https://i.ibb.co/HPHX6rW/Screenshot-2024-07-21-200837.png",
                "https://i.ibb.co/gPtmGbC/Screenshot-2024-07-21-200810.png",
                "https://i.ibb.co/6RsyQg3/Screenshot-2024-07-21-200741.png",
                "https://i.ibb.co/gb1ScRg/Screenshot-2024-07-21-200712.png",
            ]
        },
        {
            "main_title": "Student Enrollment",
            "description": "The Student Enrollment project is developed using Java Servlets and deployed on a Tomcat server. For the backend, I utilized the MySQL JDBC driver to facilitate database connectivity. The application handles HTTP Servlet requests and responses to interact with JSP and HTML pages. I implemented all CRUD (Create, Read, Update, Delete) operations to manage student data effectively, allowing for seamless storage and retrieval of information from the database.",
            "image": "https://i.ibb.co/ZWZryFp/image.png",
            "git_link": "https://github.com/username/project3",
            "weblink": "https://example.com/project3",
             "snapshots": [
                "https://i.ibb.co/C1hfrNs/Screenshot-2024-07-21-200150.png",
                "https://i.ibb.co/55Bgg4f/Screenshot-2024-07-21-195750.png",
                "https://i.ibb.co/F00PXZg/Screenshot-2024-07-21-195703.png",
                "https://i.ibb.co/fDRZSTm/Screenshot-2024-07-21-195651.png",
                "https://i.ibb.co/LQYqvYk/Screenshot-2024-07-21-195625.png",
                "https://i.ibb.co/RTFwgsH/Screenshot-2024-07-21-195559.png",
                "https://i.ibb.co/1Z1YFsH/Screenshot-2024-07-21-195547.png",
                "https://i.ibb.co/pZyNnXP/Screenshot-2024-07-21-195450.png",
                "https://i.ibb.co/DMFMV87/Screenshot-2024-07-21-195438.png",
                "https://i.ibb.co/kGMzqSd/Screenshot-2024-07-21-200215.png",
            ]
        },
        {
            "main_title": "Service Management",
            "description": "The Service Management project follows a similar structure to the Student Enrollment project, also built using Java Servlets and the Tomcat server. However, I introduced additional enhancements by incorporating JavaBeans, which improved the flexibility and maintainability of the application. This project also performs CRUD operations and effectively manages service-related data, providing a robust solution for service management.",
            "image": "https://i.ibb.co/rsw584q/image.png",
            "git_link": "https://github.com/username/project3",
            "weblink": "https://example.com/project3",
            "snapshots": [
                "https://i.ibb.co/By7Sb7k/Screenshot-2024-04-20-143050.png",
                "https://i.ibb.co/Khxc4cG/Screenshot-2024-04-20-143041.png",
                "https://i.ibb.co/vvzsy2B/Screenshot-2024-04-20-143029.png",
                "https://i.ibb.co/Vg00zVT/Screenshot-2024-04-20-143017.png",
                "https://i.ibb.co/XjM4ZFH/Screenshot-2024-07-21-200244.png",
                "https://i.ibb.co/GJjm7Rs/Screenshot-2024-04-20-143058.png"
            ]
        },
        # Add more projects as needed
    ]

   
    return render(request, 'apps.html',{'projects': projects})
def experience1(request):

    images = [
    #     "https://i.ibb.co/CwPwVmP/20221208-112555-AMBy-GPSMap-Camera.jpg",
    #     "https://i.ibb.co/bbpDyCP/20221208-110937-AMBy-GPSMap-Camera.jpg",
    #     "https://i.ibb.co/Jk5cyy1/20221208-104050am-By-GPSMap-Camera.jpg",
    #     "https://i.ibb.co/Hhyg2PP/20221208-104034-AMBy-GPSMap-Camera.jpg",
    #     "https://i.ibb.co/qJXN87m/20221208-103952-AMBy-GPSMap-Camera.jpg",
    #     "https://i.ibb.co/RH9GGH4/20221208-103942-AMBy-GPSMap-Camera.jpg",
    #     "https://i.ibb.co/c1YwVYS/20221208-103927-AMBy-GPSMap-Camera.jpg",
    #     "https://i.ibb.co/V2ZMS1G/20221208-102308-AMBy-GPSMap-Camera.jpg",
    #     "https://i.ibb.co/z6z15sP/20221208-102306-AMBy-GPSMap-Camera.jpg",
    #     "https://i.ibb.co/QKVzZtf/20221208-102241-AMBy-GPSMap-Camera.jpg",
    #     "https://i.ibb.co/gr3Sp3W/20221208-102059-AMBy-GPSMap-Camera.jpg",
    #     "https://i.ibb.co/884ktr9/20221208-101156-AMBy-GPSMap-Camera.jpg",
    #     "https://i.ibb.co/tcr8Psk/20221208-100312am-By-GPSMap-Camera.jpg",
    #     "https://i.ibb.co/MGKkyg2/20221208-95629am-By-GPSMap-Camera.jpg",
    #     "https://i.ibb.co/9ZBRQVj/20221208-95524am-By-GPSMap-Camera.jpg",
    #     "https://i.ibb.co/x3Psx3G/20221208-95109am-By-GPSMap-Camera.jpg",
    #     "https://i.ibb.co/vd22DVw/20221208-95056am-By-GPSMap-Camera.jpg",
    #     "https://i.ibb.co/djPDgtP/20221208-94643am-By-GPSMap-Camera.jpg",
    #     "https://i.ibb.co/s5cCGC2/IMG20221208093639.jpg",
    #     "https://i.ibb.co/QkrzXpk/1670774555199.jpg",
    #     "https://i.ibb.co/GvD7QDB/1670774555234.jpg",
    #     "https://i.ibb.co/rZj0qcC/1670774554878.jpg",
    #     "https://i.ibb.co/YhXj5pQ/20221208-112603-AMBy-GPSMap-Camera.jpg"
    ]
    items = [
        {
            "main_title": "CODE GEEKS 3.0",
            "sub_title": "1st coding competition",
            "image": "https://i.ibb.co/CwPwVmP/20221208-112555-AMBy-GPSMap-Camera.jpg",
            "description": "...."        },
        {
            "main_title": "CODE FURIA 4.0",
            "sub_title": "2nd coding competition",
            "image": "https://i.ibb.co/bbpDyCP/20221208-110937-AMBy-GPSMap-Camera.jpg",
            "description": "...."
        },
        {
            "main_title": "CODE FURIA 5.0",
            "sub_title": "3rd coding competition",
            "image": "https://i.ibb.co/Jk5cyy1/20221208-104050am-By-GPSMap-Camera.jpg",
            "description": "...."        },
        {
            "main_title": "CODE FURIA 6.0",
            "sub_title": "4th coding competition",
            "image": "https://i.ibb.co/Hhyg2PP/20221208-104034-AMBy-GPSMap-Camera.jpg",
            "description": "...."
        },
        {
            "main_title": "Food Donation",
            "sub_title": "FOOD DRIVE",
            "image": "https://i.ibb.co/qJXN87m/20221208-103952-AMBy-GPSMap-Camera.jpg",
            "description": "...."        },
        {
            "main_title": "Latex Doccon",
            "sub_title": "webinar on latex ",
            "image": "https://i.ibb.co/Hhyg2PP/20221208-104034-AMBy-GPSMap-Camera.jpg",
            "description": "...."
        },
        {
            "main_title": "Awareness on coding ",
            "sub_title": "Code Grip",
            "image": "https://i.ibb.co/Hhyg2PP/20221208-104034-AMBy-GPSMap-Camera.jpg",
            "description": "...."
        },
            {
            "main_title": "Code Wars 1.0",
            "sub_title": "Fest Coding Competitions",
            "image": "https://i.ibb.co/Hhyg2PP/20221208-104034-AMBy-GPSMap-Camera.jpg",
            "description": "...."
        },
            {
            "main_title": "Code wars 2.0",
            "sub_title": "Fest Coding Competitions",
            "image": "https://i.ibb.co/Hhyg2PP/20221208-104034-AMBy-GPSMap-Camera.jpg",
            "description": "...."
        },
            {
            "main_title": "Code wars 3.0",
            "sub_title": "Fest Coding Competitions",
            "image": "https://i.ibb.co/Hhyg2PP/20221208-104034-AMBy-GPSMap-Camera.jpg",
            "description": "...."
        },
            {
            "main_title": "Membership Drive ",
            "sub_title": "building ACM community",
            "image": "https://i.ibb.co/Hhyg2PP/20221208-104034-AMBy-GPSMap-Camera.jpg",
            "description": "...."
        },
    ]

    return render(request , 'Experience.html' , { 'images' : images,'items':items})
    
def experience2(request):
    projects = [
        {
            "main_title": "Teckybot Internship",
            "description": "I was selected for this online internship after an interview, along with my friends Jai Sai Srikar (IT) and Neelima (CSE) from our college, as AI/ML developers. We have been working on this project for over two and a half months, and it is still ongoing. This internship has been a memorable experience, thanks to the exceptional mentorship from Bandaru Bhargavi Ma'am and Venkat Sir. I have learned a lot about machine learning and developed models using various methods throughout this journey.",
            "image": "https://i.ibb.co/6WnzT92/Screenshot-2024-07-31-153256.png",
        },
        {
            "main_title": "Codsoft Internship",
            "description": "This was an online Android app development internship. I was supposed to complete 5 tasks given to me, but I only finished two. You can download my Android applications and feel free to check my code on GitHub.",
            "image":"https://i.ibb.co/rykrvxW/codsoft.png",
        },
            {
            "main_title": "Brain o vision",
            "description": "This is an online data science internship I obtained from APSCHE. Although I found it less interesting, I am pursuing it to earn credits for my 4th-year completion.",
            "image":"https://i.ibb.co/CHdM2mz/image.png",
        },
       
    ]
    return render(request, 'intern.html',{'projects': projects})
def experience3(request):
    projects = [
        {
            "main_title": "Smart India Hackathon",
            "description": "My team, consisting of Srikar, Meeravali, Sandeep Banodhar, Archana, and myself, was selected for the Smart India Hackathon 2023. We traveled to Sambalpur, Odisha, for this exciting journey. Although I was just a team member, I played a significant role during the two-day hackathon by preparing presentations, designing the backend for our project, and integrating everything. While we did not win, we put forth our best effort in developing a project, which you can find in my projects.",
            "image":"https://i.ibb.co/Gx0B5bT/1715325222708.jpg",
        },

        {
            "main_title": "Ityukta2k24",
            "description": "Ityukta2k24 is a two-day technical symposium for which our team worked diligently for over two months. I gained valuable experience in securing sponsorships and promoting the event, successfully raising over 20k by conducting three consecutive coding competitions prior to the fest. Additionally, I designed the fest logo, posters, and banners. While it was a team effort with many contributions, I took on significant responsibilities during the event days, particularly in conducting workshops that attracted the maximum number of visitors to our fest.",
            "image": "https://i.ibb.co/StC59H5/ITYUKTA-8.png",
        },
      
    ]
    expertise = [
        {
            "main_title": "Design and Animations",
            "description": "I had the opportunity to learn Blender and design wireframes for my laptop animation project. Through this process, I gained valuable knowledge and skills in 3D modeling, which has sparked my interest in the field of animation. This experience has opened up exciting new avenues for me to explore in 3D design, and I look forward to applying what I've learned in future projects.",
            "image": "https://i.ibb.co/1sjnfgS/Screenshot-2024-07-21-230855.png",
            "snapshots": [
               "https://i.ibb.co/NCfPtP5/Screenshot-2024-04-07-221154.png",
    "https://i.ibb.co/TYZWKfd/Screenshot-2024-04-07-215425.png",
    "https://i.ibb.co/6tFNvBD/Screenshot-2024-04-07-215226.png",
    "https://i.ibb.co/zVp7Ysy/Screenshot-2024-04-07-214848.png",
    "https://i.ibb.co/CMd7fzR/Screenshot-2024-04-07-214049.png",
    "https://i.ibb.co/ySLJkJD/Screenshot-2024-04-07-213950.png",
    "https://i.ibb.co/6RmmXn4/Screenshot-2024-04-07-213903.png",
     "https://i.ibb.co/TBtzH1y/Screenshot-2024-07-21-231627.png",
    "https://i.ibb.co/zbqGbpG/Screenshot-2024-07-21-231455.png",
    "https://i.ibb.co/2nLXrkC/Screenshot-2024-07-21-231408.png",
    "https://i.ibb.co/MSgNTdj/Screenshot-2024-07-21-231209.png",
    "https://i.ibb.co/9hMq6XK/Screenshot-2024-07-21-230834.png",
    "https://i.ibb.co/cN5yJqX/Screenshot-2024-07-21-230817.png",
    "https://i.ibb.co/GtZz7YD/Screenshot-2024-07-21-230757.png",
    "https://i.ibb.co/cLg75N6/Screenshot-2024-07-21-230749.png",
    "https://i.ibb.co/khjnkC4/Screenshot-2024-07-21-230739.png",
    "https://i.ibb.co/pyCGjkb/Screenshot-2024-07-21-230638.png",
    "https://i.ibb.co/dDDRRp5/Screenshot-2024-07-21-230622.png",
    "https://i.ibb.co/25YSx2x/Screenshot-2024-07-21-230613.png",
    "https://i.ibb.co/WcsXfW4/Screenshot-2024-07-21-230600.png",
    "https://i.ibb.co/xGh4xZr/Screenshot-2024-07-21-230505.png",
    "https://i.ibb.co/rMZ226t/Screenshot-2024-07-21-230433.png",
    "https://i.ibb.co/c20FryG/Screenshot-2024-07-21-230358.png",
    "https://i.ibb.co/GQyC7CQ/Screenshot-2024-07-21-230338.png",
    "https://i.ibb.co/9s9ZvGk/Screenshot-2024-07-21-230320.png",
    "https://i.ibb.co/mBVdZsv/Screenshot-2024-07-21-230257.png",
    "https://i.ibb.co/jTchpNn/Screenshot-2024-07-21-230241.png",
    "https://i.ibb.co/VS9WNQH/Screenshot-2024-07-21-230215.png",
    "https://i.ibb.co/8DhHqf2/Screenshot-2024-07-21-230041.png",
    "https://i.ibb.co/0yFHwBW/Screenshot-2024-07-21-230027.png",
    "https://i.ibb.co/nBdhB7Z/Screenshot-2024-07-21-225948.png",
    "https://i.ibb.co/2t30qBP/Screenshot-2024-07-21-225851.png",
    "https://i.ibb.co/4NqDCzj/Screenshot-2024-07-21-225832.png",
    "https://i.ibb.co/pxTJN3Q/Screenshot-2024-07-21-225811.png",
    "https://i.ibb.co/g3cs477/Screenshot-2024-07-21-225719.png",
    "https://i.ibb.co/dg7Qvp3/Screenshot-2024-07-21-225650.png",
    "https://i.ibb.co/42Bms5Q/Screenshot-2024-07-21-225629.png",
    "https://i.ibb.co/Wg1msmk/Screenshot-2024-07-21-225606.png",
    "https://i.ibb.co/855cwT6/Screenshot-2024-07-21-211841.png",
    "https://i.ibb.co/wz7N1rK/Screenshot-2024-07-21-211716.png"
            ]
        },]
    return render(request, 'experience2.html',{'projects': projects,'expertise':expertise})
def aboutme(request):
    images = [
        "https://i.ibb.co/d2JGFPb/A-drawing-page-0001.jpg",
        "https://i.ibb.co/JQVwJtC/My-drawings-page-0001.jpg",
        "https://i.ibb.co/DgLntDG/My-drawings-page-0006.jpg",
        "https://i.ibb.co/qFwrJ9Z/My-drawings-page-0007.jpg",
        "https://i.ibb.co/gMG09yR/My-drawings-page-0008.jpg",
        "https://i.ibb.co/njz0113/My-drawings-page-0002.jpg",
        "https://i.ibb.co/hdnkJSX/My-drawings-page-0003.jpg",
        "https://i.ibb.co/bBgYKdn/My-drawings-page-0004.jpg",
        "https://i.ibb.co/qrDYDZS/My-drawings-page-0014.jpg",
        "https://i.ibb.co/b2ccpSg/A-drawing-page-0002.jpg"
    ]
    return render(request,'me.html',{'images': images})
def certifications(request):
    certificates1 = [
      {
            'link': 'https://i.ibb.co/ZfNT6F4/Programming-in-Modern-C.jpg',
            'title': 'Programming in Modern C++',
            'description': 'Completed a 12-month course on Programming in Modern C++ with a score of 55% in the final exam.',
        },
        {
            'link': 'https://i.ibb.co/TRP7c3j/sih.jpg',
            'title': 'Smart India Hackathon',
            'description': 'My team was selected for the Smart India Hackathon Grand Finale 2024, a truly memorable experience for me.',
        },
        {
            'link': 'https://i.ibb.co/0fd1GYC/21-VV1-A1201-1.jpg',
            'title': 'Oracle Java Foundations',
            'description': 'Studied Java Foundations and successfully passed the exams provided by Oracle.',
        },
        {
            'link': 'https://i.ibb.co/C0j7Jkc/Screenshot-2024-08-02-204430.png',
            'title': 'Social Network Analysis',
            'description': 'Completed a 12-month course on Social Network Analysis with a 51% score in the examination.',
        },
        {
            'link': 'https://i.ibb.co/R4XQSDb/Screenshot-2024-08-02-204251.png',
            'title': 'Microsoft Azure Fundamentals',
            'description': 'Participated in and passed the Microsoft Azure AI Fundamentals exam, earning this badge.',
        },
        {
            'link': 'https://i.ibb.co/56jbqtc/Screenshot-2024-08-02-204043.png',
            'title': 'Android App Development',
            'description': 'Completed a 2-month online internship in Android App Development and received this certificate from Codsoft as recognition.verify',
        },
        {
            'link': 'https://i.ibb.co/74F9vmP/edx-course-on-english.jpg',
            'title': 'Conversational Skills',
            'description': 'Earned a certification in English Conversational Skills from edX.',
        },
        
          {
            'link': 'https://i.ibb.co/q1b63K2/automation-udemy.jpg',
            'title': 'Automation with Python',
            'description': 'Completed a comprehensive course on Automation with Python.',
        },
        {
            'link': 'https://i.ibb.co/nkt3RpL/webscraping-udemy.jpg',
            'title': 'Web Scraping Certification',
            'description': 'Earned a certification in Web Scraping techniques.',
        },
        
    ]
    certificates2=[
        {
            'link': 'https://i.ibb.co/8cvFx8F/ncc.jpg',
            'title': 'National Cadet Corps',
            'description': 'Served as CPL in the 14 Andhra Battalion NCC (Army) for 2 years, gaining experience in operating .22mm rifles, attending 5 different camps, and leading as a platoon leader.',
        },
    ]
    # Correctly pass the images as a dictionary
    return render(request, 'certifications.html', {"certificates1": certificates1,"certificates2": certificates2})
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
            'github_link': 'https://github.com/Eswarkarthikk/Ml_projects/tree/main/object%20detection',
            'weblink': 'https://aarieswarmlprojects.vercel.app/',
            'hugging_face_link': 'https://eswarkarthikk-object-detection.hf.space'
        },
        {
            'sectiontitle': 'Heart Disease',
            'title': 'Medical Diagnosis Heart Disease',
            'description': 'This project is a heart disease prediction application developed using a machine learning model and deployed on Hugging Face Spaces with a Gradio interface. Users can input various health parameters, such as age, cholesterol levels, and heart rate, to receive real-time predictions about the likelihood of heart disease. The model is trained using Scikit-learn and can be accessed via a shareable API for integration into other applications. This tool aims to assist individuals in assessing their heart health based on key indicators.',
            'image_link': 'https://i.ibb.co/2n5kdJx/image.png',
            'github_link': 'https://github.com/Eswarkarthikk/Ml_projects/tree/main/medical%20diagnosis%20heart%20disease',
            'weblink': 'https://aarieswarmlprojects.vercel.app/predict_heart_disease/',
            'hugging_face_link': 'https://edwardhuero-heart-disease.hf.space/'
        },
        {
            'sectiontitle': 'Digit Recognition',
            'title': 'Handwritten digit recognition',
            'description': 'This is a small project that i have done as a part of teckybot internship . you should check this project . I developed this model to detect the single digit at once . ',
            'image_link': 'https://i.ibb.co/bNpNKfC/image.png',
            'github_link': 'https://github.com/Eswarkarthikk/Ml_projects/tree/main/Hand%20written%20digit%20recognition',
            'weblink': 'https://example.com/test3',
            'hugging_face_link': 'https://eswarkarthikk-digit-recognition.hf.space/'
        },
        {
            'sectiontitle': 'Route Finder',
            'title': 'Andra Pradesh route finding ',
            'description': ' This is not a machine learning project but i have developed this from scratch . i got the dataset built by me and you should check this . It results the routs according to the location of the cities rather than the actual route between them . ',
            'image_link': 'https://i.ibb.co/T42rZ25/image.png',
            'github_link': 'https://github.com/Eswarkarthikk/Ml_projects/tree/main/Route%20Finding',
            'weblink': 'https://example.com/test4',
            'hugging_face_link': 'https://edwardhuero-route-finding.hf.space/'
        },
        {
            'sectiontitle': 'Fraud Detection',
            'title': 'Credit Card Fraud Detection',
            'description': 'This model is trained on the previous credit card users which used them to do the fraudulant transactions . so by using the past dataset i made this model to detect the fraudsters before even authorizing a credit card to them . ',
            'image_link': 'https://i.ibb.co/KVKFGGG/image.png',
            'github_link': 'https://github.com/Eswarkarthikk/Ml_projects/tree/main/Credit%20card%20fraud%20detection',
            'weblink': 'https://aarieswarmlprojects.vercel.app/predict_fraud/',
            'hugging_face_link': 'https://eswarkarthikk-credit-card-fraud-detection.hf.space/'
        }
    ]

    
    # Render the template with the projects data
    return render(request, 'mlprojects.html', {'projects': projects})

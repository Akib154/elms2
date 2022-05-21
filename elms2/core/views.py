from django.shortcuts import render

# Create your views here.

course_list = [
    {
        'id': 1,
        'title': "web programming",
        'notice': [
            {
                'id': 1,
                'title': "notice1"
            }
        ]
    },
    {
        'id': 2,
        'title': "system programming",
        'notice': [
            {
                'id': 1,
                'title': "notice3"
            }
        ]
    },
    {'id': 3,
     'title': "operating system",
     'notice': [
         {
             'id': 1,
             'title': "notice3"
         }
     ]
     },
    {'id': 4,
     'title': "software engineer",
     'notice': [
         {
             'id': 1,
             'title': "notice3"
         }
     ]
     },
]


def home(request):
    return render(request, 'login.html',)


def dashboard(request):

    return render(request, 'dashboard.html', {'courses': course_list})

def course_details(request,course_id):
    course = course_list[course_id-1]
    return render(request,'course_detail.html', {'course': course})

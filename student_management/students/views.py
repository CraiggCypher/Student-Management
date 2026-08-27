from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def student_list(request):

    students = [
        {
            'name': 'Cypher',
            'age': 30,
            'course': 'Computer Science',
            'score': 93
        },
        {
            'name': 'Collins',
            'age': 32,
            'course': 'System Engineering',
            'score': 77
        },
        {
            'name': 'Rose',
            'age': 28,
            'course': 'Software Engineering',
            'score': 69
        },
        {
            'name': 'Dukes',
            'age': 27,
            'course': 'Cyber Security',
            'score': 44
        }
    ]

    context = {
        'students': students,
        'school_name': 'CraigLink University'
    }

    return render(request, 'student_list.html', context)


def about(request):
    return render(request, 'about.html')
# Контроллер (view)
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Course



# Create your views here.
# Создание функции индекс
# def index(request):
#     courses = Course.objects.all()
#     return HttpResponse(courses)

# def index(request):
#     courses = Course.objects.all()
#     return render(request, 'courses.html')

def index(request):
    courses = Course.objects.all()
    return render(request, 'shop/courses.html', {'courses': courses})

def single_course(request, course_id):
    # OPTION1
    """ try:
        course = Course.objects.get(pk=course_id)
        return render(request, 'shop/single_course.html', {'course': course})
    except Course.DoesNotExist:
        raise Http404 """

    # OPTION2
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'shop/single_course.html', {'course': course})

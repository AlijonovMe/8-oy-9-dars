from django.shortcuts import render, redirect, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest
from django.contrib import messages
from datetime import datetime
from .models import *
from .forms import *


def index(request):
    courses = Course.objects.all()
    lessons = Lessons.objects.all()

    context = {
        'courses': courses,
        'lessons': lessons,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)


def courses(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = Lessons.objects.filter(course_id=course_id)

    context = {
        'courses': [course],
        'lessons': lessons,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)


def lessons(request, lesson_id):
    lesson = get_object_or_404(Lessons, id=lesson_id)

    context = {
        'lesson': lesson,
        'current_year': datetime.now().year
    }

    return render(request, 'detail.html', context)


def addCourse(request: WSGIRequest):
    if request.method == 'POST':
        form = CourseForms(data=request.POST, files=request.FILES)
        if form.is_valid():
            if Course.objects.filter(name=form.cleaned_data['name']).exists():
                messages.success(request, "Ma'lumot saqlanmadi. Bunday kurs allaqachon mavjud!")
            else:
                Course.objects.create(**form.cleaned_data)
                messages.success(request, "Ma'lumot muvaffaqiyatli saqlandi!")
            return redirect('addCourse')

    context = {
        'forms': CourseForms()
    }
    return render(request, 'addCourse.html', context)


def addLesson(request: WSGIRequest):
    if request.method == 'POST':
        form = LessonForms(data=request.POST, files=request.FILES)
        if form.is_valid():
            if Lessons.objects.filter(name=form.cleaned_data['name'], course=form.cleaned_data['course']).exists():
                messages.success(request, "Ma'lumot saqlanmadi.Bunday vazifa allaqachon mavjud!")
            else:
                Lessons.objects.create(**form.cleaned_data)
                messages.success(request, "Ma'lumotlar muvaffaqiyatli saqlandi!")
            return redirect('addLesson')

    context = {
        'forms': LessonForms()
    }
    return render(request, 'addLesson.html', context)

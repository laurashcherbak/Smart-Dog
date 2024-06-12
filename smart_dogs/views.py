from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
# from django.utils.translation import activate

from .models import Topic, Feedback, Course, Entry, About_course, CourseModule, RegisteredCourse, ModuleSection, DogQuiz 
from .forms import TopicForm, EntryForm, CourseForm, FeedbackForm, DogQuizForm


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django.utils.safestring import SafeText

# activate("uk")

# Create your views here.
def index(request):
    """Main page"""
    return render(request, 'smart_dogs/index.html')

def courses(request):
    """Courses page"""
    courses = Course.objects.order_by('date_added')
    context = {'courses': courses}
    return render(request, 'smart_dogs/courses.html', context)

@login_required
def new_course(request):
    """Add a new course."""
    if request.method != 'POST':
        # No data sent. Create an empty form.
        form = CourseForm()
    else:
        # Sent POST; process the data.
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('smart_dogs:courses')
        
    # Show empty or invalid form.
    context = {'form': form}
    return render(request, 'smart_dogs/new_course.html', context)


def about_course(request, course_id):
    """About course page"""
    course = Course.objects.get(id=course_id)
    about_course_set = course.about_course_set.all()
    modules = CourseModule.objects.filter(course=course)
    context = {'course': course, 'about_course_set': about_course_set, 'modules': modules}
    return render(request, 'smart_dogs/about_course.html', context)



def forum(request):
    """Forum page"""
    # Display all topics
    forum = Topic.objects.order_by('date_added')
    context = {'forum': forum}
    return render(request, 'smart_dogs/forum.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data sent. Create an empty form.
        form = TopicForm()
    else:
        # Sent POST; process the data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('smart_dogs:forum')
        
    # Show empty or invalid form.
    context = {'form': form}
    return render(request, 'smart_dogs/new_topic.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'smart_dogs/topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data sent. Create an empty form.
        form = EntryForm()
    else:
        # Sent POST; process the data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.owner = request.user  
            new_entry.save()
            return redirect('smart_dogs:topic', topic_id=topic_id)
        
    # Show empty or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'smart_dogs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
 
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('smart_dogs:topic', topic_id=topic.id)
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'smart_dogs/edit_entry.html', context)
        

def feedbacks(request):
    """Feedbacks page"""
    # Display all feedbacks
    feedbacks = Feedback.objects.order_by('-date_added')
    context = {'feedbacks': feedbacks}
    return render(request, 'smart_dogs/feedbacks.html', context)

@login_required
def new_feedback(request):
    """Add a new feedback."""
    if request.method != 'POST':
        # No data sent. Create an empty form.
        form = FeedbackForm()
    else:
        # Sent POST; process the data.
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            new_feedback = form.save(commit=False)
            new_feedback.owner = request.user  
            new_feedback.save()
            return redirect('smart_dogs:feedbacks')
        
    # Show empty or invalid form.
    context = {'form': form}
    return render(request, 'smart_dogs/new_feedback.html', context)


@login_required
def edit_feedback(request, feedback_id):
    """Edit an existing feedback."""
    feedback = Feedback.objects.get(id=feedback_id)
 
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = FeedbackForm(instance=feedback)
    else:
        # POST data submitted; process data.
        form = FeedbackForm(instance=feedback, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('smart_dogs:feedbacks')
        
    context = {'feedback': feedback, 'form': form}
    return render(request, 'smart_dogs/edit_feedback.html', context)


def cooperation(request):
    """Cooperation page"""
    return render(request, 'smart_dogs/cooperation.html')

def authentication(request):
    """Authentication page"""
    return render(request, 'smart_dogs/authentication.html')

def user_courses(request):
    """User courses page"""
    return render(request, 'smart_dogs/user_courses.html')

# from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

@login_required
def register_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    # Перевірка, чи користувач ще не зареєстрований на цей курс
    if not RegisteredCourse.objects.filter(user=request.user, course=course).exists():
        RegisteredCourse.objects.create(user=request.user, course=course)

    return redirect('smart_dogs:user_courses')

from django.shortcuts import render
from .models import RegisteredCourse

@login_required
def user_courses(request):
    # Отримати курси, на які користувач зареєстрований
    user_courses = RegisteredCourse.objects.filter(user=request.user).select_related('course')

    context = {'user_courses': user_courses}
    return render(request, 'smart_dogs/user_courses.html', context)


def about_user_course(request, course_id):
    """About user's course page"""
    course = Course.objects.get(id=course_id)
    modules = CourseModule.objects.filter(course=course)
    context = {'user': request.user, 'course': course, 'modules': modules}
    return render(request, 'smart_dogs/about_user_course.html', context)

@login_required
def section_detail(request, section_id):
    section = get_object_or_404(ModuleSection, id=section_id)

    registered_course = get_object_or_404(RegisteredCourse, user=request.user, course=section.module.course)

    # Отримайте попередній і наступний розділ
    previous_section = ModuleSection.objects.filter(module=section.module, id__lt=section_id).order_by('-id').first()
    next_section = ModuleSection.objects.filter(module=section.module, id__gt=section_id).order_by('id').first()

    context = {'section': section, 'previous_section': previous_section, 'next_section': next_section, 'course_id': registered_course.course.id}
    return render(request, 'smart_dogs/section_detail.html', context)

def success_page(request):
    return render(request, 'smart_dogs/success_page.html')

@login_required
def dog_quiz(request):
    if request.method == 'POST':
        form = DogQuizForm(request.POST)
        if form.is_valid():
            form.save()
            recommended_course = analyze_user_responses(form.cleaned_data)
            if recommended_course:
                return render(request, 'smart_dogs/dog_quiz.html', {'form': form, 'recommended_course': recommended_course})
            else:
                return render(request, 'smart_dogs/dog_quiz.html', {'form': form, 'no_course_found': True})
    else:
        form = DogQuizForm()
    
    return render(request, 'smart_dogs/dog_quiz.html', {'form': form})


import random

def analyze_user_responses(form_data):
    # Отримання рівня підготовки користувача
    user_level = form_data.get('skill_level')

    # Перевірка, чи отримано значення рівня підготовки користувача з форми
    if user_level is not None:
        user_level = user_level.lower()
    else:
        return "Рівень підготовки користувача не визначено"

    # Отримання всіх описів курсів та їх цільової аудиторії
    courses_info = About_course.objects.all()

    # Ініціалізація змінних для збереження найкращого курсу та його схожості з користувачем
    best_courses = []
    best_similarity = -1

    # Проходження по кожному курсу
    for course_info in courses_info:
        # Перевірка для рівня навичок "Новачок"
        if user_level == 'beginner':
            if 'beginners' in course_info.target_audience.lower():
                # Обчислення схожості
                vectorizer = CountVectorizer().fit_transform([str(form_data[field_name]) for field_name in form_data] + [course_info.course_description])
                similarity_matrix = cosine_similarity(vectorizer)
                similarity = similarity_matrix[0][-1]

                # Оновлення найкращого курсу, якщо знайдено краще зіставлення або якщо це перший підходящий курс
                if similarity > best_similarity or not best_courses:
                    best_courses = [(course_info.course, similarity)]
                    best_similarity = similarity
                elif similarity == best_similarity:
                    best_courses.append((course_info.course, similarity))
        
        # Перевірка для рівня навичок "Любитель"
        elif user_level == 'intermediate':
            if 'enthusiasts' in course_info.target_audience.lower():
                # Обчислення схожості
                vectorizer = CountVectorizer().fit_transform([str(form_data[field_name]) for field_name in form_data] + [course_info.course_description])
                similarity_matrix = cosine_similarity(vectorizer)
                similarity = similarity_matrix[0][-1]

                # Оновлення найкращого курсу, якщо знайдено краще зіставлення або якщо це перший підходящий курс
                if similarity > best_similarity or not best_courses:
                    best_courses = [(course_info.course, similarity)]
                    best_similarity = similarity
                elif similarity == best_similarity:
                    best_courses.append((course_info.course, similarity))

        # Перевірка для рівня навичок "Професіонал"
        elif user_level == 'professional':
            if 'experts' in course_info.target_audience.lower():
                # Обчислення схожості
                vectorizer = CountVectorizer().fit_transform([str(form_data[field_name]) for field_name in form_data] + [course_info.course_description])
                similarity_matrix = cosine_similarity(vectorizer)
                similarity = similarity_matrix[0][-1]

                # Оновлення найкращого курсу, якщо знайдено краще зіставлення або якщо це перший підходящий курс
                if similarity > best_similarity or not best_courses:
                    best_courses = [(course_info.course, similarity)]
                    best_similarity = similarity
                elif similarity == best_similarity:
                    best_courses.append((course_info.course, similarity))

    # Вибір рекомендованого курсу з найвищою схожістю або випадкового, якщо кілька курсів мають однакову схожість
    if best_courses:
        recommended_course, _ = random.choice(best_courses)
        recommended_course_name = recommended_course.text
    else:
        recommended_course_name = "Рекомендований курс не знайдено"

    return recommended_course_name


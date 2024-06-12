"""Define URL patterns for smart_dogs."""

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'smart_dogs'
urlpatterns = [
    # Main page
    path('', views.index, name='index'),
    # Courses page
    path('courses/', views.courses, name='courses'),
    # Add course
    path('new_course/', views.new_course, name='new_course'),
    # About course
    path('courses/<int:course_id>/', views.about_course, name='about_course'),

    # Forum page
    path('forum/', views.forum, name='forum'),
    # Add new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Topic page
    path('forum/<int:topic_id>/', views.topic, name='topic'),
    # Add entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Feedbacks page
    path('feedbacks/', views.feedbacks, name='feedbacks'),
    # Add feedback
    path('new_feedback/', views.new_feedback, name='new_feedback'),
    # Edit feedback
    path('edit_feedback/<int:feedback_id>/', views.edit_feedback, name='edit_feedback'),
    # Cooperation page
    path('cooperation/', views.cooperation, name='cooperation'),
    # Authentication Page - Login or Registration page
    path('authentication/', views.authentication, name='authentication'),

    # User home page with courses
    path('user_courses/', views.user_courses, name='user_courses'),

    path('register_course/<int:course_id>/', views.register_course, name='register_course'),

    path('about_user_course/<int:course_id>/', views.about_user_course, name='about_user_course'),

    path('section_detail/<int:section_id>/', views.section_detail, name='section_detail'),
    
    # Quiz
    path('dog_quiz/', views.dog_quiz, name='dog_quiz'),
    path('success_page/<int:course_id>/', views.success_page, name='success_page'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



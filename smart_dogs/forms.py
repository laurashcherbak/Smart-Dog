from django import forms
from django.utils.translation import gettext_lazy as _
# from django.utils.translation import activate

from .models import Topic, Entry, Course, Feedback, DogQuiz
# activate("uk")

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class CourseForm(forms.ModelForm):
    image = forms.ImageField(required=False, initial='', help_text='', widget=forms.ClearableFileInput(attrs={'multiple': False}), label=_('Image'))   

    class Meta:
        model = Course
        fields = ['text', 'image']
        labels = {'text': 'Назва курсу:', 'image': 'Image'}

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class DogQuizForm(forms.ModelForm):
    class Meta:
        model = DogQuiz
        fields = ['name', 'age', 'size', 'skill_level']
        labels = {
            'name': 'Ім\'я собаки',
            'age': 'Вік собаки',
            'size': 'Розмір собаки',
            'skill_level': 'Рівень підготовки собаки',
        }


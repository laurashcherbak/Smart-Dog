from django.contrib import admin
from .models import Topic, Entry, Feedback, Course, About_course, CourseModule, ModuleSection, SectionDetail, DogQuiz

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Feedback)
admin.site.register(Course)
admin.site.register(About_course)
admin.site.register(CourseModule)
admin.site.register(ModuleSection)
admin.site.register(SectionDetail)
admin.site.register(DogQuiz)

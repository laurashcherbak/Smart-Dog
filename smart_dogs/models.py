from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """The topic the user is discussing in forum."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Some specific information on this topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."

class Feedback(models.Model):
    """Feedback."""
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    # date_added = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'feedbacks'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."


class Course(models.Model):
    """Course name."""
    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='smart_dogs/templates/smart_dogs/course_images/', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

    
class CourseModule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()  # Номер модуля
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"Модуль {self.number}: {self.title}"

class ModuleSection(models.Model):
    module = models.ForeignKey(CourseModule, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return f"Розділ: {self.title}"


class About_course(models.Model):
    """About course"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # New fields
    phrase = models.CharField(max_length=200, default='Default Phrase')
    course_description = models.TextField(default='Default Course Description')
    target_audience = models.CharField(max_length=100, choices=[
        ('beginners', 'Новачки'),
        ('enthusiasts', 'Любителям'),
        ('experts', 'Експертам'),
    ], default='beginners')
    modules = models.ManyToManyField(CourseModule, related_name='about_courses')


    class Meta:
        verbose_name_plural = 'about_courses'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.phrase[:50]}..."


class RegisteredCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.course.text}"


class SectionDetail(models.Model):
    section = models.ForeignKey(ModuleSection, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='section_photos/', blank=True, null=True)
    video = models.FileField(upload_to='section_videos/', blank=True, null=True)

    def __str__(self):
        return f'Detail for Section {self.section.title}'


class DogQuiz(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    size = models.CharField(max_length=50, choices=[
        ('small', 'Маленька'),
        ('medium', 'Середня'),
        ('large', 'Велика'),
    ])
    skill_level = models.CharField(max_length=50, choices=[
        ('beginner', 'Новачок'),
        ('intermediate', 'Любитель'),
        ('professional', 'Професіонал'),
    ])

    def __str__(self):
        return self.name



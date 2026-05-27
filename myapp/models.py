from django.db import models
from django.contrib.auth.models import User


# User Profile
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    bio = models.TextField(
        blank=True,
        null=True
    )

    skills = models.CharField(
        max_length=300,
        blank=True
    )

    profile_image = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username


# Interview Role
class InterviewRole(models.Model):

    ROLE_CHOICES = [
        ('software', 'Software Engineer'),
        ('data', 'Data Analyst'),
        ('hr', 'HR'),
        ('marketing', 'Marketing'),
    ]

    role_name = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES
    )

    description = models.TextField()

    def __str__(self):
        return self.get_role_name_display()


# Interview Question
class InterviewQuestion(models.Model):

    role = models.ForeignKey(
        InterviewRole,
        on_delete=models.CASCADE
    )

    question_text = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.question_text[:50]


# Interview Session
class InterviewSession(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    role = models.ForeignKey(
        InterviewRole,
        on_delete=models.CASCADE
    )

    started_at = models.DateTimeField(
        auto_now_add=True
    )

    completed = models.BooleanField(
        default=False
    )

    overall_score = models.IntegerField(
        default=0
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# User Answers
class InterviewAnswer(models.Model):

    session = models.ForeignKey(
        InterviewSession,
        on_delete=models.CASCADE
    )

    question = models.ForeignKey(
        InterviewQuestion,
        on_delete=models.CASCADE
    )

    answer_text = models.TextField()

    score = models.IntegerField(
        default=0
    )

    feedback = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.session.user.username} Answer"


# AI Feedback Report
class FeedbackReport(models.Model):

    session = models.OneToOneField(
        InterviewSession,
        on_delete=models.CASCADE
    )

    confidence_score = models.IntegerField(
        default=0
    )

    communication_score = models.IntegerField(
        default=0
    )

    technical_score = models.IntegerField(
        default=0
    )

    strengths = models.TextField(
        blank=True,
        null=True
    )

    weaknesses = models.TextField(
        blank=True,
        null=True
    )

    ai_suggestions = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Report - {self.session.user.username}"
# Create your models here.

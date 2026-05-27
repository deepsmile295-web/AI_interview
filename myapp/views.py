from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def login_view(request):
    return render(request, 'login.html')


def register_view(request):
    return render(request, 'register.html')


def profile(request):
    return render(request, 'profile.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def role_selection(request):
    return render(request, 'role_selection.html')


def interview_room(request):
    return render(request, 'interview_room.html')


def feedback_result(request):
    return render(request, 'feedback_result.html')
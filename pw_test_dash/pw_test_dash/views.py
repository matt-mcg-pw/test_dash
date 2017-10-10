from django.shortcuts import render


def index(request):
    return render(request, 'pw_test_dash/index.html', {})

from django.shortcuts import render
from build_dataframe import get_frame


def index(request):
    dataframe = get_frame()
    return render(request, 'pw_test_dash/index.html', {'df': dataframe})

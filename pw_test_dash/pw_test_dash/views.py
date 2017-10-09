from django.shortcuts import render, get_object_or_404
from django.utils import timezone


def index(request):
    return render(request, 'pw_test_dash/index.html', {})


# Use as a model for building data frames, original at hack/pandas_hackery.py
def __build_frame():
    from pandas import pandas as pd
    from bs4 import BeautifulSoup as bs
    html = '/var/system-test_reports/allure-html/index.html'
    with open(html, 'r') as f:
        soup = bs(f, 'lxml')
        table = soup.find_all('table')[0]
    return table

    def __get_html()
        table = get_html()
        for row in table.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) == 2:
                vals = {}
                vals[cols[0]] = cols[1]
        return pd.DataFrame(list(vals.items()),
                columns=['detail link','suite fails'])


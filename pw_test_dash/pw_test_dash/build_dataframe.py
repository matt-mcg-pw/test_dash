from pandas import pandas as pd
from bs4 import BeautifulSoup as bs


def _get_html():
    html = '/var/system-test_reports/allure-html/index.html'
    with open(html, 'r') as f:
        soup = bs(f, 'lxml')
        table = soup.find_all('table')[0]
    return table


def get_frame():
    table = _get_html()
    for row in table.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) == 2:
            vals = {}
            vals[cols[0]] = cols[1]
    return pd.DataFrame(list(vals.items()),
                        columns=['detail link', 'suite fails'])

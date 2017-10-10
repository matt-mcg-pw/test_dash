"""
Module to pull xunit reports from 3rd party tools into a Panda's Dataframe used
to keep historical data on test suite runs.
"""


from glob import iglob
from pandas import pandas as pd


_PATH_TO_REPORTS = '/var/system-test_reports/allure-html/**/xunit.json'
_LAST_REPORT_DATE = '19701231'


def _get_pickled_dataframe():
    # retrieve the serialized dataframe storing historical data
    pass


def _get_date_last_report():
    # Get the date of the last report that was recorded in the dataframe
    pass


def _get_allure_reports():
    # Pull pickled dataframe from db, check for TS of last report seen
    # Pickled dataframe used for historical data
    # No need to save anything else, all static reports saved by allure
    for report in iglob(_PATH_TO_REPORTS, recursive=True):
        # parse date of report from path
        # if report date < last report date break
        pass
    # Merge with pickled dataframe from db


def _get_jenkins_reports():
    # Placeholder for when we start using Jenkins
    pass


def get_historical_dataframe():
    # publicly accessible method to get dataframe
    pass

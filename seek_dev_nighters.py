import requests
import json
import sys
import pytz
from datetime import datetime


def get_request_url():
    return 'https://devman.org/api/challenges/solution_attempts'


def get_attemps_info():
    url = get_request_url()
    attempts_info = []
    page = 1

    while True:
        params = {'page': page}
        response = requests.get(url, params=params)
        if not response.ok:
            return None

        json_data = response.json()

        if json_data is None:
            return None

        attempts_info += json_data['records']

        if not page < json_data['number_of_pages']:
            break

        page += 1

    return attempts_info


def get_midnighters_info(attempts_info):
    midnighters_info = {}

    for attempt in attempts_info:
        timezone = pytz.timezone(attempt['timezone'])
        date = datetime.fromtimestamp(attempt['timestamp'], tz=timezone)

        midnight_from = date.replace(hour=0, minute=0, second=0, microsecond=0)
        midnight_to = date.replace(hour=4, minute=0, second=0, microsecond=0)

        if midnight_from <= date <= midnight_to:
            date_format = date.strftime('%d-%m-%Y %H:%M')
            username = attempt['username']
            midnighters_info.setdefault(username, []).append(date_format)

    return midnighters_info


def output_midnighters_to_console(midnighters_info):
    print('Midnighters log:', '\n')
    for midnighter, dates in midnighters_info.items():
        print(midnighter)
        print('\n'.join(dates), '\n')


if __name__ == '__main__':
    attempts_info = get_attemps_info()

    if not attempts_info:
        sys.exit('Failed to load attemps info')

    midnighters_info = get_midnighters_info(attempts_info)

    if not midnighters_info:
        sys.exit('There are not any midnighters')

    output_midnighters_to_console(midnighters_info)

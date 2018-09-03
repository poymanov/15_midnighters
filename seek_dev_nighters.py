import requests
import json
import pytz
from datetime import datetime


def get_request_url():
    return 'https://devman.org/api/challenges/solution_attempts'


def load_attempts(pages_count):
    url = get_request_url()

    for page in range(1, pages_count):
        params = {'page': page}
        response = requests.get(url, params=params)

        if not response.ok:
            return None

        attempts_list = response.json()

        for attempt in attempts_list['records']:
            yield {
                'username': attempt['username'],
                'timestamp': attempt['timestamp'],
                'timezone': attempt['timezone']
            }


def get_pages_count():
    url = get_request_url()

    response = requests.get(url)

    if not response.ok:
        return None

    pages_info = response.json()

    return pages_info['number_of_pages']


def get_attemps_info():
    attempts_info = []

    pages_count = get_pages_count()

    if not pages_count:
        return None

    for attempt in load_attempts(pages_count):
        attempts_info.append(attempt)

    return attempts_info


def get_midnighters_info(attempts_info):
    midnighters_info = {}
    midnight_from = 0
    midnight_to = 4

    for attempt in attempts_info:
        timezone = pytz.timezone(attempt['timezone'])
        timestamp = attempt['timestamp']
        local_user_datetime = datetime.fromtimestamp(timestamp, tz=timezone)

        if midnight_from <= local_user_datetime.hour <= midnight_to:
            date_format = local_user_datetime.strftime('%d-%m-%Y %H:%M')
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
        exit('Failed to load attemps info')

    midnighters_info = get_midnighters_info(attempts_info)

    if not midnighters_info:
        exit('There are not any midnighters')

    output_midnighters_to_console(midnighters_info)

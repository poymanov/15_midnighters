import requests
import json
import pytz
from datetime import datetime


def get_request_url():
    return 'https://devman.org/api/challenges/solution_attempts'


def load_attempts():
    url = get_request_url()
    page = 1

    while True:
        params = {'page': page}
        response = requests.get(url, params=params)

        if not response.ok:
            return None

        attempts_page = response.json()

        if attempts_page is None:
            return None

        for attempt in attempts_page['records']:
            yield attempt

        if not page < attempts_page['number_of_pages']:
            break

        page += 1


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
    attempts_info = load_attempts()

    if not attempts_info:
        exit('Failed to load attemps info')

    midnighters_info = get_midnighters_info(attempts_info)

    if not midnighters_info:
        exit('There are not any midnighters')

    output_midnighters_to_console(midnighters_info)

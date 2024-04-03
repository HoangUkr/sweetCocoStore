import secrets
import random
import datetime
import decimal
from dateutil import relativedelta

def string_generator():
    length=10
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    # Generate the secure random string code
    string_code = ''.join(secrets.choice(characters) for _ in range(length))
    
    return string_code

def decimal_generator():
    random_decimal = random.random()
    random_decimal_with_two_digits = round(random_decimal, 2)
    return random_decimal_with_two_digits

def dateTime_generator():
    start_date = datetime.datetime.now()
    end_date = datetime.date.today() + relativedelta.relativedelta(months=1)
    time_between_dates = end_date - start_date
    total_seconds = time_between_dates.total_seconds()
    random_second = random.uniform(0, total_seconds)
    random_datetime = start_date + datetime.timedelta(seconds=random_second)
    return random_datetime
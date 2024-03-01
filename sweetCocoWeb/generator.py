import secrets
import random
import datetime
from dateutil import relativedelta

def string_generator():
    length=10
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    # Generate the secure random string code
    string_code = ''.join(secrets.choice(characters) for _ in range(length))
    
    return string_code

def float_generator():
    minVal=0.0
    maxVal=100.0
    return random.uniform(minVal, maxVal)

def dateTime_generator():
    start_date = datetime.datetime.now()
    end_date = datetime.date.today() + relativedelta.relativedelta(months=1)
    time_between_dates = end_date - start_date
    total_seconds = time_between_dates.total_seconds()
    random_second = random.uniform(0, total_seconds)
    random_datetime = start_date + datetime.timedelta(seconds=random_second)
    return random_datetime
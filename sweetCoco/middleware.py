from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth import logout
from .settings import SESSION_COOKIE_AGE
import datetime
import json

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.session)
        def serialize_data(data):
            """Serializes data, converting datetime objects to strings."""
            def default_handler(obj):
                if isinstance(obj, datetime):
                    return obj.isoformat()
                raise TypeError(f"Object of type '{obj.__class__.__name__}' is not JSON serializable")

            return json.dumps(data, default=default_handler)
        if request.user.is_authenticated:
            try:
                last_visit = request.session['last_visit']
            except KeyError:
                last_visit = None

            if last_visit:
                # time_delta = timezone.now() - last_visit
                time_delta = datetime.datetime.now() - last_visit
                if time_delta.seconds > SESSION_COOKIE_AGE:
                    logout(request)
                    return redirect('login')  # Replace 'login' with your login URL
            data = {
                'last_visit': datetime.datetime.now()
            }
            json_data = serialize_data(data)
            request.session['last_visit'] = json_data

        response = self.get_response(request)
        return response
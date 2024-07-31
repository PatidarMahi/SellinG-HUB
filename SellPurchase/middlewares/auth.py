from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
         
        if not request.session.get('student'):
           return redirect('student_login')

        response = get_response(request)
        return response

    return middleware
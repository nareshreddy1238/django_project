from django.http import HttpResponse

class MiddleWareLifeCycle:
    def __init__(self, get_response):
        print("Init Method Called")
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        print("Before view is called")
        response = self.get_response(request)
        print("After view is called")

        # Code to be executed for each request/response after
        # the view is called.

        return response


class ExceptionHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        return self.get_response(request)
    
    def process_exception(self, request, exception):
        print(exception)
        print(exception.__class__.__name__)
        return HttpResponse("<b> We currently facing issues. Please check back in a few minutess. </b>")
         
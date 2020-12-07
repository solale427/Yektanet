class IpMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if hasattr(view_func, 'view_class') and getattr(view_func.view_class, 'process_ip', False):
            user_ip = request.META['REMOTE_ADDR']
            request.user_ip = user_ip

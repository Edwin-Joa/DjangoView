from django.utils.deprecation import MiddlewareMixin


class TestMiddleware1(MiddlewareMixin):
    def process_request(self, requset):
        print('request1')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('view1')

    def process_response(self, request, response):
        print('response1')
        return response


class TestMiddleware2(MiddlewareMixin):
    def process_request(self, requset):
        print('request2')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('view2')

    def process_response(self, request, response):
        print('response2')
        return response

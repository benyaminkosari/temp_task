from rest_framework.response import Response

class BaseResponseMixin:
    def custom_response(self, message, data, status):
        response_data = {
            'message': message,
            'data': data
        }
        return Response(response_data, status)
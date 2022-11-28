from rest_framework.response import Response
from rest_framework import status
from functools import wraps

def resource_checker(model):
    def check_entity(fun):
        @wraps(fun)
        def inner_fun(*args, **kwargs):
            try:
                x = fun(*args, **kwargs)
                return x
            except model.DoesNotExist:
                return Response({
                                'status': False,
                                'status_code':status.HTTP_204_NO_CONTENT,
                                'message': 'The requested resource is not found'

                            })
             
        return inner_fun
    return check_entity
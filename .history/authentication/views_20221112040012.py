from django.utils import timezone
from django.db import transaction


from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.hashers import check_password


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny


from rest_framework_simplejwt.tokens import RefreshToken,OutstandingToken

from drf_yasg.utils import swagger_auto_schema

from authentication.models import EmpactUser
from authentication.serializers import RegisterSerializer, EmpactUserSerializer, LoginSerializer


User = get_user_model()



class RegisterAPIView(APIView):
    """
    """
    An api endpoint to register any Empact user. Email should be unique 
    '''
    serializer_class = RegisterSerializer

    @swagger_auto_schema(
    request_body=RegisterSerializer
)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            mobile_no = request.data.get('mobile_no')
            email = request.data.get('email')
            user_type = request.data.get('user_type')
            member_type = request.data.get('member_type')
            country = request.data.get('country')
            password = request.data.get('password')
            profile_pic_url = request.data.get('profile_pic_url')

            today = timezone.now().astimezone().strftime('Y-m-d')

            if len(password) < 6:
                return Response({
                    'status': False,
                    'message': 'Password should be atleast 6 characters'
                })
            else:
                with transaction.atomic():
                    first_name = first_name.strip()
                    last_name = last_name.strip()
                    mobile_number = mobile_no.strip()
                    user_type = user_type
                    email = email.strip()
                    profile_pic_url = profile_pic_url.strip()
                    member_type = member_type
                    country = country.strip()

                    user = User.objects.filter(username=email)
                    date_created=timezone.datetime.now()

                    if not user.exists():
                        try:
                            user = User.objects.create_user(
                                username=email, password=password)
                            empactUser = EmpactUser(user=user, first_name=first_name, last_name=last_name,
                                                    mobile_number=mobile_number, email=email, 
                                                    profile_pic_url=profile_pic_url, member_type=member_type,
                                                    country=country,date_created=date_created,user_type=user_type
                                                    )
                            empactUser.save()      
                            user = EmpactUser.objects.get(email=email,first_name=first_name)
                            serializer = EmpactUserSerializer(user)    
                            return Response({
                                'status':True,
                                'message':'Registration successfull',
                                'status_code':status.HTTP_200_OK,
                                'data':serializer.data,
                            })
                        except Exception as e:
                            print(f"Registration error {e}")

                            return Response({
                                'status': False,
                                'status_code':status.HTTP_500_INTERNAL_SERVER_ERROR,
                                'message': f'{e}'

                            })
                    else:
                        return Response({
                                'status': False,
                                'status_code':status.HTTP_400_BAD_REQUEST,
                                'message': 'Given user already exists'

                            })
        else:
            return Response({
                                'status':False,
                                'message':'Registration failed',
                                'status_code':status.HTTP_400_BAD_REQUEST,
                                'error':serializer.errors,
                            })

class LoginAPIView(APIView):
    """
    Takes a username and a password and the returns an access type JSON web
   
    """
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer

    def get(self, request):
        return Response()

    def post(self, request):
        print(request.data)
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = request.data.get('email')
            password = request.data.get('password')

        else:
            return Response({
                'status': False,
                'message': 'Login Failed',
                'status_code':status.HTTP_400_BAD_REQUEST,
                'errors': serializer.errors
            })

        user_qs = User.objects.filter(username=email)

        if user_qs.exists():
            user_obj = user_qs.first()
            if not user_obj.is_active:
                return Response({
                    'status': False,
                    'message': 'User has a dormant account',
                    'status_code': status.HTTP_401_UNAUTHORIZED
                })
            else:
                password_match = check_password(
                    password=password, encoded=user_obj.password)
                if not password_match:
                    return Response({
                        'status': False,
                        'message': 'Kindly provide correct username or password',
                        'status_code': status.HTTP_401_UNAUTHORIZED
                    })
                else:
                    refresh = RefreshToken.for_user(user=user_obj)
                    loggedin_user = EmpactUser.objects.get(user=user_obj)
                    serializer = EmpactUserSerializer(loggedin_user)
                    return Response({
                        'status': True,
                        'message': 'You have successfully logged in.',
                        'status_code':status.HTTP_200_OK,
                        'access_token': str(refresh.access_token),
                        'refresh_token': str(refresh),
                        'data': serializer.data
                    })
        else:
            return Response({
                        'status': False,
                        'message': 'Provided credentials does not exist.',
                        'status_code': status.HTTP_400_BAD_REQUEST,
                    })

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            email = request.user
            print("Email:", email)
            if not email:
                return Response({
                    'status': False,
                    'message': 'Either the email or the password is incorrect.'
                }, status=status.HTTP_401_UNAUTHORIZED)
            else:
                user = User.objects.filter(username=email)
                if not user.exists():
                    return Response({
                        'status': False,
                        'message': 'A user with this email does not exists.',
                        
                    })
                else:
                    user = user.first()
                    user_outstanding_tokens = OutstandingToken.objects.filter(
                        user=user)
                    if not len(user_outstanding_tokens):
                        return Response(
                            {'status': False,
                             'message': 'The token is not valid.',
                             'status_code':status.HTTP_401_UNAUTHORIZED
                             })

                    else:
                        user_outstanding_tokens.delete()
                        return Response({'status': True,
                                        'message': 'User successfully signed out.',
                                        'status_code':status.HTTP_200_OK,
                                         })
        except Exception as error:
            print('ERROR:', str(error))
            return Response({
                'status': False,
                'message': str(error),
                'status_code': status.HTTP_400_BAD_REQUEST,
            })

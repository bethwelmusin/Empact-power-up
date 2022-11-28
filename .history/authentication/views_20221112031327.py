from django.utils import timezone
from django.db import transaction


from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.hashers import check_password


from rest_framework.response import Response
from rest_framework import status,permissions
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken


from authentication.models import EmpactUser
from authentication.serializers import RegisterSerializer, EmpactUserSerializer, LoginSerializer


User = get_user_model()


class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer

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
                    user_type = user_type.strip()
                    email = email.strip()
                    profile_pic_url = profile_pic_url.strip()
                    member_type = member_type.strip()
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
    permission_classes = (permissions.AllowAny, )
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
                    profile = Profile.objects.get(user=user_obj)
                    serializer = ProfileSerializer(profile)
                    return Response({
                        'status': True,
                        'message': ResponseMessages.login_message,
                        'access_token': str(refresh.access_token),
                        'refresh_token': str(refresh),
                        'profile': serializer.data
                    }, status=status.HTTP_200_OK)

            payload = json.dumps({
                "email": username,
                "password": password,
                "returnSecureToken": True
            })
            headers = {
                'Content-Type': 'application/json'
            }

            res = requests.request(
                "POST", url, headers=headers, data=payload)
            if res.status_code == 200:
                response = res.json()
                user_id = response['localId']
                email = response['email']
                refreshToken = response['refreshToken']
                accessToken = response['idToken']
                expiresIn = response['expiresIn']
                user = User.objects.get(username=username)
                dagizo_user = DagizoUser.objects.get(email=username)
                print(f'USER {dagizo_user}')
                request.session['uid']=str(accessToken)

                if not hasattr(dagizo_user, 'user_type'):
                    return Response({
                        'status': False,
                        'message': 'A valid Dagizo Account is required'
                    })
                auth_user = UserSerializer(user)
                dagizo_user = DagizoUserSerializer(dagizo_user)
                refresh = RefreshToken.for_user(user)

                return Response({
                    'status': True,
                    'message': 'User login successful',
                    'access_token': accessToken,
                    'refresh_token':refreshToken,
                    'token_type': 'Bearer',
                    'expires_in':expiresIn,
                    'user_id':user_id,
                    'user': dagizo_user.data,

                })

            else:
                response = res.json()
                print(f'RESPOMSE===> {response}')
                return Response({
                    'status': False,
                    'message': response['error']['message'],

                })

        else:
            return Response({
                'status': False,
                'message': 'Please provide correct username and password',
            })

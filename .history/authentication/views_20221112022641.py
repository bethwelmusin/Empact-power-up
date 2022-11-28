import json
from django.utils import timezone
from django.db import transaction


from django.contrib.auth import get_user_model
from django.utils import timezone
from restaurant.serializers import RestaurantSerializer
from authentication.models import Chef, Client, Waiter

from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

from authentication.serializers import SuperSerializer, UserSerializer, RegisterSerializer, LoginSerializer, DagizoUserSerializer,RegisterRestaurantSerializer

from authentication.models import DagizoUser
import requests

User = get_user_model()

url = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyAnHGWa8k7RaAeLrONWFjJxxmfKmzM2xrY'


class CommandCenter(APIView):
    serializer_class = SuperSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # The magic line
        # try:
        user = User.objects.create_user('dagizoAdmin', password='dagizo@123')
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return Response({
            'data': "created"
        })
        # except:
        #     return Response({
        #         'data':"failed"
        #     })


class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        mobile_no = request.data.get('mobile_no')
        email = request.data.get('email')
        user_type = request.data.get('user_type')
        password = request.data.get('password')
        profile_pic_url = request.data.get('profile_pic_url')
        restaurant_code = request.data.get('restaurant_code')

        today = timezone.now().astimezone().strftime('Y-m-d')

        if len(password) < 6:
            return Response({
                'status': False,
                'message': 'Password should be atleast 6 characters'
            })
        else:
            # try:
            with transaction.atomic():
                first_name = first_name
                last_name = last_name
                mobile_no = mobile_no[-9:]
                mobile_number = f'254{mobile_no}'
                user_type = user_type
                email = email
                profile_pic_url = profile_pic_url
                restaurant_code = restaurant_code

                user = User.objects.filter(username=mobile_number)

                if not user.exists():
                    try:
                        fb_user = auth.create_user(email=email, email_verified=False, password=password,
                                                   display_name=f'{first_name} {last_name}', photo_url=profile_pic_url, disabled=False)
                        if fb_user.uid is not None:
                            user_id = fb_user.uid
                            user = User.objects.create_user(
                                username=email, password=password)
                            dagizo_user = DagizoUser(id=user_id,
                                                     user=user,  mobile_number=mobile_number, email=email, user_type=user_type, first_name=first_name, last_name=last_name)
                            dagizo_user.save()
                            user_obj=  DagizoUser.objects.get(id=user_id)
                            serializer = DagizoUserSerializer(user_obj)
                            if restaurant_code is not None:

                                restaurant = RestaurantBranch.objects.filter(
                                    restaurant_code=restaurant_code)
                                if restaurant.exists():
                                    restaurant = RestaurantBranch.objects.get(
                                        restaurant_code=restaurant_code)

                                    if user_type == 'Chef':

                                        Chef(restaurant_code=restaurant,
                                             dagizo_user=dagizo_user, date_created=today,profile_pic_url=profile_pic_url).save()                                        
                                        return Response({
                                            'status': True,
                                            'message': f'Chef Registration to {restaurant.restaurant_name}completed successfully',
                                            'user': serializer.data
                                        })
                                    elif user_type == 'Waiter':

                                        Waiter(restaurant_code=restaurant,
                                               dagizo_user=dagizo_user, date_created=today,profile_pic_url=profile_pic_url).save()
                                        return Response({
                                            'status': True,
                                            'message': f'Waiter Registration to {restaurant.restaurant_name}completed successfully',
                                            'user': serializer.data
                                        })

                                else:
                                    return Response({
                                        'status': False,
                                        'message': 'Member registration failed. Restaurant does not exist'
                                    })
                            else:
                                Client(dagizo_user=dagizo_user,
                                       profile_picture_url=profile_pic_url, date_created=today).save()

                                return Response({
                                                'status': True,
                                                'message': 'Registration completed successfully',
                                                'user': serializer.data
                                                })
                        else:
                            return Response({
                                'status': False,
                                'message': 'Member registration failed. User id not found'
                            })
                    except Exception as e:
                        print(f"Firebase error {e}")

                        return Response({
                            'status': False,
                            'message': f'{e}'
                        })

                else:
                    return Response({
                        'status': False,
                        'message': 'User with the same record already exists'
                    })

            # except IntegrityError as error:
            #     print('ERROR:', str(error))
            #     return Response({
            #         'status': False,
            #         'message': 'Mobile number already in use.'
            #     })
            # except Exception as error:
            #     print('ERROR:', str(error))
            #     return Response({
            #         'status': False,
            #         'message': 'Member registration failed'
            #     })


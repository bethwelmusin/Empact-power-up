from django.utils import timezone
from django.db import transaction


from django.contrib.auth import get_user_model
from django.utils import timezone
from authentication.models import EmpactUser


from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from authentication.serializers import RegisterSerializer, EmpactUserSerializer


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


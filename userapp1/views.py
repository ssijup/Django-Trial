from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
import random
import string

#Imports from other files
from .serializers import UserDetailsSerializer,UserLoginSerializer,AllUserDetailsSerializer
from .models import UserDetails




def user(request):
    return HttpResponse("Hii siju")

def generate_unique_id():
    characters = string.ascii_uppercase + string.digits
    unique_id = ''.join(random.choices(characters, k=8))
    print(unique_id)
    return unique_id


@api_view(['POST' ,"GET"])
def user_demo(request):
    if request.method == 'POST' :
        data = request.data
        user_entrolment_id = generate_unique_id()
        while UserDetails.objects.filter(user_entrolment_id =user_entrolment_id).exists():
            user_entrolment_id = generate_unique_id()
        data['user_entrolment_id'] =  user_entrolment_id
        serializer = UserDetailsSerializer(data=data)
        if serializer.is_valid():  
            serializer.save()
            return Response(serializer.data,status =status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET' :
        users = UserDetails.objects.all()
        serializer = AllUserDetailsSerializer(users ,many = True)
        return Response(serializer.data)
    else :
        return Response(serializer.errors)



@api_view(['POST'])
def user_registeration(request):
    if request.method == 'POST' :
        data = request.data
        user_entrolment_id = generate_unique_id()
        while UserDetails.objects.filter(user_entrolment_id =user_entrolment_id).exists():
            user_entrolment_id = generate_unique_id()
        data['user_entrolment_id'] =  user_entrolment_id
        serializer = UserDetailsSerializer(data=data)
        if serializer.is_valid():
            user_email = serializer.validated_data['user_email']
            # if UserDetails.objects.filter(user_email = user_email).exists():
            user_obj , user_created =UserDetails.objects.get_or_create(user_email = user_email ,defaults= data)
            print(user_obj.user_name)
            if not user_created:
                return Response({"message" : "Email already exists"} ,status=status.HTTP_409_CONFLICT)
            return Response({"message" :"Registration sucessfull" ,"data" : serializer.data },status =status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class UserLogin(APIView):
    def post(self,request):
        data = request.data
        serializer = UserLoginSerializer(data = data)
        if serializer.is_valid():
            user_password = serializer.validated_data['user_password']
            user_entrolment_id = serializer.validated_data['user_entrolment_id']
            user_obj = UserDetails.objects.filter(user_entrolment_id = user_entrolment_id ,user_password = user_password).first()
            if user_obj:
                refresh = RefreshToken.for_user(user_obj)
                # access_token = refresh.access_token
                return Response({"message": "Login successful" ,
                                  'refresh': str(refresh) ,
                                 'access': str(refresh.access_token) ,
                                 'data' :serializer.data} ,
                                   status =status.HTTP_200_OK)
            return Response({"error": "Invalid credentials" }, status=401)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    





           
                






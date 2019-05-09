from home.api.serializers import LinkSerializer, LoginSerializer
from home.models import Link
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import status


@api_view(['GET', 'POST'])
def link_list(request):

    if request.method == 'GET':
        data = Link.objects.all()
        serializer = LinkSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LinkSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'GET'])
def link_details(request, short_code):
    try:
        link = Link.objects.get(short_code=short_code)
    except Link.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        link.delete()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'GET':
        serializer = LinkSerializer(link)
        return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = LoginSerializer(data=data)
        print(serializer.initial_data)
        if serializer.is_valid():
            user = User.objects.get(email=serializer.data['email'])
            user = authenticate(username=user.username, password=serializer.data['password'])
            if user is not None:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
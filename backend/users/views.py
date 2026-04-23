from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import User

@api_view(['POST'])
def register(request):
    email = request.data.get('email')
    password = request.data.get('password')
    username = request.data.get('username')
    
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email уже используется'}, status=400)
    
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    token, _ = Token.objects.get_or_create(user=user)
    return Response({
        'token': token.key,
        'user': {
            'id': user.id,
            'email': user.email,
            'username': user.username,
        }
    }, status=201)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    try:
        user = User.objects.get(email=email)
        user = authenticate(username=user.username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'username': user.username,
                }
            })
        return Response({'error': 'Неверный пароль'}, status=400)
    except User.DoesNotExist:
        return Response({'error': 'Пользователь не найден'}, status=400)

@api_view(['GET'])
def me(request):
    if not request.user.is_authenticated:
        return Response({'error': 'Не авторизован'}, status=401)
    return Response({
        'id': request.user.id,
        'email': request.user.email,
        'username': request.user.username,
    })
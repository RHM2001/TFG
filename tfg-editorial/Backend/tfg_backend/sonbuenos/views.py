from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

@api_view(['POST', 'OPTIONS'])
@permission_classes([AllowAny])
@csrf_exempt
def login_view(request):
    error_message = None

    if request.method == 'OPTIONS':
        # Manejar solicitudes OPTIONS aquí si es necesario
        return JsonResponse({"detail": "OPTIONS request handled successfully"}, status=200)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        print(f'Usuario recibido en la solicitud: {username}')
        print(f'Contraseña recibida en la solicitud: {password}')

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Iniciar sesión si la autenticación fue exitosa
            login(request, user)
            
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            # Puedes devolver más información según tus necesidades
            response_data = {
                "detail": "Login successful",
                "access_token": access_token,
                "refresh_token": refresh_token,
            }
            
            return JsonResponse(response_data, status=200)
        else:
            # Mostrar un mensaje de error si la autenticación falla
            error_message = "Usuario o contraseña incorrectos"

    # En caso de solicitud no POST o fallo en la autenticación, devolver un error
    return JsonResponse({"error": error_message or "Error en la autenticación"}, status=400)

    

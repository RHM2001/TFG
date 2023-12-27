from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Solicitud

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

@require_http_methods(['PUT'])
@permission_classes([AllowAny])
@csrf_exempt
def marcar_solicitud_como_tratada(request, solicitud_id):
    try:
        solicitud = Solicitud.objects.get(id=solicitud_id)
        solicitud.tratado = True
        solicitud.save()
        return JsonResponse({'message': 'Solicitud marcada como tratada correctamente'}, status=200)
    except Solicitud.DoesNotExist:
        return JsonResponse({'error': 'Solicitud no encontrada'}, status=404)
    
@require_http_methods(['DELETE'])
@permission_classes([AllowAny])
@csrf_exempt
def eliminar_solicitud(request, solicitud_id):
    try:
        solicitud = Solicitud.objects.get(id=solicitud_id)
        solicitud.delete()
        return JsonResponse({'message': 'Solicitud eliminada correctamente'}, status=200)
    except Solicitud.DoesNotExist:
        return JsonResponse({'error': 'Solicitud no encontrada'}, status=404)

    

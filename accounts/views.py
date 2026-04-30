import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import OTP

class SendOTP(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({"error": "Email is required"}, status=400)
        
        # Генерируем 6 цифр
        code = str(random.randint(100000, 999999))
        OTP.objects.create(email=email, code=code)
        
        # В реальном проекте здесь был бы send_mail(). 
        # Сейчас просто выведем в консоль:
        print(f"DEBUG: OTP для {email} это {code}")
        
        return Response({"message": "OTP sent to email"})

class VerifyOTP(APIView):
    def post(self, request):
        email = request.data.get('email')
        code = request.data.get('code')
        
        otp_record = OTP.objects.filter(email=email, code=code).last()
        
        if otp_record and otp_record.is_valid():
            # Находим или создаем пользователя
            user, created = User.objects.get_or_create(username=email, email=email)
            user.is_active = True
            user.save()
            
            # Генерируем JWT токен
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        
        return Response({"error": "Invalid or expired OTP"}, status=400)
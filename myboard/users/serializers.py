from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

# JWT 설정 핸들러 가져오기
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        write_only=True,
        required=True, 
        validators=[UniqueValidator(queryset=User.objects.all())]  # 중복 검증
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]  # 비밀번호 검증
    )
    passwordcheck = serializers.CharField(write_only=True, required=True)  # 비밀번호 확인
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    bio = serializers.CharField(required=False, allow_blank=True, label="소개글")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'bio', 'password', 'passwordcheck', 'email')

    def validate(self, data):
        if data['password'] != data['passwordcheck']:
            raise serializers.ValidationError(
                {"password": "패스워드가 일치하지 않습니다"}
            )
        return data

    def create(self, validated_data):
        # 사용자 생성 및 기본 정보 설정
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.is_active = False  # 활성화되지 않은 계정으로 설정
        user.save()

        # 프로필의 bio 필드 설정
        if 'bio' in validated_data:
            user.profile.bio = validated_data['bio']
            user.profile.save()

        # JWT 토큰 생성
        payload = JWT_PAYLOAD_HANDLER(user)
        jwt_token = JWT_ENCODE_HANDLER(payload)

        # 인증 이메일 생성 및 전송
        message = render_to_string('users/user_activate_email.html', {
            'user': user,
            'domain': 'localhost:8000',  # 실제 도메인 또는 IP 주소로 대체해야 함
            'uid': force_str(urlsafe_base64_encode(force_bytes(user.pk))),
            'token': jwt_token,
        })
        mail_subject = '[SDP] 회원가입 인증 메일입니다'
        to_email = user.email
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

        return user


#로그인 시리얼라이저
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True, write_only = True) 

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if user : 
            token, created = Token.objects.get_or_create(user=user)
            return {
                'user': user,
                'token': token
            }
        raise serializers.ValidationError(
            {"error" : "로그인 할 수 없습니다. 이메일 또는 비밀번호를 확인하세요."}
        )
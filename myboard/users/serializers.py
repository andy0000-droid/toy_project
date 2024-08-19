from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password 
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator #이메일 중복 방지를 위한 검증 도구


#회원가입 시리얼라이저
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        write_only=True,
        required = True, 
        validators = [UniqueValidator(queryset=User.objects.all())] #중복 검증
    )
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password] #비밀번호 검증
    )
    passwordcheck = serializers.CharField(write_only=True, required = True) #비밀번호 확인
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    bio = serializers.CharField(required = False, allow_blank = True, label = "소개글")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'bio', 'password','passwordcheck','email')

    def validate(self, data) :
        if data['password'] != data['passwordcheck']:
            raise serializers.ValidationError(
                {"password" : "패스워드가 일치하지 않습니다"}
            )
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username =validated_data['email'],
            email = validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()

        if 'bio' in validated_data:
            user.profile.bio = validated_data['bio']
            user.profile.save()

        token = Token.objects.create(user=user)
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
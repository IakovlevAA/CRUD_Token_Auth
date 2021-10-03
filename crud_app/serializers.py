from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator



class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=2,write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'],first_name=self.validated_data['first_name'],
    last_name=self.validated_data['last_name'],is_active=self.validated_data['is_active'])

        return user


    class Meta:
        model = User
        fields = ['id', 'username', 'email','password','first_name','last_name','is_active','last_login','is_superuser']
        write_only_fields=['username', 'email','password','first_name','last_name','is_active','is_superuser']
        read_only_fields=['id','last_login',]

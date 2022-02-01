from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'name', 'email','password']


    def create(self, validated_data):
        user = User.objects.create(
            **validated_data
        )
        # add groups to the user ↓
        user.set_password(make_password(validated_data['password']))
        user.save()
        return user



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        token['email'] = user.email
        token['phone'] = user.phone
        token['roll'] = user.roll
        # ...

        return token

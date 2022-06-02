from rest_framework import serializers
from django.contrib.auth.models import User
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('username','first_name','last_name','email','url')
        
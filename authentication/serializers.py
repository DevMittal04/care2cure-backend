from rest_framework import serializers
from .models import User, Anonymous_User, Counsellor, Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    #def __init__(self, instance=None, **kwargs):
    #    super().__init__(instance=instance, **kwargs)
    #article = ArticleSerializer()
    # To update only certain attributes
    #def __init__(self, *args, **kwargs):
    #    kwargs['partial'] = True
    #    super(UserSerializer, self).__init__(*args, **kwargs)
    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','password')

class AnonymousSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anonymous_User
        fields = '__all__'

class CounsellorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsellor
        fields = '__all__'
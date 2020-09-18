from rest_framework import serializers
from .models import User, Anonymous_User, Counsellor, Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

<<<<<<< HEAD
    #def __init__(self, instance=None, **kwargs):
    #    super().__init__(instance=instance, **kwargs)
    #article = ArticleSerializer()
=======
    # Tried to associate Users Article with the User Model
    #def __init__(self, instance=None, **kwargs):
    #    super().__init__(instance=instance, **kwargs)
    #article = ArticleSerializer(allow_null=True)
    
>>>>>>> c38e296d755c709215072727a24de593986b11a3
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
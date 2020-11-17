from rest_framework import serializers
from .models import User, Counsellor, Article, AgeMorbidityChart, StateDisorderChart, SuicidalRiskChart, HumanResourcesChart, ChatBots, MentalStates

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)
    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    
    # Tried to associate Users Article with the User Model
    #def __init__(self, instance=None, **kwargs):
    #    super().__init__(instance=instance, **kwargs)
    #article = ArticleSerializer(allow_null=True)
    
    # To update only certain attributes
    #def __init__(self, *args, **kwargs):
    #    kwargs['partial'] = True
    #    super(UserSerializer, self).__init__(*args, **kwargs)
    # profile_pic = Base64ImageField(
    #     max_length=None, use_url=True,
    # )
    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','password','name')

class CounsellorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsellor
        fields = '__all__'

class AgeMorbidityChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeMorbidityChart
        fields = '__all__'       

class StateDisorderChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateDisorderChart
        fields = '__all__'

class SuicidalRiskChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuicidalRiskChart
        fields = '__all__'

class HumanResourcesChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanResourcesChart
        fields = '__all__'

class ChatBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatBots
        fields = '__all__'

class MentalStatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentalStates
        fields = '__all__'
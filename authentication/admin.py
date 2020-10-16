from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Anonymous_User)
admin.site.register(Profile)
admin.site.register(Anonymous_Profile)
admin.site.register(Article)
admin.site.register(Counsellor)
admin.site.register(AgeMorbidityChart)
admin.site.register(StateDisorderChart)
admin.site.register(SuicidalRiskChart)
admin.site.register(HumanResourcesChart)
admin.site.register(ChatBots)
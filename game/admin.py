from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Questions)
admin.site.register(Result)
admin.site.register(ActivateQuiz)
admin.site.register(ActivateLeaderboard)
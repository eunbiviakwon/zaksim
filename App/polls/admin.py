from django.contrib import admin
from polls.models import Question, Choice, Image

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Image)

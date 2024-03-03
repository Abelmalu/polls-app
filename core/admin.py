from django.contrib import admin
from .models import *
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice 
    extra =3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic information',{'fields':['question_text']}),
          (
              'Date INformation', {'fields': [ 'pub_data'], 'classes':['collapse']}
          ),
    ]


    inlines = [ChoiceInline]







admin.site.register(Question,QuestionAdmin)
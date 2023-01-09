from django.contrib import admin
from django.forms import Textarea
from .models import *
# Register your models here.
admin.site.register(Questions)

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    fields =("id","answer_questions","questions","answer")
    # formfield_overrides = {
    #     models.TextField: {'widget': Textarea(
    #         attrs={'rows': 3,
    #                'cols': 50})},
    # }


class AnswerAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('id','answer_questions.user', 'created_at')
    # search_fields = ['user__username']
    search_help_text = 'search on here'
admin.site.register(DayAnswerQuestons,AnswerAdmin)
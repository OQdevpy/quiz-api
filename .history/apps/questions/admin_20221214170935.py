from django.contrib import admin
from .models import Questions,Answer
# Register your models here.
admin.site.register(Questions)
admin.site.register(Answer)

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    fields = ('author', 'message')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 3,
                   'cols': 50})},
    }


class AnswerAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('id', 'author', 'is_reply','created_at')
    search_fields = ['author__username']
    search_help_text = 'search on here'
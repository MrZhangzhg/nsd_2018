from django.contrib import admin
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    date_hierarchy = 'pub_date'
    list_filter = ('pub_date',)
    search_fields = ('question_text',)
    ordering = ('-pub_date',)

class ChoiceAdmin(admin.ModelAdmin):
    raw_id_fields = ('question',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

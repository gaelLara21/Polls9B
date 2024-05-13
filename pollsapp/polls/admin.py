from django.contrib import admin

from .models import Question, Choice

# Register your models here.
#admin.site.register(Question)
#admin.site.register(Choice)

class ChoiceInLine(admin.StackedInline):
    model = Choice

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]
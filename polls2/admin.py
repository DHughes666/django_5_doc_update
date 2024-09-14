from django.contrib import admin

from .models import Question, Choice

# Register your models here.
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # Method I
    # fields = ["pub_date", "question_text"]

    # Method II
    """
    This is for multiple form fields. The first element of each tuple in
    the fieldset is the title of the fieldset
    """
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)



from django.contrib import admin
from .models import *


# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ['question']
    fieldsets = [
        ('question', {'fields': ['question']}),
        ('date', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]


admin.site.register(Poll, PollAdmin)

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email', 'role', 'approved']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('approved', 'role')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('approved', 'role')}),
    )

# class QuizAdmin(UserAdmin):
#     add_form = AddQuizForm
#     form = QuizForm
#     model = Quiz
#     list_display = ['question','answer']
#     fieldsets = (None, {'fields': ('question','answer')})

admin.site.register(CustomUser, CustomUserAdmin)

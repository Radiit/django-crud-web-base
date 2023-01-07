from django.contrib import admin
from .models import TodoItem, TodoList, UserData
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm

admin.site.register(TodoList)
admin.site.register(TodoItem)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserData
    list_display = ["email", "username",]

admin.site.register(UserData, CustomUserAdmin)
# Register your models here.

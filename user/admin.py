from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import User
from rest_framework.authtoken.models import Token


admin.site.register(User)
# User = get_user_model()


# class CustomTokenAdmin(DefaultTokenAdmin):
#     def get_user(self, obj):
#         return obj.user
#     get_user.short_description = 'User'


# class TokenAdmin(admin.ModelAdmin):
#     search_fields = ('key', 'user__username', 'user__email')  # Add any other fields you want to search
#     list_display = ('key', 'get_user', 'created')
#     list_filter = ('created',)


# admin.site.register(Token, CustomTokenAdmin)

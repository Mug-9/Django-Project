from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Class)
admin.site.register(UsersOfB)
admin.site.register(VideosData)
admin.site.register(WebReply)
admin.site.register(WebComment)
admin.site.register(UserLikeReply)
admin.site.register(UserOperator)
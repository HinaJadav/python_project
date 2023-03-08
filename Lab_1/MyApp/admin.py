from django.contrib import admin
from MyApp.models import User
from MyApp.models import Administrator
from MyApp.models import Content
from MyApp.models import like_content
from MyApp.models import Image

# Register your models here.
admin.site.register(User)
admin.site.register(Administrator)
admin.site.register(Content)
admin.site.register(like_content)
admin.site.register(Image)

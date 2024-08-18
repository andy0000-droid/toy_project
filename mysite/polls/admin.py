from django.contrib import admin

from .models import Question, Choice

admin.site.register(Choice)
admin.site.register(Question)

#from .models import Post

#admin.site.register(Post)


# Register your models here.

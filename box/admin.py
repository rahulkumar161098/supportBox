from django.contrib import admin
from .models import Article
from django.contrib.admin.options import ModelAdmin
# Register your models here.
class articleAdmin(ModelAdmin):
    list_display=['title','date']
    search_fields=['title','body']
    list_filter=['date']
    # prepopulated_fields={'slug':('title'),}

admin.site.register(Article,articleAdmin)
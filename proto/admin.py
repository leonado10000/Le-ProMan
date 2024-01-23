from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Courses)
admin.site.register(models.Topics)
admin.site.register(models.CTtable)
admin.site.register(models.Prograss)
from django.contrib import admin
from.models import user

# Register your models here.
@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_dsplay=('id','name','email','password','mobile_no')
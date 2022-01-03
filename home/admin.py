from django.contrib import admin
from home.models import Contact


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('id','name','phone','email','desc')


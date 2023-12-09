from django.contrib import admin
from .models import PhoneNumber

@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('country', 'country_code', 'phone_number')
    list_filter = ('country', 'country_code', 'state')
    search_fields = ('country', 'country_code', 'phone_number')


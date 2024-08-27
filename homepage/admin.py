from django.contrib import admin
from django import forms
from .models import Listings, Contact, ListingImage


# Classes that create an inline tab to insert images in the listing admin panel.
class ListingImageInline(admin.TabularInline):
    model = ListingImage
    extra = 1

class ListingAdmin(admin.ModelAdmin):
    inlines = [ListingImageInline]

# Specify the fields to be displayed in the admin list view.
class ContactAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email", "phone", "message")

# Register your models here.
admin.site.register(Listings, ListingAdmin)
admin.site.register(Contact, ContactAdmin)

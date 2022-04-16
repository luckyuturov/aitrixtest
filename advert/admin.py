from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from .models import Category, Subcategory, Advert

class AdverAdminForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = '__all__'

class AdverAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'category', 'subcategory', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    list_display_links = ('title', 'content')


admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Advert, AdverAdmin)

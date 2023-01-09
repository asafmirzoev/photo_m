from django.contrib import admin

from .models import Image, Person


class PersonAdminInline(admin.TabularInline):

    model = Person
    readonly_fields = ('name',)
    can_delete = False


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id',)
    readonly_fields = ('image', 'location', 'description')
    inlines = [PersonAdminInline]

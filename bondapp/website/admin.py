from django.contrib import admin
from .models import Characters, Factions, Gallery
from django.utils.safestring import mark_safe


class GalleryInline(admin.TabularInline):
    """Creates inline image upload in admin panel for characters"""
    model = Gallery
    fk_name = 'character'
    extra = 1


@admin.register(Characters)
class CharactersAdmin(admin.ModelAdmin):
    """Creates panel for characters with automatic slugs"""
    list_display = ('first_name', 'last_name', 'race', 'char_class', 'get_photo')
    list_display_links = ('first_name', 'last_name')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    list_filter = ('first_name', 'last_name')
    inlines = (GalleryInline,)

    def get_photo(self, obj):
        """For thumbnails"""
        if obj.images:
            return mark_safe(f'<img src="{obj.images.all()[0].image.url}" width="75" height="75">')
        else:
            return '-'

    get_photo.short_description = 'Thumbnail'


@admin.register(Factions)
class FactionsAdmin(admin.ModelAdmin):
    """Creates panel for factions with automatic slugs"""
    list_display = ('faction_name', 'parent')
    list_display_links = ('faction_name', 'parent')
    prepopulated_fields = {'slug': ('faction_name',)}
    list_filter = ('faction_name', 'parent')


admin.site.register(Gallery)

from django.contrib import admin
from .models import Movies, Actor, Category, Review, IdentityNamber
# Register your models here.

class InlineReview(admin.StackedInline):
    model = Review



class MoviesAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name','actors__first_name','actors__id_name__number')
    list_display = ('name','watch_count','likes','production_date', 'my_custom_field')
    readonly_fields = ('my_custom_field',)
    inlines = [InlineReview]


    def my_custom_field(self, obj):
        if obj.likes and obj.watch_count:
            total = 100 * (obj.likes / obj.watch_count)
            return '{} %'.format(round(total))
        return '0'

    fieldsets = (
        ["main section",{"fields":["name", "description"]}],
        ["None", {"fields": ["likes", "watch_count","my_custom_field"]}],
        ["Media", {"fields": ["poster", "video"]}],
        ["Actors", {"fields": ["actors"]}],
    )

    my_custom_field.short_description ='watch/likes Rating'


admin.site.register(Movies, MoviesAdmin)
admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(IdentityNamber)

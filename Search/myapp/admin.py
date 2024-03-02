from django.contrib import admin
from .models import User
from .models import SearchData

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'dob', 'created_at', 'modified_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at', 'modified_at')

admin.site.register(User, UserAdmin)

class SearchDataAdmin(admin.ModelAdmin):
    list_display = ('paragraph', 'word', 'created_at')
    list_filter = ('created_at','word' )
    search_fields = ('paragraph', 'word')
    readonly_fields = ('created_at', )

admin.site.register(SearchData, SearchDataAdmin)
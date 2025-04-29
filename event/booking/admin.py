from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Event
from .models import Contact

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'name', 'mobile', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'name', 'mobile')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('name', 'email', 'mobile', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'email', 'mobile', 'address', 'password1', 'password2'),
        }),
    )

# Event Admin
class EventAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_event_type_display', 'date', 'time', 'catering', 'people_count', 'created_at')
    list_filter = ('event_type', 'catering', 'date')
    search_fields = ('user__username', 'user__name', 'special_requests')
    date_hierarchy = 'date'
    ordering = ('-date', '-time')
    raw_id_fields = ('user',)
    
    def get_event_type_display(self, obj):
        return obj.get_event_type_display()
    get_event_type_display.short_description = 'Event Type'

# Register your models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Event, EventAdmin)

admin.site.site_header = "Event Booking Administration"
admin.site.site_title = "Event Booking Admin Portal"
admin.site.index_title = "Welcome to Event Booking Admin"

# contact
admin.site.register(Contact)
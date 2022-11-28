from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'full_name','gender', 'created_by', 'created',)
    readonly_fields = ('created', )

    def full_name(self, obj):
        return obj.name + " " +obj.last_name
        
admin.site.register(Customer,CustomerAdmin)

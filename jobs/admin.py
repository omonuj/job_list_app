from django.contrib import admin

from jobs.models import JobPost, Location, Authors, Skills


class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'salary','date_time')
    list_filter = ('date_time', 'expiry', 'salary')
    search_fields = ('title', 'description')
    search_help_text = ('Write in your search and hit enter')
    # fieldsets = ('title', 'description', 'salary')
    # exclude = ('title', 'description')
    fieldsets = [
        ('Basic Information', {
            'fields': [
                'title', 'description'
            ],
        }),
        ('More Information', {
            'fields': [
                ('expiry', 'salary'), 'slug'
            ]
        })
    ]
# Register your models here.

admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Authors)
admin.site.register(Skills)


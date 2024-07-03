from django.contrib import admin
from .models import *
# Register your models here.

class BulletPointInline(admin.TabularInline):
    model = Bulletpoint
    extra = 1

class DescriptionAdmin(admin.ModelAdmin):
    inlines = [BulletPointInline]

class Requirementsinline(admin.TabularInline):
    model = Requirement
    extra = 1

class RequirementAdmin(admin.ModelAdmin):
    inlines = [Requirementsinline]

admin.site.register(Homepage,DescriptionAdmin)
admin.site.register(Bulletpoint)
admin.site.register(Raw_material)
admin.site.register(Production_capcity)
admin.site.register(Team_Member)
admin.site.register(Certificates)
admin.site.register(Career)
admin.site.register(Announcement,RequirementAdmin)
admin.site.register(Requirement)

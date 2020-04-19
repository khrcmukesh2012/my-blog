from django.contrib import admin
from .models import *
# Register your models here.
class CMS(admin.ModelAdmin):
    list_display = ['title', 'added','updated']
    search_fields = ('title',)
    def get_actions(self, request):
        #Disable delete
        actions = super(CMS, self).get_actions(request)
        
        return actions

    def has_delete_permission(self, request, obj=None):
        return True
admin.site.register(CMSPages,CMS)

class News(admin.ModelAdmin):
    list_display = ['title', 'added','updated']
    search_fields = ('title',)
    def get_actions(self, request):
        #Disable delete
        actions = super(News, self).get_actions(request)
        
        return actions

    def has_delete_permission(self, request, obj=None):
        return True
admin.site.register(NewsEvent,News)

class Contact(admin.ModelAdmin):
    list_display = ['name',"added", 'email','mobile',"comment","updated"]
    search_fields = ('name',)
    def get_actions(self, request):
        #Disable delete
        actions = super(Contact, self).get_actions(request)
        
        return actions

    def has_delete_permission(self, request, obj=None):
        return True
admin.site.register(ContactUs,Contact)

class VideoUpload(admin.ModelAdmin):
    list_display = ['name',"added","user","updated"]
    search_fields = ('name',)
    def get_actions(self, request):
        #Disable delete
        actions = super(VideoUpload, self).get_actions(request)
        
        return actions

    def has_delete_permission(self, request, obj=None):
        return True
admin.site.register(Video,VideoUpload)

class AddBlog(admin.ModelAdmin):
    list_display = ['title',"added","user","updated"]
    search_fields = ('name',)
    def get_actions(self, request):
        #Disable delete
        actions = super(AddBlog, self).get_actions(request)
        
        return actions

    def has_delete_permission(self, request, obj=None):
        return True
admin.site.register(Blog,AddBlog)
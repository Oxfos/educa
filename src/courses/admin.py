from django.contrib import admin
from .models import Subject, Course, Module, Content, Text


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug':('title',)}

class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug':('title',)}
    inlines = [ModuleInline]

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['module', 'item']

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
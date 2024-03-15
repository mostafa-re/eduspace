from django.contrib import admin

from .models import Category, Course, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson
    fields = ["title", "video_url", "duration"]
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at", "is_published"]
    search_fields = ["title", "slug", "short_description", "description"]
    list_filter = ["created_at", "updated_at"]
    fieldsets = [
        (
            None,
            {"fields": ["is_published", "title", "category", "short_description"]},
        ),
        (
            "Media",
            {"fields": ["thumbnail", "video_url"]},
        ),
        (
            "Information",
            {
                "fields": [
                    "level",
                    "requirements",
                    "language",
                    "price",
                    "outcome",
                    "description",
                ]
            },
        ),
    ]
    inlines = [LessonInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    search_fields = ["title", "slug"]
    fields = ["title"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)

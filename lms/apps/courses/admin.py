from django.contrib import admin
from apps.courses.models import Course, CourseOutcome

class CourseOutcomeInline(admin.TabularInline):
    model = CourseOutcome
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseOutcomeInline]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(CourseOutcome)

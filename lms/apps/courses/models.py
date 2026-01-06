from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    instructor = models.ForeignKey(User,on_delete=models.CASCADE,related_name="courses",limit_choices_to={'is_superuser':True})
    thumbnail = models.ImageField(upload_to="course_thumbnails/",blank=True,null=True)
    price = models.DecimalField(max_digits=8,decimal_places=2,default=0.00)

    level = models.CharField(
        max_length=20,
        choices=[
            ("beginner", "Beginner"),
            ("intermediate", "Intermediate"),
            ("advanced", "Advanced"),
        ]
    )

    duration = models.CharField(max_length=50)  # e.g. "6 weeks"
    is_published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

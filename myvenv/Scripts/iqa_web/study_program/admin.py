from django.contrib import admin


# Register your models here.

from .models import StudyProgram
from .models import Professor

admin.site.register(StudyProgram)
admin.site.register(Professor)
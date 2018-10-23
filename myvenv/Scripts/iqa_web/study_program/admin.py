from django.contrib import admin


# Register your models here.

from .models import StudyProgram
from .models import Professor
from .models import Committee

admin.site.register(StudyProgram)
admin.site.register(Professor)
admin.site.register(Committee)
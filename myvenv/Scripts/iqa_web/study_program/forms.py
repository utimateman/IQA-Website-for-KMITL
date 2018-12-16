from django import forms
from .models import StudyProgram

class StudyProgramForm(forms.ModelForm):
    class Meta:
        model = StudyProgram
        fields = [
            'name', 'program_status', 'degree_and_major', 'collaboration_with_other_institues',
            'pdf_docs', 'responsible_professors', 'past_assessment'
        ]
        
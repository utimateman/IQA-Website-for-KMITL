from django import forms
from .models import StudyProgram, Professor, AssessmentResult, Committee

class StudyProgramForm(forms.ModelForm):
    class Meta:
        model = StudyProgram
        fields = [
            'name', 'program_status', 'degree_and_major', 'collaboration_with_other_institues',
            'pdf_docs', 'responsible_professors', 'past_assessment'
        ]
        

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = [
            'academic_title', 'name_surname', 'date_of_birth', 'bsc', 'bsc_grad_institute', 'bsc_year',
            'msc', 'msc_grad_institute', 'msc_year', 'phd', 'phd_grad_institute', 'phd_year', 'phone',
            'email', 'university', 'additional_degree', 'responsible_program', 'committee_profile'
        ]


class AssessmentResultForm(forms.ModelForm):
    class Meta:
        model = AssessmentResult
        fields = [
            'committee_id', 'program_id', 'year', 'curriculum_status', 'curriculum_status_year', 'curriculum_standard',
            'pdf_docs', 'aun_id'
        ]
         

class CommitteeForm(forms.ModelForm):
    class Meta:
        model = Committee
        fields = [
            'year', 'assessment_level', 'profession', 'assessment_programs'
        ]


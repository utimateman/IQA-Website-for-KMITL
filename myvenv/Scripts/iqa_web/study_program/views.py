from django.shortcuts import render, get_object_or_404

from .models import StudyProgram

# Create your views here.

def all_programs(request):
    programs = StudyProgram.objects
    return render(request, 'study_program/all_program.html', {'programs': programs})

def program_detail(request, program_id):
    detail = get_object_or_404(StudyProgram, pk=program_id)

    faculties_list = {'1':'Science', '2':'Engineering', '3':'Medicine'}
  
    return render(request, 'study_program/program_detail.html', {'program_detail': detail, 'faculties': faculties_list})

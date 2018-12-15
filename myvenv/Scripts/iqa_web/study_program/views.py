from django.shortcuts import render, get_object_or_404
from .models import StudyProgram, Professor, AssessmentResult, Committee

import math


#### Create your views here ####
def main_menu(request):
    return render(request, 'main_page/main_menu_page.html')

def assessment_menu(request):
    return render(request, 'main_page/assessment_menu_page.html')

def all_programs(request, page_number = 1):
    
    from_item = (page_number * 10) - 10
    to_item = page_number * 10

    sp = StudyProgram.objects # get object
    programs = sp.all() # get all objects
    total_program = sp.count() # get length of object

    program_list = []


    # check searching program
    found = False
    faculty_search = request.GET.get('faculty_name')
    if(faculty_search != None):
        #print(faculty_search)
        for item in programs:
            #print(item.name)
            if(item.name == faculty_search):
                found = True
                program_list.append(item)
                #search_list = item


    if(found == True):
        prev_page = 1
        current_page = 1
        next_page = 1
        return render(request, 'study_program/all_program.html', {'programs': program_list, 'current_page': current_page, 'prev_page': prev_page, 'next_page':next_page})

    else:
        for item in programs:
            program_list.append(item)
        
        # get 10 items/ page
        program_list = program_list[from_item:to_item]

        # adjust page button
        prev_page = page_number - 1
        if(page_number - 1 < 1):
            prev_page = 1  

        current_page = page_number

        next_page = page_number + 1
        if(next_page > math.ceil(total_program/10)):
            next_page = current_page

        return render(request, 'study_program/all_program.html', {'programs': program_list, 'current_page': current_page, 'prev_page': prev_page, 'next_page':next_page})



def program_detail(request, program_id):
    detail = get_object_or_404(StudyProgram, pk=program_id)

    faculties_list = {'1':'Science', '2':'Engineering', '3':'Medicine'}

    professor_list = []
    for professor in detail.responsible_professors.all():
        professor_list.append(professor)

    assessment_list =[]
    for assessment in detail.past_assessment.all():
        assessment_list.append(assessment)

    return render(request, 'study_program/program_detail.html', {'program_detail': detail, 'faculties': faculties_list, 'professors':professor_list, 'assessment_list':assessment_list, 'pk': program_id})


def professor_detail(request, professor_id):
    profile = get_object_or_404(Professor, pk=professor_id)

    responsible_program = []
    for program in profile.responsible_program.all():
        responsible_program.append(program)

    committee_list = []
    for comittee_per_year in profile.committee_profile.all():
        committee_list.append(comittee_per_year)

   

    return render(request, 'professor/professor_profile.html', {'professor_profile': profile, 'responsible_program':responsible_program, 'committee_list':committee_list})



def all_assessments(request, page_number=1):
        
    from_item = (page_number * 10) - 10
    to_item = page_number * 10

    ar = AssessmentResult.objects # get object
    assessments = ar.all() # get all objects
    total_assessment = ar.count() # get length of object

    assessment_list = []

    for assessment in assessments:
        assessment_list.append(assessment)
    
    # get 10 items/ page
    assessment_list = assessment_list[from_item:to_item]

    # adjust page button
    prev_page = page_number - 1
    if(page_number - 1 < 1):
        prev_page = 1  

    current_page = page_number

    next_page = page_number + 1
    if(next_page > math.ceil(total_assessment/10)):
        next_page = current_page

   
    return render(request, 'assessment/all_assessment.html', {'assessments': assessment_list, 'current_page': current_page, 'prev_page': prev_page, 'next_page':next_page})

def assessment_result(request, assessment_id):
    detail = get_object_or_404(AssessmentResult, pk=assessment_id)

    commitee_list = []
    for committee in detail.committee_id.all():
        commitee_list.append(committee)

    #assessment_result.aun_id

    return render(request, 'assessment/assessment_result.html', {'assessment_result': detail, 'commitee_list':commitee_list})

def all_committees(request, page_number=1):
        
    from_item = (page_number * 10) - 10
    to_item = page_number * 10

    c = Committee.objects # get object
    committees = c.all() # get all objects
    total_committee = c.count() # get length of object

    committee_list = []

    for committee in committees:
        committee_list.append(committee)
    
    # get 10 items/ page
    committee_list = committee_list[from_item:to_item]

    # adjust page button
    prev_page = page_number - 1
    if(page_number - 1 < 1):
        prev_page = 1  

    current_page = page_number

    next_page = page_number + 1
    if(next_page > math.ceil(total_committee/10)):
        next_page = current_page

   
    return render(request, 'committee/all_committee.html', {'committee_list': committee_list, 'current_page': current_page, 'prev_page': prev_page, 'next_page':next_page})
  

def committee_profile(request, committee_id):
    detail = get_object_or_404(Committee, pk=committee_id)

    assessment_list = []
    for assessment in detail.assessment_programs.all():
        assessment_list.append(assessment)
    
    id_kub = detail.professor_id.id
    print(id_kub)
    return render(request, 'committee/committee_detail.html', {'committee_detail': detail, 'professor_profile':id_kub, 'assessment_list': assessment_list})


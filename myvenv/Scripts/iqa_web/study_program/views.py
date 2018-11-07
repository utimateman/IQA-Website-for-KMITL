from django.shortcuts import render, get_object_or_404

from .models import StudyProgram, Professor

import math


#### Create your views here ####

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
    return render(request, 'study_program/program_detail.html', {'program_detail': detail, 'faculties': faculties_list, 'professors':professor_list})


def professor_detail(request, professor_id):
    profile = get_object_or_404(Professor, pk=professor_id)


    return render(request, 'professors/professor_profile.html', {'professor_profile': profile})
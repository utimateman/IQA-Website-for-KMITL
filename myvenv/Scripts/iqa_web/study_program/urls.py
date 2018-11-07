from django.urls import path, include

from . import views




urlpatterns = [
    path('study_program/', views.all_programs, name = 'all_program'),
    path('study_program/<int:page_number>/', views.all_programs, name = 'all_program'),
    path('<int:program_id>/', views.program_detail, name='program_detail'),
    
    path('professors/<int:professor_id>/', views.professor_detail, name='professor_profile')
]



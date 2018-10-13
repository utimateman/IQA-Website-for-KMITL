from django.db import models

# Create your models here.

class StudyProgram(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    status_choices = (
        ('ACTIVE', 'ACTIVE'),
        ('GOING TO CLOSE', 'GOING TO CLOSE'),
        ('NOT ACTIVE', 'NOT ACTIVE'),
    )
    program_status = models.CharField(max_length=200, choices=status_choices )


    degree_and_major = models.CharField(max_length=400)


    collaboration_choices = (
        ('Program issued specifically by KMITL', 'Program issued specifically by KMITL'),
        ('Program supported by other institutes', 'Program supported by other institutes'),
        ('Collaborated program with other institutes', 'Collaborated program with other institutes'),
    )
    collaboration_with_other_institues = models.TextField(max_length=400, choices = collaboration_choices)
    pdf_docs = models.FileField(upload_to='study_program_details/')

    def __str__(self):
        return self.name
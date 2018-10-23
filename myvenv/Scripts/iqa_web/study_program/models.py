from django.db import models
import datetime
# Create your models here.

# Handling many to many relationship
# https://stackoverflow.com/questions/4881578/django-bi-directional-manytomany-how-to-prevent-table-creation-on-second-model

class Professor(models.Model):
    professor_id = models.CharField(max_length = 200)
    academic_title = models.CharField(max_length = 200)
    name_surname = models.CharField(max_length = 200)
    date_of_birth = models.DateField()

    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    bsc = models.CharField(max_length = 200)
    bsc_grad_institute = models.CharField(max_length = 200)
    bsc_year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    #https://groups.google.com/forum/#!msg/django-users/al95x1TXFV4/7mCCWQE3jtAJ
    
    msc = models.CharField(max_length = 200)
    msc_grad_institute = models.CharField(max_length = 200)
    msc_year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    phd = models.CharField(max_length = 200)
    phd_grad_institute = models.CharField(max_length = 200)
    phd_year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    
    phone = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    university = models.CharField(max_length = 200)
    additional_degree = models.CharField(max_length = 200, blank = True)

    responsible_program = models.ManyToManyField('StudyProgram', blank=True)
    assessment_committee = models.CharField('Committee', max_length=200,blank=True)
    def __str__(self):
        return self.name_surname


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

    responsible_professors = models.ManyToManyField(Professor, through=Professor.responsible_program.through, blank=True)

    def __str__(self):
        return self.name



class Committee(models.Model):
    code = models.CharField(max_length=200)
    professor_id = models.ForeignKey(Professor, on_delete=models.PROTECT, null=True)

    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    assessment_level_choices = (
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Novice', 'Novice'),
        ('Apprentice-C','Apprentice-C')
    )
    assessment_level = models.TextField(max_length=400, choices = assessment_level_choices)
    profession = models.CharField(max_length=200)
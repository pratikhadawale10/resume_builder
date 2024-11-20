from django.db import models

class ResumeExperience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    responsibilities = models.TextField()

    class Meta:
        db_table = 'resume_experience'

class ResumeEducation(models.Model):
    degree = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        db_table = 'resume_education'


class ResumeDetail(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    summary = models.TextField()
    skills = models.TextField()
    experiences = models.ManyToManyField(ResumeExperience)
    educations = models.ManyToManyField(ResumeEducation)

    class Meta:
        db_table = 'resume_details'

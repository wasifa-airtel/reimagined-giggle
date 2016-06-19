from django.db import models
from django.core.urlresolvers import reverse
from .district_model import District
from .division_model import  Division

class Gender(models.Model):
    name = models.CharField(max_length=200,unique=True)
    gender_code=models.CharField(max_length=200,unique=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
     return reverse('gender_edit', kwargs={'pk': self.pk})

class Country(models.Model):
    name=models.CharField(max_length=200,unique=True)
    country_code=models.CharField(max_length=200,unique=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
     return reverse('country_edit', kwargs={'pk': self.pk})

class Thana(models.Model):
    name=models.CharField(max_length=200,unique=True)
    thana_code=models.CharField(max_length=200,unique=True)
    division_id=models.ForeignKey(Division)
    district_id=models.ForeignKey(District)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
     return reverse('thana_edit', kwargs={'pk': self.pk})


class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200,default='',blank=True)
    last_name=models.CharField(max_length=200)
    division_id=models.ForeignKey(Division)
    district_id=models.ForeignKey(District)
    country_id = models.ForeignKey(Country)
    thana_id=models.ForeignKey(Thana)
    zip_code=models.CharField(max_length=200)
    Street = models.CharField(max_length=200)
    mobile_number=models.CharField(max_length=200)
    email=models.EmailField(max_length=70,unique=True)
    Date_of_birth=models.DateField()
    NID=models.CharField(max_length=200,unique=True)
    Profession=models.CharField(max_length=200)
    gender_id=models.ForeignKey(Gender)
    user_name=models.CharField(max_length=200,unique=True)
    password=models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
     return reverse('patient_edit', kwargs={'pk': self.pk})





class DegreeHealth(models.Model):
    name = models.CharField(max_length=200,unique=True)
    degreeHealth_code = models.CharField(max_length=200,unique=True)


    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
     return reverse('degreeHeath_edit', kwargs={'pk': self.pk})


class Year(models.Model):
    name = models.CharField(max_length=200,unique=True)
    year_code = models.CharField(max_length=200,unique=True)


    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
     return reverse('year_edit', kwargs={'pk': self.pk})




class Month (models.Model):
    month_name = models.CharField(max_length=200,unique=True)
    month_code = models.CharField(max_length=200,unique=True)
    month_shortname = models.CharField(max_length=200,unique=True)


    def __unicode__(self):
        return self.month_name

    def get_absolute_url(self):
     return reverse('month_edit', kwargs={'pk': self.pk})


class Day (models.Model):
    day_name = models.CharField(max_length=200,unique=True)


    def __unicode__(self):
        return self.day_name

    def get_absolute_url(self):
     return reverse('day_edit', kwargs={'pk': self.pk})


class DegreeGeneral (models.Model):
    name = models.CharField(max_length=200,unique=True)
    degreeGeneral_code =  models.CharField(max_length=200,unique=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
     return reverse('degreeGeneral_edit', kwargs={'pk': self.pk})




class EduBoard (models.Model):
    edu_name = models.CharField(max_length=200,unique=True)
    edu_code =  models.CharField(max_length=200,unique=True)

    def __unicode__(self):
        return self.edu_name

    def get_absolute_url(self):
     return reverse('eduboard_edit', kwargs={'pk': self.pk})




class ResultDivision(models.Model):
    res_name = models.CharField(max_length=200,unique=True)
    res_code =  models.CharField(max_length=200,unique=True)

    def __unicode__(self):
        return self.res_name

    def get_absolute_url(self):
     return reverse('resultdivision', kwargs={'pk': self.pk})

class Physician(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200,default='',blank=True)
    last_name=models.CharField(max_length=200)
    division_id=models.ForeignKey(Division)
    district_id=models.ForeignKey(District)
    country_id = models.ForeignKey(Country)
    thana_id=models.ForeignKey(Thana)
    zip_code=models.CharField(max_length=200)
    Street = models.CharField(max_length=200)
    mobile_number=models.CharField(max_length=200)
    email=models.EmailField(max_length=70,unique=True)
    Date_of_birth=models.DateField()
    NID=models.CharField(max_length=200,unique=True)
    Profession=models.CharField(max_length=200)
    gender_id=models.ForeignKey(Gender)
    user_name=models.CharField(max_length=200,unique=True)
    password=models.CharField(max_length=200)

    def __unicode__(self):
        return self.first_name

    def get_absolute_url(self):
        return ('physician', [self.pk])


class PhysicianEduHealthMapping(models.Model):
    physician_id = models.ForeignKey(Physician)
    degree_edu_health_id=models.ForeignKey(DegreeHealth)
    country_id=models.ForeignKey(Country)
    institute=models.CharField(max_length=200)
    year_id = models.ForeignKey(Year)
    ref_no = models.CharField(max_length=200)


    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return ('phycisian', [self.pk])


class PhysicianTraining (models.Model):
    physician_id = models.ForeignKey(Physician)
    training_course=models.CharField(max_length=200)
    country_id=models.ForeignKey(Country)
    institute=models.CharField(max_length=200)
    year_id = models.ForeignKey(Year)
    ref_no = models.CharField(max_length=200)


    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return ('phycisian', [self.pk])


class PhysicianEduQualification (models.Model):
    physician_id = models.ForeignKey(Physician)
    degree  = models.ForeignKey(DegreeGeneral)
    country_id=models.ForeignKey(Country)
    Education_Board  = models.ForeignKey(EduBoard )
    institute=models.CharField(max_length=200)
    year_id = models.ForeignKey(Year)
    Result_Division  = models.ForeignKey(ResultDivision)
    Result_CGPA=models.CharField(max_length=200)
    CGPA_Scale=models.CharField(max_length=200)
    Ref_no=models.CharField(max_length=200)

    def __unicode__(self):
      return self.title

    def get_absolute_url(self):
        return ('phycisian', [self.pk])



class PhysicianProfessional (models.Model):
    physician_id = models.ForeignKey(Physician)
    Role=models.CharField(max_length=200)
    Organization=models.CharField(max_length=200)
    country_id=models.ForeignKey(Country)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)
    Ref_no=models.CharField(max_length=200)

    def __unicode__(self):
      return self.title

    def get_absolute_url(self):
        return ('phycisian', [self.pk])
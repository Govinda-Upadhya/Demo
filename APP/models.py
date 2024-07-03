from django.db import models

# Create your models here.

class Homepage(models.Model):
    hero_title = models.CharField(max_length=200)
    hero_image = models.ImageField(upload_to='image/')
    home_image = models.ImageField(upload_to='image/')
    statistic_estalblished = models.CharField(max_length=200)
    statistic_happy_client = models.CharField(max_length=200)
    statistic_production = models.CharField(max_length=200)
    def __str__ (self):
        return self.hero_title

class Bulletpoint(models.Model):
    homepage = models.ForeignKey(Homepage,related_name='bullet_points',on_delete= models.CASCADE)
    point = models.CharField(max_length=200)
    
    def __str__ (self):
        return f'Bullet point for {self.homepage.hero_title}'

class Raw_material(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')

    def __str__ (self):
        return self.name

class Production_capcity(models.Model):
    hour = models.CharField(max_length=200)
    day = models.CharField(max_length=200)
    year = models.CharField(max_length=200)

    def __str__ (self):
        return f"Production Capacity" 

class Team_Member(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    phone = models.IntegerField(max_length=200,blank=True,null=True)
    image = models.ImageField(upload_to='image/')
    facebook = models.URLField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=300,blank=True,null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)

    def __str__ (self):
        return self.name

class Certificates(models.Model):
    image = models.ImageField(upload_to='image/')
    def __str__ (self):
        return  f"Certificates"

class Career(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')

    def __str__ (self):
        return self.title

class Announcement(models.Model):
    announcement = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    hiring_process = models.TextField()
    descriptions = models.TextField(blank=True,null=True)
    def __str__ (self):
        return self.announcement

class Requirement(models.Model):
    announcement = models.ForeignKey(Announcement,related_name='requirement',on_delete= models.CASCADE)
    requirement = models.CharField(max_length=200)

    def __str__ (self):
        return f'requirement for {self.announcement.announcement}'

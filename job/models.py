from django.db import models
from user.models import Company
from slugify import slugify

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    jobdesc = models.TextField()
    jobtype = models.CharField(max_length=255)
    statdate = models.DateField()
    applyby = models.DateField()
    salary = models.IntegerField()
    aboutjob = models.TextField()
    skills = models.CharField(max_length=255)
    slug = models.CharField(max_length=1000, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title + " - " + self.company.company_name

    def save(self, *args, **kwargs):
        slug = self.jobtype + " " + self.title + " at " + self.company.company_name
        slug = slugify(slug)
        self.slug = slug
        super(Job, self).save(*args, **kwargs)

# Create your models here.

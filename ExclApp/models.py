from django.db import models

class project(models.Model):
    BUILDER_CHOICES = [
        ('Shoba', 'Shoba'),
        # Add other builders if necessary
    ]

    PROJECT_TYPE_CHOICES = [
        ('Villas', 'Villas'),
        ('Apartment', 'Apartment'),
        ('Plots', 'Plots'),
        ('Villaments', 'Villaments'),
        ('Row Houses', 'Row Houses'),
        # Add other project types if necessary
    ]

    PROJECT_STATUS_CHOICES = [
        ('Delivered', 'Delivered'),
        ('OnGoing', 'OnGoing'),
        # Add other project statuses if necessary
    ]

    builder = models.CharField(max_length=100, choices=BUILDER_CHOICES)
    project_name = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100, choices=PROJECT_TYPE_CHOICES)
    project_status = models.CharField(max_length=100, choices=PROJECT_STATUS_CHOICES)
    configuration = models.CharField(max_length=100, blank=True, null=True)
    size = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    geo_imp = models.CharField(max_length=100, blank=True, null=True)
    theme = models.CharField(max_length=100, blank=True, null=True)
    web = models.URLField(blank=True, null=True)
    google_map = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.project_name

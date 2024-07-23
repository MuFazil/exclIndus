# from django.db import models

# class project(models.Model):
#     BUILDER_CHOICES = [
#         ('Shoba', 'Shoba'),
#         # Add other builders if necessary
#     ]

#     PROJECT_TYPE_CHOICES = [
#         ('Villas', 'Villas'),
#         ('Apartment', 'Apartment'),
#         ('Plots', 'Plots'),
#         ('Villaments', 'Villaments'),
#         ('Row Houses', 'Row Houses'),
#         # Add other project types if necessary
#     ]

#     PROJECT_STATUS_CHOICES = [
#         ('Delivered', 'Delivered'),
#         ('OnGoing', 'OnGoing'),
#         # Add other project statuses if necessary
#     ]

#     builder = models.CharField(max_length=100, choices=BUILDER_CHOICES)
#     project_name = models.CharField(max_length=100)
#     project_type = models.CharField(max_length=100, choices=PROJECT_TYPE_CHOICES)
#     project_status = models.CharField(max_length=100, choices=PROJECT_STATUS_CHOICES)
#     configuration = models.CharField(max_length=100, blank=True, null=True)
#     size = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     geo_imp = models.CharField(max_length=100, blank=True, null=True)
#     theme = models.CharField(max_length=100, blank=True, null=True)
#     web = models.URLField(blank=True, null=True)
#     google_map = models.URLField(blank=True, null=True)

#     def __str__(self):
#         return self.project_name


from django.db import models

class project(models.Model):
    builder = models.CharField(max_length=100,  default=00)
    project_name = models.CharField(max_length=100,  default=00)
    project_type = models.CharField(max_length=100,  default=00)
    project_size_acre = models.DecimalField(max_digits=5, decimal_places=2,  default=00)
    project_status = models.CharField(max_length=100,  default=00)
    possession_date = models.CharField(max_length=100, blank=True, null=True)
    unit_configuration_bhk = models.CharField(max_length=10,  default=00)
    unit_size = models.CharField( max_length=100, default=00)
    total_inventory = models.CharField( max_length=100, default=00)
    web = models.URLField(max_length=200,  default=00)
    address = models.CharField(max_length=255,  default=00)
    pin = models.CharField(max_length=6, default=00)
    google_map = models.CharField(max_length=255,  default=00)
    geo_imp = models.CharField(max_length=100,  default=00)

    def __str__(self):
        return f"{self.builder} - {self.project_name}"

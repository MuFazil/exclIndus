# In your app's management/commands directory, create a new Python file, e.g., seed_projects.py
from django.core.management.base import BaseCommand
from ExclApp.models import project

class Command(BaseCommand):
    help = 'Seed projects data'

    def handle(self, *args, **kwargs):
        # In your custom management command
        projects_data = [
    {'builder': 'Shoba', 'project_name': 'Azalea', 'project_type': 'Villas', 'project_status': 'Delivered', 'configuration': 3, 'size': 2600, 'geo_imp': 'East', 'theme': 'Residential', 'web': 'https://www.sobha.com/projects/sobha-azalea/', 'google_map': 'https://maps.app.goo.gl/foWno4snLWjnqNHn9'},
    {'builder': 'Shoba', 'project_name': 'Azalea', 'project_type': 'Villas', 'project_status': 'Delivered', 'configuration': 4, 'size': 3000, 'geo_imp': 'East', 'theme': 'Residential', 'web': 'https://www.sobha.com/projects/sobha-azalea/', 'google_map': 'https://maps.app.goo.gl/foWno4snLWjnqNHn9'},
    {'builder': 'Shoba', 'project_name': 'Dahlia', 'project_type': 'Apartment', 'project_status': 'Delivered', 'configuration': 3, 'size': 1662, 'geo_imp': 'East', 'theme': 'Residential', 'web': 'http', 'google_map': 'https://maps.app.goo.gl/5bqHyeKHaGGrtm2f7'},
    {'builder': 'Shoba', 'project_name': 'Rose', 'project_type': 'Apartment', 'project_status': 'Delivered', 'configuration': 3, 'size': 1595, 'geo_imp': 'East', 'theme': 'Residential', 'web': 'https://www.sobha.com/projects/sobha-rose/', 'google_map': 'https://maps.app.goo.gl/arAH7Ga2EFd1Tzwf7'},
    {'builder': 'Shoba', 'project_name': 'Rose', 'project_type': 'Apartment', 'project_status': 'Delivered', 'configuration': 4, 'size': 1720, 'geo_imp': 'East', 'theme': 'Residential', 'web': 'https://www.sobha.com/projects/sobha-rose/', 'google_map': 'https://maps.app.goo.gl/arAH7Ga2EFd1Tzwf7'},
    {'builder': 'Shoba', 'project_name': 'Iris', 'project_type': 'Apartment', 'project_status': 'Delivered', 'configuration': 3, 'size': 1586, 'geo_imp': 'East', 'theme': 'Residential', 'web': 'https://www.sobha.com/projects/sobha-iris/', 'google_map': 'https://maps.app.goo.gl/GittvnqZeutsWRqX6'},
    {'builder': 'Shoba', 'project_name': 'Avenue Apartments', 'project_type': 'Apartment', 'project_status': 'Delivered', 'configuration': 3, 'size': 1536, 'geo_imp': 'East', 'theme': 'Residential', 'web': 'https://www.sobha.com/bengaluru/sobha-avenue/', 'google_map': 'https://maps.app.goo.gl/6ioVm43nrhMV8J5J7'},
    {'builder': 'Shoba', 'project_name': 'Palladian', 'project_type': 'Apartment', 'project_status': 'Delivered', 'configuration': 3, 'size': 45, 'geo_imp': 'East', 'theme': 'Residential', 'web': 'http', 'google_map': 'http'},
    {'builder': 'Shoba', 'project_name': 'A', 'project_type': 'Plots', 'project_status': 'OnGoing', 'configuration': 1, 'size': 3, 'geo_imp': 'North', 'theme': 'Residential', 'web': 'https://www.sobha.com/projects/sobha-iris/', 'google_map': 'http'},
    {'builder': 'Shoba', 'project_name': 'B', 'project_type': 'Apartment', 'project_status': 'OnGoing', 'configuration': 1, 'size': 2, 'geo_imp': 'North', 'theme': 'Residential', 'web': 'https://www.sobha.com/bengaluru/sobha-avenue/', 'google_map': 'http'},
    {'builder': 'Shoba', 'project_name': 'A', 'project_type': 'Row Houses', 'project_status': 'OnGoing', 'configuration': 2, 'size': 1, 'geo_imp': 'North', 'theme': 'Residential', 'web': 'https://www.sobha.com/projects/sobha-iris/', 'google_map': 'http'},
    {'builder': 'Shoba', 'project_name': 'B', 'project_type': 'Plots', 'project_status': 'OnGoing', 'configuration': 2, 'size': 3, 'geo_imp': 'North', 'theme': 'Residential', 'web': 'https://www.sobha.com/bengaluru/sobha-avenue/', 'google_map': 'http'},
    {'builder': 'Shoba', 'project_name': 'A', 'project_type': 'Apartment', 'project_status': 'OnGoing', 'configuration': 3, 'size': 4, 'geo_imp': 'West', 'theme': 'Residential', 'web': 'https://www.sobha.com/projects/sobha-iris/', 'google_map': 'http'},
    {'builder': 'Shoba', 'project_name': 'B', 'project_type': 'Row Houses', 'project_status': 'OnGoing', 'configuration': 4, 'size': 2, 'geo_imp': 'West', 'theme': 'Residential', 'web': 'https://www.sobha.com/projects/sobha-iris/', 'google_map': 'http'},
    {'builder': 'Shoba', 'project_name': 'A', 'project_type': 'Plots', 'project_status': 'OnGoing', 'configuration': 1, 'size': 3, 'geo_imp': 'West', 'theme': 'Residential', 'web': 'https://www.sobha.com/bengaluru/sobha-avenue/', 'google_map': 'http'},
    {'builder': 'Shoba', 'project_name': 'B', 'project_type': 'Apartment', 'project_status': 'OnGoing', 'configuration': 1, 'size': 1, 'geo_imp': 'West', 'theme': 'Residential', 'web': 'https://www.sobha.com/projects/sobha-iris/', 'google_map': 'http'},
    {'builder': 'Shoba', 'project_name': 'A', 'project_type': 'Row Houses', 'project_status': 'OnGoing', 'configuration': 2, 'size': 645, 'geo_imp': 'South', 'theme': 'Residential', 'web': 'https://www.sobha.com/bengaluru/sobha-avenue/', 'google_map': 'http'},
    {'builder': 'Shoba', 'project_name': 'B', 'project_type': 'Plots', 'project_status': 'OnGoing', 'configuration': 2, 'size': 1564, 'geo_imp': 'South', 'theme': 'Residential', 'web': 'https://www.sobha.com/projects/sobha-iris/', 'google_map': 'http'},
    {'builder': 'Shoba', 'project_name': 'A', 'project_type': 'Apartment', 'project_status': 'OnGoing', 'configuration': 3, 'size': 45, 'geo_imp': 'South', 'theme': 'Residential', 'web': 'https://www.sobha.com/bengaluru/sobha-avenue/', 'google_map': 'http'},
    {'builder': 'Shoba', 'project_name': 'B', 'project_type': 'Row Houses', 'project_status': 'OnGoing', 'configuration': 4, 'size': 45, 'geo_imp': 'Central', 'theme': 'Residential', 'web': 'https://www.sobha.com/projects/sobha-iris/', 'google_map': 'http'},
    {'builder': 'Shoba', 'project_name': 'A', 'project_type': 'Plots', 'project_status': 'OnGoing', 'configuration': 1, 'size': 45, 'geo_imp': 'Central', 'theme': 'Residential', 'web': 'https://www.sobha.com/projects/sobha-iris/', 'google_map': 'http'},
    {'builder': 'Shoba', 'project_name': 'B', 'project_type': 'Apartment', 'project_status': 'OnGoing', 'configuration': 1, 'size': 45, 'geo_imp': 'Central', 'theme': 'Residential', 'web': 'https://www.sobha.com/bengaluru/sobha-avenue/', 'google_map': 'http'},
]


        for project_data in projects_data:
            project.objects.create(**project_data)

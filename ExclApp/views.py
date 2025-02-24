from django.shortcuts import render
from django.db.models import Q
from .models import project

def apartments_view(request):
    # Retrieve all projects initially
    projects = project.objects.all()

    # Check if any filters are applied
    if request.GET:
        # Initialize an empty Q object to build the query
        query = Q()

        search_query = request.GET.get('search')
        if search_query:
            query &= Q(builder__icontains=search_query) | Q(project_name__icontains=search_query)

        # Check if project type filters are applied
        selected_project_types = request.GET.getlist('project_type')
        if selected_project_types:
            # Add project type filtering to the query
            query &= Q(project_type__in=selected_project_types)

        # Check if project status filters are applied
        selected_statuses = request.GET.getlist('builder')
        if selected_statuses:
            # Add project status filtering to the query
            query &= Q(builder__in=selected_statuses)
            print(selected_statuses)

        # Check if configuration filters are applied
        selected_configurations = request.GET.getlist('unit_configuration_bhk')
        if selected_configurations:
            # Add configuration filtering to the query
            query &= Q(unit_configuration_bhk__in=selected_configurations)

        # Check if geographical importance filters are applied
        selected_geoimps = request.GET.getlist('geo_imp')
        if selected_geoimps:
            # Add geographical importance filtering to the query
            query &= Q(geo_imp__in=selected_geoimps)

        # Apply the combined query to filter projects
        projects = projects.filter(query).distinct()
        

    # Count the number of filtered projects
    project_count = projects.count()
    
    
    # Render the template with the filtered projects and project count
    return render(request, 'apartments.html', {'projects': projects, 'project_count': project_count})

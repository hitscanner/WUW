from django.contrib import admin
from .models import Movie
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class MovieResource(resources.ModelResource):
    class Meta:
        model = Movie

class MovieAdmin(ImportExportModelAdmin):
    resource_class = MovieResource

admin.site.register(Movie, MovieAdmin)

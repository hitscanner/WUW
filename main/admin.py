from django.contrib import admin
from models import Search_result

# ... export functions will go here ...

class Search_resultAdmin(admin.ModelAdmin):
    actions = [export_csv, export_xls, export_xlsx]

admin.site.register(Search_result, Search_resultAdmin)
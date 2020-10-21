# django_genie
Based on [django-code-generator]

A customizable python package for generating django and DRF(django rest framework) code.
Useful for generating CRUD(Create, Read, Update, Delete) code from models when there are a large number of models in a app.

Installation
    
    $ pip install django_genie

Or add the package to requirements.txt which installs it to a docker container.

Add 'django_genie' to INSTALLED_APPS = [...] in settings.py in your django app

Command usage:

    $ python manage.py code_generator <app_name> <template_name>

For example: for generating admin.py code for core app in terminal

    $ python manage.py code_generator core admin
    from django.contrib import admin
    from reversion.admin import VersionAdmin
    
    from YOUR_PROJECT_NAME.core.models.core import User
    
   
    @admin.register(User)
    class UserAdmin(VersionAdmin):
        """Admin class for User"""
    
        exclude = ('created_by', 'updated_by', 'deleted_at')
        list_display = ('password', 'last_login', 'is_superuser', 'email', 'name', 'is_active', 'is_staff',)
        list_filter = ('updated_at',)
        ordering = ()      # Add your required fields here
        search_fields = () # Add your required fields here
    
        def save_model(self, request, obj, form, change):
            if not obj.pk:
                obj.created_by = request.user.id
            obj.updated_by = request.user.id
            super().save_model(request, obj, form, change)

A proper formatted code is printed out at terminal which can be simply copy pasted.

References:

[1] [django-code-generator]: https://github.com/Nekmo/django-code-generator
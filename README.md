# django-code-generator
Based on django-code-generator https://github.com/Nekmo/django-code-generator

A python module which generate the django code. Useful for generating django-rest-framework code. Prints out the code in console for simple copy paste where its required. It uses templates for code generation which can be customized.

Command usage:

$ docker-compose -f local.yml run --rm django python manage.py code_generator <app_name> <template_name>

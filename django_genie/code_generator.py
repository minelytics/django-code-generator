import os
from django.template import Context, Engine

from .models import Models


class CodeGenerator:
    """
    A class for code generation

    ...

    Attributes
    ----------
    app : first parameter of command at terminal
    template : second parameter of command at terminal

    Methods
    -------
    output(): prints generated code at the terminal
    """

    def __init__(self, app, template):
        """
        declares app and template parameters as self variables

        :param app: name of app in the project for which the generated code is required
        :param template: the type of template for which code is to be generated - admin, views, urls etc.
        """

        self.app = app
        self.template = template

    def output(self):
        """
        prints generated code at the terminal

        :return: generated code
        """

        engine = Engine(
            debug=True,
            dirs=[os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")],
            libraries={
                'code_generator_tags': "django_genie.templatetags.code_generator_tags"
            }
        )

        template = engine.get_template(self.template + ".py")
        print(template.render(Context({'models': Models(self.app).models, 'app': self.app})))

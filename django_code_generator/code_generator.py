import os
from django.template import Context, Engine

from config.settings.base import APPS_DIR
from .models import Models

CRUD_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
project = str(APPS_DIR).split("/")[-1]


class CodeGenerator:
    def __init__(self, app, template):
        self.app = app
        self.template = template

    def output(self):
        engine = Engine(
            debug=True,
            dirs=[os.path.join(CRUD_BASE_DIR, "templates")],
            libraries={
                'crud_generator_tags': project + ".generator.workflow.crud_generator.templatetags.crud_generator_tags"
            }
        )

        template = engine.get_template(self.template + ".py")
        print(template.render(Context({'models': Models(self.app).models, 'app': self.app})))

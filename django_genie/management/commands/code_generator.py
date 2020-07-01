from django.core.management.base import BaseCommand
from django_genie.code_generator import CodeGenerator


class Command(BaseCommand):
    """
    A class for running code_generator command

    ...

    Attributes
    ----------
    None

    Methods
    -------
    add_arguments(parser): inbuilt django method
    handle(*args, **options): inbuilt django method
    """

    help = 'Code Generator'

    def add_arguments(self, parser):
        """
        inbuilt django method
        adds custom arguments received from terminal

        :param parser:
        :type parser:
        :return:
        :rtype:
        """

        parser.add_argument('app', type=str)
        parser.add_argument('template', type=str)

    def handle(self, *args, **options):
        """
        inbuilt django method
        calls CodeGenerator class and passes arguments as parameters

        :param args:
        :type args:
        :param options:
        :type options:
        :return:
        :rtype:
        """

        CodeGenerator(options['app'], options['template']).output()

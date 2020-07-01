from django.apps import apps
from django.utils.text import camel_case_to_spaces


def get_field_names(fields):
    """
    returns a string of field names

    :param fields: fields of a model
    :return: string of comma separated quoted field names
    """

    return ", ".join(["'{}'".format(x.name) for x in fields])


class Model:
    """
    A class for receiving a model

    ...

    Attributes
    ----------
    model : a model

    Methods
    -------
    name(): returns the name of the model
    field_names(): returns a string of all forward field names on the model and its parents, excluding ManyToManyFields
    local_field_names(): returns a string of model field names
    concrete_field_names(): returns a string of all concrete field names on the model and its parents
    serializer_field_names(): removes unnecessary field names for serializers
    admin_field_names(): removes unnecessary field names for admin
    snake_case_name(): returns model name in snake case
    __str__(): string representation of Model class
    """

    def __init__(self, model):
        """
        declares model parameter as self variable

        :param model: a model object
        :type model: model
        """

        self.model = model

    @property
    def name(self):
        """
        returns the name of the model

        :return: name
        :rtype: str
        """

        return self.model._meta.object_name

    @property
    def field_names(self):
        """
        returns a string of all forward field names on the model and its parents, excluding ManyToManyFields

        :return: model field names
        :rtype: str
        """

        return get_field_names(self.model._meta.fields)

    @property
    def local_field_names(self):
        """
        returns a string of model field names

        :return: model field names
        :rtype: str
        """

        return get_field_names(self.model._meta.local_fields)

    @property
    def concrete_field_names(self):
        """
        returns a string of all concrete field names on the model and its parents

        :return: model field names
        :rtype: str
        """

        return get_field_names(self.model._meta.concrete_fields)

    @property
    def serializer_field_names(self):
        """
        removes unnecessary field names for serializers

        :return: model field names
        :rtype: str
        """

        return ", ".join([
            "'{}'".format(x.name) for x in self.model._meta.fields if
            x.name not in ["created_at", "updated_at", "deleted_at"]
        ])

    @property
    def admin_field_names(self):
        """
        removes unnecessary field names for admin

        :return: model field names
        :rtype: str
        """

        return ", ".join([
            "'{}'".format(x.name) for x in self.model._meta.fields if
            x.name not in ["id", "created_at", "updated_at", "deleted_at", "created_by", "updated_by"]
        ])

    @property
    def snake_case_name(self):
        """
        returns model name in snake case

        :return: model field name
        :rtype: str
        """

        return camel_case_to_spaces(self.name).replace(' ', '_')

    def __str__(self):
        """
        string representation of Model class

        :return: model name
        :rtype: str
        """

        return self.name


class Models:
    """
    A class for setting up a processed list of models as self variable

    ...

    Attributes
    ----------
    app : app name

    Methods
    -------
    None
    """

    def __init__(self, app):
        """
        declares app parameter as self variable
        assigns models self variable as a list of models in a app

        :param app: app name
        :type app: str
        """

        self.app = app
        self.models = [Model(model) for model in apps.get_app_config(self.app).get_models()]

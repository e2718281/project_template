from django.apps import AppConfig


class {{cookiecutter.first_app_name|title|replace("_","")}}Config(AppConfig):
    name = '{{cookiecutter.first_app_name}}'

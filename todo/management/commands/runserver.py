from django.core.management.commands.runserver import Command as RunserverCommand

class Command(RunserverCommand):
    default_port = '8080'

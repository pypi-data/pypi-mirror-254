from django.core.management.base import BaseCommand, CommandError
from DjPyForms.form_generator import generate_form

class Command(BaseCommand):
    help = 'Generates a Django form for a given model.'

    def add_arguments(self, parser):
        parser.add_argument('model', type=str, help='Name of the template for which to generate the form.')
        parser.add_argument('--app', type=str, default='myapp', help='Name of the Django application containing the model.')
        parser.add_argument('--type', type=str, choices=['django', 'html'], default='django', help='Type of form to be generated (django or html).')
        parser.add_argument('--ext', type=str, default='html', help='File extension for HTML form (only if type=html).')
        parser.add_argument('--for-admin', action='store_true', help='Generate the form for the admin section.')

    def handle(self, *args, **options):
        model_name = options['model']
        app_name = options['app']
        form_type = options['type']
        file_extension = options['ext']
        for_admin = options['for_admin']

        try:
            generate_form(model_name, app_name, form_type, file_extension, for_admin)
            self.stdout.write(self.style.SUCCESS(f'Form successfully generated for model {model_name}.'))
        except Exception as e:
            raise CommandError(f'Form generation error : {e}')

def main():
    import sys
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

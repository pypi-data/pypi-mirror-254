import os
from django.apps import apps
from .django_integration import generate_form_code, generate_html_form_code, update_views_and_urls, update_admin_file
from .utils import create_directory_if_not_exists, confirm_overwrite

def generate_form(model_name, app_name='myapp', form_type='django', file_extension='html', for_admin=False):
    """
    Generates a form for a specified Django model.
    
    :param model_name: Name of the model for which to generate the form.
    :param app_name: Name of the Django application where the model is defined.
    :param form_type: Type of form ('django' or 'html').
    :param file_extension: File extension for HTML form.
    """
    # Récupérer le modèle
    model = apps.get_model(app_name, model_name)
    if not model:
        raise ValueError(f"Modèle '{model_name}' introuvable dans l'application '{app_name}'.")
    
    if for_admin:
        admin_path = os.path.join(app_name, 'admin.py')
        update_admin_file(admin_path, model_name, app_name)
        print(f"Admin page added for model {model_name} in application {app_name}.")
    else:

        if form_type == 'html':
            # Générer un template HTML
            template_code = generate_html_form_code(model)
            forms_dir = f"{app_name}/templates"
            form_file_path = f"{forms_dir}/{model_name.lower()}_form.{file_extension}"
        else:
            # Générer un formulaire Django
            form_code = generate_form_code(model)
            forms_dir = f"{app_name}/forms"
            form_file_path = f"{forms_dir}/{model_name.lower()}_form.py"

        # Vérifier et créer le répertoire si nécessaire
        create_directory_if_not_exists(forms_dir)

        # Vérifier si le fichier existe déjà et demander confirmation pour le remplacer
        if os.path.exists(form_file_path) and not confirm_overwrite(form_file_path):
            print("Operation cancelled.")
            return

        # Créer/Mettre à jour le fichier
        with open(form_file_path, 'w') as file:
            file.write(template_code if form_type == 'html' else form_code)

        # Mettre à jour les fichiers views.py et urls.py pour les formulaires Django
        update_views_and_urls(model_name, app_name, form_type)

        print(f"Form for '{model_name}' successfully created in {form_file_path}.")
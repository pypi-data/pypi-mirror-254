import os
from django.forms import ModelForm
from django.apps import apps

def generate_form_code(model):
    """
    Generates Django form code for a given model.

    :param model: The Django model for which to generate the form.
    :return: String containing the form code.
    """
    class_name = f"{model.__name__}Form"

    form_code = f"from django import forms\n"
    form_code += f"from .models import {model.__name__}\n\n"  # Assurez-vous que le chemin d'importation est correct
    form_code += f"class {class_name}(forms.ModelForm):\n"
    form_code += f"    class Meta:\n"
    form_code += f"        model = {model.__name__}\n"
    form_code += f"        fields = '__all__'\n"  # Utilisez '__all__' pour inclure tous les champs

    return form_code

def generate_html_form_code(model):
    """
    Generates HTML code for a form based on Django model fields.

    :param model: The Django model for which to generate the form.
    :return: String containing the HTML code for the form.
    """
    html_code = "<!DOCTYPE html>\n"
    html_code += "<html>\n<head>\n"
    html_code += f"<title>Formulaire pour {model._meta.object_name}</title>\n"
    html_code += "</head>\n<body>\n"
    html_code += "<form method='post'>\n"
    html_code += "    {% csrf_token %}\n"

    for field in model._meta.get_fields():
        if field.is_relation:
            field_name = field.name
            field_label = field.verbose_name if field.verbose_name else field_name.title()
            html_code += f"    <label for='{field_name}'>{field_label}</label>\n"
            html_code += f"    <select name='{field_name}' id='{field_name}'>\n"
            html_code += f"        {{% for item in {field_name}_set.all %}}\n"
            html_code += f"            <option value='{{{{ item.id }}}}'>'{{{{ item }}}}'</option>\n"
            html_code += f"        {{% endfor %}}\n"
            html_code += "    </select><br>\n"
        else:
            field_name = field.name
            field_label = field.verbose_name if field.verbose_name else field_name.title()
            html_code += f"    <label for='{field_name}'>{field_label}</label>\n"
            html_code += f"    <input type='text' name='{field_name}' id='{field_name}'><br>\n"

    html_code += "    <input type='submit' value='Submit'>\n"
    html_code += "</form>\n"
    html_code += "</body>\n</html>"

    return html_code

def update_or_create_urls(urls_path, model_name, app_name):
    """
    Updates or creates the urls.py file for the specified model and application.
    
    :param urls_path: Path to urls.py file.
    :param model_name: Model name.
    :param app_name: Django application name.
    """
    url_pattern = f"path('{model_name.lower()}/', views.{model_name.lower()}_form, name='{model_name.lower()}_form')"
    urls_code = f"    {url_pattern},\n"

    if os.path.exists(urls_path):
        with open(urls_path, 'r+') as file:
            content = file.readlines()

            # Vérifier si le chemin spécifique existe déjà
            if any(url_pattern in line for line in content):
                print(f"The path for {model_name} already exists in {urls_path}.")
                return

            # Trouver la liste urlpatterns et ajouter la nouvelle URL
            for i, line in enumerate(content):
                if 'urlpatterns = [' in line and i + 1 < len(content):
                    # Insérer le code de la nouvelle URL avant le crochet fermant ']' de urlpatterns
                    content.insert(i + 1, urls_code)
                    break

            file.seek(0)
            file.writelines(content)
    else:
        # Créer le fichier urls.py avec le contenu nécessaire
        with open(urls_path, 'w') as file:
            file.write("from django.urls import path\nfrom . import views\n\n")
            file.write("urlpatterns = [\n")
            file.write(urls_code)
            file.write("]\n")

    print(f"The urls.py files for the {model_name} model in the {app_name} application have been updated or created.")

def update_or_create_views(views_path, model_name, app_name, form_type):
    """
    Updates or creates the views.py file for the specified model and application.

    :param views_path: Path to views.py file.
    :param model_name: Model name.
    :param app_name: Django application name.
    :param form_type: Form type ('django' or 'html').
    """
    model = apps.get_model(app_name, model_name)
    import_code = "from django.shortcuts import render\n"
    if form_type == 'django':
        import_code += f"from {app_name}.forms import {model_name}Form\n"

    view_function_name = f"{model_name.lower()}_form"
    view_function_code = f"\n\ndef {view_function_name}(request):\n"
    template_path = f"{app_name}/templates/{model_name.lower()}_form.html"

    # Ajouter la logique pour traiter les champs relationnels
    context_code = "    context = {}\n"
    for field in model._meta.get_fields():
        if field.is_relation:
            related_model = field.related_model
            context_code += f"    context['{field.name}_set'] = {related_model.__name__}.objects.all()\n"

    if form_type == 'django':
        view_function_code += f"    form = {model_name}Form()\n"
        context_code += "    context['form'] = form\n"

    view_function_code += context_code
    view_function_code += f"    return render(request, '{template_path}', context)\n"

    if os.path.exists(views_path):
        with open(views_path, 'r+') as file:
            content = file.read()

            if import_code not in content:
                content = import_code + "\n" + content

            if view_function_name not in content:
                content += view_function_code

            file.seek(0)
            file.write(content)
    else:
        with open(views_path, 'w') as file:
            file.write(import_code + view_function_code)

    print(f"The views.py file for {model_name} in {app_name} has been updated or created.")

def update_views_and_urls(model_name, app_name, form_type='django'):
    """
    Updates or creates views.py and urls.py files for the specified model and application.

    :param model_name: Model name.
    :param app_name: Django application name.
    :param form_type: Form type ('django' or 'html').
    """
    views_path = os.path.join(app_name, 'views.py')
    urls_path = os.path.join(app_name, 'urls.py')

    # Mettre à jour ou créer views.py
    update_or_create_views(views_path, model_name, app_name, form_type)

    # Mettre à jour urls.py
    update_or_create_urls(urls_path, model_name, app_name)

    print(f"The views.py and urls.py files for the {model_name} model in the {app_name} application have been updated or created.")

def update_admin_file(admin_path, model_name, app_name):
    """
    Updates or creates the admin.py file to register the model in Django administration.

    :param admin_path: Path to admin.py file.
    :param model_name: Model name.
    :param app_name: Django application name.
    """
    import_admin_code = "from django.contrib import admin\n"
    import_model_code = f"from {app_name}.models import {model_name}\n"
    register_code = f"admin.site.register({model_name})\n"

    if os.path.exists(admin_path):
        with open(admin_path, 'r+') as file:
            content = file.readlines()

            # Vérifier et ajouter les importations au début du fichier si nécessaire
            if import_admin_code not in content:
                content.insert(0, import_admin_code)
            if import_model_code not in content:
                content.insert(1, import_model_code)

            # Vérifier si le code d'enregistrement existe déjà
            if register_code not in "".join(content):
                content.append("\n" + register_code)

            file.seek(0)
            file.writelines(content)
            file.truncate()
    else:
        # Créer le fichier admin.py avec le contenu nécessaire
        with open(admin_path, 'w') as file:
            file.write(import_admin_code)
            file.write(import_model_code)
            file.write(register_code)

    print(f"The admin.py file for {model_name} in {app_name} has been updated or created.")

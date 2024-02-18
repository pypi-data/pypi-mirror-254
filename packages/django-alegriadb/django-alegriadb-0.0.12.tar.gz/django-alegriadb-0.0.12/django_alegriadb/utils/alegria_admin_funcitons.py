import inspect
import importlib
from django.db.models import Count
from django_alegriadb import models as alegria_models

class AlegriaVerifier():

    def __init__(self,queryset):

        task = alegria_models.Verified.objects.create()
        apps_to_verify = {app.name:app.db_external_name for app in queryset}
        classes=dict()

        for app in apps_to_verify.keys():
            models = importlib.import_module(f'{app}.models')

            for model in inspect.getmembers(models, inspect.isclass):
                if '_meta' in model[1].__dict__.keys():
                    classes[model[0]]={
                        'app': app,
                        'nome':model[0],
                        'model':model[1],
                        'table_type': 'interna' if model[1]._meta.managed else 'externa',
                        'db_table': model[1]._meta.db_table,
                    }

            for model in classes.keys():
                try:
                    if classes[model]['model']._meta.managed:
                        query = classes[model]['model'].objects.all()
                    else:
                        query = classes[model]['model'].objects.using(apps_to_verify[app]).all()

                    query.first()
                    classes[model]['status'] = dict(status='ok',erro='')

                    if len(query.values('id').annotate(id_count=Count('id')).filter(id_count__gt=1))!=0:
                        classes[model]['status'] = dict(status='error',erro='dados_duplicados')

                except Exception as e:
                    classes[model]['status'] = dict(status='error',erro=e)
        task.data = classes
        task.save()
        
        print('Alegria!')
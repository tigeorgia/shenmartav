"""
Django doesn't like null=True for varchar type fields.
null=True should be removed project-wise from all varchar fields.

This command removes out-of-sync NOT NULL constraints which were added
to the database columns manually end/or by failure of migration.
(schemamigration was not detecting any changes when null=true was
removed from varchar fields)
"""

from django.core.management.base import BaseCommand
from django.db import models, connection, transaction
from django.db.utils import DatabaseError

class Command(BaseCommand):
    all_models = models.get_models()
    cursor = connection.cursor()

    def _filter_user_models(self):
        excluded_keys = ('django.', 'south.', 'reversion', 'menus', 'cms.', 'tagging.', 'licenses.', 'captcha.',)
        filtered_models = []
        for model in self.all_models:
            if not any(x in str(model) for x in excluded_keys):
                filtered_models.append(model)
        self.all_models = filtered_models

    def _get_chartextfields(self, model):
        char_fields = ('CharField', 'TextField', 'TranslationFieldSpecific')
        model_fields = model._meta.fields
        filtered_char_fields = []

        for field in model_fields:
            field_type = field.get_internal_type()
            if any(x in field_type for x in char_fields):
                filtered_char_fields.append(field)

        return filtered_char_fields

    def _convert_null_to_empty(self, model, field):
        filter = {
            '{0}__isnull'.format(field.attname): True
        }
        objects = model.objects.filter(**filter)

        if objects:
            data = {
                field.attname: ''
            }
            self.cursor.execute('UPDATE "{0}" '
                                'SET "{1}" = '' '
                                'WHERE {1} IS NULL;'.format(model._meta.db_table, field.attname))
            transaction.commit_unless_managed()

    def _alter_table_drop_null(self, model, field):
        try:
            self.cursor.execute('ALTER TABLE "{0}" '
                                'ALTER COLUMN "{1}" DROP NOT NULL;'.format(model._meta.db_table, field.attname))
        except DatabaseError:
            pass
        transaction.commit_unless_managed()

    def _handle(self):
        for model in self.all_models:
            charfields = self._get_chartextfields(model)
            for field in charfields:
                self._convert_null_to_empty(model, field)
                self._alter_table_drop_null(model, field)

    def handle(self, *args, **options):
        self._filter_user_models()
        self._handle()
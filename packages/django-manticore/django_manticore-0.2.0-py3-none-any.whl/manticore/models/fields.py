import json

from django.db import models

__all__ = ['BigMultiField', 'JSONField', 'MultiField', 'RTField']

from manticore.models import lookups


class RTField(models.TextField):
    """ Full-text search field (rt_field)."""

    def __init__(self, **kwargs):
        # null is not supported by manticore, '' is reasonable default
        kwargs['null'] = False
        kwargs['default'] = ''
        super().__init__(**kwargs)

    def db_type(self, connection):
        return 'text indexed stored'

    def get_internal_type(self):
        return "RTField"


class IndexedField(RTField):
    """ Non-stored search field which may still be used for querying."""

    def db_type(self, connection):
        return 'text indexed'


class JSONField(models.Field):
    """ JSON field (attr_json)."""
    def db_type(self, connection):
        return 'json'

    def get_internal_type(self):
        return "JSONField"

    def get_prep_value(self, value):
        if value is None:
            return ''
        return json.dumps(value)

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def from_db_value(self, value, expression, connection):
        if value is None:
            return None
        return json.loads(value)


class MultiField(models.PositiveIntegerField):
    """ Multi-field (attr_multi). Contains a list of uint32."""
    def db_type(self, connection):
        return 'multi'

    def get_internal_type(self):
        return 'MultiField'

    def get_prep_value(self, value):
        return value

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def from_db_value(self, value, expression, connection):
        if not value:
            return []
        return list(map(int, value.split(',')))


MultiField.register_lookup(lookups.MultiExact)


class BigMultiField(models.BigIntegerField):
    """ Multi-field for big integer (attr_multi64). Contains a list of int64."""

    def db_type(self, connection):
        return 'multi64'

    def get_internal_type(self):
        return 'BigMultiField'

    def get_prep_value(self, value):
        return value

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def from_db_value(self, value, expression, connection):
        if not value:
            return []
        return list(map(int, value.split(',')))


BigMultiField.register_lookup(lookups.MultiExact)

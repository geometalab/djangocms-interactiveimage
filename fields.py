from django.forms.fields import MultipleChoiceField

from .widgets import OneToManyWidget


class OneToManyField(MultipleChoiceField):
    widget = OneToManyWidget

    def to_python(self, value):
        return []

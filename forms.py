from cms.models import Page
from django.forms import HiddenInput
from django.forms import IntegerField
from django.forms import ModelForm
from django.utils.translation import ugettext as _

from .fields import OneToManyField


class InteractiveImageForm(ModelForm):
    temp_points = OneToManyField(required=False, label=_("Points"))

    def __init__(self, *args, **kwargs):
        super(InteractiveImageForm, self).__init__(*args, **kwargs)

        db_points = self.instance.interactivepoint_set.all()

        points = []
        for dbPoint in db_points:
            points.append((dbPoint.id, dbPoint.title))

        self.fields['temp_points'].widget.choices = points
        self.fields['temp_points'].widget.form_instance = self.instance


class InteractivePointForm(ModelForm):
    xCoordinate = IntegerField(widget=HiddenInput(), initial=0)
    yCoordinate = IntegerField(widget=HiddenInput(), initial=0)

    def __init__(self, *args, **kwargs):
        super(InteractivePointForm, self).__init__(*args, **kwargs)

        page_drafts = Page.objects.drafts()
        pages = []
        for page in page_drafts:
            pages.append((page.id, ''.join(['-' * (page.depth - 1), page.__str__()])))

        self.fields['pages'].widget.choices = pages

from cms.models import Page
from cms.models import get_plugin_media_path
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class InteractiveImage(CMSPlugin):
    title = models.CharField(_("Title"), max_length=50, default='')
    image = models.ImageField(_("Image"), upload_to=get_plugin_media_path, default='NULL')

    def __str__(self):
        return self.title

    def copy_relations(self, old_instance):
        for interactive_point in old_instance.interactivepoint_set.all():
            clone = interactive_point.__class__.objects.get(pk=interactive_point.pk)

            interactive_point.pk = None
            interactive_point.interactiveimage = self
            interactive_point.save()
            interactive_point.copy_relations(clone)


class InteractivePoint(models.Model):
    title = models.CharField(_("Title"), max_length=50, default='')
    description = models.TextField(_("Description"), default='')
    pages = models.ManyToManyField(to=Page, blank=True, null=True, related_name="pages", verbose_name=_("Pages"))
    xCoordinate = models.IntegerField(default=0)
    yCoordinate = models.IntegerField(default=0)
    interactiveimage = models.ForeignKey(to=InteractiveImage, null=True)

    def __str__(self):
        return self.title

    def copy_relations(self, old_instance):
        self.pages = old_instance.pages.all()

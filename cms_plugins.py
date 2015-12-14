from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .forms import InteractiveImageForm
from .models import InteractiveImage


class InteractiveImagePlugin(CMSPluginBase):
    name = _("Interactive Image")
    model = InteractiveImage
    render_template = "interactive_image_plugin.html"
    change_form_template = "interactive_image_change_form.html"
    form = InteractiveImageForm

plugin_pool.register_plugin(InteractiveImagePlugin)

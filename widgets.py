from django.core.urlresolvers import reverse
from django.forms.utils import flatatt
from django.forms.widgets import Select
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _


class OneToManyWidget(Select):
    class Media:
        js = ('js/oneToManyWidget.js',)

    def render(self, name, value, attrs=None, choices=()):
        if value is None:
            value = []
        if self.form_instance.image == 'NULL':
            output = [_("Please add an image first and save the current dialog")]
        else:
            final_attrs = self.build_attrs(attrs, name=name)
            output = [format_html('<select size="5" onChange="toggleEditLinks()" {0}>', flatatt(final_attrs))]
            options = self.render_options(choices, value)
            if options:
                output.append(options)
            output.append('</select>')

            add_url = reverse("admin:interactive_image_plugin_interactivepoint_add")
            change_url = reverse("admin:interactive_image_plugin_interactivepoint_change", args=['{id}'])
            delete_url = reverse("admin:interactive_image_plugin_interactivepoint_delete", args=['{id}'])

            output.append(
                '<a id="add_id_temp_points" class="addLink" href="' + add_url + '?_action=add" onclick="return showAddAnotherPopup(this);">' + _(
                    "Add") + '</a>')
            output.append(
                '<a id="change_id_temp_points" class="changeLink" href="' + change_url + '?_action=change" onclick="return showIdPopup(this);">' + _(
                    "Edit") + '</a>')
            output.append(
                '<a id="delete_id_temp_points" class="deleteLink" href="' + delete_url + '?_action=delete" onclick="return showIdPopup(this);">' + _(
                    "Delete") + '</a>')

        return mark_safe('\n'.join(output))

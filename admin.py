from django.contrib import admin
from django.template.response import SimpleTemplateResponse
from django.utils.translation import ugettext_lazy as _

from .forms import InteractivePointForm
from .models import InteractivePoint

IS_POPUP_VAR = '_popup'
ACTION_VAR = '_action'
POINT_ID_VAR = '_point_id'


class InteractivePointAdmin(admin.ModelAdmin):
    name = _("Interactive Point")
    change_form_template = "interactive_point_change_form.html"
    filter_horizontal = ['pages']
    form = InteractivePointForm
    model = InteractivePoint

    def get_model_perms(self, request):
        # Return empty perms dict thus hiding the model from admin index
        return {}

    def response_add(self, request, value, post_url_continue=None):
        if IS_POPUP_VAR in request.POST:
            return self.response_popup(request, value)
        else:
            super().response_add(request, value, post_url_continue)

    def response_change(self, request, value):
        if IS_POPUP_VAR in request.POST:
            return self.response_popup(request, value)
        else:
            super().response_change(request, value)

    def response_delete(self, request, value):
        if IS_POPUP_VAR in request.GET:
            return self.response_popup(request, value)
        else:
            super().response_delete(request, value)

    def response_popup(self, request, value):
        action = request.GET.get(ACTION_VAR)
        id = request.GET.get(POINT_ID_VAR)

        if id is None:
            id = value.pk

        return SimpleTemplateResponse('admin/interactive_point_popup_response.html', {
            'id': id,
            'value': value,
            'action': action
        })

admin.site.register(InteractivePoint, InteractivePointAdmin)

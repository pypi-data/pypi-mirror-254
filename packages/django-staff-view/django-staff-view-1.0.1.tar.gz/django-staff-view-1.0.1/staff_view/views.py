from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView


class StaffView(TemplateView):

    cancel_url = None

    cancel_value = _("Cancel")

    confirm_message = None

    form_class = None

    submit_value = _("Save")

    template_name = 'staff_view.html'

    title = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('admin:login'))
        elif not request.user.is_staff:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.get_form(request.POST, files=request.FILES)
        if form.is_valid():
            return self.form_valid(form)

        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def form_valid(self, form):
        raise NotImplementedError()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'confirm_message': self.get_confirm_message(),
            'submit_value': self.get_submit_value(),
            'cancel_url': self.get_cancel_url(),
            'cancel_value': self.get_cancel_value(),
            'title': self.get_title()
        })
        return context

    def get_confirm_message(self):
        return self.confirm_message

    def get_submit_value(self):
        return self.submit_value

    def get_cancel_url(self):
        return self.cancel_url

    def get_cancel_value(self):
        return self.cancel_value

    def get_title(self):
        return self.title

    def get_form(self, data=None, files=None, **kwargs):
        if self.form_class is None:
            raise ImproperlyConfigured(
                _(f"{self.__class__} needs to declare a `form_class` attribute or override the `get_form` method")
            )
        return self.form_class(data, files=files, **kwargs)

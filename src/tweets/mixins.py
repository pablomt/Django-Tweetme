from django import forms
from django.forms.utils import ErrorList


class FormUserNeededMixin(object):
	def form_valid(self, form):
		# This method is called when valid form data has been POSTed.
		# It should return an HttpResponse.
		# Se valida si el usuario esta autenticado, esta es la primer forma de validar
		if self.request.user.is_authenticated():
			form.instance.user = self.request.user
			return super(FormUserNeededMixin, self).form_valid(form)
		else:
			# Se muestra error en el tamplate
			form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["El usuario debe estar logeado para continuar"])
			return self.form_invalid(form) # form_invalid(form) es un metodo de las vistas basadas en clases

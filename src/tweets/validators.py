from django.core.exceptions import ValidationError

# Utilizando validators dentro del field en el model si se muestra el error en el field correspondiente
def validate_content(value):
	content = value
	if content == "":
		raise ValidationError("Content cannot be blank")
	return value
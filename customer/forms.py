from oscar.apps.customer.forms import EmailUserCreationForm
from oscar.core.compat import (existing_user_fields, get_user_model)
User = get_user_model()
class EmailUserCreationForm(EmailUserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone','birthday', 'gender', )
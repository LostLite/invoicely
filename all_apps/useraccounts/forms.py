from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1","password2")
        
        
class UserDetailsForm(ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone_number", "email")
        

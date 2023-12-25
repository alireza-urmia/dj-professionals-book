from django.
from allauth.account.forms import LoginForm
from .models import CustomUser

# Custom user Creation&Change form
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

# Custom Login form

class MyCustomLoginForm(LoginForm):

    def login(self, *args, **kwargs):

        # Add your own processing here.


        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)

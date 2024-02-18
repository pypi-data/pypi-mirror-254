from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from omni.pro.base.models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)

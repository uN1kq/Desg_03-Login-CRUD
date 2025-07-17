from django import forms
from .models import CustomUser

# --- Login Form ---
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Password')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            try:
                user = CustomUser.objects.get(username=username)
                if not user.check_password(password):
                    raise forms.ValidationError('Invalid username or password')
            except CustomUser.DoesNotExist:
                raise forms.ValidationError('Invalid username or password')
        return cleaned_data

# --- Registration Form ---
class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = [
            'username', 'firstName', 'lastName', 'email', 'mobileno', 'gender', 'address', 'profile_picture'
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user




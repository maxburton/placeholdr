from django import forms
from django.contrib.auth.models import User
from placeholdr.models import Page, Category, UserProfile, Place, Trip


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,
                         help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If the url is not empty and doesn't start with http:// then prepend it
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data

    class Meta:
        # Provide an association between the ModelsForm and a model
        model = Page

        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them.
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        # or specify the fields to include (i.e. not include the category field)
        # fields = ('title', 'url', 'views')


class SubmitPlaceForm(forms.ModelForm):
    placeName = forms.CharField(required=True, max_length=128)
    placeDesc = forms.CharField(required=False, max_length=400)

    class Meta:
        model = Place
        fields = ('name', 'desc', 'picLink', 'userId', 'lat', 'long', 'slug')
        widgets = {
            'picture': forms.FileInput(attrs={'class': 'custom-file', 'id': "customFile"}),
        }
		
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class PasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('password',)


class UserProfileForm(forms.ModelForm):
    favPlace = forms.ModelChoiceField(queryset=Place.objects.all(), required=False)
    recommendedTrip = forms.ModelChoiceField(queryset=Trip.objects.all(), required=False)

    class Meta:
        model = UserProfile
        fields = ('bio', 'livesIn', 'picture', 'favPlace', 'recommendedTrip')
        widgets = {
            'picture': forms.FileInput(attrs={'class': 'custom-file', 'id': "customFile"}),
        }


class ChangeUserForm(forms.ModelForm):
    username = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email')


class ChangePasswordForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    new_password = forms.CharField(required=True, widget=forms.PasswordInput())
    confirm_new_password = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('password', 'new_password', 'confirm_new_password')

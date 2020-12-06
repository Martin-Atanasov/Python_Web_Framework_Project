from django import forms

from book.models import Kids


class AddKid(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddKid, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].label = "Date of birth (YYYY-MM-DD):"

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Kids
        fields = '__all__'
        widgets = {'user': forms.HiddenInput()}


class EditKid(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditKid, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].label = "Date of birth (YYYY-MM-DD):"
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Kids
        fields = ('baby_profile_picture', 'first_name', 'last_name', 'date_of_birth', 'additional_info',)


class DeleteKid(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeleteKid, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Kids
        fields = '__all__'

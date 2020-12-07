from django import forms

from book.models import Kids, Memory


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


class AddStory(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddStory, self).__init__(*args, **kwargs)
        self.fields['date_of_memory'].label = "Date of story (YYYY-MM-DD):"
        self.fields['kid'].queryset = Kids.objects.filter(user_id=kwargs['initial']['user'].id)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Memory
        fields = '__all__'
        widgets = {'user': forms.HiddenInput()}


class EditStory(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditStory, self).__init__(*args, **kwargs)
        self.fields['date_of_memory'].label = "Date of story (YYYY-MM-DD):"
        self.fields['kid'].queryset = Kids.objects.filter(user_id=kwargs['instance'].user_id)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Memory
        fields = ('memory_picture', 'kid', 'title', 'date_of_memory', 'description', 'status',)


class DeleteStory(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeleteStory, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Memory
        fields = '__all__'

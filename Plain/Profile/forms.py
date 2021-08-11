class ProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ('name','position','genre')
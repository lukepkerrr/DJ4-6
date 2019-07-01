from django import forms

class GameForm(forms.Form):
    number = forms.IntegerField(label='Число')

    def clean_number(self):
        number = self.cleaned_data.get('number')
        if number < 0 or number > 1000:
            raise forms.ValidationError('Число должно быть в диапазоне от 0 до 1000')
        return number

    def clean(self):
        return self.cleaned_data
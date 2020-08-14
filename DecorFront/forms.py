from django import forms

from DecorFront.models import SiteReview


class ReviewForm(forms.ModelForm):
    class Meta:
        model = SiteReview
        fields = ['user', 'comment', 'image', 'choice']

    def clean_user(self):
        user = self.cleaned_data.get('user')
        print("From form", user)

        if not user.isalpha() == True or user == ' ':
            print("validation error")
            raise forms.ValidationError("Enter Name only")
        return user

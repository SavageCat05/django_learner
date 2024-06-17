from django import forms
from .models import review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length = 100, error_messages = {
#         "required": "your name must not be empty",
#         "max_length": "your name must be less than 100 characters",
#     })
#     password = forms.CharField(widget=forms.PasswordInput)
#     review_text = forms.CharField(widget = forms.Textarea, label = "remarks", max_length = 200)
#     rating = forms.IntegerField(min_value=1, max_value = 5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = review
        fields = '__all__'
        labels = {
            'username':'Your name:',
            'password' : 'password:',
            'your_review' : 'review -',
            'rating' : 'rating(out of 5):'
        }
        error_messages = {
            'username' : {
                'required':'God should bless you with a name',
                'max_length':'Your parents must have used butterflow to write your name on your birth certificate'
            }
        }
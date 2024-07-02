from django import forms 
from .models import task_loader, sign_in
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# this class is created to append the widget of calenger in date field, similarly a dateTime widget can also be created 
class dueDateForm(forms.DateInput):
    input_type = "date"
    def __init__(self,**kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)


class Input_form(forms.ModelForm):
    class Meta:
        model = task_loader
        fields = "__all__"
        labels = {
            'task_title':'Task',
            'task_priority':'Priority',
            'task_due_date':'Due Date:',
            'task_detail':'Details-'
        }
        exclude = ['user']

# this is how we add widget in .Modelforms 
        widgets = {
            'task_due_date':dueDateForm(format=["%Y-%m-%d"])
        }

    def __init__(self,*args,**kwargs):
        super(Input_form,self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

            #using self.fields we get a dict of fields
            #note that we want toh update the attribute class and hence we want the value of associated key in dict 
            #vlaue.widgeet.attrs.update({'class':'form-control'})


class Sign_up(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.IntegerField()
    address = forms.CharField(max_length=200)
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'phone','email', 'address', 'password1', 'password2')
        exclude = ['profile_pic']

    def __init__(self,*args,**kwargs):
        super(Sign_up,self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})   

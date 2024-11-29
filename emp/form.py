from django import forms
from .models import Emp
class feedbackform(forms.Form):
    email = forms.EmailField(label="Enter Your Email", max_length=100)
    name= forms.CharField(label="Enter Your Nmae" , max_length=100)
    feedback=forms.CharField(label="Your Feedback",widget=forms.Textarea)
    
    
    def __init__(self, *args, **kwargs):
        super(feedbackform, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'  


        
    
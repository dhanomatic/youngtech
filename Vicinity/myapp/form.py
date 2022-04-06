from django import forms
from .models import Post, Message, Complaints


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = '__all__'

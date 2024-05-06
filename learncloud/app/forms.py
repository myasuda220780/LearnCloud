from django import forms

from app.models import Posts


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ("skill_name",)
        labels = {"skill_name": "学びたいこと"}

from django import forms

class LikesForm(forms.Form):
    class Meta:
        model = Image
        exclude = '__all__'

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image', 'user']
        
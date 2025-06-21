from core.models import AboutUs, Lesson, Course, News
from django import forms


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'About Us'}),
            'slug': forms.HiddenInput(),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'About us', 'row': 4}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'onchange': 'loadFile(event)'})
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title of news'}),
            'slug': forms.HiddenInput(),
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Enter content of news', 'row': 5}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'onchange': 'loadFile(event)'})
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title of course'}),
            'slug': forms.HiddenInput(),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Enter description of course', 'row': 5}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'onchange': 'loadFile(event)'})
        }


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title of lesson'}),
            'slug': forms.HiddenInput(),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Enter description of lesson', 'row': 5}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'onchange': 'loadFile(event)'}),
            'description1': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Enter description of lesson', 'row': 5}),
            'image1': forms.FileInput(attrs={'class': 'form-control', 'onchange': 'loadFile(event)'}),
            'description2': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Enter description of lesson', 'row': 5}),
            'image2': forms.FileInput(attrs={'class': 'form-control', 'onchange': 'loadFile(event)'}),

        }

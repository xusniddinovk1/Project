from core.models import AboutUs, Lesson, Course, News, Teacher
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


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


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'phone_number', 'email', 'bio', 'avatar']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter bio'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'email', 'bio', 'avatar', 'is_staff', 'is_superuser', 'password']

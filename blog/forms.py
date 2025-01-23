from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from . import models as m

User = get_user_model()

# Blog:

class PostForm(forms.Form):
    
    title = forms.CharField(
        label=mark_safe('<span class="text-lg"><span class="text-red-600">*</span> Title</span>'),
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'mt-3 mb-8 block w-full md:w-[40rem] p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xl focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter a title...'
            }
        )
    )
    
    media = forms.FileField(
        label=mark_safe('<span class="text-lg">Upload an image or video</span>'),
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'mt-3 mb-8 flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100', 
                'accept': '.jpg,.png,.jpeg,.mp4,.mov'
            }
        ),
    )
    
    text_field = forms.CharField(
        label=mark_safe('<span class="text-lg"><span class="text-red-600">*</span> Post</span>'),
        required=True,
        max_length=800,
        widget=forms.Textarea(
            attrs={
                'class': 'mt-3 block p-2.5 w-full text-lg text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500',
                'id': 'text_field',
                'placeholder': 'Write here...'
            }
        )
    )
    
    def save(self):
        """create post"""
        
        data = self.cleaned_data

        post = m.Post.objects.create(**data)
        
        return post
    
class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = m.Post
        fields = ['title', 'media', 'text_field']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'mt-3 mb-8 block w-full md:w-[40rem] p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xl focus:ring-blue-500 focus:border-blue-500',
                    'placeholder': 'Enter a title...'
                }
            ),
            'media': forms.FileInput(
                attrs={
                    'class': 'mt-3 mb-8 flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100', 
                    'accept': '.jpg,.png,.jpeg,.mp4,.mov'
                }
            ),
            'text_field': forms.Textarea(
                attrs={
                    'class': 'mt-3 block p-2.5 w-full text-lg text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500',
                    'id': 'text_field',
                    'placeholder': 'Write here...'
                }
            )
        }

# User:

class LoginForm(forms.Form):
    
    email = forms.EmailField(
        label=('Your email'),
        widget=forms.EmailInput(
            attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mt-2 mb-4',
                'placeholder': 'name@domain.com'
            }
        ),
        error_messages={
            'required': 'Required field.',
            'invalid': 'Invalid value.'
        })
    password = forms.CharField(
        label=('Your password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mt-2 mb-4',
                'placeholder': '••••••••'
            }
        ),
        error_messages={
            'required': 'Required field.',
            'invalid': 'Invalid value.'
        })
    
class SignUpForm(forms.Form):
    
    first_name = forms.CharField(
        label=('Your name'),
        widget=forms.TextInput(
            attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mt-2 mb-4',
                'placeholder': 'John'
            }
        ),
        error_messages={
            'required': 'Required field.',
            'invalid': 'Invalid value.'
        })
    
    last_name = forms.CharField(
        label=('Your surname'),
        widget=forms.TextInput(
            attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mt-2 mb-4',
                'placeholder': 'Doe'
            }
        ),
        error_messages={
            'required': 'Required field.',
            'invalid': 'Invalid value.'
        })
    
    email = forms.EmailField(
        label=('Your email'),
        widget=forms.EmailInput(
            attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mt-2 mb-4',
                'placeholder': 'name@domain.com'
            }
        ),
        error_messages={
            'required': 'Required field.',
            'invalid': 'Invalid value.'
        })
    
    password = forms.CharField(
        label=('Your password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mt-2 mb-4',
                'placeholder': '••••••••'
            }
        ),
        error_messages={
            'required': 'Required field.',
            'invalid': 'Invalid value.'
        })
    
    def clean_password(self):
        password = self.cleaned_data.get('password')

        if password:
            return make_password(password)
        else:
            raise forms.ValidationError("A password is required")
        
    def save(self):
        """create user"""
        data = self.cleaned_data
        data['username'] = data['email']

        user = User.objects.create(**data)
        
        return user
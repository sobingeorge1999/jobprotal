from django import forms
from candidate.models import CandidateProfile


class CandidateProForm(forms.ModelForm):
    class Meta:
        model=CandidateProfile
        exclude=("user",)
        widgets={
            'prof_pic':forms.FileInput(attrs={'class':'form-select'}),
            'qualification':forms.TextInput(attrs={'class':'form-select rounded-pill'}),
            'skills': forms.TextInput(attrs={'class': 'form-select'}),
            'exp': forms.TextInput(attrs={'class': 'form-select'})
        }


class CandidateProfEditForm(forms.ModelForm):
    first_name=forms.CharField(max_length=120)
    last_name=forms.CharField(max_length=111)
    phone=forms.CharField(max_length=65)

    class Meta:
        model=CandidateProfile
        fields=["first_name",
                "last_name",
                'phone',
                'prof_pic',
                'resume',
                'qualification',
                'skills',
                'exp'
                ]

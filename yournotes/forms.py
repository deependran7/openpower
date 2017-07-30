from django import forms

from .models import NotesUpload

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = NotesUpload
        fields = [
            "name",
            "institution",
            "filename",
            "notefile",

        ]


from django import forms
from .models import Rentbook

class Rentbook(forms.ModelForm):
    class Meta:
        model = Rentbook
        fields = '__all__'
        labels = {
            'book_title': 'ชื่อหนังสือ',
            'renter_name': 'ผู้เช่า',
            'rent_date': 'วันที่เช่า',
            'return_date': 'วันที่คืน',
            'is_returned': 'คืนแล้วหรือไม่',
        }
        widgets = {
            'rent_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }

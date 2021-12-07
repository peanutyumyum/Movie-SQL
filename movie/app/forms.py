from django import forms
from .models import BranchOffice

bucket = ()
model = BranchOffice.objects.all()
for i in model:
    bucket += (i.name, i.name),


# 지점을 선택할 수 있게 하는 select 태그를 구성된 form
class BranchForm(forms.Form):
    CHOICES = (bucket)
    field = forms.ChoiceField(choices = CHOICES)
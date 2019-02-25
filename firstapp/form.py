from django import forms


class UserForm(forms.Form):
    choicelist=(
            ('4010', '4010'),
            ('5010', '5010'),
            ('4030', '4030'),
            ('2002','2002'),

        )

    doc_num = forms.IntegerField()
    version = forms.ChoiceField(choices=choicelist)
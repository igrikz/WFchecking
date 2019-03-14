from django import forms


class UserForm(forms.Form):
    choicelist=(
            ('4010', '4010'),
            ('5010', '5010'),
            ('4030', '4030'),


            ('4020', '4020'),
            ('4040', '4040'),
            ('4050', '4050'),
            ('4060', '4060'),
            ('5020', '5020'),
            ('5030', '5030'),
            ('5040', '5040'),
            ('5050', '5050'),
            ('6010', '6010'),
            ('6020', '6020'),



        )

    doc_num = forms.IntegerField()
    version = forms.ChoiceField(choices=choicelist)
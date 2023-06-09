from django import forms


class CouponApplyForm(forms.form):
    code = forms.CharField()

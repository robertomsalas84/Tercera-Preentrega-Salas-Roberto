from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    dni = forms.IntegerField(required = True)
    ciudad = forms.CharField(max_length=30, required = True)
    email = forms.EmailField(required=True)

class ProductoForm(forms.Form):
    producto = forms.CharField(max_length=70, required=True)
    meses_garantia = forms.IntegerField(required=True)
    promocion = forms.BooleanField(required=True)


class SucursalForm(forms.Form):
    numero_sucursal = forms.IntegerField(required=True)
    ciudad = forms.CharField(max_length=30,required=True)
    metros_cuadrados = forms.IntegerField(required=True)



    
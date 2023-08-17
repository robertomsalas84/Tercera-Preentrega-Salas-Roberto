from django.http import HttpResponse

def bienvenida(request):
	return HttpResponse("<html><h1>Hola!!!</h1></html>")

def bienvenida1(request):
	response = """
<html>
<h1>Hola!!!</h1>
<h2> Aguante el Rojo!! </h2>
</html>
"""
	return HttpResponse(response)
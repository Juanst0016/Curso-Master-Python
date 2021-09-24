from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

#MVC = MODELO VISTA CONTROLADOR -> ACCIONES (METODOS)
#MVT = MODELO TEMPLATE VISTA -> ACCIONES (METODOS)
layout = """
<h1> Sitio Web | Juan Torres </h1>
<hr/>
<ul>
    <li>
    <a href="/inicio">inicio</a>
    </li>
     <li>
    <a href="/hola-mundo">Hola mundo </a>
    </li>
    <li>
    <a href="/pagina">Pagina de pruebas</a>
    </li>
    <li>
    <a href="/contacto-dos">contacto</a>
    </li>


</ul>
<hr/>
"""


def index(request):
    html = """
    <h1>Inicio</h1>
    <p> Años hasta el 2050</p>
    <ul>
    """

    year = 2021

    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1
    

    html += "<ul/>"
    return render(request, 'index.html')

def Hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):

    if redirigir == 1:
        return redirect('Contacto', nombre="Juan", apellido= "Torres")



    return render(request,'pagina.html')
def contacto(request, nombre="", apellido=""):
    html =""
    if nombre and apellido:
        html += "<p>El nombre completo es:</p>"
        html += f"<h3>{nombre} {apellido}</h3>"

    return HttpResponse(layout+f"<h2>Contactos</h2>"+ html)


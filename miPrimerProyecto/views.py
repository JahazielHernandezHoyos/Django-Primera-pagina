from django.http import HttpResponse
import datetime


def saludar(request):
    return HttpResponse("Hola buenas tardes")

def despedirse(request):
    return HttpResponse("Hasta luego")

def fecha(request):
    fechaActual=datetime.datetime.now()
    documento=""" <HTML>
                    <HEAD>
                    <TTITLE>Esta es una estructura basica de un documento HTML</TITLE>
                    </HEAD>
                    <BODY>
                        <h1> usted ingreso o actualizo esta vista en la fecha %s<h1>
                    <BODY>
                <HTML>""" % fechaActual
    return HttpResponse(documento)

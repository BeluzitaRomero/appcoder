from django.shortcuts import render
# from django.http import HttpResponse # lo sacamos para usar render



# from AppCoder.models import Curso

# def curso(req):
#     curso = Curso(nombre='Backend', camada = '45203')
#     curso.save()
#     dicc = {'curso' :curso.nombre, "camada":curso.camada}
#     plantilla = loader. get_template('cursos.html')
#     return HttpResponse(plantilla.render(dicc))



def inicio(request):
    #render(request, NombreApp/nombre.html)
    return render(request, 'AppCoder/inicio.html')

def cursos(request):

    return render(request, 'AppCoder/cursos.html')

def profesores(request):

    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):

    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):

    return render(request, 'AppCoder/entregables.html')
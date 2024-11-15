from django.shortcuts import render, redirect, get_object_or_404
#lostatos que llegen aqui los migrara a models para ser almasenados y luego mostrados
from .models import Lista

#En este apartados son guardados los datos de agregar_recetas y luego te 
# redirecciona hacia listar_receta para mostrar los datos
def agregar_receta(request):
    if request.method == 'POST':
        receta = request.POST.get('receta')
        chef = request.POST.get('chef')
        comida = request.POST.get ('comida')
        
        Lista.objects.create(receta=receta, chef=chef, comida=comida)
        return redirect('listar_receta.html')
    return render(request, 'agregar_receta.html')

#Aqui se guardan los datos en una variable para mostrarlo en la lista

def listar_receta(request):
    recetas = Lista.objects.all()
    return render(request,'listar_receta.html',{'recetas':recetas})

#En este apartado se encarga de modificar la base de datos para actualizarla

def actualizar_receta(request,id):
    receta = get_object_or_404(Lista, id=id)
    if request.method == 'POST':
        receta.receta = request.POST.get('receta')
        receta.chef = request.POST.get('chef')
        receta.comida = request.POST.get ('comida')
        receta.save()
        return redirect('listar_receta.html')
    return render(request,'listar_receta.html',{'receta':receta})

#En este se eliminara la receta que elijas

def eliminar_receta(request,id):
    receta = get_object_or_404(Lista, id=id)
    if request.method == 'POST':
        receta.delete()
        return redirect('listar_receta.html')
    return render(request,'eliminar_receta.html',{'receta':receta})
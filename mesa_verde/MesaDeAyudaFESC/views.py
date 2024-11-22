from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado, Tecnico, Peticion
from .forms import EmpleadoForm, TecnicoForm, PeticionForm
from django.contrib import messages

def nuevo_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro de empleado exitoso')
            return redirect('nuevo_empleado')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados.html', {'form': form})

def nuevo_tecnico(request):
    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro de técnico exitoso')
            return redirect('nuevo_tecnico')
    else:
        form = TecnicoForm()
    return render(request, 'tecnicos.html', {'form': form})

def nueva_peticion(request):
    if request.method == 'POST':
        form = PeticionForm(request.POST, request.FILES)  # Manejar archivos
        if form.is_valid():
            form.save()
            messages.success(request, 'Nueva petición registrada')
            return redirect('nueva_peticion')
    else:
        form = PeticionForm()
    return render(request, 'nueva_peticion.html', {'form': form})

def asignar_ticket(request):
    peticiones = Peticion.objects.all()  # Muestra todos los tickets
    return render(request, 'asignar_ticket.html', {'peticiones': peticiones})

def resolver_ticket(request, peticion_id):
    peticion = get_object_or_404(Peticion, id_peticion=peticion_id)
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')  # Obtener el estado seleccionado
        solucion = request.POST.get('solucion')   # Obtener la solución proporcionada

        if nuevo_estado in ['En proceso', 'Testeo', 'Solucionado']:  # Validar el estado
            peticion.status = nuevo_estado
        if solucion:  # Guardar la solución si se proporcionó
            peticion.solucion = solucion

        peticion.save()
        messages.success(request, f'Ticket #{peticion_id} actualizado correctamente')
        return redirect('asignar_ticket')
    return render(request, 'resolver_ticket.html', {'peticion': peticion})


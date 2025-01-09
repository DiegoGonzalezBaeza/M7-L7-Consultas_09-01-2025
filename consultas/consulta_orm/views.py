from django.shortcuts import render
from .models import Cliente
import datetime

def todos_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'consulta_orm/todos_clientes.html', {'clientes': clientes})

def clientes_activos(request):
    clientes = Cliente.objects.filter(activo=True)
    return render(request, 'consulta_orm/clientes_activos.html', {'clientes': clientes})

def clientes_rango_fechas(request):
     # Obtener las fechas del formulario GET
    inicio = request.GET.get('inicio')
    final = request.GET.get('final')
    
    # Si no se proporcionan fechas, mostrar todos los clientes
    if not inicio or not final:
        clientes = Cliente.objects.all()
    else:
        try:
            # Convertir las fechas a objetos datetime
            inicio = datetime.datetime.strptime(inicio, '%Y-%m-%d').date()
            final = datetime.datetime.strptime(final, '%Y-%m-%d').date()
            # Aplicar el filtro de rango
            clientes = Cliente.objects.filter(fecha_nacimiento__range=(inicio, final))
        except ValueError:
            # En caso de error en las fechas, mostrar todos los clientes
            clientes = Cliente.objects.all()
    
    return render(request, 'consulta_orm/clientes_rango_fechas.html', {
        'clientes': clientes,
        'inicio': inicio,
        'final': final,
    })
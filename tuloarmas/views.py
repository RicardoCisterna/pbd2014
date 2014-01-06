# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext

# Forms
from forms import *

# Decorators
from django.contrib.auth.decorators import login_required

# Messages, Login, Logout and User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Modelos
from tuloarmas.models import *

def hola(request):
	return HttpResponse("Hello world")
def home(request):
	return HttpResponse("index")
def index(request):
	
	login_form = LoginForm()
	return render_to_response(
		'index.html',
		{
			'login_form': LoginForm,
			'user': request.user
		},
		context_instance=RequestContext(request)
	)
def about(request):
	return render_to_response(
		'about.html',
		{
			'login_form': LoginForm,
			'user': request.user
		},
		context_instance=RequestContext(request)
	)
def FAQ(request):
	return render_to_response(
		'FAQ.html',
		{
			'login_form': LoginForm,
			'user': request.user
		},
		context_instance=RequestContext(request)
	)
def login_view(request):
    """
    Vista encargada autenticar un usuario para ingresar al sistema
    """
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # redireccionar al inicio
                return HttpResponseRedirect('/productos/')
            else:
                # Mensaje warning
                messages.warning(request, 'Tu cuenta ha sido desactivada.')
                return HttpResponseRedirect('/login')
        else:
            # Mensaje de error
            messages.error(request, 'Nombre de usuario o contraseña errónea.')
            return HttpResponseRedirect('/login')
    else:
        return render_to_response(
		'login.html',
		{
			'login_form': LoginForm,
			'user': request.user
		},
		context_instance=RequestContext(request)
	)

#@login_required(login_url='/')
def logout_view(request):
    """
    Cierra la sesion de un usuario y lo redirecciona al home
    """
    logout(request)
    return HttpResponseRedirect('/')

#@login_required(login_url='/')
def productos(request):
    productos = Producto.objects.all()
    return render_to_response(
        'productos.html',
        {
            'productos':productos,
            'user':request.user
        },
        context_instance=RequestContext(request)
    )
    
def registro(request):
    return render_to_response(
        'registro.html',
        {
            
            'user':request.user
        },
        context_instance=RequestContext(request)
    )


def contacto(request):
    return render_to_response(
        'contacto.html',
        {
            
            'user':request.user
        },
        context_instance=RequestContext(request)
    )

def ingreso_material(request):
    return render_to_response(
        'ingreso_material.html',
        {
            
            'user':request.user
        },
        context_instance=RequestContext(request)
    )
    
def tutoriales(request):
    productos = Producto.objects.all()
    return render_to_response(
        'tutoriales.html',
        {
            'productos':productos,
            'user':request.user
        },
        context_instance=RequestContext(request)
    )
    
def datos(request):
	if request.method == "POST":
		form=proveedorform(request.POST)
		rut_proveedor=form.cleaned_data['rut_proveedor']
		nombre_proveedor=form.cleaned_data['nombre_proveedor']
		direc_proveedor=form.cleaned_data['direc_proveedor']
		fono_proveedor=form.cleaned_data['fono_proveedor']
		movil_proveedor=form.cleaned_data['movil_proveedor']
		correo_proveedor=form.cleaned_data['correo_proveedor']
				
				
		p=Proveedor()
		p.rut_proveedor=rut_proveedor
		p.nombre_proveedor=nombre_proveedor
		p.direc_proveedor=direc_proveedor
		p.fono_proveedor=fono_proveedor
		p.movil_proveedor=movil_proveedor
		p.correo_proveedor=correo_proveedor
		p.save()
						
		form = proveedorform()
		ctx={'form':form}
		messages.success(request,'Registro exitoso')
		return render_to_response('menu.html',ctx,context_instance=RequestContext(request))

		else: #GET
			form = proveedorform()
			ctx={'form':form}
		return render_to_response('menu.html',ctx,context_instance=RequestContext(request))
			

#@login_required(login_url='/')
def detalle(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    comentarios = Comentario.objects.filter(producto=producto_id)
    comentario_form = ComentarioForm()
    return render_to_response(
        'detalle.html',
        {
            'producto':producto,
            'comentarios': comentarios,
            'comentario_form': comentario_form,
            'user':request.user
        },
        context_instance=RequestContext(request)
    )

#@login_required(login_url='/')
def menu(request):
    if request.user.is_anonymous():
    	return HttpResponseRedirect('/login')
    else:
        return render_to_response(
		'menu.html',
		{
			'login_form': LoginForm,
			'user': request.user
		},
		context_instance=RequestContext(request)
	)

def nuevo_comentario(request, producto_id):
    # acceso mediante post
    if not request.method == 'POST':
        return HttpResponseRedirect('/')
    form = ComentarioForm(request.POST)
    
    # El formulario debe ser válido
    if not form.is_valid():
        if request.META['HTTP_REFERER']:
            url = request.META['HTTP_REFERER']
        else:
            url = '/'
        messages.error(request, 'Comentario no válido')
        return HttpResponseRedirect(url)
    
    # Una vez se sabe que el formulario es válido se obtienen sus datos
    texto = form.cleaned_data['texto']

    # Se crea el nuevo comentario y se guarda
    producto = Producto.objects.get(id=producto_id)
    new_comentario = Comentario(texto=texto, user=request.user, producto=producto)
    new_comentario.save()
    return HttpResponseRedirect('/productos/' + str(producto_id) + '/')
 

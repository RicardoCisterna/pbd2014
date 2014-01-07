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
    if request.method == 'POST':
        passwd = request.POST['pass']		
        if passwd:
            if request.user.check_password(passwd):
                newpass=request.POST['newpass']
                if newpass:
                    newpass2=request.POST['newpass2']
                    if newpass == newpass2:
                        name = request.user.first_name
                        rut = request.user.last_name
                        mail = request.user.email
                        if request.POST['name']:
                            name = request.POST['name']
                        if request.POST['rut']:
                            numRut = request.POST['rut'][:-2]
                            codVer = request.POST['rut'][-1:]
                            if esRut(request.POST['rut']) and  digito_verificador(numRut) == codVer:
                                rut = request.POST['rut']
                            else:
                                ctx={'error':"Debe ingresar un rut válido con el siguiente formato: XXXXXXXX-Y."}
                                return render_to_response('datos.html', ctx,context_instance = RequestContext(request))
                        if request.POST['mail']:
                            mail = request.POST['mail']
                        request.user.set_password(newpass)
                        request.user.save()
                        new_user = User.objects.filter(username=request.user.username).update(first_name=name,last_name=rut,email=mail)
                        return render_to_response('datos.html',context_instance=RequestContext(request))
                    else:
                        return render_to_response('datos.html', {'error':"Las nuevas contraseñas ingresadas no coinciden entre si."},context_instance = RequestContext(request))
                else:
                    name = request.user.first_name
                    rut = request.user.last_name
                    mail = request.user.email
                    if request.POST['name']:
                        name = request.POST['name']
                    if request.POST['rut']:
                        numRut = request.POST['rut'][:-2]
                        codVer = request.POST['rut'][-1:]
                        if esRut(request.POST['rut']) and digito_verificador(numRut) == codVer:
                            rut = request.POST['rut']
                        else:
                            return render_to_response('datos.html', {'error':"Debe ingresar un rut válido con el siguiente formato: XXXXXXXX-Y."},context_instance = RequestContext(request))
                    if request.POST['mail']:
                        mail = request.POST['mail']
                    new_user = User.objects.filter(username=request.user.username).update(first_name=name,last_name=rut,email=mail)
                    return render_to_response('datos.html', {'success':True},context_instance = RequestContext(request))
            else:
                return render_to_response('datos.html', {'error':"La contraseña ingresada no es correcta."},context_instance = RequestContext(request))
        else:
            return render_to_response('datos.html', {'error':"Debe ingresar su contraseña para realizar cualquier cambio."},context_instance = RequestContext(request))
    else:
        return render_to_response('datos.html',context_instance = RequestContext(request))

def vista(request):
    return render_to_response("about2.html",{},context_instance=RequestContext(request))

def cotizaciones(request):
    cotizacion = Cotizacion.objects.all()
    if len(cotizacion) > 0:
        ctx={
            'cotizacion': cotizacion,
        }
        return render_to_response('cotizaciones.html', ctx, context_instance=RequestContext(request))
    else:
        messages.error(request, "No hay productos")
        return HttpResponseRedirect('/')

def crear_tutorial(request):
    productos = Producto.objects.all()
    if len(productos) > 0:
        ctx={
            'productos': productos,
        }
        return render_to_response('crear_tutorial.html', ctx, context_instance=RequestContext(request))
    else:
        messages.error(request, "No hay productos")
        return HttpResponseRedirect('/')
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
def guardar_proceso_view(request):
    messages.success(request,request.POST.getlist('listado')[0].split('-')[1])
    return render_to_response("crear_tutorial.html",{},context_instance=RequestContext(request))
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
 
def digito_verificador(numRut):
    value = 11 - sum([ int(a)*int(b)  for a,b in zip(str(numRut).zfill(8), '32765432')])%11
    return {10: 'K', 11: '0'}.get(value, str(value))

def esRut(rut):
    try:
        val = int(rut[:-2])
    except ValueError:
        return False
    try:
        val = int(rut[-1:])
    except ValueError:
        return False
    if rut[-2:-1] == "-":
        return True
    return False

def esInt(numero):
    try:
        val = int(numero)
    except ValueError:
        return False
    return True

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
import datetime
from tuloarmas.forms import *
from django.http import *


def hola(request):
    return HttpResponse("Hello world")
def ayuda(request):
    return render_to_response('mantencion.html',context_instance=RequestContext(request))
def home(request):
	return HttpResponse("index")
def index(request):
    categoria=Categoria.objects.all()
    materiales=Material.objects.all()
    login_form = LoginForm()
    return render_to_response(
        'index.html',
        {
            'materiales':materiales,
            'categoria':categoria,
            'login_form': LoginForm,
            'user': request.user
        },
        context_instance=RequestContext(request)
    )
def about(request):
    categoria=Categoria.objects.all()
    return render_to_response(
        'about.html',{'categoria':categoria,'login_form': LoginForm,'user': request.user},context_instance=RequestContext(request))

def FAQ(request):
    categoria=Categoria.objects.all()
    return render_to_response(
        'FAQ.html',{'categoria':categoria,'login_form': LoginForm,'user': request.user},context_instance=RequestContext(request))

def login_view(request):
    """
    Vista encargada autenticar un usuario para ingresar al sistema
    """
    categoria=Categoria.objects.all()
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
            'categoria':categoria,
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
def productos(request,categoria_entrada):
    materiales = Material.objects.all()
    categoria = Categoria.objects.all()
    return render_to_response(
        'productos.html',
        {
            'categoria_entrada':categoria_entrada,
            'categoria':categoria,
            'materiales':materiales,
            'user':request.user
        },
        context_instance=RequestContext(request)
    )
def productos1(request):
    categoria = Categoria.objects.all()
    materiales = Material.objects.all()
    return render_to_response(
        'productos.html',
        {
            'categoria':categoria,
            'materiales':materiales,
            'user':request.user
        },
        context_instance=RequestContext(request)
    )
    
def registro(request):
    categoria = Categoria.objects.all()
    if not request.user.is_anonymous():
        messages.error(request, 'Usted se encuentra logueado, profavor cierre sesión para poder crear un usuario')
        return HttpResponseRedirect('/home')
    else:
        if request.method == 'POST':
            password=request.POST['password']
            nombre=request.POST['nombre']
            apellido=request.POST['apellido']
            direccion=request.POST['direccion']
            telefono=request.POST['telefono']
            celular=request.POST['celular']
            username=request.POST['username']
            correo=request.POST['correo']
            rut=request.POST['rut']
            if request.POST['rut']:
                numRut = request.POST['rut'][:-2]
                codVer = request.POST['rut'][-1:]
                if esRut(request.POST['rut']) and digito_verificador(numRut) == codVer:
                    rut = request.POST['rut']
                else:
                    rutInvalido = True
                    return render_to_response('registro.html', {'rutInvalido':rutInvalido},context_instance = RequestContext(request))
                user1= Usuario.objects.all()
                for i in user1:
                    if i.rut_usuario == rut:
                        rutRegistrado=True
                        return render_to_response('registro.html',{'rutRegistrado':rutRegistrado},context_instance=RequestContext(request))
            if request.POST['username']:
                user2= User.objects.all()
                for i in user2:
                    if i.username == username:
                        userRegistrado=True
                        return render_to_response('registro.html',{'userRegistrado':userRegistrado},context_instance=RequestContext(request))
            tipo_usuario='proveedor'
            s = User()  
            s.username=username
            s.first_name=nombre
            s.last_name=apellido
            s.email = correo
            s.password = password
            s.is_staff ='false'
            s.is_active ='yes'
            s.is_superuser ='no'
            s.last_login = '2013-12-25'
            s.date_joined = '2013-12-25'
            s.set_password(password)
            s.save()
            u = Usuario()
            u.id=s.id
            u.tipo_usuario=tipo_usuario
            u.nombre_usuario=nombre
            u.apellido_usuario=apellido
            u.correo_usuario=correo
            u.password=password
            u.direccion_usuario=direccion
            u.telefono=telefono
            u.celular_usuario=celular
            u.rut_usuario=rut
            u.estado_usuario='true'
            u.fecha_ingreso='2013-12-25'
            u.save()
            complete = True
            return render_to_response(
                'registro.html',
                {
                	  'complete':complete,
                    'categoria':categoria,
                    'user':request.user
                },
                context_instance=RequestContext(request)
            )
        else:
            return render_to_response(
                'registro.html',
                {
                    'categoria':categoria,
                    'user':request.user
                },
                context_instance=RequestContext(request)
            )


def contacto(request):
    categoria = Categoria.objects.all()
    return render_to_response(
        'contacto.html',
        {
            'categoria':categoria,
            'user':request.user
        },
        context_instance=RequestContext(request)
    )

def ingreso_material(request):
    categoria = Categoria.objects.all()
    user = User.objects.all()
    if request.method == 'POST':
        
        nombre_material= request.POST['nombre_material']
        descripcion_material = request.POST['descripcion_material']
        tipo_material= request.POST['tipo_material']
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        imagen_material= request.POST['imagen_material']
        categoria=request.POST.getlist('categoria2')
        print categoria
        m=Material()
        m.nombre_material=nombre_material
        m.descripcion_material=descripcion_material
        m.tipo_material=tipo_material
        m.marca=marca
        m.modelo=modelo
        m.imagen_material=imagen_material
        
        m.categoria_id=1
        m.save()
        ctx={'success':"material agregado correctamente",'user':request.user,'categoria':categoria}
        return render_to_response('ingreso_material.html',ctx, context_instance=RequestContext(request))
    else:
        return render_to_response('ingreso_material.html',{'user':request.user,'categoria':categoria}, context_instance=RequestContext(request))
        
    
def tutoriales(request,tutoriales_id):
    tutoriales = Tutorial.objects.all()
    categoria = Categoria.objects.all()
    return render_to_response(
        'tutoriales.html',
        {
            'categoria':categoria,
            'tutoriales':tutoriales,
            'user':request.user
        },
        context_instance=RequestContext(request)
    )
def tutoriales1(request):
    categoria = Categoria.objects.all()
    tutoriales = Tutorial.objects.all()
    return render_to_response(
        'tutoriales.html',
        {
            'categoria':categoria,
            'tutoriales':tutoriales,
            'user':request.user
        },
        context_instance=RequestContext(request)
    )
    
def datos(request):
    categoria = Categoria.objects.all()
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
                    return render_to_response('datos.html', {'success':True, 'categoria':categoria},context_instance = RequestContext(request))
            else:
                return render_to_response('datos.html', {'error':"La contraseña ingresada no es correcta."},context_instance = RequestContext(request))
        else:
            return render_to_response('datos.html', {'error':"Debe ingresar su contraseña para realizar cualquier cambio."},context_instance = RequestContext(request))
    else:
        return render_to_response('datos.html', {'categoria':categoria,'user':request.user},context_instance = RequestContext(request))

def vista(request):
    return render_to_response("about2.html",{},context_instance=RequestContext(request))

def cotizaciones(request):
    categoria = Categoria.objects.all()
    cotizacion = Cotizacion.objects.all()
    if len(cotizacion) > 0:
        ctx={
            'categoria':categoria,
            'cotizacion': cotizacion,
        }
        return render_to_response('cotizaciones.html', ctx, context_instance=RequestContext(request))
    else:
        messages.error(request, "No hay cotizaciones")
        return HttpResponseRedirect('/menu/')

def crear_tutorial(request):
    materiales = Material.objects.all()
    herramientas = Herramienta.objects.all() 
    user = User.objects.all()
    if request.method == 'POST':
        
        descripcion= request.POST['descripcion']
        HH = request.POST['numeroHH']
        materialResultante= request.POST['materialResultante']
        #nombre_proceso= request.POST['nombreProceso']
        listaAgregado = request.POST.getlist('listado-agregados')
        listaM = request.POST.getlist('listaM')
        imagen_proceso = request.POST['imagen_proceso']
        video=request.POST['video']
        m=Material()
        m.nombre_material=materialResultante
        m.descripcion_material=descripcion
        m.tipo_material='c'
        m.marca='sin-marca'
        m.modelo='sin-modelo'
        m.imagen_material=imagen_proceso
        m.categoria_id=1
        m.save()

        if(not "id-tutorial" in request.POST):
            nombreTuto = request.POST['nombreTuto']
            imagen_tutorial= request.POST['imagen_tutorial']
            desc=request.POST['desc']
            t=Tutorial()
            t.video =video
            t.nombre_tutorial = nombreTuto
            t.descripcion_tutorial=desc
            t.imagen_tutorial=imagen_tutorial
            t.Usuario_id=1
            t.categoria_id=1
            t.save()
            id_tutorial = t.id
        else:
            id_tutorial = request.POST["id-tutorial"]
            t = Tutorial.objects.get(pk=id_tutorial)

        #print t
        p=Proceso()
        p.nombre_proceso = "adsasdasdasdasd"
        p.descripcion_proceso = descripcion
        p.imagen_proceso=imagen_proceso
        p.hh = HH 

        p.numero_proceso= len(Proceso.objects.filter(tutorial=t))+1
        p.tutorial = t
        p.material = m
        p.save()
        
        for i in listaAgregado:
            c=Consumo()
            c.material = Material.objects.get(pk=int(i[0]))
            c.cantidad_consumo = i[2]
            c.proceso = p
            c.save()
        
        for i in listaM:
            h=Uso_herramienta()
            h.herramienta = Herramienta.objects.get(pk=int(i[0]))
            h.proceso = p
            h.save()

        #new_tutorial = Tutorial(video='asd', nombre_tutorial=nombreTuto, descripcion_tutorial=descripcion, imagen_tutorial='asd',Usuario_id=1, categoria_id=1)
        if(request.POST["seguir"]=="no"):
            return HttpResponseRedirect("/tutoriales")
        ctx={'success':"tutorial agregado correctamente",'materiales':materiales,'herramientas':herramientas,'nombre_tuto':t.nombre_tutorial, 'num_proceso':p.numero_proceso+1 , "id_tutorial":id_tutorial}
        return render_to_response('crear_tutorial.html',ctx, context_instance=RequestContext(request))
    else:
        return render_to_response('crear_tutorial.html',{'id_tutorial':"",'materiales':materiales,'herramientas':herramientas}, context_instance=RequestContext(request))
        

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
    categoria = Categoria.objects.all()
    if request.user.is_anonymous():
    	return HttpResponseRedirect('/login')
    else:
        return render_to_response(
		'menu.html',
		{
            'categoria':categoria,
			'login_form': LoginForm,
			'user': request.user
		},
		context_instance=RequestContext(request)
	)

def nuevo_comentario(request, producto_id):
    # acceso mediante post
    categoria = Categoria.objects.all()
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

def detalle(request, tutorial_id):
    categoria = Categoria.objects.all()
    tutorial = Tutorial.objects.get(id=tutorial_id)
    procesos = Proceso.objects.filter(tutorial=tutorial)
    return render_to_response(
        'detalle.html',
        {
            'categoria':categoria,
            'tutorial':tutorial,
            'procesos':procesos,
            'user':request.user
        },
        context_instance=RequestContext(request)
    )

def detalle_producto(request, material_id):
    categoria = Categoria.objects.all()
    materiales = Material.objects.get(id=material_id)
    return render_to_response(
        'detalle_producto.html',
        {
            'categoria':categoria,
            'materiales':materiales,
            'user':request.user
        },
        context_instance=RequestContext(request)
    )
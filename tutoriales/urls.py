from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tuloarmas.views.index', name='home'),
#    url(r'^$', 'tutoriales.views.index', name='home'),
    #url(r'^proyecto/', include('proyecto.foo.urls')),
    url(r'^productos/(\d+)/$', 'tuloarmas.views.productos'),
    url(r'^tutoriales/(\d+)/$', 'tuloarmas.views.tutoriales'),
    url(r'^productos/$', 'tuloarmas.views.productos1'),
    url(r'^tutoriales/$', 'tuloarmas.views.tutoriales1'),
    url(r'^detalle/(\d+)/$', 'tuloarmas.views.detalle'),
    url(r'^detalle/(\d+)/(\d+)/$', 'tuloarmas.views.detalle'),
    url(r'^detalle_producto/(\d+)/$', 'tuloarmas.views.detalle_producto'),
    url(r'^detalle_producto/(\d+)/(\d+)/$', 'tuloarmas.views.detalle_producto'),
    url(r'^login/$', 'tuloarmas.views.login_view'),
    url(r'^logout/$', 'tuloarmas.views.logout_view'),
    url('^home/$','tuloarmas.views.index'),
    url('^ayuda/$','tuloarmas.views.ayuda'),
    url('^menu/$','tuloarmas.views.menu'),
    url('^about/$','tuloarmas.views.about'),
    url('^faq/$','tuloarmas.views.FAQ'),
    url(r'^registro/$', 'tuloarmas.views.registro'),
    url(r'^contact/$', 'tuloarmas.views.contacto'),
    url(r'^agregar_material/$', 'tuloarmas.views.ingreso_material'),
    url(r'^datos/$', 'tuloarmas.views.datos'),
    url(r'^crear_tutorial/$', 'tuloarmas.views.crear_tutorial'),
    url(r'^cotizaciones-u/$', 'tuloarmas.views.cotizaciones'),
    url(r'^guardar/proceso/$', 'tuloarmas.views.guardar_proceso_view',name="guardar_proceso"),
    #url(r'^crear_tutorial/$', 'tuloarmas.views.crear_tutorial'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

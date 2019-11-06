from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.http import  HttpResponseRedirect
from django.http import  HttpResponse



from mascotas.models import Producto,Ventas
from .forms import UsuarioForm,VentasForm

# Create your views here.

def index(request):
    #lista_productos = Producto.objects.raw('SELECT * FROM mascotas_producto where precio < 10000')
    monto = 11500
    lista_productos = Producto.objects.filter(precio__lte=monto)
    
    context = {'lista_prod' : lista_productos}
    
    return render(request, 'index.html', context)

def indexPerro(request):
    lista_prod = Producto.objects.filter(tipo='perro')
    
    context = {'lista_prod' : lista_prod}
    
    return render(request, 'indexPerro.html', context)

def indexGato(request):
    lista_prod = Producto.objects.filter(tipo='gato')
    
    context = {'lista_prod' : lista_prod}
    
    return render(request, 'indexGato.html', context)

def indexCuy(request):
    lista_prod = Producto.objects.filter(tipo='cuy')
    
    context = {'lista_prod' : lista_prod}
    
    return render(request, 'indexCuy.html', context)

def contacto(request):
    return render(request, 'formularioContacto.html')

class RegistroUsuario(CreateView):
    model = User
    template_name = "formularioCuenta.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('index')

def mascotas_list(request):
    mascota = Producto.objects.all()
    context  ={'mascotas':mascota}
    return render(request,'mascota_list.html',context)

class VentasList(ListView):
    model  = Ventas
    template_name = 'ventas_list.html'


class VentasCreate(CreateView):
    model = Ventas
    template_name = 'ventas_crear.html'
    form_class = VentasForm 
    success_url = reverse_lazy('ventas:ventas_listar')

    def get_context_data(self,**kwargs):
        context =super(VentasCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = selft.form_class(selft.request.GET)
        return context

'''
    def post(self,request,*args,**kwargs):
        self.objects = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            ventas = form.save(commit=False)
            ventas.save()                               
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
'''

   
def ventas_crear(request):

    # Comprobamos si se ha enviado el formulario

    #form = ProductoForm(request.POST or None)

    if request.method == "POST":

            obj = Ventas()  # gets new object
            obj.rut = request.POST['rut']
            obj.nombre = request.POST['nombre']  
            obj.apellidos = request.POST['apellidos']
            obj.telefono = request.POST['telefono']
            obj.email = request.POST['email']
            obj.domicilio = request.POST['domicilio']
            obj.stock = request.POST['stock']
            obj.marca = request.POST['marca']

            obj.save()

            return redirect('/ventas_clientes/')
    else:
        return render(request, "index.html")


    return render(request, "index.html")

   
class VentasUpdate(UpdateView):
    model = Ventas
    template_name = 'ventas_crear.html'
    form_class = VentasForm
    success_url = reverse_lazy('ventas_list')

    def get_context_data(self,**kwargs):
        context =super(VentasUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        Ventas = self.model.objects.get(id=pk)
        if 'form' not in context:
            context['form'] = selft.form_class()
        context['id'] = pk
        return context

    def post(self,request,*args,**kwargs):
        self.objects = self.get_object
        id_ventas = kwargs['pk']
        solicitud = self.model.object.get(id=id_ventas)
        form = self.form_class(request.POST,instance=Ventas)
        if form.is_valid():        
            form.save()             
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class VentasDelete(DeleteView):
    model = Ventas
    template_name = 'ventas_eliminar.html'
    success_url = reverse_lazy('ventas_delete')


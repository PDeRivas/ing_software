from django.views import View
from django.shortcuts import render, redirect

from productos.repositories.supplierRepository import SupplierRepository

repo = SupplierRepository

class SupplierView(View):
    def get(self, request):
        repo = SupplierRepository()
        proveedores = repo.get_all()
        return render(
            request,
            'supplier/list.html',
            {
                'suppliers': proveedores
            },
        )
    
class SupplierCreate(View):
    def get(self, request):
        return render(
            request,
            'supplier/create.html'
        )
    
    def post(self, request):
        repo = SupplierRepository()
        data = request.POST

        name = data.get('name')
        address = data.get('address')
        phone =  data.get('phone')

        newSupplier = repo.create(nombre = name,
                                  direccion = address,
                                  telefono = phone)

        return redirect('supplier_detail', newSupplier.id)

class SupplierDetail(View):
    def get(self, request, id):
        repo = SupplierRepository()
        proveedor = repo.get_by_id(id)

        return render(
            request,
            'supplier/detail.html',
            {
                'supplier': proveedor,
            }
        )

class SupplierDelete(View):
    def get(self, request, id):
        repo = SupplierRepository()
        proveedor = repo.get_by_id(id=id)
        repo.delete(proveedor)
        return redirect('supplier_list')
    
class SupplierUpdate(View):
    def get(self, request, id):
        repo = SupplierRepository()
        proveedor = repo.get_by_id(id)

        return render(
            request,
            'supplier/update.html',
            {
                'supplier': proveedor,
            }
        )
    
    def post(self, request, id):
        repo = SupplierRepository()
        proveedor = repo.get_by_id(id)

        data = request.POST
        name = data.get('name')
        address = data.get('address')
        phone =  data.get('phone')

        repo.update(proveedor = proveedor,
                    nombre = name,
                    direccion = address,
                    telefono = phone)

        return redirect('supplier_detail', id)

def supplier_update(request, id:int):
    proveedor = repo.get_by_id(id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone =  request.POST.get('phone')

        repo.update(proveedor, name, address, phone)
        return redirect(
            'supplier_detail',
            proveedor.id
        )
    
    return render(
        request,
        'supplier/update.html',
        {
            'supplier': proveedor,
        }
    )


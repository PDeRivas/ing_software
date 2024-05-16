from django.shortcuts import render, redirect

from productos.repositories.supplierRepository import SupplierRepository

repo = SupplierRepository

def supplier_list(request):
    proveedores = repo.get_all()
    return render(
        request,
        'suppliers/list.html',
        {
            'suppliers': proveedores
        },
    )

def supplier_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone =  request.POST.get('phone')
        repo.create(name = name,
                    address = address,
                    phone = phone)

        return redirect(
            'supplier_list'
        )
    
    return render(
        request,
        'suppliers/create.html',
    )

def supplier_delete(request, id:int):
    proveedor = repo.get_by_id(id=id)
    repo.delete(proveedor)
    return redirect(supplier_list)

def supplier_update(request, id:int):
    proveedor = repo.get_by_id(id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone =  request.POST.get('phone')

        repo.update(proveedor, name, address, phone)
        return redirect(
            supplier_details,
            proveedor.id
        )
    
    return render(
        request,
        'suppliers/update.html',
        {
            'supplier': proveedor,
        }
    )

def supplier_details(request, id:int):
    proveedor = repo.get_by_id(id=id)

    return render(
        request,
        'suppliers/detail.html',
        {
            'supplier': proveedor,
        }
    )

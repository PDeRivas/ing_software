from typing import (
    List,
    Optional,
)

from productos.models import (
    Supplier    
)

class SupplierRepository:
    def get_all() -> List[Supplier]:
        return Supplier.objects.all()
    
    def create(name: str,
               address: str,
               phone: int,) -> Supplier.objects:
        return Supplier.objects.create(name = name,
                                       address = address,
                                       phone = phone)
    
    def delete(supplier: Supplier):
        supplier.delete()

    def get_by_id(id: int) -> Supplier.objects:
        return Supplier.objects.get(id=id)
    
    def update(supplier: Supplier,
               name: str,
               address: str,
               phone: int,) -> Supplier.objects:
        supplier.name = name
        supplier.address = address
        supplier.phone = phone

        supplier.save()
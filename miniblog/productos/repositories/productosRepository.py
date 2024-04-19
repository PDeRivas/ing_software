from typing import (
    List,
    Optional,
)

from productos.models import (
    Productos,
    Category
)

class ProductosRepository:
    def create(self,
               nombre: str,
               precio: float,
               stock: int,
               categoria: Optional[Category] = None,
               descripcion: Optional[str] = None,
               ) -> Productos.objects:
        
        return Productos.objects.create(
            name = nombre,
            description = descripcion,
            price = precio,
            category = categoria,
            stock = stock,
        )
    
    def get_all(self) -> List[Productos]:
        return Productos.objects.all()
    
    def get_by_id(self, producto_id,) -> Optional[Productos]:
        return Productos.objects.filter(id=producto_id).first()
    
    def get_product_on_price_range(
            self,
            min_price = float,
            max_price = float,
        ) -> List[Productos]:
        return Productos.objects.filter(
            price_range=(min_price, max_price)
        )
    
    def get_product_on_category(
            self,
            category_id = int,
    ) -> List[Productos]:
        category = Category.objects.filter(id=category_id).first()
        return Productos.objects.filter(category = category)
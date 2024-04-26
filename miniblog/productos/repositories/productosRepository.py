from typing import (
    List,
    Optional,
)

from productos.models import (
    Productos,
    Category
)

#logger = logging.getLogger(__name__)

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
    
    def filter_by_id(self, producto_id,) -> Optional[Productos]:
        return Productos.objects.filter(id=producto_id).first()
    
    def get_by_id(self, id: int,) -> Optional[Productos]:
        try:
            product = Productos.objects.get(id=id)
        except:
            product = None
        return product
    
    def get_product_on_price_range(
            self,
            min_price = float,
            max_price = float,
        ) -> List[Productos]:
        productos = Productos.objects.filter(
            price__range = (min_price, max_price)
        )
        return productos
    
    def filter_by_category(
            self,
            categoria = Category,
    ) -> List[Productos]:
        return Productos.objects.filter(category = categoria)
    
    def filter_by_category_name(
            self,
            categoria = str,
    ) -> List[Productos]:
        return Productos.objects.filter(category__name = categoria)
    
    def delete_by_id(self, id:int):
        producto = self.get_by_id(id=id)
        return producto.delete()

    def get_product_gte_stock(self,
                              cantidad: int
                              ) -> List[Productos]:
        return Productos.objects.filter(stock__gte=cantidad)
    
    def get_product_lte_stock(self,
                              cantidad: int
                              ) -> List[Productos]:
        return Productos.objects.filter(stock__lte=cantidad)
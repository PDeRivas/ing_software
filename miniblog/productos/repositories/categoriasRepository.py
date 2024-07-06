from typing import (
    List,
    Optional,
)

from productos.models import (
    Productos,
    Category
)

class CategoriasRepository:
    def get_all(self) -> List[Category]:
        return Category.objects.all()
    
    def create(self, name:str) -> Category.objects:
        return Category.objects.create(name = name)
    
    def delete(self, category: Category):
        category.delete()

    def get_by_id(self, id: int) -> Category.objects:
        return Category.objects.get(id=id)
    
    def update(self,
               category: Category,
               name: str,) -> Category.objects:
        category.name = name
        category.save()
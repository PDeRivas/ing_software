from typing import (
    List,
    Optional,
)

from productos.models import (
    Productos,
    Category
)

class CategoriasRepository:
    def get_all() -> List[Category]:
        return Category.objects.all()
    
    def create(name:str) -> Category.objects:
        return Category.objects.create(name = name)
    
    def delete(category: Category):
        category.delete()

    def get_by_id(id: int) -> Category.objects:
        return Category.objects.get(id=id)
    
    def update(category: Category,
               name: str,) -> Category.objects:
        category.name = name
        category.save()
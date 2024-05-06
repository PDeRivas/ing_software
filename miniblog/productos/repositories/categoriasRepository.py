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
from rest_framework import pagination

class MiPaginador(pagination.PageNumberPagination):
    page_size = 2
    page_query_params = 'pagina'
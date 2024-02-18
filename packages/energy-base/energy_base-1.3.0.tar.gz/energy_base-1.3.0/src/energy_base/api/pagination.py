from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class Pagination(PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'page': self.page.number,
            'pageSize': self.page.paginator.per_page,
            'count': self.page.end_index() - self.page.start_index() + 1,
            'total': self.page.paginator.count,
            'pagesCount': self.page.paginator.num_pages,
            'data': data,
        })


class LargeResultsSetPagination(Pagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 50


class StandardResultsSetPagination(Pagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50


class SmallResultsSetPagination(Pagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class MiniResultsSetPagination(Pagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 50


class FullDataPagination(PageNumberPagination):
    page_size = 1000

    def get_paginated_response(self, data):
        return Response(data)

from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response
from rest_framework import status


class CustomPagination(PageNumberPagination):
    page_size = 1  # Number of items per page
    page_size_query_param = 'page_size'  # Allow client to set page size
    page_query_param = 'page-num'  # Page query parameter
    max_page_size = 1 # Maximum limit for page size

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total_items': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'page_size': self.page_size,
            'results': data
        })
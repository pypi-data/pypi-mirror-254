"""
Custom pagination classes for REST framework
"""
from rest_framework.pagination import CursorPagination, PageNumberPagination
from rest_framework.response import Response


class LinkedHeaderPageNumberPagination(PageNumberPagination):
    """
    This overrides the default PageNumberPagination so that it only
    returns the results as an array, not the pagination controls
    (eg number of results, etc)
    """
    page_size = 25

    def get_paginated_response(self, data):
        next_url = self.get_next_link()
        previous_url = self.get_previous_link()

        link = ''
        if next_url is not None and previous_url is not None:
            link = '<{next_url}>; rel="next", <{previous_url}>; rel="prev"'
        elif next_url is not None:
            link = '<{next_url}>; rel="next"'
        elif previous_url is not None:
            link = '<{previous_url}>; rel="prev"'
        link = link.format(next_url=next_url, previous_url=previous_url)
        headers = {'Link': link} if link else {}
        return Response(data, headers=headers)


class DemodDataCursorPagination(CursorPagination):
    """
    This overrides the default CursorPagination for Telemetry endpoint
    """
    page_size = 25
    ordering = '-timestamp'

    def get_paginated_response_schema(self, schema):
        """
        This overrides the default get_paginated_response_schema to add examples for the schema of
        CursorPagination. This can be removed when 8687 pull request us released by
        django-rest-framework:
        https://github.com/encode/django-rest-framework/pull/8687
        """
        return {
            'type': 'object',
            'properties': {
                'next': {
                    'type': 'string',
                    'nullable': True,
                    'format': 'uri',
                    'example': 'http://api.example.org/accounts/?{cursor_query_param}=cD00ODY%3D"'.
                    format(cursor_query_param=self.cursor_query_param)
                },
                'previous': {
                    'type': 'string',
                    'nullable': True,
                    'format': 'uri',
                    'example': 'http://api.example.org/accounts/?{cursor_query_param}=cj0xJnA9NDg3'
                    .format(cursor_query_param=self.cursor_query_param)
                },
                'results': schema,
            },
        }

from rest_framework import status
from rest_framework.response import Response


class CreateListModelMixin:
    """
    Create list of items
    """

    def create(self, request, *args, **kwargs):
        if not isinstance(request.data, list):
            return super(CreateListModelMixin, self).create(request, *args, **kwargs)
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

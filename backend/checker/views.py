from logging import getLogger

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from checker.models import Link
from checker.serializers import LinkListRetrieveSerializer, LinkCreateUpdateSerializer

logger = getLogger('checker')


class LinkViewSet(ModelViewSet):
    """Controller for processing links."""
    http_method_names = ('get', 'post', 'put', 'delete')

    def get_queryset(self):
        return Link.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        request = {
            'list': LinkListRetrieveSerializer,
            'retrieve': LinkListRetrieveSerializer,
            'create': LinkCreateUpdateSerializer,
        }
        return request.get(self.action, LinkCreateUpdateSerializer)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        ids = [link.get('id') for link in request.data]
        self.validate_ids(ids)
        links = []
        for link_data in request.data:
            link = Link.objects.get(id=link_data.get('id'))
            link.url = link_data.get('url')
            links.append(link)
        Link.objects.bulk_update(links, ['url'])
        serializer = LinkCreateUpdateSerializer(links, many=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status.HTTP_200_OK, headers=headers)

    def validate_ids(self, ids):
        for id in ids:
            try:
                Link.objects.get(id=id)
            except (Link.DoesNotExist, ValidationError):
                logger.error(f'Link with id={id} not found.')
                raise status.HTTP_400_BAD_REQUEST
        return True

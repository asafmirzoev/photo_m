from uuid import UUID
from urllib.parse import unquote_plus

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from django.db.models import QuerySet

from images.models import Image, Person
from .serializers import ImageSerializer, ImageDetailSerializer
from . import utils


def get_images(request: Request) -> Response:
    filters = utils.images_filters(request.query_params)
    if filters:
        images: set[Image] = set(Image.objects.filter(**filters))
    else:
        images: QuerySet[Image] = Image.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)


def get_image(image_id: UUID) -> Response:

    if not Image.objects.filter(pk=image_id).exists():
        return Response({'error_message': 'Нет изображений с таким id'}, status=status.HTTP_404_NOT_FOUND)

    image: Image = Image.objects.get(pk=image_id)
    serializer = ImageDetailSerializer(image, many=False)
    return Response(serializer.data)


def create_image(request: Request) -> Response:

    fields, names = utils.get_image_fields(request.data)
    if not fields:
        return Response({'error_message': 'Изображения в запросе не найдено'}, status=status.HTTP_400_BAD_REQUEST)
    
    image: Image = Image.objects.create(**fields)

    if names:
        persons: list[Person] = [Person(name=name, image=image) for name in names]
        Person.objects.bulk_create(persons)
    
    serializer = ImageDetailSerializer(image, many=False)
    return Response(serializer.data)


def search_person(request: Request) -> Response:
    name: str | None = request.query_params.get('name')
    if name:
        name = unquote_plus(name)

    persons: set[Person] = set(Person.objects.filter(name__icontains=name).values_list('name', flat=True))
    return Response(persons)
    


    
     
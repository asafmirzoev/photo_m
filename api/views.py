from uuid import UUID

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from . import services as svc


class ImageView(APIView):
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request, image_id: UUID = None) -> Response:
        if image_id:
            return svc.get_image(image_id)
        return svc.get_images(request)
    
    def post(self, request: Request) -> Response:
        return svc.create_image(request)


class PersonView(APIView):
    parser_classes = (MultiPartParser,)

    def get(self, request: Request) -> Response:
        return svc.search_person(request)

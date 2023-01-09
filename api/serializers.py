from rest_framework import serializers

from images.models import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'image')


class ImageDetailSerializer(serializers.ModelSerializer):

    persons = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Image
        fields = ('id', 'image', 'persons', 'location', 'description', 'created_at')


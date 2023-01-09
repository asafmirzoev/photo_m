def get_image_fields(data: dict) -> tuple[dict, list]:
    fields = {}

    if not data.get('image'):
        return fields, data.get('names')

    fields['image'] = data.get('image')

    if location := data.get('location'):
        fields['location'] = location

    if description := data.get('description'):
        fields['description'] = description
    
    if names := data.get('names'):
        names = names.split(', ')
    
    return fields, names


def images_filters(params: dict) -> dict[str: str]:

    from urllib.parse import unquote_plus
    from images.models import Person

    filters = {}

    name: str | None = params.get('name')
    if name and Person.objects.filter(name=unquote_plus(name)).exists():
        filters['persons__in'] = Person.objects.filter(name=unquote_plus(name)).values_list('id', flat=True)
    
    if location := params.get('location'):
        filters['location__icontains'] = unquote_plus(location)
    
    if description := params.get('description'):
        filters['description__icontains'] = unquote_plus(description)

    if date := params.get('date'):
        filters['created_at'] = date
    
    return filters
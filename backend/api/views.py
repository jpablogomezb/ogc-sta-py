import json
# from django.forms.models import model_to_dict
from django.http import JsonResponse  # HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response

from things.models import Thing
from things.serializers import ThingSerializer


@api_view(['GET'])
def api_thing_get(request, *args, **kwargs):
    instance = Thing.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(model_data)
        data = ThingSerializer(instance).data
    return Response(data)


@api_view(['POST'])
def api_thing_post(request, *args, **kwargs):
    serializer = ThingSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        return Response(serializer.data)
    # return Response({"invalid": "Not good data"}, status=400)


# example
# def api_home(request, *args, **kwargs):
    # print(request.GET)
#    body = request.body
#    data = {}
#    try:
#        data = json.loads(body)
#    except:
#        pass
    # print(data.keys())
#    data['headers'] = dict(request.headers)
#    data['params'] = dict(request.GET)
#    data['content_type'] = request.content_type
#    return JsonResponse(data)

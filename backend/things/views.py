from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Thing
from .serializers import ThingSerializer


class ThingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        # name = serializer.validated_data.get('name')
        # description = serializer.validated_data.get('description')
        # if description is None:
        #    description = name
        # serializer.save(user=self.request.user)
        # send a Django signal
        return super().perform_create(serializer)


thing_list_create_view = ThingListCreateAPIView.as_view()


class ThingDetailAPIView(generics.RetrieveAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    # lookup_field = 'pk'


thing_detail_view = ThingDetailAPIView.as_view()


class ThingUpdateAPIView(generics.UpdateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()


thing_update_view = ThingUpdateAPIView.as_view()


class ThingDeleteAPIView(generics.DestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


thing_delete_view = ThingDeleteAPIView.as_view()

# class ThingListAPIView(generics.ListAPIView):
#    queryset = Thing.objects.all()
#    serializer_class = ThingSerializer
#    # lookup_field = 'pk'


# thing_list_view = ThingListAPIView.as_view()

class ThingMixinView(mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    lookup_field = 'pk'

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk') is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


thing_mixin_view = ThingMixinView.as_view()


@api_view(['GET', 'POST'])
def thing_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        if pk is not None:
            # detail view
            thing_obj = get_object_or_404(Thing, pk=pk)
            data = ThingSerializer(thing_obj, many=False).data
            return Response(data)
        # list view
        queryset = Thing.objects.all()
        data = ThingSerializer(queryset, many=True).data
        return Response(data)

    if method == 'POST':
        # create an item
        serializer = ThingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response({"Invalid": "Invalid data input"}, status=400)






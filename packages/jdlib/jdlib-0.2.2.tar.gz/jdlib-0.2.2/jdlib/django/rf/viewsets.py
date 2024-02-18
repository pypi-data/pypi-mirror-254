from rest_framework.exceptions import MethodNotAllowed
from rest_framework.viewsets import ModelViewSet as DRFModelViewSet


class ModelViewSet(DRFModelViewSet):
    lookup_field = 'uuid'

    def update(self, request, *args, **kwargs):
        '''
        Disable PUT and force PATCH
        '''
        partial = kwargs.pop('partial', False)
        if not partial:
            raise MethodNotAllowed(request.method)
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

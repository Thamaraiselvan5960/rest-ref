from rest_framework import viewsets
from models.models import *
from rest_framework.decorators import action



class sampleViewset(viewsets.ModelViewSet):

    # get queryset
    def get_queryset(self):
        ''' This function returns a queryset'''
        pass

    def get_serializer_class(self):
        ''' this function will return a ser class based on action'''
        if self.action == 'create':
            pass
            # return 
        if self.action == 'list':
            pass
            # return
        return None

    

    queryset = Sample.objects.all()

    




    # creating extra links 
    @action(detail=False,methods=['post'],serializer_class = None)
    def sample(self, request):
        pass




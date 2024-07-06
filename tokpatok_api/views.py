# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from tokpatok_api.models import Tokpatok
# from tokpatok_api.serializer import TokpatokSerializer

# # Create your views here.
# @api_view(['GET'])
# def tokpatok_list(request):
#     tokpatoks = Tokpatok.objects.all() #Complex Data
#   serializer = TokpatokSerializer(tokpatoks, many=True)
#   return Response(serializer.data)


# @api_view(['POST'])
# def tokpatok_create(request):
#   serializer = TokpatokSerializer(data=request.data)
#   if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#   else:
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def tokpatok(request, pk):
#   try:
#       tokpatok = Tokpatok.objects.get(pk=pk)
#   except:
#       return Response({
#           'error': 'Tokpatok does not exist'
#       }, status=status.HTTP_404_NOT_FOUND)

#   if request.method == 'GET':
#       serializer = TokpatokSerializer(tokpatok)
#       return Response(serializer.data)
    
#   if request.method == 'PUT':
#       serializer = TokpatokSerializer(tokpatok, data=request.data)
#       if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#   if request.method == "DELETE":
#       tokpatok.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework.views import APIView
from tokpatok_api.models import Tokpatok
from tokpatok_api.serializer import TokpatokSerializer
from rest_framework.response import Response
from rest_framework import status
from tokpatok_api.models import Tokpatok

class TokpatokList(APIView):
    def get(self, request):
         tokpatoks = Tokpatok.objects.all() #Complex Data
         serializer = TokpatokSerializer(tokpatoks, many=True)
         return Response(serializer.data)
    
class TokpatokCreate(APIView):
    def post(self, request):
        serializer = TokpatokSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TokpatokDetail(APIView):

    def get_tokpatok_by_pk(self, pk):
        try:
            return Tokpatok.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Tokpatok does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        tokpatok = self.get_tokpatok_by_pk(pk)
        serializer = TokpatokSerializer(tokpatok)
        return Response(serializer.data)
    
    def put(self, request, pk):
        tokpatok = self.get_tokpatok_by_pk(pk)
        serializer = TokpatokSerializer(tokpatok, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        tokpatok = self.get_tokpatok_by_pk(pk)
        tokpatok.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        

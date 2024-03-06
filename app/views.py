from django.shortcuts import render
from rest_framework.decorators import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response
# Create your views here.




class productcrud(APIView):
    def get(self,reqiest,id):
        PDO=product.objects.all()
        PJO=pcserializers(PDO,many=True)
        return Response(PJO.data)
    
    def post(self,request,id):
        JDO=request.data
        PDO=pcserializers(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'data inserted successfully'})
        else:
            return Response({'error':'data is not inserted'})
        

    def put(self,request,id):
        po=product.objects.get(id=id)
        UPDO=pcserializers(po,data=request.data)
        if UPDO.is_valid():
            UPDO.save()
            return Response('data is updated')
        else:
            return Response('error data is not updated')
        
    def patch(self,request,id):
        po=product.objects.get(id=id)
        UPDO=pcserializers(po,data=request.data,partial=True)
        if UPDO.is_valid():
            UPDO.save()
            return Response('data is updated')
        else:
            return Response('error data is not updated')
        

    def delete(self,request,id):
        product.objects.get(id=id).delete()
        return Response('deleted data successfullyh')
        
        


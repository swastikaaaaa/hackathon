from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
import random
import json
from .models import hitmole

currentslot=0
currentImage=0
currentscore=0
prevscore=0
highscore=0

def gotHit():
   if(currentImage <= 10 and currentImage != 0):
        score=prevscore+1
        return score
   elif(currentImage > 10):
        return 9999999999999999
   if (currentscore>prevscore):
       highscore=currentImage
    
       
# Create your views here.
@permission_classes([AllowAny])
class hitmoleView(APIView):

    def put(self,request,input=None):
        if(input == currentslot):
            result = gotHit()
            return Response(result)
        return Response(9999999999999999)


    def get(self,request):
        currentslot = random.randint(1, 5)
        currentImage = random.randint(1,20)
        data = {'currentSlot': currentslot, 'currentImage': currentImage}
        return HttpResponse(content=json.dumps(data), content_type='application/json',status=200)
        # return HttpResponse({'msg':'hfhgf'})
    





        
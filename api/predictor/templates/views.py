from django.shortcuts import render

from .apps import PredictorConfig

from django.http import JsonResponse
from rest_framework.views import APIView

import numpy as np

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def get(request):
    if request.method == 'GET':

        return render(request, "WebApp/form.html", {})
    
    elif request.method == 'POST':

        print("data :")
        print(request.POST)

        F1 = request.POST.get('f1',None)

        F2 = request.POST.get('f2',None)

        F3 = request.POST.get('f3',None)

        F4 = request.POST.get('f4', None)

        F5 = request.POST.get('f5',None)

        F6 = request.POST.get('f6',None)

        F7 = request.POST.get('f7',None)

        F8 = request.POST.get('f8',None)

        F9 = request.POST.get('f9',None)

        F10 = request.POST.get('f10',None)

        fields = [F1, F2, F3, F4, F5, F6, F7, F8, F9, F10]
        print(fields)

        if not None in fields:

            F1 = float(F1)
            F2 = float(F2)
            F3 = float(F3)
            F4 = float(F4)
            F5 = float(F5)
            F6 = float(F6)
            F7 = float(F7)
            F8 = float(F8)
            F9 = float(F9)
            F10 = float(F10)
            result = [F1, F2, F3, F4, F5, F6, F7, F8, F9, F10]
            prediction = PredictorConfig.model.predict([result])[0]

            predictions = {
            'error' : '0',
            'message' : 'Successfull',
            'prediction' : prediction
            }
        else:
            predictions = {
                'error' : '1',
                'message': 'Invalid Parameters'                
            }

        return JsonResponse(predictions)
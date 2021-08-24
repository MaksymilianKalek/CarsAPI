from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

import requests
import json
from statistics import mean

from .serializers import CarSerializer
from .models import Car

# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def create(self, request):
        make = request.data['make']
        model = request.data['model']
        URL = f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json'

        try:
            car = Car.objects.get(make=make, model=model)
        except:
            car = None

        if car is None:
            results = requests.get(URL).json()['Results']
            match = [x for x in results if x['Model_Name'] == model]
            if len(match) > 0:
                car = Car(make=make, model=model)
                car.save()
                return Response(status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class RatePost(APIView):

    def post(self, request):
        car_id = request.data['car_id']
        rating = float(request.data['rating'])

        if rating >= 1 and rating <= 5:
            car = Car.objects.get(id=car_id)
            try:
                car.ratings.append(rating)
                car.rates_number = len(car.ratings)
                car.avg_rating = round(mean(car.ratings), 1)
                car.save()
                
                return Response(status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class PopularGet(APIView):

    def get(self, request):
        cars = Car.objects.all().order_by('-rates_number')[:5]
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

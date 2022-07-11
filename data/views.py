from django.shortcuts import render
from django.http import JsonResponse
from orders.models import ClothName,PaymentDetail,ClothCategory,OrdersSummary
from rest_framework import serializers
from rest_framework import generics
from rest_framework.views import APIView
import pandas as pd
from rest_framework.response import Response


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetail
        fields = '__all__'

class PaymentList(generics.ListCreateAPIView):
    queryset = PaymentDetail.objects.all()
    serializer_class = PaymentSerializer

class ChartData(APIView):
    def get(self):
        df = pd.DataFrame(list(OrdersSummary.objects.all().values("delivery","price")))
        df1 = pd.DataFrame(list(OrdersSummary.objects.all().values("puckup_date")))

        data2 = df1.pivot_table(index = ['puckup_date'], aggfunc ='size').to_dict()
        count_rev = [val for val in data2.values()]
        lavel_rev = [val for val in data2.keys()]
        print(count_rev)
        print(lavel_rev)

        delivery = df.groupby('delivery', as_index=False).sum().to_dict()
        label = [val for val in delivery['delivery'].values()]
        price = [val for val in delivery['price'].values()]
        print(label)
        print(price)
        return Response({"label":label,"price":price,"count_rev":count_rev,"lavel_rev":lavel_rev})


def data(request):

    df = pd.DataFrame(list(OrdersSummary.objects.all().values("delivery","price")))
    df1 = pd.DataFrame(list(OrdersSummary.objects.all().values("puckup_date")))

    data2 = df1.pivot_table(index = ['puckup_date'], aggfunc ='size').to_dict()
    count_rev = [val for val in data2.values()]
    lavel_rev = [val for val in data2.keys()]
    print(count_rev)
    print(lavel_rev)

    delivery = df.groupby('delivery', as_index=False).sum().to_dict()
    label = [val for val in delivery['delivery'].values()]
    price = [val for val in delivery['price'].values()]
    print(label)
    print(price)
    return JsonResponse({"label":label,"price":price,"count_rev":count_rev,"lavel_rev":lavel_rev})







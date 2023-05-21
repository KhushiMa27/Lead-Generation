from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse

from LeadGenerationAPP.serializers import StatesSerializer
from LeadGenerationAPP.serializers import CitiesSerializer
from LeadGenerationAPP.serializers import CustomerSerializer
from LeadGenerationAPP.models import States
from LeadGenerationAPP.models import Cities
from LeadGenerationAPP.models import Customer
from . import tuple_to_dict
from django.db import connection

@api_view(['GET', 'POST', 'DELETE'])
def CustomerInterface(request):
    return render(request,"Customer.html",{})

@api_view(['GET', 'POST', 'DELETE'])
def CustomerSubmit(request):
    if request.method == 'POST':
        customer_serializer = CustomerSerializer(data=request.data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return render(request,"Customer.html",{"message":"Record Submitted Successfully"})
        return render(request,"Customer.html",{"message":"Fail to Submit Record"})

@api_view(['GET', 'POST', 'DELETE'])
def DisplayAllCustomer(request):
    return render(request,"DisplayAllCustomer.html",{})

@api_view(['GET', 'POST', 'DELETE'])
def Customer_List(request):
    if request.method == 'GET':
        customer_list = Customer.objects.raw('select * from leadgenerationapp_customer')
        customer_serializer = CustomerSerializer(customer_list, many=True)
        return JsonResponse(customer_serializer.data, safe=False)
    return JsonResponse({}, safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def Customer_List_By_Id(request):
   if request.method=='GET':
    customerid=request.GET['customerid']
    cursor=connection.cursor()
    q="select Cu.*,(select S.statename from leadgenerationapp_states S where S.stateid=Cu.state) as statename,(select C.cityname from leadgenerationapp_cities C where C.cityid=Cu.city) as cityname from leadgenerationapp_customer Cu where Cu.id={0}".format(customerid)
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictOne(cursor)
    data['dob']=str(data['dob'])
    return render(request,"CustomerById.html",{'record':data})
  
   return JsonResponse({},safe=False)
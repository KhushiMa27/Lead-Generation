
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from LeadGenerationAPP.models import Manager
from LeadGenerationAPP.models import States
from LeadGenerationAPP.models import Cities
from django.db import connection
from .import tuple_to_dict
from LeadGenerationAPP.serializers import ManagerSerializer
from LeadGenerationAPP.serializers import StatesSerializer
from LeadGenerationAPP.serializers import CitiesSerializer
from django.http.response import JsonResponse



@api_view(['GET','POST','DELETE'])
def ManagerInterface(request):
    return render(request,"Manager.html",{})


def DisplayAllManager(request):
       
    return render(request,"DisplayAllManager.html",{})

@api_view(['GET','POST','DELETE'])
def ManagerSubmit(request):
   if request.method == 'POST':
      #employee_data = request.GET.dict()
      #print("employeeeeee",request.data)
      manager_serializer = ManagerSerializer(data=request.data)
      if manager_serializer.is_valid():
        manager_serializer.save()
        return render(request,"Manager.html",{"message":"Record Submitted Successfully"})
     
      
      return render(request,"Manager.html",{"message":"Fail to Submit Record"})
    
    
'''
@api_view(['GET','POST','DELETE'])
def Manager_List(request):
  if request.method=='GET':
    manager_list=Manager.objects.all()
    manager_serializer=ManagerSerializer(manager_list,many=True)
    #print("Employee",employee_serializer.data)
    return JsonResponse(manager_serializer.data,safe=False)
  return JsonResponse({},safe=False)
'''
@api_view(['GET', 'POST', 'DELETE'])
def Manager_List(request):
  if request.method=='GET':
    cursor=connection.cursor() 
    q="select E.*,(select S.statename from leadgenerationapp_states S where S.stateid=E.state) as statename,(select C.cityname from leadgenerationapp_cities C where C.cityid=E.city) as cityname,(select M.firstname from leadgenerationapp_manager M where M.id=E.managerid) as mfirstname,(select M.lastname from leadgenerationapp_manager M where M.id=E.managerid) as mlastname from leadgenerationapp_employee E"
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictAll(cursor)
    return JsonResponse(data,safe=False)
  
  return JsonResponse({},safe=False)



   










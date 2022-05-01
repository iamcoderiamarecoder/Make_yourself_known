from django.shortcuts import render,redirect

from .models import investors
from django.http import JsonResponse



from django.views.generic import View
from django.shortcuts import render

from django.http import JsonResponse
import requests


# Create your views here.


user_id =None



def add(request):
    if request.method =="POST":
        name = request.POST.get("name")
        link = request.POST.get("link")
        image_link = request.POST.get("image_link")
        

        data = investors(name=name,link=link,image_link=image_link)
        data.save()

        try:
            object= investors.objects.get(name=name,link=link,image_link=image_link,payment="Payment_not_done")
            global user_id
            user_id=object.id
            
            param = {"id":id}
            return render(request,"add.html",param)
        except:
            response= "Already Exist Try Changing the details."
            param= {"id":response}
            return render(request,"add.html",param)

         
           
            
    return render(request,"add.html")



def khalti_request(request):


    return render(request, "khaltirequest.html")


def homepage(request):
    paid_users= investors.objects.filter(payment="Payment_done")
    for i in paid_users:
        param=  {"investors1":paid_users}
    
    return render(request,"homepage.html",param)





class KhaltiVerifyView(View):
    def get(self, request, *args, **kwargs):
        token = request.GET.get("token")
        amount = request.GET.get("amount")
     #   o_id = request.GET.get("order_id")
       # print(o_id)
        url = "https://khalti.com/api/v2/payment/verify/"
        payload = {
            "token": token,
            "amount": amount

        }
        headers = {
            "Authorization": "Key test_secret_key_bc0580e7bf264493afbc37e253a179a3"
        }

       # order_obj = investors.objects.get(id=o_id)
        response = requests.post(url, payload, headers=headers)
        resp_dict = response.json()
        
        user=investors.objects.get(id=user_id)
        name= user.name
        link=user.link
        image_link= user.image_link
        print(user)
        if resp_dict.get("idx"):
            success = True
            paid_status=investors(name=name,link=link,image_link=image_link,payment="Payment_done")
            paid_status.save()

        else:
            success = False
        data = {
            "success": success
        }
        return JsonResponse(data)
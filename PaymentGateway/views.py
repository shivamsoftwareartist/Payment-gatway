from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from paywix.payu import PAYU
import uuid


def home(request):
    # return render(request, "test.html")
    return render(request, "test.html")

payu = PAYU()

# Payu checkout page
@csrf_exempt
def payu_checkout(request):
    if request.method == 'POST':
        data = dict(zip(request.POST.keys(), request.POST.values()))
        data['txnid'] = payu.generate_txnid()
        payu_data = payu.initiate_transaction(data)
        # return render(request, 'payu_checkout.html', {"posted": payu_data})
        return render(request, 'success.html', {"posted": payu_data})
    return render(request, 'payu.html', {})


# Payu success return page
@csrf_exempt
def payu_success(request):
    data = dict(zip(request.POST.keys(), request.POST.values()))
    response = payu.check_hash(data)
    return JsonResponse(response)


# Payu failure page
@csrf_exempt
def payu_failure(request):
    data = dict(zip(request.POST.keys(), request.POST.values()))
    response = payu.check_hash(data)
    return JsonResponse(response)    

# def checkout(request):
#     if request.method == 'POST':
#         data = {'amount': '10', 
#                 'firstname': 'renjith', 
#                 'email': 'sraj@gmail.com',
#                 'phone': '9746272610', 'productinfo': 'test', 
#                 'lastname': 'test', 'address1': 'test', 
#                 'address2': 'test', 'city': 'test', 
#                 'state': 'test', 'country': 'test', 
#                 'zipcode': 'tes', 'udf1': '', 
#                 'udf2': '', 'udf3': '', 'udf4': '', 'udf5': ''
#             }
#         # You can generate the transaction id, save to db
#         # Here paywix.payu providing dynamic transaction id's 
#         # if  you this method please ensure that, the ID is not existed in the
#         # db
#         data['txnid'] = payu.generate_txnid()
#         # Please dont forget to include this part, The paywix.payu included the hidden
#         # Payu form, will post the data to payu based on your mode selection, if you
#         # required more detils please go through : 
#         # https://github.com/renjithsraj/paywix/blob/master/paywix/templates/payu_checkout.html
#         payu_data = payu.initiate_transaction(data)
#         return render(request, 'payu_checkout.html', {"posted": payu_data})
#     else:
#         return render(request, 'checkout.html', {"posted": payu_data})


# Payu success return page
# @csrf_exempt
# def payu_success(request):
#     data = dict(zip(request.POST.keys(), request.POST.values()))
#     response = payu.check_hash(data)
#     # Store response to the db
#     return JsonResponse(response)        

# from django.http import HttpResponse
# from payu.gateway import check_hash
# from payment_gateway.settings import *
# from payu.gateway import payu_url
# from hashlib import sha512
# from payu.gateway import get_hash
# from uuid import uuid4
# from payu.gateway import verify_payment


# payu_url = payu_url()
# sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||<SALT>)


# data = {
#     'txnid':uuid4().hex, 'amount':10.00, 'productinfo': 'Sample Product',
#     'firstname': 'test', 'email': 'test@example.com', 'udf1': 'Userdefined field',
# }
# hash_value = get_hash(data)

# sha512(<SALT>|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)




# def success_response(request):
#     hash_value = check_hash(request.POST)
#     if check_hash(request.POST):
#         return HttpResponse("Transaction has been Successful.")




# response = verify_payment("Your txnid")
# print response       


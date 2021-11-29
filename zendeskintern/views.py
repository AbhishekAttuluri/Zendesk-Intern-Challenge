from django.http import response
from django.shortcuts import render
import requests
from requests.auth import HTTPBasicAuth
import json
from . import templates
i=1
global username
username = 'aattulur@buffalo.edu/token'
global tokenid
tokenid='MPtt4aCRPYGH9q8kd9YrifWa61Hz3YqTLr8cFn50'
def home(request):
    try:
        ss='https://zccabhishek121297.zendesk.com/api/v2/tickets.json?per_page=25&page='+str(i)
        resp= requests.get(ss, auth=HTTPBasicAuth(username, tokenid))
        if resp.status_code==200:
            data=resp.json()
            return render(request, 'home.html', {'response':data})
        else:
            rep=responsecode(resp)
            return render(request, 'error.html', {'response':rep})
    except:
        print("Error in Code!!! Please check!!!")


def get_ticket_details(request, product_id):
    try:
        ss='https://zccabhishek121297.zendesk.com/api/v2/tickets/' + str(product_id) +'.json'
        resp= requests.get(ss, auth=HTTPBasicAuth(username, tokenid))
        if resp.status_code==200:
            data=resp.json()
            return render(request, 'details.html', {'response': data['ticket']})
        else:
            rep=responsecode(resp)
            return render(request, 'error.html', {'response':rep})
    except:
        print('Error in code!!! Please check!!!')

def next(request):
    try:
        global i
        i=i+1
        pagesting='https://zccabhishek121297.zendesk.com/api/v2/tickets.json?per_page=25&page='+str(i)
        resp= requests.get(pagesting, auth=HTTPBasicAuth(username, tokenid))
        data=resp.json()
        if not data['tickets']:
            i=i-1
            pagesting='https://zccabhishek121297.zendesk.com/api/v2/tickets.json?per_page=25&page='+str(i)
            resp= requests.get(pagesting, auth=HTTPBasicAuth(username, tokenid))
        if resp.status_code==200 and resp.json() is None:
            data=resp.json()
            return render(request, 'home.html', {'response': data})
        elif resp.status_code==200:
            data=resp.json()
            return render(request, 'home.html', {'response': data})
        else:
            rep=responsecode(resp)
            return render(request, 'error.html', {'response':rep})
    except:
        print('Error in code!!! Please check!!!')

def previous(request):
    try:
        global i
        if i==1:
            pagesting='https://zccabhishek121297.zendesk.com/api/v2/tickets.json?per_page=25&page='+str(i)
        else:
            i=i-1
            pagesting='https://zccabhishek121297.zendesk.com/api/v2/tickets.json?per_page=25&page='+str(i)
        resp= resp= requests.get(pagesting, auth=HTTPBasicAuth(username, tokenid))
        if resp.status_code==200:
            data=resp.json()
            return render(request, 'home.html', {'response': data})
        else:
            rep=responsecode(resp)
            return render(request, 'error.html', {'response':rep})
    except:
        print('Error in code!!! Please check!!!')


def responsecode(resp):
    if resp.status_code==404:
        return 'SORRY for the Inconvenience!!! Please try again later!!!'
    elif resp.status_code==401:
        return 'Authentication mismatch!!! Please check'
    else:
        return 'Something is wrong!!! Please check!!!'
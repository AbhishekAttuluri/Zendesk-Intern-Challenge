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

#This function fetches the starting 25 tickets from API and displays them in home page.
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


#This function fetches the details of a specific ticket.
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

#This function fetches the next tickets after the current page.
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
        
#This function fetches the previous tickets before the current page.
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

#This function handles the errors in the code.
def responsecode(resp):
    if resp.status_code==404:
        return 'SORRY for the Inconvenience!!! Please try again later!!!'
    elif resp.status_code==401:
        return 'Authentication mismatch!!! Please check'
    else:
        return 'Something is wrong!!! Please check!!!'

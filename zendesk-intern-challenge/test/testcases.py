from django.shortcuts import render
import requests
from requests.auth import HTTPBasicAuth
from django.test import TestCase

class UserLoginTestCase(TestCase):
    sampleid=10
    def test_for_page_not_found(self):
        # The URL given here is not present. So we get 404 PAGE NOT FOUND error. This test checks for the Page not found condition.
        ss='https://zccabhishek121297.zendesk.com/api/vckets.jsopage=25&page=1'
        resp= requests.get(ss, auth=HTTPBasicAuth('aattulur@buffalo.edu/token', 'MPtt4aCRPYGH9q8kd9YrifWa61Hz3YqTLr8cFn50'))
        self.assertEqual(resp.status_code, 404)

    def test_for_authentication_failure(self):
        # The Authentication details given here are wrong. So when we try to authenticate 401 AUTHENTICATION ERROR should occur.
        ss='https://zccabhishek121297.zendesk.com/api/v2/tickets.json?per_page=25&page=1'
        resp= requests.get(ss, auth=HTTPBasicAuth('xyz@buffalo.edu/token', 'MPtt4aCRPYGH9q8kd9YrifWa61Hz3YqTLr8cFn50'))
        self.assertEqual(resp.status_code, 401)

    def test_for_correct_response(self):
        # If there are no issues we get the correct response which is 200 STATUS CODE.
        ss='https://zccabhishek121297.zendesk.com/api/v2/tickets.json?per_page=25&page=1'
        resp= requests.get(ss, auth=HTTPBasicAuth('aattulur@buffalo.edu/token', 'MPtt4aCRPYGH9q8kd9YrifWa61Hz3YqTLr8cFn50'))
        self.assertEqual(resp.status_code, 200)
    
    def test_for_correct_ticket_details(self):
        # This testcase checks for the response we get when we request a ticket details.
        response = self.client.post(self.sampleid)
        ss='https://zccabhishek121297.zendesk.com/api/v2/tickets/' + str(self.sampleid) +'.json'
        resp= requests.get(ss, auth=HTTPBasicAuth('aattulur@buffalo.edu/token', 'MPtt4aCRPYGH9q8kd9YrifWa61Hz3YqTLr8cFn50'))
        data=resp.json()
        self.assertEqual(data['ticket']['id'],self.sampleid)

    def test_for_data_in_home_page(self):
        # This test case checks for the presence of response in the home page.
        response = self.client.post(' ')
        ss='https://zccabhishek121297.zendesk.com/api/v2/tickets.json?per_page=25&page=1'
        resp= requests.get(ss, auth=HTTPBasicAuth('aattulur@buffalo.edu/token', 'MPtt4aCRPYGH9q8kd9YrifWa61Hz3YqTLr8cFn50'))
        data=resp.json()
        self.assertEqual(bool(data['tickets']), not None)


    

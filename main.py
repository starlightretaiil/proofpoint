import requests

'''
This script pulls data out of Poofpoint API and returns the data as json 
Proofpoint API v1.0
Michael Earls
www.michaelearls.com
Python 3.7
'''

def list_org_info(username, password, domain):
    '''
    :param username:
    :param password:
    :param domain:
    :return: Returns a single organisation identified by :domain in JSON format
    '''
    url = 'https://us1.proofpointessentials.com/api/v1/orgs/' + domain
    headers = {'X-User': username, 'X-Password': password, 'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    get_json = r.json()
    print(get_json)


def list_user_email(username, password, domain, email):
    '''
    :param username:
    :param password:
    :param domain:
    :param email:
    :return: Returns a single user identified by :email from the organisation identified by :domain in JSON format
    '''
    url = 'https://us1.proofpointessentials.com/api/v1/orgs/' + domain + '/' + 'users' + '/' + email
    headers = {'X-User': username, 'X-Password': password, 'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    get_json = r.json()
    print(get_json)


def list_org_licensing(username, password, domain):
    '''
    :param username:
    :param password:
    :param domain:
    :return: Returns organisation licensing information
    '''
    url = 'https://us1.proofpointessentials.com/api/v1/orgs/' + domain + '/' + 'licensing'
    headers = {'X-User': username, 'X-Password': password, 'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    get_json = r.json()
    print(get_json)


def list_org_domain(username, password, domain):
    '''
    :param username:
    :param password:
    :param domain:
    :return: Returns a single domain :domain in JSON format
    '''
    url = 'https://us1.proofpointessentials.com/api/v1/orgs/' + domain + '/domains/'  + domain
    headers = {'X-User': username, 'X-Password': password, 'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    get_json = r.json()
    print(get_json)


def return_endpoint(username, password, domain):
    '''

    :param username:
    :param password:
    :param domain:
    :return: Returns the Organization URL
    '''
    url = 'https://us1.proofpointessentials.com/api/v1/endpoints/' + domain
    headers = {'X-User': username, 'X-Password': password, 'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    get_json = r.json()
    print(get_json)


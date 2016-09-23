import requests
import json


def list_orgs_info(username, password, domain):
    '''
    :param username:
    :param password:
    :param domain:
    :return: Return all organisations under a parent organisation identified by :domain in JSON format
    '''
    url = 'https://us1.proofpointessentials.com/api/orgs/' + domain + '/' + 'orgs'
    headers = {'X-User': username, 'X-Password': password, 'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    get_json = r.json()
    print(get_json)


def list_org_info(username, password, domain):
    '''
    :param username:
    :param password:
    :param domain:
    :return: Returns a single organisation identified by :domain in JSON format
    '''
    url = 'https://us1.proofpointessentials.com/api/orgs/' + domain
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
    url = 'https://us1.proofpointessentials.com/api/orgs/' + domain + '/' + 'users' + '/' + email
    headers = {'X-User': username, 'X-Password': password, 'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    get_json = r.json()
    print(get_json)

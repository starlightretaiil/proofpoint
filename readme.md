# ProofPoint Essentails API 

Proofpoint Essentials Rest API

Introduction
The Proofpoint Essentials API is a REST API based around resource-focused, noun URLs, with HTTP verbs being used to operate on these resources. 

Supported Functions:

*list_org_info: Returns a single organisation identified by :domain in JSON format

*list_user_email: Returns a single user identified by :email from the organisation identified by :domain in JSON format

*list_org_licensing: Returns organisation licensing information

*list_org_domain: Returns a single domain :domain in JSON format

*return_endpoint: Returns the Organization URL

Organization
In this context ‘Organization’ can refer to entities of any type (OEM Partner, Strategic Partner, Channel Partner and Organization). An Organization is core resource which owns various sub-resources such as Domains and Users. When referring to an Organization in an API request, we do so using the primary domain. For example to read data for the Organization "My Company" the following URL would be used.

Domain
An Organization may have a number of domains associated with it. In the example above My Company may also be associated with mycompany.ca, mycompany.co.uk etc. A GET to an Organization will return all of the domains associated with it, but if actions are required on a single domain it can be addressed as follows.

Users
As with Domains, Users are resources owned by a single Organization, so all requests to individual users are addressed via the Organization, and identified using the primary email address of the User.

Endpoint
An Organization may exist on any Proofpoint Essentials instance (in some cases more than one). To find out which endpoint to use for a particular Organization the following URL may be used against any instance. All further requests should be directed at the correct instance.

Package
As mentioned previously each Organization is defined by its Package. The package may be updated via the API (it can be read by reading the orgs resource).

Licensing
The licensing endpoint allows basic Organization license information to be read (GET) and updated (PUT) via the following URL:

https://us1.proofpointessentials.com/api/v1/docs/index.php

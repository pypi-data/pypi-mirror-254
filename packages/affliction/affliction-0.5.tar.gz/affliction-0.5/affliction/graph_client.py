import posixpath

from .base import SynchronousMicrosoftApiClient


class SynchronousGraphClient(SynchronousMicrosoftApiClient):
    def __init__(
            self,
            tenant_id,
            client_id=None,
            client_secret=None,
            creds=None,
            scope='https://graph.microsoft.com/.default'):
        super().__init__(
            tenant_id,
            client_id,
            client_secret,
            creds,
            scope=scope,
            base_url='https://graph.microsoft.com/v1.0')

    def get(self, url, params=None, headers=None, token_retry=False, **kwargs):
        """
        Send a GET request to the specified URL.

        Available OData query parameters for Microsoft Graph API:

        - $filter: Filters the results based on a condition (e.g., "startswith(displayName, 'A')")
        - $select: Narrows the properties returned (e.g., "id,displayName")
        - $orderby: Orders the results based on properties (e.g., "displayName asc")
        - $skip: Skips a specified number of results
        - $top: Limits the number of results returned (up to 999)
        - $search: Performs a full-text search (e.g., "$search="displayName: 'John'")
        - $count: Returns the count of results (true or false)
        - $expand: Expands related entities inline

        Note: Not all parameters are available for all endpoints. Always
        consult Microsoft Graph API documentation for endpoint-specific details.

        :param url: URL for the GET request
        :param headers: Optional headers dictionary
        :param params: Optional dictionary of query parameters
        :param token_retry: Internal flag to ensure we don't enter an infinite
                            loop if there's a token issue
        :return: JSON response from the server
        """
        headers = self.adjust_headers_for_odata(params, headers)
        return super().get(
            url, params, headers=headers,
            token_retry=token_retry, **kwargs)

    def post_headers(self):
        return {
            'accept': 'application/json',
        }

    def post(self, url, params=None, headers=None, token_retry=False,
             json_data=None, **kwargs):
        post_headers = self.post_headers()
        if headers:  # pragma: no cover
            post_headers.update(headers)
        return super().post(
            url, params=params, json=json_data, headers=headers,
            token_retry=token_retry, **kwargs)

    def get_users(self, select=None, params=None):
        """
        fetch a list of users from the microsoft graph api.

        available odata query parameters for the /users endpoint:

        - $filter: filters the results based on a condition (e.g., "accountEnabled eq true")
        - $select: narrows the properties returned (e.g., "id,displayName,mail")
        - $orderby: orders the results based on properties (e.g., "displayName asc")
        - $skip: skips a specified number of results
        - $top: limits the number of results returned (up to 999)
        - $count: returns the count of results (true or false)
        - $expand: expands related entities inline (e.g., "manager,memberOf")
        - $search: performs a full-text search on specific properties
                   (requires 'ConsistencyLevel' header to be set to 'eventual')

        for detailed information and additional query options, consult the
        official microsoft graph api documentation for the /users endpoint:
        https://docs.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0

        :param params: optional dictionary of query parameters
        :param select: list of user properties to include
        :return: list of users
        """
        select = select or [
            'id',
            'userPrincipalName',
            'displayName',
            'mail',
            'accountEnabled',
            'assignedLicenses',
            'identities',
            'lastPasswordChangeDateTime',
            'onPremisesDistinguishedName',
            'onPremisesDomainName',
            'onPremisesImmutableId',
            'onPremisesLastSyncDateTime',
            'onPremisesSamAccountName',
            'onPremisesSyncEnabled',
            'otherMails',
            'proxyAddresses',
            'userType',
        ]
        params = params or {}
        params['$select'] = ','.join(select)
        endpoint = f'{self.base_url}/users'
        return list(self.yield_result(endpoint, params))

    def get_user(self, n_id=None, select=None):
        """
        returns the specified user, select should be a list of strings
        that include one or more properties from https://docs.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0
        """
        endpoint = f"{self.base_url}/users('{n_id}')"
        select = select or [
            'id',
            'userPrincipalName',
            'displayName',
            'mail',
            'accountEnabled',
            'assignedLicenses',
            'identities',
            'lastPasswordChangeDateTime',
            'onPremisesDistinguishedName',
            'onPremisesDomainName',
            'onPremisesImmutableId',
            'onPremisesLastSyncDateTime',
            'onPremisesSamAccountName',
            'onPremisesSyncEnabled',
            'otherMails',
            'proxyAddresses',
            'userType',
        ]
        params = {
            '$select': ','.join(select),
        }
        result = self.get(endpoint, params=params)
        return result

    def subscribed_skus(self, **kwargs):
        url = f'{self.base_url}/subscribedSkus'
        return list(self.yield_result(url, **kwargs))

    def subscribed_skus_map(self, **kwargs):
        return {
            x['skuId']: x['skuPartNumber']
            for x in self.subscribed_skus(params={
                '$select': 'skuId,skuPartNumber',
            })
        }

    def get_groups(self, params=None, **kwargs):
        """
        https://learn.microsoft.com/en-us/graph/api/group-list?view=graph-rest-1.0&tabs=http
        """
        url = f'{self.base_url}/groups'
        return list(self.yield_result(url, params=params, **kwargs))

    def get_group_app_assignments(self, group_id, params=None, **kwargs):
        """
        https://learn.microsoft.com/en-us/graph/api/group-list?view=graph-rest-1.0&tabs=http
        """
        url = f'{self.base_url}/groups/{group_id}/appRoleAssignments'
        return list(self.yield_result(url, params=params, **kwargs))

    def assign_group_to_app(
            self, group_id,
            service_principal_id=None, app_id=None, app_name=None,
            role_id=None, **kwargs):
        principal = None
        if not service_principal_id and (app_id or app_name):
            principal = self.get_service_principal(app_id=app_id, name=app_name)
            service_principal_id = principal['id']
        if not role_id:
            if not principal:
                principal = self.get_service_principal(service_principal_id)
            roles = principal['appRoles']
            for x in roles:
                name = x['displayName'] or ''
                name = name.lower()
                if name == 'user':
                    role_id = x['id']
                    break
            if not role_id and roles:  # pragma: no cover
                role_id = roles[0]['id']
        data = {
            'resourceId': service_principal_id,
            'principalId': group_id,
            'appRoleId': role_id,
        }
        url = f'{self.base_url}/groups/{group_id}/appRoleAssignments'
        return self.post(url, json_data=data)

    def delete_group_from_app(
            self, group_id, assignment_id=None,
            service_principal_id=None, app_id=None, app_name=None,
            **kwargs):
        if not assignment_id:
            assignments = self.get_group_app_assignments(group_id)
            if not service_principal_id and (app_id or app_name):
                p = self.get_service_principal(app_id=app_id, name=app_name)
                service_principal_id = p['id']
            for x in assignments:
                if x['resourceId'] == service_principal_id:
                    assignment_id = x['id']
                    break
        if not assignment_id:  # pragma: no cover
            return True
        url = '/'.join([
            self.base_url,
            'groups', group_id,
            'appRoleAssignments', assignment_id])
        return self.delete(url, raw=True, **kwargs)

    def search_groups(self, display_name=None, params=None, **kwargs):
        """
        https://learn.microsoft.com/en-us/graph/api/group-list?view=graph-rest-1.0&tabs=http#example-4-use-filter-and-top-to-get-one-group-with-a-display-name-that-starts-with-a-including-a-count-of-returned-objects
        """
        params = params or {}
        if display_name:
            params.setdefault('$search', f'"displayName:{display_name}"')
        return self.get_groups(params=params)

    def create_group(
            self,
            display_name=None,
            mail_enabled=False,
            mail_nickname=None,
            security_enabled=True,
            description=None):
        """
        creates a new group using the microsoft graph api
        """
        data = {}
        if display_name:
            data['displayName'] = display_name
        data['mailEnabled'] = mail_enabled
        data['securityEnabled'] = security_enabled
        data['mailNickname'] = mail_nickname or display_name
        if description:  # pragma: no cover
            data['description'] = description
        url = f'{self.base_url}/groups'
        return self.post(url, json_data=data)

    def delete_group(
            self,
            group_id=None):
        """
        deletes group using the microsoft graph api
        """
        url = f'{self.base_url}/groups/{group_id}'
        return self.delete(url, raw=True)

    def get_app(self, object_id=None, app_id=None):
        if object_id:
            url = f'{self.base_url}/applications/{object_id}'
        else:
            url = f"{self.base_url}/applications(appId='{app_id}')"
        return self.get(url)

    def get_apps(self, params=None, **kwargs):
        """
        https://learn.microsoft.com/en-us/graph/api/application-list?view=graph-rest-1.0&tabs=http
        """
        url = f'{self.base_url}/applications'
        return list(self.yield_result(url, params=params, **kwargs))

    def search_apps(self, display_name=None, params=None, **kwargs):
        """
        https://learn.microsoft.com/en-us/graph/api/application-list?view=graph-rest-1.0&tabs=http
        """
        params = params or {}
        if display_name:
            params.setdefault('$search', f'"displayName:{display_name}"')
        return self.get_apps(params=params)

    def get_service_principal(self, object_id=None, app_id=None, name=None,
                              params=None, **kwargs):
        """
        https://learn.microsoft.com/en-us/graph/api/serviceprincipal-get?view=graph-rest-1.0&tabs=http
        """
        if object_id:
            url = f'{self.base_url}/servicePrincipals/{object_id}'
            return self.get(url)
        if app_id:
            url = f"{self.base_url}/servicePrincipals(appId='{app_id}')"
            return self.get(url)
        principals = self.search_service_principals(name)
        if len(principals) == 1:
            return principals[0]
        for x in principals:  # pragma: no cover
            if x['displayName'].lower() == name.lower():
                return x
        return None  # pragma: no cover

    def get_service_principals(self, params=None, **kwargs):
        """
        https://learn.microsoft.com/en-us/graph/api/serviceprincipal-list?view=graph-rest-1.0&tabs=http
        """
        url = f'{self.base_url}/servicePrincipals'
        return list(self.yield_result(url, params=params, **kwargs))

    def search_service_principals(self, display_name, params=None):
        params = params or {}
        if display_name:
            params.setdefault('$search', f'"displayName:{display_name}"')
        return self.get_service_principals(params=params)

    def get_service_principal_id(self, app_id=None, app_name=None, **kwargs):
        principal = self.get_service_principal(app_id=app_id, name=app_name)
        return principal['id']

    def get_app_jobs(self, service_principal_id=None,
                     app_id=None, app_name=None, **kwargs):
        if not service_principal_id:
            service_principal_id = self.get_service_principal_id(
                app_id=app_id,
                app_name=app_name,
            )
        url = posixpath.join(
            self.base_url,
            'servicePrincipals', service_principal_id,
            'synchronization', 'jobs'
        )
        return list(self.yield_result(url, **kwargs))

    def get_app_job_schema(
            self, job_id, service_principal_id=None,
            app_id=None, app_name=None, **kwargs):
        if not service_principal_id:
            service_principal_id = self.get_service_principal_id(
                app_id=app_id,
                app_name=app_name,
            )
        url = posixpath.join(
            self.base_url,
            'servicePrincipals', service_principal_id,
            'synchronization', 'jobs', job_id,
            'schema',
        )
        return self.get(url)

    def provision_group_on_demand(self, group_id, app_name, rule_name=None, **kwargs):
        service_principal = self.get_service_principal(name=app_name)
        service_principal_id = service_principal['id']
        jobs = self.get_app_jobs(service_principal_id=service_principal_id)
        job = jobs[0]
        job_id = job['id']
        schema = self.get_app_job_schema(job_id, service_principal_id)
        rules = schema['synchronizationRules']
        rule_id = 'sesame_meow_cat'
        if rule_name:
            for rule in rules:
                if rule['name'] == rule_name:
                    rule_id = rule['id']
                    break
        else:
            rule_id = rules[0]['id']
        subjects = [{
            'objectId': group_id,
            'objectTypeName': 'Group',
        }]
        data = {
            'parameters': [{
                'subjects': subjects,
                'ruleId': rule_id,
            }],
        }
        url = posixpath.join(
            self.base_url,
            'servicePrincipals', service_principal_id,
            'synchronization', 'jobs', job_id,
            'provisionOnDemand'
        )
        return self.post(url, json_data=data, **kwargs)

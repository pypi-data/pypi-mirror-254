# itential-iag-sdk
Lightweight SDK to simplify the process of interacting with the Itential Automation Gateway API.

This is an beta release. Please ensure the package works as expected in your environment before using it in production as there may still be bugs.
This package uses Pydantic models to validate the input parameters for each API call.

This package was written for Itential Automation Gateway 2023.1. 

## Getting Started
Make sure you have a supported version of Python installed and then create and activate a virtual environment:
```bash
python -m venv venv

source /venv/bin/activate
```
You can install the iag_sdk from Pypi as follows:
```bash
pip install iag-sdk
```
Or you can install it from source as follows:
```bash
git clone https://github.com/awetomate/itential-iag-sdk.git
cd itential-iag-sdk
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Usage
```python
from iag_sdk import Iag

username = "admin@itential"
password = "your_password"
host = "your_server"

iag = Iag(host=host, username=username, password=password, verify=False)

iag.accounts.get_account(name="admin@itential")
#{'email': 'admin@itential.com', 'firstname': None, 'lastname': None, 'username': 'admin@itential'}
```
iag_sdk uses the following default values. You can overwrite any of them during instantiation:
```python
class Iag(ClientBase):
    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        base_url: Optional[str] = "/api/v2.0",
        protocol: Optional[str] = "http",
        port: Optional[Union[int, str]] = 8083,
        verify: Optional[bool] = True,
    ) -> None:
```

The iag_sdk methods are grouped in the same manner as in Itential's API documentation. 
I.e. all API calls related to collections are available under iag.collections. and all API calls related to (Ansible) devices are available under iag.devices.

### Examples
```python
# get the server status
iag.system.get_status()

# list the first 10 Ansible devices that have 'SW' in their hostname
iag.devices.get_devices(limit=10, filter='contains({"name": "SW"})')

# get a specific Ansible device
iag.devices.get_device(name="device1")

# check the state for a specific Ansible device
iag.devices.get_device_state(name="device1")
```

Work with Ansible collections:
```python
# list all collections
iag.collections.get_collections()

# get one collection
iag.collections.get_collection(collection_name="cisco.asa")

# get modules for a specific collection
iag.collections.get_modules(collection_name="cisco.asa")

# refresh collections / perform a collection discovery
iag.collections.refresh()
```
Work with Netmiko:
```python
# IAG native
iag.netmiko.execute_send_command_native(
    host="device1", 
    command_string="show version"
)

# legacy
iag.netmiko.execute_send_command_legacy(
    host="device1", 
    commands=["show version"], 
    device_type="cisco_ftd", 
    username="your_username", 
    password="your_password", 
    port=22
)
```

### The all-purpose 'query' method
The iag_sdk includes a generic 'query' method that can be used for every Itential automation gateway API call. In fact, all the other methods ultimately use the generic 'query' method to send calls to AG.

The query method by default sends GET requests without any data or parameters. 
However, you can use the 'query' method to send get, delete, post, put, and patch requests by changing the 'method' argument. You can also send data by various means (params, data, jsonbody).

The generic 'query' method potentially could come in handy to overcome differences in the API between automation gateway versions. If any of the existing methods don't work with your AG version, try the generic 'query' method as a fallback.

The 'query' method takes the following arguments:
| argument | description |
| --- | --- |
| endpoint | Itential IAG API endpoint. E.g. /devices.|
| method | Optional. API method: get (default),post,put,patch,delete.|
| data | Optional. A dictionary to send as the body.|
| jsonbody | Optional. A JSON object to send as the body.|
| params | Optional. A dictionary to send as URL parameters.|

#### Basic GET call using 'query'
```python
# get the server status
iag.query("/status")
# or to be more explicit
iag.query("/status", method="get")

# get a specific collection
collection_name = "cisco.asa"
iag.query(f"collections/{collection_name}")
# or define the endpoint statically
iag.query("collections/cisco.asa")

# list the first 10 Ansible devices that have 'SW' in their hostname
iag.query("/devices", params={"limit": 10, "filter": 'contains({"name":"SW"})'})
```

#### Basic POST call using 'query'
```python
iag.query("/collections/refresh", method="post")

iag.query("/netmiko/send_command/execute", method="post", jsonbody={"host": "networkdevice", "command_string": "show version"})
```

## List of all modules and methods
### accounts
| methods | description |
| ---- | ---- |
| add_account |Add a new user account.|
| confirm_eula |Confirm EULA for account.|
| delete_account |Delete a user account.|
| get_account |Get information for a user account.|
| get_accounts |Get a list of user accounts.|
| update_account |Update details of a user account.|
| update_password |Update user login credentials.|

### collections
| methods | description |
| ---- | ---- |
| add_collection|Install an Ansible collection from a Galaxy server or from a tarball.|
| delete_module_schema|Remove a schema for a module in the Ansible collection.|
| delete_role_schema|Remove a schema for a role in the Ansible collection.|
| execute_module|Execute a module contained within the Ansible collection.|
| execute_role|Execute a role which is contained within the Ansible collection.|
| get_collection|Get details for an Ansible collection.|
| get_collections|Get list of installed Ansible collections.|
| get_module|Get details for a module in the Ansible collection.|
| get_module_history|Get execution log events for an Ansible collection module.|
| get_module_schema|Get the schema for a module in the Ansible collection.|
| get_modules|Get module list for an Ansible collection.|
| get_role|Get details for a role in the Ansible collection.|
| get_role_history|Get execution log events for an Ansible collection role.|
| get_role_schema|Get the schema for a role in the Ansible collection.|
| get_roles|Get role list for an Ansible collection.|
| refresh|Perform Ansible collection discovery and update internal cache.|
| update_module_schema|Update/Insert a schema document for module in the Ansible collection.|
| update_role_schema|Update/Insert a schema document for role in the Ansible collection.|

### config
| methods | description |
| ---- | ---- |
| get_config|Fetch config value from AG server database.|
| update_config|Update config to AG server database.|

### devices
| methods | description |
| ---- | ---- |
| add_device|Add a new device to Ansible inventory.|
| delete_device|Delete a device from Ansible inventory.|
| get_device|Get information for an Ansible device.|
| get_device_state|Get the connectivity state for an Ansible device.|
| get_device_variable|Get the value of a connection variable for an Ansible device.|
| get_device_variables|Get the connection variables for an Ansible device.|
| get_devices|Get a list of Ansible devices.|
| update_device|Merge or replace the variables for a device in the Ansible inventory.|

### groups
| methods | description |
| ---- | ---- |
| add_group|Add a new Ansible device group.|
| add_group_children|Add new child groups to an Ansible device group.|
| add_group_devices|Add new devices to an Ansible device group.|
| delete_group|Delete an Ansible device group.|
| delete_group_child|Delete a child group from an Ansible device group.|
| delete_group_device|Delete a device from an Ansible device group.|
| get_group|Get information for an Ansible device group.|
| get_group_children|Get a list of child groups for an Ansible device group.|
| get_group_devices|Get the devices for an Ansible device group.|
| get_group_variable|Get the contents of a variable for an Ansible device group.|
| get_group_variables|Get the variables for an Ansible device group.|
| get_groups|Get a list of Ansible device groups.|
| update_group|Update the variables in an Ansbile device group.|

### http_requests
| methods | description |
| ---- | ---- |
| execute_request|Send an HTTP/1.1 request to an inventory device.|
| get_request_history|Get execution log events for an HTTP request.|
| get_request_schema|Get the json schema for http_requests' request endpoint.|

### inventory
| methods | description |
| ---- | ---- |
| add_http_requests_device|Create a device in the http_requests inventory.|
| add_netconf_device|Create a device in the netconf inventory.|
| add_netmiko_device|Create a device in the netmiko inventory|
| delete_http_requests_device|Delete a device from the http_requests inventory.|
| delete_netconf_device|Delete a device from the netconf inventory.|
| delete_netmiko_device|Delete a device from the netmiko inventory.|
| get_http_requests_device|Get information for a device in the http_requests inventory.|
| get_http_requests_device_group|Get information for a device group in the http_requests inventory.|
| get_http_requests_device_group_children|Get a list of child groups in the http_requests inventory device group.|
| get_http_requests_device_group_devices|Get a list of devices in the http_requests inventory device group.|
| get_http_requests_device_groups|Get a list of device groups in http_requests inventory.|
| get_http_requests_devices|Get a list of devices in the http_requests inventory.|
| get_netconf_device|Get information for a device in the netconf inventory.|
| get_netconf_device_group|Get information for a device group in the netconf inventory.|
| get_netconf_device_group_children|Get a list of child groups in the netconf inventory device group.|
| get_netconf_device_group_devices|Get a list of devices in the netconf inventory device group.|
| get_netconf_device_groups|Get a list of device groups in netconf inventory.|
| get_netconf_devices|Get a list of devices in the netconf inventory.|
| get_netmiko_device|Get information for a device in the netmiko inventory.|
| get_netmiko_device_group|Get information for a device group in the netmiko inventory.|
| get_netmiko_device_group_children|Get a list of child groups in the netmiko inventory device group.|
| get_netmiko_device_group_devices|Get a list of devices in the netmiko inventory device group.|
| get_netmiko_device_groups|Get a list of device groups in netmiko inventory.|
| get_netmiko_devices|Get a list of devices in the netmiko inventory.|
| refresh|Perform external inventory discovery and update internal cache.|
| update_http_requests_device|Update a device in the http_requests inventory.|
| update_netconf_device|Update variables for a device in the netconf inventory.|
| update_netmiko_device|Update a device in the netmiko inventory.|

### ldap
| methods | description |
| ---- | ---- |
| test_bind|test LDAP connection|

### modules
| methods | description |
| ---- | ---- |
| delete_module_schema|Remove an Ansible module schema.|
| execute_module|Execute an Ansible module.|
| get_module|Get information for an Ansible module.|
| get_module_history|Get execution log events for an Ansible module.|
| get_module_schema|Get the schema for an Ansible module.|
| get_modules|Get a list of Ansible modules.|
| refresh|Perform Ansible module discovery and update internal cache.|
| update_module_schema|Update/Insert an Ansible module schema document.|

### netconf
|netconf||
| ---- | ---- |
| execute_get_config|Retrieve configuration from a device using the NETCONF protocol|
| execute_rpc|Execute proprietary operations on a device using the NETCONF protocol.|
| execute_set_config|Configure a device using the NETCONF protocol|
| get_history|Get execution log events for Netconf command.|

### netmiko
| methods | description |
| ---- | ---- |
| execute_send_command_legacy |Wrapper of netmiko send_command|
| execute_send_command_native |IAG Native Netmiko send_command.|
| execute_send_config_set_legacy |Wrapper of netmiko send_config_set|
| execute_send_config_set_native |IAG Native Netmiko send_config_set.|
| get_command_schema |Get IAG Native Netmiko command schema.|
| get_send_command_history|Get execution log events for the Netmiko send_command.|
| get_send_config_set_history|Get execution log events for Netmiko send_config_set.|

### nornir
| methods | description |
| ---- | ---- |
| delete_module_schema|Remove a Nornir module schema.|
| execute_module|Execute a Nornir module.|
| get_module|Get Nornir module information.|
| get_module_history|Get execution log events for a Nornir module.|
| get_module_schema|Get the schema for a Nornir module.|
| get_modules|Get a list of Nornir modules.|
| refresh|Perform Nornir module discovery and update internal cache.|
| update_module_schema|Update/Insert a Nornir module schema document.|

### password_reset
| methods | description |
| ---- | ---- |
| reset_password|Reset password for user on the AG server.|
| update_change_flag|Update the password change flag to false on the AG server.|
| update_password|Update password for user on the AG server.|
| update_security_questions|Update security questions and answers for user on the AG server.|
| validate_password_change|Validate if password is changed in the AG server.|

### playbooks
| methods | description |
| ---- | ---- |
| delete_playbook_schema|Remove an Ansible playbook schema.|
| execute_playbook|Execute an Ansible playbook.|
| get_playbook|Get information for an Ansible playbook.|
| get_playbook_schema|Get the schema for an Ansible playbook.|
| get_playbooks|Get a list of Ansible playbooks.|
| get_playook_history|Get execution log events for an Ansible playbook.|
| refresh|Perform Ansible playbook discovery and update internal cache.|
| update_playbook_schema|Update/Insert an Ansible playbook schema document.|

### pronghorn
| methods | description |
| ---- | ---- |
| get_pronghorn|Get pronghorn.json for the AG server.|

### rbac
| methods | description |
| ---- | ---- |
| add_group|Add a new RBAC group|
| add_group_roles|Add new roles to the RBAC group.|
| add_group_users|Add new users to the RBAC group.|
| delete_group|Delete an RBAC group.|
| delete_group_role|Delete a role from the RBAC group.|
| delete_group_user|Delete a user from the RBAC group.|
| get_group|Get information for an RBAC group.|
| get_group_roles|Get roles for an RBAC group.|
| get_group_users|Get users for an RBAC group.|
| get_groups|Get a list of RBAC groups.|
| get_role|Get information for an RBAC role.|
| get_roles|Get a list of RBAC roles.|
| get_user_groups|Get RBAC group information for a user.|
| get_user_roles|Get RBAC role information for a user.|
| update_group|Update an RBAC group.|

### roles
| methods | description |
| ---- | ---- |
| delete_role_schema|Remove an Ansible role schema.|
| execute_role|Execute an Ansible role.|
| get_role|Get information for an Ansible role.|
| get_role_history|Get execution log events for an Ansible role.|
| get_role_schema|Get the schema for an Ansible role.|
| get_roles|Get a list of Ansible roles.|
| refresh|Perform Ansible role discovery and update internal cache.|
| update_role_schema|Update/Insert an Ansible role schema document.|

### scripts
| methods | description |
| ---- | ---- |
| delete_script_schema|Remove a script schema.|
| execute_script|Execute a script.|
| get_script|Get script information.|
| get_script_history|Get execution log events for a script.|
| get_script_schema|Get the schema for a script.|
| get_scripts|Get a list of scripts.|
| refresh|Perform script discovery and update internal cache.|
| update_script_schema|Update/Insert a script schema document.|

### secrets
| methods | description |
| ---- | ---- |
| add_secret|Add a new Hashicorp Vault secret.|
| delete_secret|Delete a Hashicorp Vault secret.|
| get_secret|Get a list of Hashicorp Vault secrets.|
| update_secret|Update a Hashicorpy Vault secret.|

### security_questions
| methods | description |
| ---- | ---- |
| get_security_questions|Get security questions for the AG server.|
| get_security_questions_user|Get security questions for email id on the AG server.|
| validate_security_answers_user|Validate security answers for email id on the AG server.|

### system
| methods | description |
| ---- | ---- |
| get_audit_log|Get execution history payload.|
| get_audit_logs|Retrieve execution audit log persisted in the database.|
| get_health|Determine if AG server is up and running (/poll).|
| get_openapi_spec|Get the current OpenAPI spec from the running instance of IAG|
| get_status|Get the AG server status (version, ansible version, etc).|

### terraforms
| methods | description |
| ---- | ---- |
| delete_module_schema|Remove a Terraform module schema.|
| execute_terraform_apply|Apply the configuration of a Terraform module|
| execute_terraform_destroy|Destroy the resources of a Terraform module.|
| execute_terraform_init|Initialize the providers of a Terraform module.|
| execute_terraform_plan|Plan the execution of a Terraform module.|
| execute_terraform_validate|Validate the configuration of a Terraform module.|
| get_module|Get information on a Terraform module.|
| get_module_history|Get execution log events for a Terraform module.|
| get_module_schema|Get the schema for a Terraform module.|
| get_modules|Get list of Terraform modules.|
| refresh|Perform Terraform discovery and update internal cache.|
| update_module_schema|Update/Insert a Terraform schema document.|

### user_schema
| methods | description |
| ---- | ---- |
| delete_schema|Remove a user schema.|
| update_schema|Update/Insert a user schema document.|

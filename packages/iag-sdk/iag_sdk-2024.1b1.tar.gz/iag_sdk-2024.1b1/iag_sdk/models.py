from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field, RootModel, StringConstraints, model_validator
from typing_extensions import Annotated


class Detail(Enum):
    full = "full"
    summary = "summary"


class DeviceType(Enum):
    a10 = "a10"
    accedian = "accedian"
    adtran_os = "adtran_os"
    alcatel_aos = "alcatel_aos"
    alcatel_sros = "alcatel_sros"
    allied_telesis_awplus = "allied_telesis_awplus"
    apresia_aeos = "apresia_aeos"
    arista_eos = "arista_eos"
    aruba_os = "aruba_os"
    aruba_osswitch = "aruba_osswitch"
    aruba_procurve = "aruba_procurve"
    avaya_ers = "avaya_ers"
    avaya_vsp = "avaya_vsp"
    broadcom_icos = "broadcom_icos"
    brocade_fos = "brocade_fos"
    brocade_fastiron = "brocade_fastiron"
    brocade_netiron = "brocade_netiron"
    brocade_nos = "brocade_nos"
    brocade_vdx = "brocade_vdx"
    brocade_vyos = "brocade_vyos"
    checkpoint_gaia = "checkpoint_gaia"
    calix_b6 = "calix_b6"
    cdot_cros = "cdot_cros"
    centec_os = "centec_os"
    ciena_saos = "ciena_saos"
    cisco_asa = "cisco_asa"
    cisco_ftd = "cisco_ftd"
    cisco_ios = "cisco_ios"
    cisco_nxos = "cisco_nxos"
    cisco_s300 = "cisco_s300"
    cisco_tp = "cisco_tp"
    cisco_wlc = "cisco_wlc"
    cisco_xe = "cisco_xe"
    cisco_xr = "cisco_xr"
    cloudgenix_ion = "cloudgenix_ion"
    coriant = "coriant"
    dell_dnos9 = "dell_dnos9"
    dell_force10 = "dell_force10"
    dell_os6 = "dell_os6"
    dell_os9 = "dell_os9"
    dell_os10 = "dell_os10"
    dell_powerconnect = "dell_powerconnect"
    dell_isilon = "dell_isilon"
    dlink_ds = "dlink_ds"
    endace = "endace"
    eltex = "eltex"
    eltex_esr = "eltex_esr"
    enterasys = "enterasys"
    ericsson_ipos = "ericsson_ipos"
    extreme = "extreme"
    extreme_ers = "extreme_ers"
    extreme_exos = "extreme_exos"
    extreme_netiron = "extreme_netiron"
    extreme_nos = "extreme_nos"
    extreme_slx = "extreme_slx"
    extreme_vdx = "extreme_vdx"
    extreme_vsp = "extreme_vsp"
    extreme_wing = "extreme_wing"
    f5_ltm = "f5_ltm"
    f5_tmsh = "f5_tmsh"
    f5_linux = "f5_linux"
    flexvnf = "flexvnf"
    fortinet = "fortinet"
    generic = "generic"
    generic_termserver = "generic_termserver"
    hp_comware = "hp_comware"
    hp_procurve = "hp_procurve"
    huawei = "huawei"
    huawei_smartax = "huawei_smartax"
    huawei_olt = "huawei_olt"
    huawei_vrpv8 = "huawei_vrpv8"
    ipinfusion_ocnos = "ipinfusion_ocnos"
    juniper = "juniper"
    juniper_junos = "juniper_junos"
    juniper_screenos = "juniper_screenos"
    keymile = "keymile"
    keymile_nos = "keymile_nos"
    linux = "linux"
    mikrotik_routeros = "mikrotik_routeros"
    mikrotik_switchos = "mikrotik_switchos"
    mellanox = "mellanox"
    mellanox_mlnxos = "mellanox_mlnxos"
    mrv_lx = "mrv_lx"
    mrv_optiswitch = "mrv_optiswitch"
    netapp_cdot = "netapp_cdot"
    netgear_prosafe = "netgear_prosafe"
    netscaler = "netscaler"
    nokia_sros = "nokia_sros"
    oneaccess_oneos = "oneaccess_oneos"
    ovs_linux = "ovs_linux"
    paloalto_panos = "paloalto_panos"
    pluribus = "pluribus"
    quanta_mesh = "quanta_mesh"
    rad_etx = "rad_etx"
    raisecom_roap = "raisecom_roap"
    ruckus_fastiron = "ruckus_fastiron"
    ruijie_os = "ruijie_os"
    sixwind_os = "sixwind_os"
    sophos_sfos = "sophos_sfos"
    supermicro_smis = "supermicro_smis"
    tplink_jetstream = "tplink_jetstream"
    ubiquiti_edge = "ubiquiti_edge"
    ubiquiti_edgerouter = "ubiquiti_edgerouter"
    ubiquiti_edgeswitch = "ubiquiti_edgeswitch"
    ubiquiti_unifiswitch = "ubiquiti_unifiswitch"
    vyatta_vyos = "vyatta_vyos"
    vyos = "vyos"
    watchguard_fireware = "watchguard_fireware"
    zte_zxros = "zte_zxros"
    yamaha = "yamaha"


class Order(Enum):
    ascending = "ascending"
    descending = "descending"


class Method(Enum):
    get = "get"
    GET = "GET"
    options = "options"
    OPTIONS = "OPTIONS"
    head = "head"
    HEAD = "HEAD"
    post = "post"
    POST = "POST"
    put = "put"
    PUT = "PUT"
    patch = "patch"
    PATCH = "PATCH"
    delete = "delete"
    DELETE = "DELETE"


class NetconfCommands(Enum):
    set_config = "set_config"
    get_config = "get_config"
    exec_rpc = "exec_rpc"


class NetmikoCommands(Enum):
    send_command = "send_command"
    send_config_set = "send_config_set"


class NetconfTargetDatastoreGet(Enum):
    candidate = "candidate"
    running = "running"
    startup = "startup"


class NetconfTargetDatastoreSet(Enum):
    candidate = "candidate"
    running = "running"


class Platform(Enum):
    default = "default"
    alu = "alu"
    csr = "csr"
    ericsson = "ericsson"
    h3c = "h3c"
    huawei = "huawei"
    huaweiyang = "huaweiyang"
    iosxe = "iosxe"
    iosxr = "iosxr"
    junos = "junos"
    nexus = "nexus"
    sros = "sros"


class UpdateMerged(Enum):
    patch = "patch"
    put = "put"


class AccountModel(BaseModel):
    email: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    username: str


class AccountParameters(BaseModel):
    email: str
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    password: str
    username: str

class AccountUpdateParameters(BaseModel):
    email: str
    firstname: str
    lastname: str


class AccountUpdatePassword(BaseModel):
    new_password: str
    old_password: str

    @model_validator(mode="after")
    def check_passwords_do_not_match(self) -> "AccountUpdatePassword":
        pw1 = self.new_password
        pw2 = self.old_password
        if pw1 is not None and pw2 is not None and pw1 == pw2:
            raise ValueError("New password cannot be same as old password!")
        return self


class ConfigParameters(BaseModel):
    class Config:
        extra = "forbid"

    ansible_debug: Optional[bool] = None
    ansible_enabled: Optional[bool] = None
    collection_path: Optional[list[str]] = Field(None, min_items=0)
    extended_device_role_path: Optional[list[str]] = Field(None, min_items=0)
    http_requests_enabled: Optional[bool] = None
    inventory_file: Optional[str] = None
    ldap_always_search_bind: Optional[bool] = None
    ldap_auth_enabled: Optional[bool] = None
    ldap_base_dn: Optional[str] = None
    ldap_bind_user_dn: Optional[str] = None
    ldap_bind_user_password: Optional[str] = None
    ldap_ca_certs_file: Optional[str] = None
    ldap_group_dn: Optional[str] = None
    ldap_group_members_attr: Optional[str] = None
    ldap_group_search_filter: Optional[str] = None
    ldap_group_search_scope: Optional[str] = None
    ldap_secure_enabled: Optional[bool] = None
    ldap_secure_validation_enabled: Optional[bool] = None
    ldap_secure_validation_tls_version: Optional[str] = None
    ldap_server: Optional[str] = None
    ldap_user_dn: Optional[str] = None
    ldap_user_login_attr: Optional[str] = None
    ldap_user_rdn_attr: Optional[str] = None
    ldap_user_search_filter: Optional[str] = None
    ldap_user_search_scope: Optional[str] = None
    module_path: Optional[list[str]] = Field(None, min_items=0)
    netconf_enabled: Optional[bool] = None
    netmiko_enabled: Optional[bool] = None
    no_cleanup: Optional[bool] = None
    nornir_config_file: Optional[str] = None
    nornir_enabled: Optional[bool] = None
    nornir_module_path: Optional[list[str]] = Field(None, min_items=0)
    nornir_module_recursive: Optional[bool] = None
    playbook_path: Optional[list[str]] = Field(None, min_items=0)
    playbook_recursive: Optional[bool] = None
    process_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    repos_enabled: Optional[bool] = None
    repos_path: Optional[str] = None
    role_path: Optional[list[str]] = Field(None, min_items=0)
    script_path: Optional[list[str]] = Field(None, min_items=0)
    script_recursive: Optional[bool] = None
    scripts_enabled: Optional[bool] = None
    terraform_enabled: Optional[bool] = None
    terraform_path: Optional[list[str]] = Field(None, min_items=0)
    terraform_recursive: Optional[bool] = None
    vault_access_token: Optional[str] = None
    vault_ca_file: Optional[str] = None
    vault_cert_verification: Optional[bool] = None
    vault_client_cert_file: Optional[str] = None
    vault_client_key_file: Optional[str] = None
    vault_enabled: Optional[bool] = None
    vault_mount_point: Optional[str] = None
    vault_password_file: Optional[str] = None
    vault_server: Optional[str] = None


class DeviceAddParameters(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1)]
    variables: dict[str, Any]


class DeviceUpdateParameters(BaseModel):
    variables: dict[str, Any]


class InventoryHttpAddVariables(BaseModel):
    class Config:
        extra = "allow"

    base_url: str = Field(..., example="jsonplaceholder.typicode.com")
    port: Optional[int] = Field(None, example="443")
    protocol: str = Field(..., example="https")


class InventoryHttpAddParameters(BaseModel):
    class Config:
        extra = "forbid"

    name: Annotated[str, StringConstraints(min_length=1)] = Field(..., example="IOS")
    variables: InventoryHttpAddVariables


class InventoryHttpUpdateVariables(BaseModel):
    class Config:
        extra = "allow"

    base_url: Optional[str] = Field(None, example="jsonplaceholder.typicode.com")
    port: Optional[int] = Field(None, example="443")
    protocol: Optional[str] = Field(None, example="https")


class InventoryHttpUpdateParameters(BaseModel):
    class Config:
        extra = "forbid"

    name: Optional[Annotated[str, StringConstraints(min_length=1)]] = Field(..., example="IOS")
    variables: Optional[InventoryHttpUpdateVariables]


class InventoryNetconfAddVariables(BaseModel):
    class Config:
        extra = "allow"
        use_enum_values = True

    host: Optional[str] = None
    password: Optional[str] = None
    platform: Optional[Platform] = None
    port: Optional[int] = None
    timeout: Optional[int] = None
    username: Optional[str] = None


class InventoryNetconfAddParameters(BaseModel):
    class Config:
        extra = "forbid"

    name: Annotated[str, StringConstraints(min_length=1)]
    variables: InventoryNetconfAddVariables


class InventoryNetconfUpdateVariables(BaseModel):
    class Config:
        extra = "forbid"
        use_enum_values = True

    host: str
    password: str
    platform: Platform
    port: Optional[int] = None
    timeout: Optional[int] = None
    username: str


class InventoryNetconfUpdateParameters(BaseModel):
    class Config:
        extra = "forbid"

    name: Optional[Annotated[str, StringConstraints(min_length=1)]]
    variables: Optional[InventoryNetconfUpdateVariables]


class InventoryNetmikoAddVariables(BaseModel):
    class Config:
        extra = "forbid"

    allow_agent: Optional[bool] = Field(None, description="Enable use of SSH key-agent.")
    allow_auto_change: Optional[bool] = Field(None, description="Allow automatic configuration changes for terminal settings. (default to False)",)
    alt_host_keys: Optional[bool] = Field(None, description="If `True` host keys will be loaded from the file specified in",)
    alt_key_file: Optional[str] = Field(None, description="SSH host key file to use (if alt_host_keys=True).")
    auth_timeout: Optional[float] = Field(None, description="Set a timeout (in seconds) to wait for an authentication response.",)
    auto_connect: Optional[bool] = Field(None, description="Control whether Netmiko automatically establishes the connection as part of the object creation (default to True).",)
    banner_timeout: Optional[float] = Field(None, description="Set a timeout to wait for the SSH banner (pass to Paramiko).")
    default_enter: Optional[str] = Field(None, description="Character(s) to send to correspond to enter key (default to \\n).",)
    device_type: DeviceType = Field(..., description="Netmiko supported device type", example="cisco_ios")
    enable: Optional[bool] = Field(False, description="Enter enable mode.")
    encoding: Optional[str] = Field(None, description="Encoding to be used when writing bytes to the output channel. (default to ascii)",)
    fast_cli: Optional[bool] = Field(None, description="Provide a way to optimize for performance. Converts select_delay_factor to select smallest of global and specific. Sets default global_delay_factor to .1 (default to False)",)
    global_delay_factor: Optional[int] = Field(None, description="Multiplication factor affecting Netmiko delays (default to 1).",)
    host: Annotated[str, StringConstraints(min_length=1)] = Field(..., description="hostname or IP address of the netmiko device")
    keepalive: Optional[int] = Field(None, description="Send SSH keepalive packets at a specific interval, in seconds. Currently defaults to 0, for backwards compatibility (it will not attempt to keep the connection alive).",)
    key_file: Optional[str] = Field(None, description="Filename path of the SSH key file to use.")
    passphrase: Optional[str] = Field(None, description="Passphrase to use for encrypted key; password will be used for key decryption if not specified.",)
    password: Optional[str] = Field(None, description="Password to authenticate against target device if required.", example="password",)
    port: Optional[int] = Field(None, description="The destination port used to connect to the target device.", example="22",)
    response_return: Optional[str] = Field(None,description="Character(s) to use in normalized return data to represent enter key (default to \\n)",)
    secret: Optional[str] = Field(None, description="The enable password if target device requires one.")
    session_log: Optional[str] = Field(None, description="File path or BufferedIOBase subclass object to write the session log to.",)
    session_log_file_mode: Optional[str] = Field(None, description="write or append for session_log file mode (default to write)")
    session_log_record_writes: Optional[bool] = Field(None, description="The session log generally only records channel reads due to eliminate command duplication due to command echo. You can enable this if you want to record both channel reads and channel writes in the log (default to False).",)
    session_timeout: Optional[float] = Field(None, description="Set a timeout for parallel requests.")
    ssh_config_file: Optional[str] = Field(None, description="File name of OpenSSH configuration file.")
    ssh_strict: Optional[bool] = Field(None, description="Automatically reject unknown SSH host keys (default to False, which means unknown SSH host keys will be accepted)",)
    system_host_keys: Optional[bool] = Field(None, description="Load host keys from the users known_hosts file.")
    timeout: Optional[float] = Field(None, description="Connection timeout.")
    use_keys: Optional[bool] = Field(None, description="Connect to target device using SSH keys.")
    username: Optional[str] = Field(None, description="Username to authenticate against target device if required.", example="username",)
    verbose: Optional[bool] = Field(None, description="Enable additional messages to standard output.")


class InventoryNetmikoAddParameters(BaseModel):
    class Config:
        extra = "forbid"

    name: Annotated[str, StringConstraints(min_length=1)] = Field(..., example="host or ip of device")
    variables: InventoryNetmikoAddVariables


class InventoryNetmikoUpdateVariables(BaseModel):
    class Config:
        extra = "forbid"

    allow_agent: Optional[bool] = Field(None, description="Enable use of SSH key-agent.")
    allow_auto_change: Optional[bool] = Field(None, description="Allow automatic configuration changes for terminal settings. (default to False)",)
    alt_host_keys: Optional[bool] = Field(None, description="If `True` host keys will be loaded from the file specified in",)
    alt_key_file: Optional[str] = Field(None, description="SSH host key file to use (if alt_host_keys=True).")
    auth_timeout: Optional[float] = Field(None, description="Set a timeout (in seconds) to wait for an authentication response.",)
    auto_connect: Optional[bool] = Field(None, description="Control whether Netmiko automatically establishes the connection as part of the object creation (default to True).",)
    banner_timeout: Optional[float] = Field(None, description="Set a timeout to wait for the SSH banner (pass to Paramiko).")
    default_enter: Optional[str] = Field(None, description="Character(s) to send to correspond to enter key (default to \\n).",)
    device_type: Optional[DeviceType] = Field(..., description="Netmiko supported device type", example="cisco_ios")
    enable: Optional[bool] = Field(False, description="Enter enable mode.")
    encoding: Optional[str] = Field(None, description="Encoding to be used when writing bytes to the output channel. (default to ascii)",)
    fast_cli: Optional[bool] = Field(None, description="Provide a way to optimize for performance. Converts select_delay_factor to select smallest of global and specific. Sets default global_delay_factor to .1 (default to False)",)
    global_delay_factor: Optional[int] = Field(None, description="Multiplication factor affecting Netmiko delays (default to 1).",)
    host: Optional[Annotated[str, StringConstraints(min_length=1)]] = Field(..., description="hostname or IP address of the netmiko device")
    keepalive: Optional[int] = Field(None, description="Send SSH keepalive packets at a specific interval, in seconds. Currently defaults to 0, for backwards compatibility (it will not attempt to keep the connection alive).",)
    key_file: Optional[str] = Field(None, description="Filename path of the SSH key file to use.")
    passphrase: Optional[str] = Field(None, description="Passphrase to use for encrypted key; password will be used for key decryption if not specified.",)
    password: Optional[str] = Field(None, description="Password to authenticate against target device if required.", example="password",)
    port: Optional[int] = Field(None, description="The destination port used to connect to the target device.", example="22",)
    response_return: Optional[str] = Field(None,description="Character(s) to use in normalized return data to represent enter key (default to \\n)",)
    secret: Optional[str] = Field(None, description="The enable password if target device requires one.")
    session_log: Optional[str] = Field(None, description="File path or BufferedIOBase subclass object to write the session log to.",)
    session_log_file_mode: Optional[str] = Field(None, description="write or append for session_log file mode (default to write)")
    session_log_record_writes: Optional[bool] = Field(None, description="The session log generally only records channel reads due to eliminate command duplication due to command echo. You can enable this if you want to record both channel reads and channel writes in the log (default to False).",)
    session_timeout: Optional[float] = Field(None, description="Set a timeout for parallel requests.")
    ssh_config_file: Optional[str] = Field(None, description="File name of OpenSSH configuration file.")
    ssh_strict: Optional[bool] = Field(None, description="Automatically reject unknown SSH host keys (default to False, which means unknown SSH host keys will be accepted)",)
    system_host_keys: Optional[bool] = Field(None, description="Load host keys from the users known_hosts file.")
    timeout: Optional[float] = Field(None, description="Connection timeout.")
    use_keys: Optional[bool] = Field(None, description="Connect to target device using SSH keys.")
    username: Optional[str] = Field(None, description="Username to authenticate against target device if required.", example="username",)
    verbose: Optional[bool] = Field(None, description="Enable additional messages to standard output.")



class InventoryNetmikoUpdateParameters(BaseModel):
    class Config:
        extra = "forbid"

    name: Optional[Annotated[str, StringConstraints(min_length=1)]] = Field(..., example="IOS")
    variables: Optional[InventoryNetmikoUpdateVariables]


class GroupAddParameters(BaseModel):
    childGroups: Optional[list[str]] = None
    devices: list[str]
    name: Annotated[str, StringConstraints(min_length=1)]
    variables: Optional[dict[str, Any]] = None


class GroupUpdateParameters(BaseModel):
    variables: dict[str, Any]


class GroupChildren(RootModel):
    root: list[str]


class GroupDevices(RootModel):
    root: list[str]


class Auth(BaseModel):
    class Config:
        extra = "forbid"

    password: str = Field(..., example="password")
    username: str = Field(..., example="username")


class Timeout(BaseModel):
    class Config:
        extra = "forbid"

    connect: Optional[str] = Field(None, example="3.05")
    read: Optional[str] = Field(None, example="27")


class HttpRequestsExecuteParameters(BaseModel):
    class Config:
        extra = "forbid"
        use_enum_values = True

    allow_redirects: Optional[bool] = Field(True, description="A flag which enables or disables HTTP redirection.")
    auth: Optional[Auth] = Field(None, description="Keys/values to send as the username and password for Basic Authentication.", example={"password": "password", "username": "username"},)
    cookies: Optional[dict[str, Any]] = Field(None, description="Keys/values to send as the request's cookies.", example={})
    data: Optional[dict[str, Any]] = Field(None, description="Keys/values to send as the request's body.", example={})
    endpoint: str = Field(..., description="The endpoint to append to the url built from your inventory/host.", example="/api/v2/todos",)
    headers: Optional[dict[str, Any]] = Field(None, description="Keys/values to send as the request's HTTP headers.", example={"content-type": "application/json"},)
    host: str = Field(..., description="The name of a host to execute against.", example="IOS")
    method: Method = Field(..., description="Request method - one of GET, OPTIONS, HEAD, POST, PUT, PATCH, DELETE", example="GET",)
    params: Optional[dict[str, Any]] = Field(None, description="Keys/values to convert into the request's query string.", example={"id": "1"},)
    proxies: Optional[dict[str, Any]] = Field(None, description="The keys/values which describe proxies to use for the request.", example={"http": "http://10.0.0.1:8080", "https": "http://10.0.0.1:4343"},)
    timeout: Optional[Timeout] = Field(None, description="The connect and read timeouts for the request. See: https://docs.python-requests.org/en/latest/user/advanced/#timeouts", example={"connect": "3.05", "read": "27"},)
    verify: Optional[bool] = Field(True, description="A flag which enables or disables TLS certificate verification.")


class PathParam(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1)]


class PathParams(PathParam):
    module: Annotated[str, StringConstraints(min_length=1)]


class QueryParams(BaseModel):
    class Config:
        use_enum_values = True

    offset: Optional[int] = Field(None, description="The number of items to skip before starting to collect the result set.",)
    limit: Optional[int] = Field(None, description="The number of items to return.")
    order: Optional[Order] = Field("descending", description="Sort indication. Available values : ascending, descending",)


class QueryParamsFilter(QueryParams):
    filter: Optional[str] = Field(None, description='Response filter function with JSON name/value pair argument, i.e., contains({"username":"admin"}) Valid filter functions - contains, equals, startswith, endswith',)


class QueryParamsDetail(QueryParamsFilter):
    detail: Optional[Detail] = "summary"


class ServerParams(BaseModel):
    auth_url: Optional[str] = None
    password: Optional[str] = None
    token: Optional[str] = None
    url: Optional[str] = None
    username: Optional[str] = None


class UpdateMethod(BaseModel):
    class Config:
        use_enum_values = True
    
    method: UpdateMerged


class CollectionInstallParameters(BaseModel):
    filename: Optional[str] = Field(None, description="Path to package if installing locally")
    force: Optional[bool] = Field(None, description="Add force flag to force package installation (when collection is already installed and you want to upgrade or downgrade version)",)
    package_name: Optional[str] = Field(None, description="Name of package to install if installing from Galaxy server")
    server_params: Optional[ServerParams] = Field(None, description="Parameters for connection to Galaxy server")
    version: Optional[str] = Field(None, description="Version of Collection to be installed")


class ModuleExecuteParameters(BaseModel):
    args: dict[str, Any]
    groups: Optional[list[str]] = None
    hosts: Optional[list[str]] = None
    provider_required: Optional[bool] = Field(None, description="Enable/disable automation of provider object")
    strict_args: Optional[bool] = Field(None, description="Override global strict args setting")
    template: Optional[str] = Field(None, description="TextFSM template")


class RoleExecuteParameters(BaseModel):
    args: dict[str, Any]
    groups: Optional[list[str]] = None
    hosts: Optional[list[str]] = None
    strict_args: Optional[bool] = Field(None, description="Override global strict args setting")
    template: Optional[str] = Field(None, description="TextFSM template")


class Schema(BaseModel):
    properties: Optional[dict[str, Any]] = None
    required: Optional[list[str]] = None
    title: Optional[str] = None
    type: Optional[str] = None


class NetconfRpcParameters(BaseModel):
    host: str = Field(..., description="Name of device in netconf inventory to execute against.")
    rpc: str = Field(..., description="Name of RPC operation to be executed on the remote device.")


class NetconfGetConfigParameters(BaseModel):
    class Config:
        use_enum_values = True

    filter: Optional[str] = Field(None, description="An xml string which acts as a filter to restrict the data retrieved from the device",)
    host: str = Field(..., description="Either hostname or ip address accepted", example="10.0.0.1")
    lock: Optional[bool] = Field(False, description="Lock the datastore specified in 'target_datastore'")
    target_datastore: Optional[NetconfTargetDatastoreGet] = Field("running", description="Name of the datastore from which to retrieve configuration data",)


class NetconfSetConfigParameters(BaseModel):
    config_content: str = Field(..., description="The configuration data in xml string format")
    host: str = Field(..., description="Either hostname or ip address accepted", example="10.0.0.1")
    lock: Optional[bool] = Field(True, description="Lock the datastore specified in 'target_datastore'")
    save_to_startup: Optional[bool] = Field(False, description="Save the config updates of the datastore specified in 'target_datastore' to the startup-config",)
    target_datastore: Optional[NetconfTargetDatastoreSet] = Field("candidate", description="Name of the configuration datastore to be updated")
    validate_: Optional[bool] = Field(False, alias="validate", description="Validate the config updates of the datastore specified in 'target_datastore'",)


class NetconfGetHistoryParameters(BaseModel):
    class Config:
        use_enum_values = True

    netconf_command: NetconfCommands = Field(..., description="Name of netconf command. Available values : set_config, get_config, exec_rpc")


class NetmikoConnectionOptions(BaseModel):
    device_type: DeviceType = Field(..., example='cisco_ios')
    password: Optional[str] = Field(None, example='password')
    port: Optional[int] = Field(None, example='22')
    username: Optional[str] = Field(None, example='username')


class NetmikoSendCommandLegacyParameters(BaseModel):
    commands: list[str] = Field(..., example=['show version', 'show ip int brief'])
    connection_options: NetmikoConnectionOptions
    host: str = Field(..., example='10.0.0.1')


class NetmikoSendCommandNativeParameters(BaseModel):
    cmd_verify: Optional[bool] = Field(None, description="Verify command echo before proceeding (default to True).")
    command_string: str = Field(..., description="The command to be executed on the remote device", example="show version",)
    delay_factor: Optional[int] = Field(None, description="Multiplying factor used to adjust delays (default to 1).")
    expect_string: Optional[str] = Field(None, description="Regular expression pattern to use for determining end of output. If left blank will default to being based on router prompt.",)
    host: str = Field(..., description="netmiko device name", example="cisco_device")
    max_loops: Optional[int] = Field(None, description="Controls wait time in conjunction with delay_factor. Will default to be based upon the timeout in netmiko device",)
    normalize: Optional[bool] = Field(None, description="Ensure the proper enter is sent at end of command (default to True).",)
    strip_command: Optional[bool] = Field(None, description="Remove the echo of the command from the output (default to True).",)
    strip_prompt: Optional[bool] = Field(None, description="Remove the trailing router prompt from the output (default to True).",)
    textfsm_template: Optional[str] = Field(None, description="Name of template to parse output with; can be fully qualified path, relative path, or name of file in current directory. (default to None).",)
    ttp_template: Optional[str] = Field(None, description="Name of template to parse output with; can be fully qualified path, relative path, or name of file in current directory. (default to None).",)
    use_genie: Optional[bool] = Field(None, description="Process command output through PyATS/Genie parser (default to False).",)
    use_textfsm: Optional[bool] = Field(None, description="Process command output through TextFSM template (default to False).",)
    use_ttp: Optional[bool] = Field(None, description="Process command output through TTP template (default to False).",)


class NetmikoSendConfigLegacyParameters(BaseModel):
    config_commands: list[str] = Field(
        ...,
        example=[
            "hostname ROUTER1",
            "interface Ethernet 1/1",
            "  description ROUTER1 Uplink",
        ],
    )
    connection_options: NetmikoConnectionOptions
    host: str = Field(..., example="10.0.0.1")


class NetmikoSendConfigNativeParameters(BaseModel):
    cmd_verify: Optional[bool] = Field(None, description="Whether or not to verify command echo for each command in config_set",)
    config_commands: list[str] = Field(
        ...,
        description="Multiple configuration commands to be sent to the device",
        example=[
            "hostname ROUTER1",
            "interface Ethernet 1/1",
            "  description ROUTER1 Uplink",
        ],
    )
    config_mode_command: Optional[str] = Field(None, description="The command to enter into config mode")
    delay_factor: Optional[int] = Field(None, description="Factor to adjust delays")
    enter_config_mode: Optional[bool] = Field(None, description="Do you enter config mode before sending config commands")
    error_pattern: Optional[str] = Field(None, description="Regular expression pattern to detect config errors in the output.",)
    exit_config_mode: Optional[bool] = Field(None, description="Determines whether or not to exit config mode after complete")
    host: str = Field(..., description="Either hostname or ip accepted", example="device_name")
    max_loops: Optional[int] = Field(None, description="Controls wait time in conjunction with delay_factor (default to 150)",)
    strip_command: Optional[bool] = Field(None, description="Determines whether or not to strip the command")
    strip_prompt: Optional[bool] = Field(None, description="Determines whether or not to strip the prompt")


class NetmikoGetCommandSchema(BaseModel):
    class Config:
        use_enum_values = True
    
    netmiko_command: NetmikoCommands


class NornirModuleExecuteParameters(BaseModel):
    args: dict[str, Any]
    env: Optional[dict[str, Any]] = None
    groups: Optional[list[str]] = None
    hosts: Optional[list[str]] = None
    strict_args: Optional[bool] = Field(None, description="Override global strict args setting")


class PasswordResetParameters(BaseModel):
    email: str
    new_password: str
    security_ques1: str
    security_ques1_ans: str
    security_ques2: str
    security_ques2_ans: str
    temp_password: Annotated[str, StringConstraints(min_length=1)]
    username: str


class PasswordUpdateParameters(BaseModel):
    email: str
    password: str
    security_ques1: Optional[str] = None
    security_ques1_ans: Optional[str] = None
    security_ques2: Optional[str] = None
    security_ques2_ans: Optional[str] = None
    username: str

class PasswordUpdateQuestionsParameters(BaseModel):
    security_ques1: str
    security_ques1_ans: str
    security_ques2: str
    security_ques2_ans: str
    username: str


class PlaybookExecuteParameters(BaseModel):
    args: dict[str, Any]
    groups: Optional[list[str]] = None
    hosts: Optional[list[str]] = None
    strict_args: Optional[bool] = Field(None, description="Override global strict args setting")
    syntax_check: Optional[bool] = Field(None, description="perform a syntax check on the playbook, but do not execute it",)
    template: Optional[str] = Field(None, description="TextFSM template")
    verbosity: Optional[Annotated[int, Field(ge=1, le=4)]] = Field(None, description="Control how verbose the output of ansible-playbook is")


class RbacAddGroupParameters(BaseModel):
    class Config:
        extra = "forbid"

    description: Optional[Annotated[str, StringConstraints(min_length=1)]] = None
    name: Annotated[str, StringConstraints(min_length=1)]
    roles: list[str] = Field(..., min_items=1)
    users: Optional[list[str]] = Field(None, min_items=1)


class RbacAddGroupRolesParameters(BaseModel):
    class Config:
        extra = "forbid"

    roles: list[str] = Field(..., min_items=1)


class RbacAddGroupUsersParameters(BaseModel):
    class Config:
        extra = "forbid"

    users: list[str] = Field(..., min_items=1)


class RbacUpdateGroupParameters(BaseModel):
    description: Optional[str] = None
    roles: Optional[list[str]] = Field(None, min_items=1)
    users: Optional[list[str]] = Field(None, min_items=1)


class ScriptExecuteParameters(BaseModel):
    args: dict[str, Any]
    env: Optional[dict[str, Any]] = None
    hosts: Optional[list[str]] = None
    strict_args: Optional[bool] = Field(None, description="Override global strict args setting")
    template: Optional[str] = Field(None, description="TextFSM template")


class SecretAddParameters(BaseModel):
    path: str
    secret_data: dict[str, Any]

class ValidateSecurityQuestionsParameters(BaseModel):
    email: str
    security_ques1: str
    security_ques1_ans: str
    security_ques2: str
    security_ques2_ans: str


class TerraformParameters(BaseModel):
    args: dict[str, Any]
    strict_args: Optional[bool] = Field(None, description="Override global strict args setting")

'''
# `provider`

Refer to the Terraform Registry for docs: [`snowflake`](https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class SnowflakeProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.provider.SnowflakeProvider",
):
    '''Represents a {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs snowflake}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        authenticator: typing.Optional[builtins.str] = None,
        browser_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        client_ip: typing.Optional[builtins.str] = None,
        client_request_mfa_token: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        client_store_temporary_credential: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        client_timeout: typing.Optional[jsii.Number] = None,
        disable_query_context_cache: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        disable_telemetry: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        external_browser_timeout: typing.Optional[jsii.Number] = None,
        host: typing.Optional[builtins.str] = None,
        insecure_mode: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        jwt_client_timeout: typing.Optional[jsii.Number] = None,
        jwt_expire_timeout: typing.Optional[jsii.Number] = None,
        keep_session_alive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        login_timeout: typing.Optional[jsii.Number] = None,
        oauth_access_token: typing.Optional[builtins.str] = None,
        oauth_client_id: typing.Optional[builtins.str] = None,
        oauth_client_secret: typing.Optional[builtins.str] = None,
        oauth_endpoint: typing.Optional[builtins.str] = None,
        oauth_redirect_url: typing.Optional[builtins.str] = None,
        oauth_refresh_token: typing.Optional[builtins.str] = None,
        ocsp_fail_open: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        okta_url: typing.Optional[builtins.str] = None,
        params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        passcode: typing.Optional[builtins.str] = None,
        passcode_in_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        private_key: typing.Optional[builtins.str] = None,
        private_key_passphrase: typing.Optional[builtins.str] = None,
        private_key_path: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        request_timeout: typing.Optional[jsii.Number] = None,
        role: typing.Optional[builtins.str] = None,
        session_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        token: typing.Optional[builtins.str] = None,
        token_accessor: typing.Optional[typing.Union["SnowflakeProviderTokenAccessor", typing.Dict[builtins.str, typing.Any]]] = None,
        user: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        validate_default_parameters: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        warehouse: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs snowflake} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account: Specifies your Snowflake account identifier assigned, by Snowflake. For information about account identifiers, see the `Snowflake documentation <https://docs.snowflake.com/en/user-guide/admin-account-identifier.html>`_. Can also be sourced from the ``SNOWFLAKE_ACCOUNT`` environment variable. Required unless using ``profile``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#account SnowflakeProvider#account}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#alias SnowflakeProvider#alias}
        :param authenticator: Specifies the `authentication type <https://pkg.go.dev/github.com/snowflakedb/gosnowflake#AuthType>`_ to use when connecting to Snowflake. Valid values include: Snowflake, OAuth, ExternalBrowser, Okta, JWT, TokenAccessor, UsernamePasswordMFA. Can also be sourced from the ``SNOWFLAKE_AUTHENTICATOR`` environment variable. It has to be set explicitly to JWT for private key authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#authenticator SnowflakeProvider#authenticator}
        :param browser_auth: Required when ``oauth_refresh_token`` is used. Can also be sourced from ``SNOWFLAKE_USE_BROWSER_AUTH`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#browser_auth SnowflakeProvider#browser_auth}
        :param client_ip: IP address for network checks. Can also be sourced from the ``SNOWFLAKE_CLIENT_IP`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#client_ip SnowflakeProvider#client_ip}
        :param client_request_mfa_token: When true the MFA token is cached in the credential manager. True by default in Windows/OSX. False for Linux. Can also be sourced from the ``SNOWFLAKE_CLIENT_REQUEST_MFA_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#client_request_mfa_token SnowflakeProvider#client_request_mfa_token}
        :param client_store_temporary_credential: When true the ID token is cached in the credential manager. True by default in Windows/OSX. False for Linux. Can also be sourced from the ``SNOWFLAKE_CLIENT_STORE_TEMPORARY_CREDENTIAL`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#client_store_temporary_credential SnowflakeProvider#client_store_temporary_credential}
        :param client_timeout: The timeout in seconds for the client to complete the authentication. Default is 900 seconds. Can also be sourced from the ``SNOWFLAKE_CLIENT_TIMEOUT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#client_timeout SnowflakeProvider#client_timeout}
        :param disable_query_context_cache: Should HTAP query context cache be disabled. Can also be sourced from the ``SNOWFLAKE_DISABLE_QUERY_CONTEXT_CACHE`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#disable_query_context_cache SnowflakeProvider#disable_query_context_cache}
        :param disable_telemetry: Indicates whether to disable telemetry. Can also be sourced from the ``SNOWFLAKE_DISABLE_TELEMETRY`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#disable_telemetry SnowflakeProvider#disable_telemetry}
        :param external_browser_timeout: The timeout in seconds for the external browser to complete the authentication. Default is 120 seconds. Can also be sourced from the ``SNOWFLAKE_EXTERNAL_BROWSER_TIMEOUT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#external_browser_timeout SnowflakeProvider#external_browser_timeout}
        :param host: Supports passing in a custom host value to the snowflake go driver for use with privatelink. Can also be sourced from the ``SNOWFLAKE_HOST`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#host SnowflakeProvider#host}
        :param insecure_mode: If true, bypass the Online Certificate Status Protocol (OCSP) certificate revocation check. IMPORTANT: Change the default value for testing or emergency situations only. Can also be sourced from the ``SNOWFLAKE_INSECURE_MODE`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#insecure_mode SnowflakeProvider#insecure_mode}
        :param jwt_client_timeout: The timeout in seconds for the JWT client to complete the authentication. Default is 10 seconds. Can also be sourced from the ``SNOWFLAKE_JWT_CLIENT_TIMEOUT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#jwt_client_timeout SnowflakeProvider#jwt_client_timeout}
        :param jwt_expire_timeout: JWT expire after timeout in seconds. Can also be sourced from the ``SNOWFLAKE_JWT_EXPIRE_TIMEOUT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#jwt_expire_timeout SnowflakeProvider#jwt_expire_timeout}
        :param keep_session_alive: Enables the session to persist even after the connection is closed. Can also be sourced from the ``SNOWFLAKE_KEEP_SESSION_ALIVE`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#keep_session_alive SnowflakeProvider#keep_session_alive}
        :param login_timeout: Login retry timeout EXCLUDING network roundtrip and read out http response. Can also be sourced from the ``SNOWFLAKE_LOGIN_TIMEOUT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#login_timeout SnowflakeProvider#login_timeout}
        :param oauth_access_token: Token for use with OAuth. Generating the token is left to other tools. Cannot be used with ``browser_auth``, ``private_key_path``, ``oauth_refresh_token`` or ``password``. Can also be sourced from ``SNOWFLAKE_OAUTH_ACCESS_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#oauth_access_token SnowflakeProvider#oauth_access_token}
        :param oauth_client_id: Required when ``oauth_refresh_token`` is used. Can also be sourced from ``SNOWFLAKE_OAUTH_CLIENT_ID`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#oauth_client_id SnowflakeProvider#oauth_client_id}
        :param oauth_client_secret: Required when ``oauth_refresh_token`` is used. Can also be sourced from ``SNOWFLAKE_OAUTH_CLIENT_SECRET`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#oauth_client_secret SnowflakeProvider#oauth_client_secret}
        :param oauth_endpoint: Required when ``oauth_refresh_token`` is used. Can also be sourced from ``SNOWFLAKE_OAUTH_ENDPOINT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#oauth_endpoint SnowflakeProvider#oauth_endpoint}
        :param oauth_redirect_url: Required when ``oauth_refresh_token`` is used. Can also be sourced from ``SNOWFLAKE_OAUTH_REDIRECT_URL`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#oauth_redirect_url SnowflakeProvider#oauth_redirect_url}
        :param oauth_refresh_token: Token for use with OAuth. Setup and generation of the token is left to other tools. Should be used in conjunction with ``oauth_client_id``, ``oauth_client_secret``, ``oauth_endpoint``, ``oauth_redirect_url``. Cannot be used with ``browser_auth``, ``private_key_path``, ``oauth_access_token`` or ``password``. Can also be sourced from ``SNOWFLAKE_OAUTH_REFRESH_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#oauth_refresh_token SnowflakeProvider#oauth_refresh_token}
        :param ocsp_fail_open: True represents OCSP fail open mode. False represents OCSP fail closed mode. Fail open true by default. Can also be sourced from the ``SNOWFLAKE_OCSP_FAIL_OPEN`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#ocsp_fail_open SnowflakeProvider#ocsp_fail_open}
        :param okta_url: The URL of the Okta server. e.g. https://example.okta.com. Can also be sourced from the ``SNOWFLAKE_OKTA_URL`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#okta_url SnowflakeProvider#okta_url}
        :param params: Sets other connection (i.e. session) parameters. `Parameters <https://docs.snowflake.com/en/sql-reference/parameters>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#params SnowflakeProvider#params}
        :param passcode: Specifies the passcode provided by Duo when using multi-factor authentication (MFA) for login. Can also be sourced from the ``SNOWFLAKE_PASSCODE`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#passcode SnowflakeProvider#passcode}
        :param passcode_in_password: False by default. Set to true if the MFA passcode is embedded in the login password. Appends the MFA passcode to the end of the password. Can also be sourced from the ``SNOWFLAKE_PASSCODE_IN_PASSWORD`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#passcode_in_password SnowflakeProvider#passcode_in_password}
        :param password: Password for username+password auth. Cannot be used with ``browser_auth`` or ``private_key_path``. Can also be sourced from the ``SNOWFLAKE_PASSWORD`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#password SnowflakeProvider#password}
        :param port: Support custom port values to snowflake go driver for use with privatelink. Can also be sourced from the ``SNOWFLAKE_PORT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#port SnowflakeProvider#port}
        :param private_key: Private Key for username+private-key auth. Cannot be used with ``browser_auth`` or ``password``. Can also be sourced from ``SNOWFLAKE_PRIVATE_KEY`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#private_key SnowflakeProvider#private_key}
        :param private_key_passphrase: Supports the encryption ciphers aes-128-cbc, aes-128-gcm, aes-192-cbc, aes-192-gcm, aes-256-cbc, aes-256-gcm, and des-ede3-cbc. Can also be sourced from ``SNOWFLAKE_PRIVATE_KEY_PASSPHRASE`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#private_key_passphrase SnowflakeProvider#private_key_passphrase}
        :param private_key_path: Path to a private key for using keypair authentication. Cannot be used with ``browser_auth``, ``oauth_access_token`` or ``password``. Can also be sourced from ``SNOWFLAKE_PRIVATE_KEY_PATH`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#private_key_path SnowflakeProvider#private_key_path}
        :param profile: Sets the profile to read from ~/.snowflake/config file. Can also be sourced from the ``SNOWFLAKE_PROFILE`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#profile SnowflakeProvider#profile}
        :param protocol: Either http or https, defaults to https. Can also be sourced from the ``SNOWFLAKE_PROTOCOL`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#protocol SnowflakeProvider#protocol}
        :param region: Snowflake region, such as "eu-central-1", with this parameter. However, since this parameter is deprecated, it is best to specify the region as part of the account parameter. For details, see the description of the account parameter. `Snowflake region <https://docs.snowflake.com/en/user-guide/intro-regions.html>`_ to use. Required if using the `legacy format for the ``account`` identifier <https://docs.snowflake.com/en/user-guide/admin-account-identifier.html#format-2-legacy-account-locator-in-a-region>`_ in the form of ``<cloud_region_id>.<cloud>``. Can also be sourced from the ``SNOWFLAKE_REGION`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#region SnowflakeProvider#region}
        :param request_timeout: request retry timeout EXCLUDING network roundtrip and read out http response. Can also be sourced from the ``SNOWFLAKE_REQUEST_TIMEOUT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#request_timeout SnowflakeProvider#request_timeout}
        :param role: Specifies the role to use by default for accessing Snowflake objects in the client session. Can also be sourced from the ``SNOWFLAKE_ROLE`` environment variable. . Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#role SnowflakeProvider#role}
        :param session_params: Sets session parameters. `Parameters <https://docs.snowflake.com/en/sql-reference/parameters>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#session_params SnowflakeProvider#session_params}
        :param token: Token to use for OAuth and other forms of token based auth. Can also be sourced from the ``SNOWFLAKE_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#token SnowflakeProvider#token}
        :param token_accessor: token_accessor block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#token_accessor SnowflakeProvider#token_accessor}
        :param user: Username. Can also be sourced from the ``SNOWFLAKE_USER`` environment variable. Required unless using ``profile``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#user SnowflakeProvider#user}
        :param username: Username for username+password authentication. Can also be sourced from the ``SNOWFLAKE_USERNAME`` environment variable. Required unless using ``profile``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#username SnowflakeProvider#username}
        :param validate_default_parameters: True by default. If false, disables the validation checks for Database, Schema, Warehouse and Role at the time a connection is established. Can also be sourced from the ``SNOWFLAKE_VALIDATE_DEFAULT_PARAMETERS`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#validate_default_parameters SnowflakeProvider#validate_default_parameters}
        :param warehouse: Specifies the virtual warehouse to use by default for queries, loading, etc. in the client session. Can also be sourced from the ``SNOWFLAKE_WAREHOUSE`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#warehouse SnowflakeProvider#warehouse}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dffb8c16f0bdbd356b60ba75b76332c0fa5872a9b67c09d939ada39e30798782)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = SnowflakeProviderConfig(
            account=account,
            alias=alias,
            authenticator=authenticator,
            browser_auth=browser_auth,
            client_ip=client_ip,
            client_request_mfa_token=client_request_mfa_token,
            client_store_temporary_credential=client_store_temporary_credential,
            client_timeout=client_timeout,
            disable_query_context_cache=disable_query_context_cache,
            disable_telemetry=disable_telemetry,
            external_browser_timeout=external_browser_timeout,
            host=host,
            insecure_mode=insecure_mode,
            jwt_client_timeout=jwt_client_timeout,
            jwt_expire_timeout=jwt_expire_timeout,
            keep_session_alive=keep_session_alive,
            login_timeout=login_timeout,
            oauth_access_token=oauth_access_token,
            oauth_client_id=oauth_client_id,
            oauth_client_secret=oauth_client_secret,
            oauth_endpoint=oauth_endpoint,
            oauth_redirect_url=oauth_redirect_url,
            oauth_refresh_token=oauth_refresh_token,
            ocsp_fail_open=ocsp_fail_open,
            okta_url=okta_url,
            params=params,
            passcode=passcode,
            passcode_in_password=passcode_in_password,
            password=password,
            port=port,
            private_key=private_key,
            private_key_passphrase=private_key_passphrase,
            private_key_path=private_key_path,
            profile=profile,
            protocol=protocol,
            region=region,
            request_timeout=request_timeout,
            role=role,
            session_params=session_params,
            token=token,
            token_accessor=token_accessor,
            user=user,
            username=username,
            validate_default_parameters=validate_default_parameters,
            warehouse=warehouse,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a SnowflakeProvider resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the SnowflakeProvider to import.
        :param import_from_id: The id of the existing SnowflakeProvider that should be imported. Refer to the {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the SnowflakeProvider to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65a3a5ee41e1141e62bec029bdb8709bf3cc38a98cb6c277789fc640ecc924d2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAccount")
    def reset_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccount", []))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetAuthenticator")
    def reset_authenticator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticator", []))

    @jsii.member(jsii_name="resetBrowserAuth")
    def reset_browser_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBrowserAuth", []))

    @jsii.member(jsii_name="resetClientIp")
    def reset_client_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientIp", []))

    @jsii.member(jsii_name="resetClientRequestMfaToken")
    def reset_client_request_mfa_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientRequestMfaToken", []))

    @jsii.member(jsii_name="resetClientStoreTemporaryCredential")
    def reset_client_store_temporary_credential(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientStoreTemporaryCredential", []))

    @jsii.member(jsii_name="resetClientTimeout")
    def reset_client_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientTimeout", []))

    @jsii.member(jsii_name="resetDisableQueryContextCache")
    def reset_disable_query_context_cache(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableQueryContextCache", []))

    @jsii.member(jsii_name="resetDisableTelemetry")
    def reset_disable_telemetry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableTelemetry", []))

    @jsii.member(jsii_name="resetExternalBrowserTimeout")
    def reset_external_browser_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalBrowserTimeout", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetInsecureMode")
    def reset_insecure_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureMode", []))

    @jsii.member(jsii_name="resetJwtClientTimeout")
    def reset_jwt_client_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJwtClientTimeout", []))

    @jsii.member(jsii_name="resetJwtExpireTimeout")
    def reset_jwt_expire_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJwtExpireTimeout", []))

    @jsii.member(jsii_name="resetKeepSessionAlive")
    def reset_keep_session_alive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeepSessionAlive", []))

    @jsii.member(jsii_name="resetLoginTimeout")
    def reset_login_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginTimeout", []))

    @jsii.member(jsii_name="resetOauthAccessToken")
    def reset_oauth_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthAccessToken", []))

    @jsii.member(jsii_name="resetOauthClientId")
    def reset_oauth_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthClientId", []))

    @jsii.member(jsii_name="resetOauthClientSecret")
    def reset_oauth_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthClientSecret", []))

    @jsii.member(jsii_name="resetOauthEndpoint")
    def reset_oauth_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthEndpoint", []))

    @jsii.member(jsii_name="resetOauthRedirectUrl")
    def reset_oauth_redirect_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRedirectUrl", []))

    @jsii.member(jsii_name="resetOauthRefreshToken")
    def reset_oauth_refresh_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRefreshToken", []))

    @jsii.member(jsii_name="resetOcspFailOpen")
    def reset_ocsp_fail_open(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOcspFailOpen", []))

    @jsii.member(jsii_name="resetOktaUrl")
    def reset_okta_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOktaUrl", []))

    @jsii.member(jsii_name="resetParams")
    def reset_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParams", []))

    @jsii.member(jsii_name="resetPasscode")
    def reset_passcode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasscode", []))

    @jsii.member(jsii_name="resetPasscodeInPassword")
    def reset_passcode_in_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasscodeInPassword", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPrivateKey")
    def reset_private_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateKey", []))

    @jsii.member(jsii_name="resetPrivateKeyPassphrase")
    def reset_private_key_passphrase(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateKeyPassphrase", []))

    @jsii.member(jsii_name="resetPrivateKeyPath")
    def reset_private_key_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateKeyPath", []))

    @jsii.member(jsii_name="resetProfile")
    def reset_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProfile", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetRequestTimeout")
    def reset_request_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestTimeout", []))

    @jsii.member(jsii_name="resetRole")
    def reset_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRole", []))

    @jsii.member(jsii_name="resetSessionParams")
    def reset_session_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionParams", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="resetTokenAccessor")
    def reset_token_accessor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenAccessor", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetValidateDefaultParameters")
    def reset_validate_default_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidateDefaultParameters", []))

    @jsii.member(jsii_name="resetWarehouse")
    def reset_warehouse(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarehouse", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="synthesizeHclAttributes")
    def _synthesize_hcl_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeHclAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accountInput")
    def account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticatorInput")
    def authenticator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticatorInput"))

    @builtins.property
    @jsii.member(jsii_name="browserAuthInput")
    def browser_auth_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "browserAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIpInput")
    def client_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIpInput"))

    @builtins.property
    @jsii.member(jsii_name="clientRequestMfaTokenInput")
    def client_request_mfa_token_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "clientRequestMfaTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="clientStoreTemporaryCredentialInput")
    def client_store_temporary_credential_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "clientStoreTemporaryCredentialInput"))

    @builtins.property
    @jsii.member(jsii_name="clientTimeoutInput")
    def client_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "clientTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="disableQueryContextCacheInput")
    def disable_query_context_cache_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableQueryContextCacheInput"))

    @builtins.property
    @jsii.member(jsii_name="disableTelemetryInput")
    def disable_telemetry_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableTelemetryInput"))

    @builtins.property
    @jsii.member(jsii_name="externalBrowserTimeoutInput")
    def external_browser_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "externalBrowserTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureModeInput")
    def insecure_mode_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecureModeInput"))

    @builtins.property
    @jsii.member(jsii_name="jwtClientTimeoutInput")
    def jwt_client_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "jwtClientTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="jwtExpireTimeoutInput")
    def jwt_expire_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "jwtExpireTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="keepSessionAliveInput")
    def keep_session_alive_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "keepSessionAliveInput"))

    @builtins.property
    @jsii.member(jsii_name="loginTimeoutInput")
    def login_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "loginTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthAccessTokenInput")
    def oauth_access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthAccessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthClientIdInput")
    def oauth_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthClientSecretInput")
    def oauth_client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthClientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthEndpointInput")
    def oauth_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRedirectUrlInput")
    def oauth_redirect_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthRedirectUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRefreshTokenInput")
    def oauth_refresh_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthRefreshTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="ocspFailOpenInput")
    def ocsp_fail_open_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ocspFailOpenInput"))

    @builtins.property
    @jsii.member(jsii_name="oktaUrlInput")
    def okta_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oktaUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="paramsInput")
    def params_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "paramsInput"))

    @builtins.property
    @jsii.member(jsii_name="passcodeInPasswordInput")
    def passcode_in_password_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "passcodeInPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="passcodeInput")
    def passcode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passcodeInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyInput")
    def private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyPassphraseInput")
    def private_key_passphrase_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyPassphraseInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyPathInput")
    def private_key_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyPathInput"))

    @builtins.property
    @jsii.member(jsii_name="profileInput")
    def profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="requestTimeoutInput")
    def request_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "requestTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionParamsInput")
    def session_params_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sessionParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenAccessorInput")
    def token_accessor_input(self) -> typing.Optional["SnowflakeProviderTokenAccessor"]:
        return typing.cast(typing.Optional["SnowflakeProviderTokenAccessor"], jsii.get(self, "tokenAccessorInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="validateDefaultParametersInput")
    def validate_default_parameters_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "validateDefaultParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="warehouseInput")
    def warehouse_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warehouseInput"))

    @builtins.property
    @jsii.member(jsii_name="account")
    def account(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "account"))

    @account.setter
    def account(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c95f157df42af058823cb6b649f9183b7256fb0ab7fd9117970ad5629398e73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "account", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cdc7cd12d304b2eddd5316af316d83f132ecae360404d6176a8e6a997e8dc2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="authenticator")
    def authenticator(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticator"))

    @authenticator.setter
    def authenticator(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b6d6a40d1a5605a9094439f3d2d1e57d143ffa3c2083b130937df91f19b35b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticator", value)

    @builtins.property
    @jsii.member(jsii_name="browserAuth")
    def browser_auth(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "browserAuth"))

    @browser_auth.setter
    def browser_auth(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8c0e664296c25b62d60022f48050f4a74aa8c1523109e28179f692a2663de4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "browserAuth", value)

    @builtins.property
    @jsii.member(jsii_name="clientIp")
    def client_ip(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIp"))

    @client_ip.setter
    def client_ip(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__370f87780241c7b2653971c27701eed45e4fc0fea1e1c19909bf4822f9a35139)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientIp", value)

    @builtins.property
    @jsii.member(jsii_name="clientRequestMfaToken")
    def client_request_mfa_token(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "clientRequestMfaToken"))

    @client_request_mfa_token.setter
    def client_request_mfa_token(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f642b106f9ead7f93ccfef26461a60434d7ce40769a4318d6de7980d579723d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientRequestMfaToken", value)

    @builtins.property
    @jsii.member(jsii_name="clientStoreTemporaryCredential")
    def client_store_temporary_credential(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "clientStoreTemporaryCredential"))

    @client_store_temporary_credential.setter
    def client_store_temporary_credential(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6586aace401480ef0ce4ab53207770ca079b6a438409c516fcce530b59649f36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientStoreTemporaryCredential", value)

    @builtins.property
    @jsii.member(jsii_name="clientTimeout")
    def client_timeout(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "clientTimeout"))

    @client_timeout.setter
    def client_timeout(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__818f5069d0221466e050c5c53b6b1e3eaaac0d5a53109481e4ead46297f0b141)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="disableQueryContextCache")
    def disable_query_context_cache(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableQueryContextCache"))

    @disable_query_context_cache.setter
    def disable_query_context_cache(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9abcf60fa4330b65affc6db33362afcc184ad771a4fafb37665309283f9986ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableQueryContextCache", value)

    @builtins.property
    @jsii.member(jsii_name="disableTelemetry")
    def disable_telemetry(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableTelemetry"))

    @disable_telemetry.setter
    def disable_telemetry(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__269dfbf8bd7e9687bd9093ed943acb915d1e33d5f2a1d222d2ebe73340152dd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableTelemetry", value)

    @builtins.property
    @jsii.member(jsii_name="externalBrowserTimeout")
    def external_browser_timeout(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "externalBrowserTimeout"))

    @external_browser_timeout.setter
    def external_browser_timeout(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be356c932dd3785d09f2c4a5c787d88fcbbb1846738765a3ac6f6118bf230c45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalBrowserTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "host"))

    @host.setter
    def host(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25df655b6fdfcfce4cc80d4c7d317296ba4b1b1e6a48e51e051a48b933da7a96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="insecureMode")
    def insecure_mode(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecureMode"))

    @insecure_mode.setter
    def insecure_mode(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c0b770f66297cf03ca54574462492185fa522c242f96b03b32317dc69d38166)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureMode", value)

    @builtins.property
    @jsii.member(jsii_name="jwtClientTimeout")
    def jwt_client_timeout(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "jwtClientTimeout"))

    @jwt_client_timeout.setter
    def jwt_client_timeout(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86c2273f5de1a2697d59b298ef8372bd657956bd24ac15953410953c6bc5e48e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jwtClientTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="jwtExpireTimeout")
    def jwt_expire_timeout(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "jwtExpireTimeout"))

    @jwt_expire_timeout.setter
    def jwt_expire_timeout(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e006c8754a599103a5f7c5d6363a2fd8f44dbc569d9882eab0fe73527000b263)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jwtExpireTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="keepSessionAlive")
    def keep_session_alive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "keepSessionAlive"))

    @keep_session_alive.setter
    def keep_session_alive(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a87491bfb7b1ecfe9103c8dddaf7734ff39eb830fb1a351d40dc0f7c1adb4d2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keepSessionAlive", value)

    @builtins.property
    @jsii.member(jsii_name="loginTimeout")
    def login_timeout(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "loginTimeout"))

    @login_timeout.setter
    def login_timeout(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e932bf3dd2379e89075f4162cb5bc10d1da873452b7e84361af61777412cd1fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="oauthAccessToken")
    def oauth_access_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthAccessToken"))

    @oauth_access_token.setter
    def oauth_access_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5450d12035fdb7aaeb95891a55c7092fd9095bf121f6a46710c8d0c0dec4e47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthAccessToken", value)

    @builtins.property
    @jsii.member(jsii_name="oauthClientId")
    def oauth_client_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthClientId"))

    @oauth_client_id.setter
    def oauth_client_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04343d423fd2ac1d04d8dc2589d3d4e29413748a1ee5c9c2b0550410c98eaee5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthClientId", value)

    @builtins.property
    @jsii.member(jsii_name="oauthClientSecret")
    def oauth_client_secret(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthClientSecret"))

    @oauth_client_secret.setter
    def oauth_client_secret(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7480aa87e81ad2f94226ea84240e1ecc31b405fa1a0b01bdf20de287d88791c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthClientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="oauthEndpoint")
    def oauth_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthEndpoint"))

    @oauth_endpoint.setter
    def oauth_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92517d42922dc0c4dffe77d60eb82ffb67cf253e0cd04d4e1f3350fe80ca0c75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="oauthRedirectUrl")
    def oauth_redirect_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthRedirectUrl"))

    @oauth_redirect_url.setter
    def oauth_redirect_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6be019a61f9ea18a8a1b32731eadb4549c228e9ede8c9435b4758f99753584cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthRedirectUrl", value)

    @builtins.property
    @jsii.member(jsii_name="oauthRefreshToken")
    def oauth_refresh_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthRefreshToken"))

    @oauth_refresh_token.setter
    def oauth_refresh_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ef289860c28b0549c58795a27ffbdc287f7d4899317c1c4e9337b035b23deb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthRefreshToken", value)

    @builtins.property
    @jsii.member(jsii_name="ocspFailOpen")
    def ocsp_fail_open(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ocspFailOpen"))

    @ocsp_fail_open.setter
    def ocsp_fail_open(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5794c009d8765aa8f769a80e9753aabe08dc725863ff7b18eab0341eed543c64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ocspFailOpen", value)

    @builtins.property
    @jsii.member(jsii_name="oktaUrl")
    def okta_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oktaUrl"))

    @okta_url.setter
    def okta_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d2acb8cea3c2b00df9129f4f3b5786e34b302b4fbbe61119d57006a7804f3f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oktaUrl", value)

    @builtins.property
    @jsii.member(jsii_name="params")
    def params(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "params"))

    @params.setter
    def params(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5079b47ba384ea5e3aaafe6322f07c7068ea187e00a883751b397324ec04b6c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "params", value)

    @builtins.property
    @jsii.member(jsii_name="passcode")
    def passcode(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passcode"))

    @passcode.setter
    def passcode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8aeb67752ef65d8786754b2e094e8334d801727dcb831c2a6d6bbbd59c0c6ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passcode", value)

    @builtins.property
    @jsii.member(jsii_name="passcodeInPassword")
    def passcode_in_password(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "passcodeInPassword"))

    @passcode_in_password.setter
    def passcode_in_password(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90d285d39d0d7dfff15a4462be9b03f6e0824d61185275e2de835935b4db1d4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passcodeInPassword", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4647c5ce21749b9912e9bb483866a4fe9decad7840786080279fac4bf9b9881)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14ab59f5493ec686723d4a013bc5f681695f8805e1a21d0e2961ffb9ba96bb2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__174acb5ca0c2f03f2c07759d01042240477d689ab50d9a3e5014d671f7072072)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="privateKeyPassphrase")
    def private_key_passphrase(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyPassphrase"))

    @private_key_passphrase.setter
    def private_key_passphrase(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8e45747860bace19eea01fe56764a0071fb76645a7df1767604942c712bc7fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKeyPassphrase", value)

    @builtins.property
    @jsii.member(jsii_name="privateKeyPath")
    def private_key_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyPath"))

    @private_key_path.setter
    def private_key_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a869d7e0ed58d955c8747da9c6e46d8bcb7d2e8292dc085324fc4f66cd00101c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKeyPath", value)

    @builtins.property
    @jsii.member(jsii_name="profile")
    def profile(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profile"))

    @profile.setter
    def profile(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2890938b1cd71ed7815000e422a912b7b3d54903511d4f7b45712b5a30212795)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profile", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__272d3205644fbaa065eff9f5ac6d27774f4829ae96c327fd974c31e2c14d17ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))

    @region.setter
    def region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f532710ad9671b193f560280c447d334b62fa15f62b4acf87f79137b647b9c9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="requestTimeout")
    def request_timeout(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "requestTimeout"))

    @request_timeout.setter
    def request_timeout(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee0543502fab097af52ebd9c81a19791d58a795a589dead81d2ddb4e53710eab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "role"))

    @role.setter
    def role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63c825aa96baa5ca037e135d9294ae15fc9d5395c87a9275884dd82a5edd2ce8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="sessionParams")
    def session_params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sessionParams"))

    @session_params.setter
    def session_params(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1a9fc5c69b7d4729ea79396ad290778ac78f6cf5f7a4ed625289b1d10760b75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionParams", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "token"))

    @token.setter
    def token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40535fefad35c2491bb2aa60c6522f5cd80fc0876e21c80deb2f684e33cf2380)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="tokenAccessor")
    def token_accessor(self) -> typing.Optional["SnowflakeProviderTokenAccessor"]:
        return typing.cast(typing.Optional["SnowflakeProviderTokenAccessor"], jsii.get(self, "tokenAccessor"))

    @token_accessor.setter
    def token_accessor(
        self,
        value: typing.Optional["SnowflakeProviderTokenAccessor"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89b86051ecb7af168b4414164285a52653116c6c1fd66e45e577d5e94b071fe5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenAccessor", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "user"))

    @user.setter
    def user(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc30eb22eb05f35288fb4961dd14be1e1fe9101084acdde298c42009214db961)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "username"))

    @username.setter
    def username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6a7f197bfe45836bef3f6471be6cc78940528379421b34d0bd051af02cc9b5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="validateDefaultParameters")
    def validate_default_parameters(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "validateDefaultParameters"))

    @validate_default_parameters.setter
    def validate_default_parameters(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b43646ed314e4eea24bb621b967fbe094538e70a124a4c7cc36c518a3834ac02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validateDefaultParameters", value)

    @builtins.property
    @jsii.member(jsii_name="warehouse")
    def warehouse(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warehouse"))

    @warehouse.setter
    def warehouse(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d86a20638ec60e4335171ba31cc595ce61cbb7fbb325816de15f3387860facb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warehouse", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.provider.SnowflakeProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "alias": "alias",
        "authenticator": "authenticator",
        "browser_auth": "browserAuth",
        "client_ip": "clientIp",
        "client_request_mfa_token": "clientRequestMfaToken",
        "client_store_temporary_credential": "clientStoreTemporaryCredential",
        "client_timeout": "clientTimeout",
        "disable_query_context_cache": "disableQueryContextCache",
        "disable_telemetry": "disableTelemetry",
        "external_browser_timeout": "externalBrowserTimeout",
        "host": "host",
        "insecure_mode": "insecureMode",
        "jwt_client_timeout": "jwtClientTimeout",
        "jwt_expire_timeout": "jwtExpireTimeout",
        "keep_session_alive": "keepSessionAlive",
        "login_timeout": "loginTimeout",
        "oauth_access_token": "oauthAccessToken",
        "oauth_client_id": "oauthClientId",
        "oauth_client_secret": "oauthClientSecret",
        "oauth_endpoint": "oauthEndpoint",
        "oauth_redirect_url": "oauthRedirectUrl",
        "oauth_refresh_token": "oauthRefreshToken",
        "ocsp_fail_open": "ocspFailOpen",
        "okta_url": "oktaUrl",
        "params": "params",
        "passcode": "passcode",
        "passcode_in_password": "passcodeInPassword",
        "password": "password",
        "port": "port",
        "private_key": "privateKey",
        "private_key_passphrase": "privateKeyPassphrase",
        "private_key_path": "privateKeyPath",
        "profile": "profile",
        "protocol": "protocol",
        "region": "region",
        "request_timeout": "requestTimeout",
        "role": "role",
        "session_params": "sessionParams",
        "token": "token",
        "token_accessor": "tokenAccessor",
        "user": "user",
        "username": "username",
        "validate_default_parameters": "validateDefaultParameters",
        "warehouse": "warehouse",
    },
)
class SnowflakeProviderConfig:
    def __init__(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        authenticator: typing.Optional[builtins.str] = None,
        browser_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        client_ip: typing.Optional[builtins.str] = None,
        client_request_mfa_token: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        client_store_temporary_credential: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        client_timeout: typing.Optional[jsii.Number] = None,
        disable_query_context_cache: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        disable_telemetry: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        external_browser_timeout: typing.Optional[jsii.Number] = None,
        host: typing.Optional[builtins.str] = None,
        insecure_mode: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        jwt_client_timeout: typing.Optional[jsii.Number] = None,
        jwt_expire_timeout: typing.Optional[jsii.Number] = None,
        keep_session_alive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        login_timeout: typing.Optional[jsii.Number] = None,
        oauth_access_token: typing.Optional[builtins.str] = None,
        oauth_client_id: typing.Optional[builtins.str] = None,
        oauth_client_secret: typing.Optional[builtins.str] = None,
        oauth_endpoint: typing.Optional[builtins.str] = None,
        oauth_redirect_url: typing.Optional[builtins.str] = None,
        oauth_refresh_token: typing.Optional[builtins.str] = None,
        ocsp_fail_open: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        okta_url: typing.Optional[builtins.str] = None,
        params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        passcode: typing.Optional[builtins.str] = None,
        passcode_in_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        private_key: typing.Optional[builtins.str] = None,
        private_key_passphrase: typing.Optional[builtins.str] = None,
        private_key_path: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        request_timeout: typing.Optional[jsii.Number] = None,
        role: typing.Optional[builtins.str] = None,
        session_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        token: typing.Optional[builtins.str] = None,
        token_accessor: typing.Optional[typing.Union["SnowflakeProviderTokenAccessor", typing.Dict[builtins.str, typing.Any]]] = None,
        user: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        validate_default_parameters: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        warehouse: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account: Specifies your Snowflake account identifier assigned, by Snowflake. For information about account identifiers, see the `Snowflake documentation <https://docs.snowflake.com/en/user-guide/admin-account-identifier.html>`_. Can also be sourced from the ``SNOWFLAKE_ACCOUNT`` environment variable. Required unless using ``profile``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#account SnowflakeProvider#account}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#alias SnowflakeProvider#alias}
        :param authenticator: Specifies the `authentication type <https://pkg.go.dev/github.com/snowflakedb/gosnowflake#AuthType>`_ to use when connecting to Snowflake. Valid values include: Snowflake, OAuth, ExternalBrowser, Okta, JWT, TokenAccessor, UsernamePasswordMFA. Can also be sourced from the ``SNOWFLAKE_AUTHENTICATOR`` environment variable. It has to be set explicitly to JWT for private key authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#authenticator SnowflakeProvider#authenticator}
        :param browser_auth: Required when ``oauth_refresh_token`` is used. Can also be sourced from ``SNOWFLAKE_USE_BROWSER_AUTH`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#browser_auth SnowflakeProvider#browser_auth}
        :param client_ip: IP address for network checks. Can also be sourced from the ``SNOWFLAKE_CLIENT_IP`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#client_ip SnowflakeProvider#client_ip}
        :param client_request_mfa_token: When true the MFA token is cached in the credential manager. True by default in Windows/OSX. False for Linux. Can also be sourced from the ``SNOWFLAKE_CLIENT_REQUEST_MFA_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#client_request_mfa_token SnowflakeProvider#client_request_mfa_token}
        :param client_store_temporary_credential: When true the ID token is cached in the credential manager. True by default in Windows/OSX. False for Linux. Can also be sourced from the ``SNOWFLAKE_CLIENT_STORE_TEMPORARY_CREDENTIAL`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#client_store_temporary_credential SnowflakeProvider#client_store_temporary_credential}
        :param client_timeout: The timeout in seconds for the client to complete the authentication. Default is 900 seconds. Can also be sourced from the ``SNOWFLAKE_CLIENT_TIMEOUT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#client_timeout SnowflakeProvider#client_timeout}
        :param disable_query_context_cache: Should HTAP query context cache be disabled. Can also be sourced from the ``SNOWFLAKE_DISABLE_QUERY_CONTEXT_CACHE`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#disable_query_context_cache SnowflakeProvider#disable_query_context_cache}
        :param disable_telemetry: Indicates whether to disable telemetry. Can also be sourced from the ``SNOWFLAKE_DISABLE_TELEMETRY`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#disable_telemetry SnowflakeProvider#disable_telemetry}
        :param external_browser_timeout: The timeout in seconds for the external browser to complete the authentication. Default is 120 seconds. Can also be sourced from the ``SNOWFLAKE_EXTERNAL_BROWSER_TIMEOUT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#external_browser_timeout SnowflakeProvider#external_browser_timeout}
        :param host: Supports passing in a custom host value to the snowflake go driver for use with privatelink. Can also be sourced from the ``SNOWFLAKE_HOST`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#host SnowflakeProvider#host}
        :param insecure_mode: If true, bypass the Online Certificate Status Protocol (OCSP) certificate revocation check. IMPORTANT: Change the default value for testing or emergency situations only. Can also be sourced from the ``SNOWFLAKE_INSECURE_MODE`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#insecure_mode SnowflakeProvider#insecure_mode}
        :param jwt_client_timeout: The timeout in seconds for the JWT client to complete the authentication. Default is 10 seconds. Can also be sourced from the ``SNOWFLAKE_JWT_CLIENT_TIMEOUT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#jwt_client_timeout SnowflakeProvider#jwt_client_timeout}
        :param jwt_expire_timeout: JWT expire after timeout in seconds. Can also be sourced from the ``SNOWFLAKE_JWT_EXPIRE_TIMEOUT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#jwt_expire_timeout SnowflakeProvider#jwt_expire_timeout}
        :param keep_session_alive: Enables the session to persist even after the connection is closed. Can also be sourced from the ``SNOWFLAKE_KEEP_SESSION_ALIVE`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#keep_session_alive SnowflakeProvider#keep_session_alive}
        :param login_timeout: Login retry timeout EXCLUDING network roundtrip and read out http response. Can also be sourced from the ``SNOWFLAKE_LOGIN_TIMEOUT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#login_timeout SnowflakeProvider#login_timeout}
        :param oauth_access_token: Token for use with OAuth. Generating the token is left to other tools. Cannot be used with ``browser_auth``, ``private_key_path``, ``oauth_refresh_token`` or ``password``. Can also be sourced from ``SNOWFLAKE_OAUTH_ACCESS_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#oauth_access_token SnowflakeProvider#oauth_access_token}
        :param oauth_client_id: Required when ``oauth_refresh_token`` is used. Can also be sourced from ``SNOWFLAKE_OAUTH_CLIENT_ID`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#oauth_client_id SnowflakeProvider#oauth_client_id}
        :param oauth_client_secret: Required when ``oauth_refresh_token`` is used. Can also be sourced from ``SNOWFLAKE_OAUTH_CLIENT_SECRET`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#oauth_client_secret SnowflakeProvider#oauth_client_secret}
        :param oauth_endpoint: Required when ``oauth_refresh_token`` is used. Can also be sourced from ``SNOWFLAKE_OAUTH_ENDPOINT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#oauth_endpoint SnowflakeProvider#oauth_endpoint}
        :param oauth_redirect_url: Required when ``oauth_refresh_token`` is used. Can also be sourced from ``SNOWFLAKE_OAUTH_REDIRECT_URL`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#oauth_redirect_url SnowflakeProvider#oauth_redirect_url}
        :param oauth_refresh_token: Token for use with OAuth. Setup and generation of the token is left to other tools. Should be used in conjunction with ``oauth_client_id``, ``oauth_client_secret``, ``oauth_endpoint``, ``oauth_redirect_url``. Cannot be used with ``browser_auth``, ``private_key_path``, ``oauth_access_token`` or ``password``. Can also be sourced from ``SNOWFLAKE_OAUTH_REFRESH_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#oauth_refresh_token SnowflakeProvider#oauth_refresh_token}
        :param ocsp_fail_open: True represents OCSP fail open mode. False represents OCSP fail closed mode. Fail open true by default. Can also be sourced from the ``SNOWFLAKE_OCSP_FAIL_OPEN`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#ocsp_fail_open SnowflakeProvider#ocsp_fail_open}
        :param okta_url: The URL of the Okta server. e.g. https://example.okta.com. Can also be sourced from the ``SNOWFLAKE_OKTA_URL`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#okta_url SnowflakeProvider#okta_url}
        :param params: Sets other connection (i.e. session) parameters. `Parameters <https://docs.snowflake.com/en/sql-reference/parameters>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#params SnowflakeProvider#params}
        :param passcode: Specifies the passcode provided by Duo when using multi-factor authentication (MFA) for login. Can also be sourced from the ``SNOWFLAKE_PASSCODE`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#passcode SnowflakeProvider#passcode}
        :param passcode_in_password: False by default. Set to true if the MFA passcode is embedded in the login password. Appends the MFA passcode to the end of the password. Can also be sourced from the ``SNOWFLAKE_PASSCODE_IN_PASSWORD`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#passcode_in_password SnowflakeProvider#passcode_in_password}
        :param password: Password for username+password auth. Cannot be used with ``browser_auth`` or ``private_key_path``. Can also be sourced from the ``SNOWFLAKE_PASSWORD`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#password SnowflakeProvider#password}
        :param port: Support custom port values to snowflake go driver for use with privatelink. Can also be sourced from the ``SNOWFLAKE_PORT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#port SnowflakeProvider#port}
        :param private_key: Private Key for username+private-key auth. Cannot be used with ``browser_auth`` or ``password``. Can also be sourced from ``SNOWFLAKE_PRIVATE_KEY`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#private_key SnowflakeProvider#private_key}
        :param private_key_passphrase: Supports the encryption ciphers aes-128-cbc, aes-128-gcm, aes-192-cbc, aes-192-gcm, aes-256-cbc, aes-256-gcm, and des-ede3-cbc. Can also be sourced from ``SNOWFLAKE_PRIVATE_KEY_PASSPHRASE`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#private_key_passphrase SnowflakeProvider#private_key_passphrase}
        :param private_key_path: Path to a private key for using keypair authentication. Cannot be used with ``browser_auth``, ``oauth_access_token`` or ``password``. Can also be sourced from ``SNOWFLAKE_PRIVATE_KEY_PATH`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#private_key_path SnowflakeProvider#private_key_path}
        :param profile: Sets the profile to read from ~/.snowflake/config file. Can also be sourced from the ``SNOWFLAKE_PROFILE`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#profile SnowflakeProvider#profile}
        :param protocol: Either http or https, defaults to https. Can also be sourced from the ``SNOWFLAKE_PROTOCOL`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#protocol SnowflakeProvider#protocol}
        :param region: Snowflake region, such as "eu-central-1", with this parameter. However, since this parameter is deprecated, it is best to specify the region as part of the account parameter. For details, see the description of the account parameter. `Snowflake region <https://docs.snowflake.com/en/user-guide/intro-regions.html>`_ to use. Required if using the `legacy format for the ``account`` identifier <https://docs.snowflake.com/en/user-guide/admin-account-identifier.html#format-2-legacy-account-locator-in-a-region>`_ in the form of ``<cloud_region_id>.<cloud>``. Can also be sourced from the ``SNOWFLAKE_REGION`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#region SnowflakeProvider#region}
        :param request_timeout: request retry timeout EXCLUDING network roundtrip and read out http response. Can also be sourced from the ``SNOWFLAKE_REQUEST_TIMEOUT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#request_timeout SnowflakeProvider#request_timeout}
        :param role: Specifies the role to use by default for accessing Snowflake objects in the client session. Can also be sourced from the ``SNOWFLAKE_ROLE`` environment variable. . Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#role SnowflakeProvider#role}
        :param session_params: Sets session parameters. `Parameters <https://docs.snowflake.com/en/sql-reference/parameters>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#session_params SnowflakeProvider#session_params}
        :param token: Token to use for OAuth and other forms of token based auth. Can also be sourced from the ``SNOWFLAKE_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#token SnowflakeProvider#token}
        :param token_accessor: token_accessor block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#token_accessor SnowflakeProvider#token_accessor}
        :param user: Username. Can also be sourced from the ``SNOWFLAKE_USER`` environment variable. Required unless using ``profile``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#user SnowflakeProvider#user}
        :param username: Username for username+password authentication. Can also be sourced from the ``SNOWFLAKE_USERNAME`` environment variable. Required unless using ``profile``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#username SnowflakeProvider#username}
        :param validate_default_parameters: True by default. If false, disables the validation checks for Database, Schema, Warehouse and Role at the time a connection is established. Can also be sourced from the ``SNOWFLAKE_VALIDATE_DEFAULT_PARAMETERS`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#validate_default_parameters SnowflakeProvider#validate_default_parameters}
        :param warehouse: Specifies the virtual warehouse to use by default for queries, loading, etc. in the client session. Can also be sourced from the ``SNOWFLAKE_WAREHOUSE`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#warehouse SnowflakeProvider#warehouse}
        '''
        if isinstance(token_accessor, dict):
            token_accessor = SnowflakeProviderTokenAccessor(**token_accessor)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e84bb0483800dda7e061db008e0e400dcb834624a9f09076e86185fce1a232ed)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument authenticator", value=authenticator, expected_type=type_hints["authenticator"])
            check_type(argname="argument browser_auth", value=browser_auth, expected_type=type_hints["browser_auth"])
            check_type(argname="argument client_ip", value=client_ip, expected_type=type_hints["client_ip"])
            check_type(argname="argument client_request_mfa_token", value=client_request_mfa_token, expected_type=type_hints["client_request_mfa_token"])
            check_type(argname="argument client_store_temporary_credential", value=client_store_temporary_credential, expected_type=type_hints["client_store_temporary_credential"])
            check_type(argname="argument client_timeout", value=client_timeout, expected_type=type_hints["client_timeout"])
            check_type(argname="argument disable_query_context_cache", value=disable_query_context_cache, expected_type=type_hints["disable_query_context_cache"])
            check_type(argname="argument disable_telemetry", value=disable_telemetry, expected_type=type_hints["disable_telemetry"])
            check_type(argname="argument external_browser_timeout", value=external_browser_timeout, expected_type=type_hints["external_browser_timeout"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument insecure_mode", value=insecure_mode, expected_type=type_hints["insecure_mode"])
            check_type(argname="argument jwt_client_timeout", value=jwt_client_timeout, expected_type=type_hints["jwt_client_timeout"])
            check_type(argname="argument jwt_expire_timeout", value=jwt_expire_timeout, expected_type=type_hints["jwt_expire_timeout"])
            check_type(argname="argument keep_session_alive", value=keep_session_alive, expected_type=type_hints["keep_session_alive"])
            check_type(argname="argument login_timeout", value=login_timeout, expected_type=type_hints["login_timeout"])
            check_type(argname="argument oauth_access_token", value=oauth_access_token, expected_type=type_hints["oauth_access_token"])
            check_type(argname="argument oauth_client_id", value=oauth_client_id, expected_type=type_hints["oauth_client_id"])
            check_type(argname="argument oauth_client_secret", value=oauth_client_secret, expected_type=type_hints["oauth_client_secret"])
            check_type(argname="argument oauth_endpoint", value=oauth_endpoint, expected_type=type_hints["oauth_endpoint"])
            check_type(argname="argument oauth_redirect_url", value=oauth_redirect_url, expected_type=type_hints["oauth_redirect_url"])
            check_type(argname="argument oauth_refresh_token", value=oauth_refresh_token, expected_type=type_hints["oauth_refresh_token"])
            check_type(argname="argument ocsp_fail_open", value=ocsp_fail_open, expected_type=type_hints["ocsp_fail_open"])
            check_type(argname="argument okta_url", value=okta_url, expected_type=type_hints["okta_url"])
            check_type(argname="argument params", value=params, expected_type=type_hints["params"])
            check_type(argname="argument passcode", value=passcode, expected_type=type_hints["passcode"])
            check_type(argname="argument passcode_in_password", value=passcode_in_password, expected_type=type_hints["passcode_in_password"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument private_key_passphrase", value=private_key_passphrase, expected_type=type_hints["private_key_passphrase"])
            check_type(argname="argument private_key_path", value=private_key_path, expected_type=type_hints["private_key_path"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument request_timeout", value=request_timeout, expected_type=type_hints["request_timeout"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument session_params", value=session_params, expected_type=type_hints["session_params"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument token_accessor", value=token_accessor, expected_type=type_hints["token_accessor"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument validate_default_parameters", value=validate_default_parameters, expected_type=type_hints["validate_default_parameters"])
            check_type(argname="argument warehouse", value=warehouse, expected_type=type_hints["warehouse"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if account is not None:
            self._values["account"] = account
        if alias is not None:
            self._values["alias"] = alias
        if authenticator is not None:
            self._values["authenticator"] = authenticator
        if browser_auth is not None:
            self._values["browser_auth"] = browser_auth
        if client_ip is not None:
            self._values["client_ip"] = client_ip
        if client_request_mfa_token is not None:
            self._values["client_request_mfa_token"] = client_request_mfa_token
        if client_store_temporary_credential is not None:
            self._values["client_store_temporary_credential"] = client_store_temporary_credential
        if client_timeout is not None:
            self._values["client_timeout"] = client_timeout
        if disable_query_context_cache is not None:
            self._values["disable_query_context_cache"] = disable_query_context_cache
        if disable_telemetry is not None:
            self._values["disable_telemetry"] = disable_telemetry
        if external_browser_timeout is not None:
            self._values["external_browser_timeout"] = external_browser_timeout
        if host is not None:
            self._values["host"] = host
        if insecure_mode is not None:
            self._values["insecure_mode"] = insecure_mode
        if jwt_client_timeout is not None:
            self._values["jwt_client_timeout"] = jwt_client_timeout
        if jwt_expire_timeout is not None:
            self._values["jwt_expire_timeout"] = jwt_expire_timeout
        if keep_session_alive is not None:
            self._values["keep_session_alive"] = keep_session_alive
        if login_timeout is not None:
            self._values["login_timeout"] = login_timeout
        if oauth_access_token is not None:
            self._values["oauth_access_token"] = oauth_access_token
        if oauth_client_id is not None:
            self._values["oauth_client_id"] = oauth_client_id
        if oauth_client_secret is not None:
            self._values["oauth_client_secret"] = oauth_client_secret
        if oauth_endpoint is not None:
            self._values["oauth_endpoint"] = oauth_endpoint
        if oauth_redirect_url is not None:
            self._values["oauth_redirect_url"] = oauth_redirect_url
        if oauth_refresh_token is not None:
            self._values["oauth_refresh_token"] = oauth_refresh_token
        if ocsp_fail_open is not None:
            self._values["ocsp_fail_open"] = ocsp_fail_open
        if okta_url is not None:
            self._values["okta_url"] = okta_url
        if params is not None:
            self._values["params"] = params
        if passcode is not None:
            self._values["passcode"] = passcode
        if passcode_in_password is not None:
            self._values["passcode_in_password"] = passcode_in_password
        if password is not None:
            self._values["password"] = password
        if port is not None:
            self._values["port"] = port
        if private_key is not None:
            self._values["private_key"] = private_key
        if private_key_passphrase is not None:
            self._values["private_key_passphrase"] = private_key_passphrase
        if private_key_path is not None:
            self._values["private_key_path"] = private_key_path
        if profile is not None:
            self._values["profile"] = profile
        if protocol is not None:
            self._values["protocol"] = protocol
        if region is not None:
            self._values["region"] = region
        if request_timeout is not None:
            self._values["request_timeout"] = request_timeout
        if role is not None:
            self._values["role"] = role
        if session_params is not None:
            self._values["session_params"] = session_params
        if token is not None:
            self._values["token"] = token
        if token_accessor is not None:
            self._values["token_accessor"] = token_accessor
        if user is not None:
            self._values["user"] = user
        if username is not None:
            self._values["username"] = username
        if validate_default_parameters is not None:
            self._values["validate_default_parameters"] = validate_default_parameters
        if warehouse is not None:
            self._values["warehouse"] = warehouse

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''Specifies your Snowflake account identifier assigned, by Snowflake.

        For information about account identifiers, see the `Snowflake documentation <https://docs.snowflake.com/en/user-guide/admin-account-identifier.html>`_. Can also be sourced from the ``SNOWFLAKE_ACCOUNT`` environment variable. Required unless using ``profile``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#account SnowflakeProvider#account}
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#alias SnowflakeProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authenticator(self) -> typing.Optional[builtins.str]:
        '''Specifies the `authentication type <https://pkg.go.dev/github.com/snowflakedb/gosnowflake#AuthType>`_ to use when connecting to Snowflake. Valid values include: Snowflake, OAuth, ExternalBrowser, Okta, JWT, TokenAccessor, UsernamePasswordMFA. Can also be sourced from the ``SNOWFLAKE_AUTHENTICATOR`` environment variable. It has to be set explicitly to JWT for private key authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#authenticator SnowflakeProvider#authenticator}
        '''
        result = self._values.get("authenticator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def browser_auth(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Required when ``oauth_refresh_token`` is used. Can also be sourced from ``SNOWFLAKE_USE_BROWSER_AUTH`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#browser_auth SnowflakeProvider#browser_auth}
        '''
        result = self._values.get("browser_auth")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def client_ip(self) -> typing.Optional[builtins.str]:
        '''IP address for network checks. Can also be sourced from the ``SNOWFLAKE_CLIENT_IP`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#client_ip SnowflakeProvider#client_ip}
        '''
        result = self._values.get("client_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_request_mfa_token(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When true the MFA token is cached in the credential manager.

        True by default in Windows/OSX. False for Linux. Can also be sourced from the ``SNOWFLAKE_CLIENT_REQUEST_MFA_TOKEN`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#client_request_mfa_token SnowflakeProvider#client_request_mfa_token}
        '''
        result = self._values.get("client_request_mfa_token")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def client_store_temporary_credential(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When true the ID token is cached in the credential manager.

        True by default in Windows/OSX. False for Linux. Can also be sourced from the ``SNOWFLAKE_CLIENT_STORE_TEMPORARY_CREDENTIAL`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#client_store_temporary_credential SnowflakeProvider#client_store_temporary_credential}
        '''
        result = self._values.get("client_store_temporary_credential")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def client_timeout(self) -> typing.Optional[jsii.Number]:
        '''The timeout in seconds for the client to complete the authentication.

        Default is 900 seconds. Can also be sourced from the ``SNOWFLAKE_CLIENT_TIMEOUT`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#client_timeout SnowflakeProvider#client_timeout}
        '''
        result = self._values.get("client_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disable_query_context_cache(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Should HTAP query context cache be disabled. Can also be sourced from the ``SNOWFLAKE_DISABLE_QUERY_CONTEXT_CACHE`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#disable_query_context_cache SnowflakeProvider#disable_query_context_cache}
        '''
        result = self._values.get("disable_query_context_cache")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def disable_telemetry(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Indicates whether to disable telemetry. Can also be sourced from the ``SNOWFLAKE_DISABLE_TELEMETRY`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#disable_telemetry SnowflakeProvider#disable_telemetry}
        '''
        result = self._values.get("disable_telemetry")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def external_browser_timeout(self) -> typing.Optional[jsii.Number]:
        '''The timeout in seconds for the external browser to complete the authentication.

        Default is 120 seconds. Can also be sourced from the ``SNOWFLAKE_EXTERNAL_BROWSER_TIMEOUT`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#external_browser_timeout SnowflakeProvider#external_browser_timeout}
        '''
        result = self._values.get("external_browser_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Supports passing in a custom host value to the snowflake go driver for use with privatelink.

        Can also be sourced from the ``SNOWFLAKE_HOST`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#host SnowflakeProvider#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure_mode(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, bypass the Online Certificate Status Protocol (OCSP) certificate revocation check.

        IMPORTANT: Change the default value for testing or emergency situations only. Can also be sourced from the ``SNOWFLAKE_INSECURE_MODE`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#insecure_mode SnowflakeProvider#insecure_mode}
        '''
        result = self._values.get("insecure_mode")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def jwt_client_timeout(self) -> typing.Optional[jsii.Number]:
        '''The timeout in seconds for the JWT client to complete the authentication.

        Default is 10 seconds. Can also be sourced from the ``SNOWFLAKE_JWT_CLIENT_TIMEOUT`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#jwt_client_timeout SnowflakeProvider#jwt_client_timeout}
        '''
        result = self._values.get("jwt_client_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def jwt_expire_timeout(self) -> typing.Optional[jsii.Number]:
        '''JWT expire after timeout in seconds. Can also be sourced from the ``SNOWFLAKE_JWT_EXPIRE_TIMEOUT`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#jwt_expire_timeout SnowflakeProvider#jwt_expire_timeout}
        '''
        result = self._values.get("jwt_expire_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def keep_session_alive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enables the session to persist even after the connection is closed.

        Can also be sourced from the ``SNOWFLAKE_KEEP_SESSION_ALIVE`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#keep_session_alive SnowflakeProvider#keep_session_alive}
        '''
        result = self._values.get("keep_session_alive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def login_timeout(self) -> typing.Optional[jsii.Number]:
        '''Login retry timeout EXCLUDING network roundtrip and read out http response.

        Can also be sourced from the ``SNOWFLAKE_LOGIN_TIMEOUT`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#login_timeout SnowflakeProvider#login_timeout}
        '''
        result = self._values.get("login_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def oauth_access_token(self) -> typing.Optional[builtins.str]:
        '''Token for use with OAuth.

        Generating the token is left to other tools. Cannot be used with ``browser_auth``, ``private_key_path``, ``oauth_refresh_token`` or ``password``. Can also be sourced from ``SNOWFLAKE_OAUTH_ACCESS_TOKEN`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#oauth_access_token SnowflakeProvider#oauth_access_token}
        '''
        result = self._values.get("oauth_access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_client_id(self) -> typing.Optional[builtins.str]:
        '''Required when ``oauth_refresh_token`` is used. Can also be sourced from ``SNOWFLAKE_OAUTH_CLIENT_ID`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#oauth_client_id SnowflakeProvider#oauth_client_id}
        '''
        result = self._values.get("oauth_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_client_secret(self) -> typing.Optional[builtins.str]:
        '''Required when ``oauth_refresh_token`` is used. Can also be sourced from ``SNOWFLAKE_OAUTH_CLIENT_SECRET`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#oauth_client_secret SnowflakeProvider#oauth_client_secret}
        '''
        result = self._values.get("oauth_client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_endpoint(self) -> typing.Optional[builtins.str]:
        '''Required when ``oauth_refresh_token`` is used. Can also be sourced from ``SNOWFLAKE_OAUTH_ENDPOINT`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#oauth_endpoint SnowflakeProvider#oauth_endpoint}
        '''
        result = self._values.get("oauth_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_redirect_url(self) -> typing.Optional[builtins.str]:
        '''Required when ``oauth_refresh_token`` is used. Can also be sourced from ``SNOWFLAKE_OAUTH_REDIRECT_URL`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#oauth_redirect_url SnowflakeProvider#oauth_redirect_url}
        '''
        result = self._values.get("oauth_redirect_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_refresh_token(self) -> typing.Optional[builtins.str]:
        '''Token for use with OAuth.

        Setup and generation of the token is left to other tools. Should be used in conjunction with ``oauth_client_id``, ``oauth_client_secret``, ``oauth_endpoint``, ``oauth_redirect_url``. Cannot be used with ``browser_auth``, ``private_key_path``, ``oauth_access_token`` or ``password``. Can also be sourced from ``SNOWFLAKE_OAUTH_REFRESH_TOKEN`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#oauth_refresh_token SnowflakeProvider#oauth_refresh_token}
        '''
        result = self._values.get("oauth_refresh_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ocsp_fail_open(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''True represents OCSP fail open mode.

        False represents OCSP fail closed mode. Fail open true by default. Can also be sourced from the ``SNOWFLAKE_OCSP_FAIL_OPEN`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#ocsp_fail_open SnowflakeProvider#ocsp_fail_open}
        '''
        result = self._values.get("ocsp_fail_open")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def okta_url(self) -> typing.Optional[builtins.str]:
        '''The URL of the Okta server. e.g. https://example.okta.com. Can also be sourced from the ``SNOWFLAKE_OKTA_URL`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#okta_url SnowflakeProvider#okta_url}
        '''
        result = self._values.get("okta_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def params(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Sets other connection (i.e. session) parameters. `Parameters <https://docs.snowflake.com/en/sql-reference/parameters>`_.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#params SnowflakeProvider#params}
        '''
        result = self._values.get("params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def passcode(self) -> typing.Optional[builtins.str]:
        '''Specifies the passcode provided by Duo when using multi-factor authentication (MFA) for login.

        Can also be sourced from the ``SNOWFLAKE_PASSCODE`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#passcode SnowflakeProvider#passcode}
        '''
        result = self._values.get("passcode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def passcode_in_password(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''False by default.

        Set to true if the MFA passcode is embedded in the login password. Appends the MFA passcode to the end of the password. Can also be sourced from the ``SNOWFLAKE_PASSCODE_IN_PASSWORD`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#passcode_in_password SnowflakeProvider#passcode_in_password}
        '''
        result = self._values.get("passcode_in_password")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password for username+password auth.

        Cannot be used with ``browser_auth`` or ``private_key_path``. Can also be sourced from the ``SNOWFLAKE_PASSWORD`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#password SnowflakeProvider#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Support custom port values to snowflake go driver for use with privatelink.

        Can also be sourced from the ``SNOWFLAKE_PORT`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#port SnowflakeProvider#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''Private Key for username+private-key auth.

        Cannot be used with ``browser_auth`` or ``password``. Can also be sourced from ``SNOWFLAKE_PRIVATE_KEY`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#private_key SnowflakeProvider#private_key}
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_key_passphrase(self) -> typing.Optional[builtins.str]:
        '''Supports the encryption ciphers aes-128-cbc, aes-128-gcm, aes-192-cbc, aes-192-gcm, aes-256-cbc, aes-256-gcm, and des-ede3-cbc.

        Can also be sourced from ``SNOWFLAKE_PRIVATE_KEY_PASSPHRASE`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#private_key_passphrase SnowflakeProvider#private_key_passphrase}
        '''
        result = self._values.get("private_key_passphrase")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_key_path(self) -> typing.Optional[builtins.str]:
        '''Path to a private key for using keypair authentication.

        Cannot be used with ``browser_auth``, ``oauth_access_token`` or ``password``. Can also be sourced from ``SNOWFLAKE_PRIVATE_KEY_PATH`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#private_key_path SnowflakeProvider#private_key_path}
        '''
        result = self._values.get("private_key_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Sets the profile to read from ~/.snowflake/config file. Can also be sourced from the ``SNOWFLAKE_PROFILE`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#profile SnowflakeProvider#profile}
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Either http or https, defaults to https. Can also be sourced from the ``SNOWFLAKE_PROTOCOL`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#protocol SnowflakeProvider#protocol}
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Snowflake region, such as "eu-central-1", with this parameter.

        However, since this parameter is deprecated, it is best to specify the region as part of the account parameter. For details, see the description of the account parameter. `Snowflake region <https://docs.snowflake.com/en/user-guide/intro-regions.html>`_ to use.  Required if using the `legacy format for the ``account`` identifier <https://docs.snowflake.com/en/user-guide/admin-account-identifier.html#format-2-legacy-account-locator-in-a-region>`_ in the form of ``<cloud_region_id>.<cloud>``. Can also be sourced from the ``SNOWFLAKE_REGION`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#region SnowflakeProvider#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_timeout(self) -> typing.Optional[jsii.Number]:
        '''request retry timeout EXCLUDING network roundtrip and read out http response.

        Can also be sourced from the ``SNOWFLAKE_REQUEST_TIMEOUT`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#request_timeout SnowflakeProvider#request_timeout}
        '''
        result = self._values.get("request_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''Specifies the role to use by default for accessing Snowflake objects in the client session.

        Can also be sourced from the ``SNOWFLAKE_ROLE`` environment variable. .

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#role SnowflakeProvider#role}
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Sets session parameters. `Parameters <https://docs.snowflake.com/en/sql-reference/parameters>`_.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#session_params SnowflakeProvider#session_params}
        '''
        result = self._values.get("session_params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''Token to use for OAuth and other forms of token based auth.

        Can also be sourced from the ``SNOWFLAKE_TOKEN`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#token SnowflakeProvider#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_accessor(self) -> typing.Optional["SnowflakeProviderTokenAccessor"]:
        '''token_accessor block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#token_accessor SnowflakeProvider#token_accessor}
        '''
        result = self._values.get("token_accessor")
        return typing.cast(typing.Optional["SnowflakeProviderTokenAccessor"], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''Username. Can also be sourced from the ``SNOWFLAKE_USER`` environment variable. Required unless using ``profile``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#user SnowflakeProvider#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Username for username+password authentication. Can also be sourced from the ``SNOWFLAKE_USERNAME`` environment variable. Required unless using ``profile``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#username SnowflakeProvider#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validate_default_parameters(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''True by default.

        If false, disables the validation checks for Database, Schema, Warehouse and Role at the time a connection is established. Can also be sourced from the ``SNOWFLAKE_VALIDATE_DEFAULT_PARAMETERS`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#validate_default_parameters SnowflakeProvider#validate_default_parameters}
        '''
        result = self._values.get("validate_default_parameters")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def warehouse(self) -> typing.Optional[builtins.str]:
        '''Specifies the virtual warehouse to use by default for queries, loading, etc.

        in the client session. Can also be sourced from the ``SNOWFLAKE_WAREHOUSE`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#warehouse SnowflakeProvider#warehouse}
        '''
        result = self._values.get("warehouse")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SnowflakeProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.provider.SnowflakeProviderTokenAccessor",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "redirect_uri": "redirectUri",
        "refresh_token": "refreshToken",
        "token_endpoint": "tokenEndpoint",
    },
)
class SnowflakeProviderTokenAccessor:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        redirect_uri: builtins.str,
        refresh_token: builtins.str,
        token_endpoint: builtins.str,
    ) -> None:
        '''
        :param client_id: The client ID for the OAuth provider when using a refresh token to renew access token. Can also be sourced from the ``SNOWFLAKE_TOKEN_ACCESSOR_CLIENT_ID`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#client_id SnowflakeProvider#client_id}
        :param client_secret: The client secret for the OAuth provider when using a refresh token to renew access token. Can also be sourced from the ``SNOWFLAKE_TOKEN_ACCESSOR_CLIENT_SECRET`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#client_secret SnowflakeProvider#client_secret}
        :param redirect_uri: The redirect URI for the OAuth provider when using a refresh token to renew access token. Can also be sourced from the ``SNOWFLAKE_TOKEN_ACCESSOR_REDIRECT_URI`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#redirect_uri SnowflakeProvider#redirect_uri}
        :param refresh_token: The refresh token for the OAuth provider when using a refresh token to renew access token. Can also be sourced from the ``SNOWFLAKE_TOKEN_ACCESSOR_REFRESH_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#refresh_token SnowflakeProvider#refresh_token}
        :param token_endpoint: The token endpoint for the OAuth provider e.g. https://{yourDomain}/oauth/token when using a refresh token to renew access token. Can also be sourced from the ``SNOWFLAKE_TOKEN_ACCESSOR_TOKEN_ENDPOINT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#token_endpoint SnowflakeProvider#token_endpoint}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1128816df89d2a749b0e5810c787caadc6cc459628345c3c8a737c1565945960)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
            check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
            check_type(argname="argument token_endpoint", value=token_endpoint, expected_type=type_hints["token_endpoint"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
            "refresh_token": refresh_token,
            "token_endpoint": token_endpoint,
        }

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The client ID for the OAuth provider when using a refresh token to renew access token.

        Can also be sourced from the ``SNOWFLAKE_TOKEN_ACCESSOR_CLIENT_ID`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#client_id SnowflakeProvider#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''The client secret for the OAuth provider when using a refresh token to renew access token.

        Can also be sourced from the ``SNOWFLAKE_TOKEN_ACCESSOR_CLIENT_SECRET`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#client_secret SnowflakeProvider#client_secret}
        '''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def redirect_uri(self) -> builtins.str:
        '''The redirect URI for the OAuth provider when using a refresh token to renew access token.

        Can also be sourced from the ``SNOWFLAKE_TOKEN_ACCESSOR_REDIRECT_URI`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#redirect_uri SnowflakeProvider#redirect_uri}
        '''
        result = self._values.get("redirect_uri")
        assert result is not None, "Required property 'redirect_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def refresh_token(self) -> builtins.str:
        '''The refresh token for the OAuth provider when using a refresh token to renew access token.

        Can also be sourced from the ``SNOWFLAKE_TOKEN_ACCESSOR_REFRESH_TOKEN`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#refresh_token SnowflakeProvider#refresh_token}
        '''
        result = self._values.get("refresh_token")
        assert result is not None, "Required property 'refresh_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token_endpoint(self) -> builtins.str:
        '''The token endpoint for the OAuth provider e.g. https://{yourDomain}/oauth/token when using a refresh token to renew access token. Can also be sourced from the ``SNOWFLAKE_TOKEN_ACCESSOR_TOKEN_ENDPOINT`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs#token_endpoint SnowflakeProvider#token_endpoint}
        '''
        result = self._values.get("token_endpoint")
        assert result is not None, "Required property 'token_endpoint' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SnowflakeProviderTokenAccessor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SnowflakeProvider",
    "SnowflakeProviderConfig",
    "SnowflakeProviderTokenAccessor",
]

publication.publish()

def _typecheckingstub__dffb8c16f0bdbd356b60ba75b76332c0fa5872a9b67c09d939ada39e30798782(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    account: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    authenticator: typing.Optional[builtins.str] = None,
    browser_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    client_ip: typing.Optional[builtins.str] = None,
    client_request_mfa_token: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    client_store_temporary_credential: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    client_timeout: typing.Optional[jsii.Number] = None,
    disable_query_context_cache: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    disable_telemetry: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    external_browser_timeout: typing.Optional[jsii.Number] = None,
    host: typing.Optional[builtins.str] = None,
    insecure_mode: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    jwt_client_timeout: typing.Optional[jsii.Number] = None,
    jwt_expire_timeout: typing.Optional[jsii.Number] = None,
    keep_session_alive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    login_timeout: typing.Optional[jsii.Number] = None,
    oauth_access_token: typing.Optional[builtins.str] = None,
    oauth_client_id: typing.Optional[builtins.str] = None,
    oauth_client_secret: typing.Optional[builtins.str] = None,
    oauth_endpoint: typing.Optional[builtins.str] = None,
    oauth_redirect_url: typing.Optional[builtins.str] = None,
    oauth_refresh_token: typing.Optional[builtins.str] = None,
    ocsp_fail_open: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    okta_url: typing.Optional[builtins.str] = None,
    params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    passcode: typing.Optional[builtins.str] = None,
    passcode_in_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    private_key: typing.Optional[builtins.str] = None,
    private_key_passphrase: typing.Optional[builtins.str] = None,
    private_key_path: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    request_timeout: typing.Optional[jsii.Number] = None,
    role: typing.Optional[builtins.str] = None,
    session_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    token: typing.Optional[builtins.str] = None,
    token_accessor: typing.Optional[typing.Union[SnowflakeProviderTokenAccessor, typing.Dict[builtins.str, typing.Any]]] = None,
    user: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
    validate_default_parameters: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    warehouse: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65a3a5ee41e1141e62bec029bdb8709bf3cc38a98cb6c277789fc640ecc924d2(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c95f157df42af058823cb6b649f9183b7256fb0ab7fd9117970ad5629398e73(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cdc7cd12d304b2eddd5316af316d83f132ecae360404d6176a8e6a997e8dc2e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b6d6a40d1a5605a9094439f3d2d1e57d143ffa3c2083b130937df91f19b35b4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8c0e664296c25b62d60022f48050f4a74aa8c1523109e28179f692a2663de4a(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__370f87780241c7b2653971c27701eed45e4fc0fea1e1c19909bf4822f9a35139(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f642b106f9ead7f93ccfef26461a60434d7ce40769a4318d6de7980d579723d(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6586aace401480ef0ce4ab53207770ca079b6a438409c516fcce530b59649f36(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__818f5069d0221466e050c5c53b6b1e3eaaac0d5a53109481e4ead46297f0b141(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9abcf60fa4330b65affc6db33362afcc184ad771a4fafb37665309283f9986ed(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__269dfbf8bd7e9687bd9093ed943acb915d1e33d5f2a1d222d2ebe73340152dd5(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be356c932dd3785d09f2c4a5c787d88fcbbb1846738765a3ac6f6118bf230c45(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25df655b6fdfcfce4cc80d4c7d317296ba4b1b1e6a48e51e051a48b933da7a96(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c0b770f66297cf03ca54574462492185fa522c242f96b03b32317dc69d38166(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86c2273f5de1a2697d59b298ef8372bd657956bd24ac15953410953c6bc5e48e(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e006c8754a599103a5f7c5d6363a2fd8f44dbc569d9882eab0fe73527000b263(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a87491bfb7b1ecfe9103c8dddaf7734ff39eb830fb1a351d40dc0f7c1adb4d2b(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e932bf3dd2379e89075f4162cb5bc10d1da873452b7e84361af61777412cd1fc(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5450d12035fdb7aaeb95891a55c7092fd9095bf121f6a46710c8d0c0dec4e47(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04343d423fd2ac1d04d8dc2589d3d4e29413748a1ee5c9c2b0550410c98eaee5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7480aa87e81ad2f94226ea84240e1ecc31b405fa1a0b01bdf20de287d88791c3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92517d42922dc0c4dffe77d60eb82ffb67cf253e0cd04d4e1f3350fe80ca0c75(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6be019a61f9ea18a8a1b32731eadb4549c228e9ede8c9435b4758f99753584cb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ef289860c28b0549c58795a27ffbdc287f7d4899317c1c4e9337b035b23deb8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5794c009d8765aa8f769a80e9753aabe08dc725863ff7b18eab0341eed543c64(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d2acb8cea3c2b00df9129f4f3b5786e34b302b4fbbe61119d57006a7804f3f1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5079b47ba384ea5e3aaafe6322f07c7068ea187e00a883751b397324ec04b6c8(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8aeb67752ef65d8786754b2e094e8334d801727dcb831c2a6d6bbbd59c0c6ec(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90d285d39d0d7dfff15a4462be9b03f6e0824d61185275e2de835935b4db1d4d(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4647c5ce21749b9912e9bb483866a4fe9decad7840786080279fac4bf9b9881(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14ab59f5493ec686723d4a013bc5f681695f8805e1a21d0e2961ffb9ba96bb2a(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__174acb5ca0c2f03f2c07759d01042240477d689ab50d9a3e5014d671f7072072(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8e45747860bace19eea01fe56764a0071fb76645a7df1767604942c712bc7fe(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a869d7e0ed58d955c8747da9c6e46d8bcb7d2e8292dc085324fc4f66cd00101c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2890938b1cd71ed7815000e422a912b7b3d54903511d4f7b45712b5a30212795(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__272d3205644fbaa065eff9f5ac6d27774f4829ae96c327fd974c31e2c14d17ff(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f532710ad9671b193f560280c447d334b62fa15f62b4acf87f79137b647b9c9f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee0543502fab097af52ebd9c81a19791d58a795a589dead81d2ddb4e53710eab(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63c825aa96baa5ca037e135d9294ae15fc9d5395c87a9275884dd82a5edd2ce8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1a9fc5c69b7d4729ea79396ad290778ac78f6cf5f7a4ed625289b1d10760b75(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40535fefad35c2491bb2aa60c6522f5cd80fc0876e21c80deb2f684e33cf2380(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89b86051ecb7af168b4414164285a52653116c6c1fd66e45e577d5e94b071fe5(
    value: typing.Optional[SnowflakeProviderTokenAccessor],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc30eb22eb05f35288fb4961dd14be1e1fe9101084acdde298c42009214db961(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6a7f197bfe45836bef3f6471be6cc78940528379421b34d0bd051af02cc9b5c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b43646ed314e4eea24bb621b967fbe094538e70a124a4c7cc36c518a3834ac02(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d86a20638ec60e4335171ba31cc595ce61cbb7fbb325816de15f3387860facb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e84bb0483800dda7e061db008e0e400dcb834624a9f09076e86185fce1a232ed(
    *,
    account: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    authenticator: typing.Optional[builtins.str] = None,
    browser_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    client_ip: typing.Optional[builtins.str] = None,
    client_request_mfa_token: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    client_store_temporary_credential: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    client_timeout: typing.Optional[jsii.Number] = None,
    disable_query_context_cache: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    disable_telemetry: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    external_browser_timeout: typing.Optional[jsii.Number] = None,
    host: typing.Optional[builtins.str] = None,
    insecure_mode: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    jwt_client_timeout: typing.Optional[jsii.Number] = None,
    jwt_expire_timeout: typing.Optional[jsii.Number] = None,
    keep_session_alive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    login_timeout: typing.Optional[jsii.Number] = None,
    oauth_access_token: typing.Optional[builtins.str] = None,
    oauth_client_id: typing.Optional[builtins.str] = None,
    oauth_client_secret: typing.Optional[builtins.str] = None,
    oauth_endpoint: typing.Optional[builtins.str] = None,
    oauth_redirect_url: typing.Optional[builtins.str] = None,
    oauth_refresh_token: typing.Optional[builtins.str] = None,
    ocsp_fail_open: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    okta_url: typing.Optional[builtins.str] = None,
    params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    passcode: typing.Optional[builtins.str] = None,
    passcode_in_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    private_key: typing.Optional[builtins.str] = None,
    private_key_passphrase: typing.Optional[builtins.str] = None,
    private_key_path: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    request_timeout: typing.Optional[jsii.Number] = None,
    role: typing.Optional[builtins.str] = None,
    session_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    token: typing.Optional[builtins.str] = None,
    token_accessor: typing.Optional[typing.Union[SnowflakeProviderTokenAccessor, typing.Dict[builtins.str, typing.Any]]] = None,
    user: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
    validate_default_parameters: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    warehouse: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1128816df89d2a749b0e5810c787caadc6cc459628345c3c8a737c1565945960(
    *,
    client_id: builtins.str,
    client_secret: builtins.str,
    redirect_uri: builtins.str,
    refresh_token: builtins.str,
    token_endpoint: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

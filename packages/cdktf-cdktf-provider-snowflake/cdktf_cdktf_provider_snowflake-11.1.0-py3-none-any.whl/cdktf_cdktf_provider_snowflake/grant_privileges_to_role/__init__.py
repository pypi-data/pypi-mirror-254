'''
# `snowflake_grant_privileges_to_role`

Refer to the Terraform Registry for docs: [`snowflake_grant_privileges_to_role`](https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role).
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


class GrantPrivilegesToRole(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.grantPrivilegesToRole.GrantPrivilegesToRole",
):
    '''Represents a {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role snowflake_grant_privileges_to_role}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        role_name: builtins.str,
        all_privileges: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        on_account: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        on_account_object: typing.Optional[typing.Union["GrantPrivilegesToRoleOnAccountObject", typing.Dict[builtins.str, typing.Any]]] = None,
        on_schema: typing.Optional[typing.Union["GrantPrivilegesToRoleOnSchema", typing.Dict[builtins.str, typing.Any]]] = None,
        on_schema_object: typing.Optional[typing.Union["GrantPrivilegesToRoleOnSchemaObject", typing.Dict[builtins.str, typing.Any]]] = None,
        privileges: typing.Optional[typing.Sequence[builtins.str]] = None,
        with_grant_option: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role snowflake_grant_privileges_to_role} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param role_name: The fully qualified name of the role to which privileges will be granted. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#role_name GrantPrivilegesToRole#role_name}
        :param all_privileges: Grant all privileges on the account role. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#all_privileges GrantPrivilegesToRole#all_privileges}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#id GrantPrivilegesToRole#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param on_account: If true, the privileges will be granted on the account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#on_account GrantPrivilegesToRole#on_account}
        :param on_account_object: on_account_object block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#on_account_object GrantPrivilegesToRole#on_account_object}
        :param on_schema: on_schema block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#on_schema GrantPrivilegesToRole#on_schema}
        :param on_schema_object: on_schema_object block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#on_schema_object GrantPrivilegesToRole#on_schema_object}
        :param privileges: The privileges to grant on the account role. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#privileges GrantPrivilegesToRole#privileges}
        :param with_grant_option: Specifies whether the grantee can grant the privileges to other users. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#with_grant_option GrantPrivilegesToRole#with_grant_option}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df9b6bac89d7b7dd746aef9ebbff86facffbdbd9cbbcc1b272c36297b61ff96b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GrantPrivilegesToRoleConfig(
            role_name=role_name,
            all_privileges=all_privileges,
            id=id,
            on_account=on_account,
            on_account_object=on_account_object,
            on_schema=on_schema,
            on_schema_object=on_schema_object,
            privileges=privileges,
            with_grant_option=with_grant_option,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a GrantPrivilegesToRole resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the GrantPrivilegesToRole to import.
        :param import_from_id: The id of the existing GrantPrivilegesToRole that should be imported. Refer to the {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the GrantPrivilegesToRole to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da59db44f797e9bc59ec58ecb3d276fbdad3c41cb534f937d8a01b79cdad2508)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putOnAccountObject")
    def put_on_account_object(
        self,
        *,
        object_name: builtins.str,
        object_type: builtins.str,
    ) -> None:
        '''
        :param object_name: The fully qualified name of the object on which privileges will be granted. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#object_name GrantPrivilegesToRole#object_name}
        :param object_type: The object type of the account object on which privileges will be granted. Valid values are: USER | RESOURCE MONITOR | WAREHOUSE | DATABASE | INTEGRATION | FAILOVER GROUP | REPLICATION GROUP | EXTERNAL VOLUME Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#object_type GrantPrivilegesToRole#object_type}
        '''
        value = GrantPrivilegesToRoleOnAccountObject(
            object_name=object_name, object_type=object_type
        )

        return typing.cast(None, jsii.invoke(self, "putOnAccountObject", [value]))

    @jsii.member(jsii_name="putOnSchema")
    def put_on_schema(
        self,
        *,
        all_schemas_in_database: typing.Optional[builtins.str] = None,
        future_schemas_in_database: typing.Optional[builtins.str] = None,
        schema_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param all_schemas_in_database: The fully qualified name of the database. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#all_schemas_in_database GrantPrivilegesToRole#all_schemas_in_database}
        :param future_schemas_in_database: The fully qualified name of the database. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#future_schemas_in_database GrantPrivilegesToRole#future_schemas_in_database}
        :param schema_name: The fully qualified name of the schema. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#schema_name GrantPrivilegesToRole#schema_name}
        '''
        value = GrantPrivilegesToRoleOnSchema(
            all_schemas_in_database=all_schemas_in_database,
            future_schemas_in_database=future_schemas_in_database,
            schema_name=schema_name,
        )

        return typing.cast(None, jsii.invoke(self, "putOnSchema", [value]))

    @jsii.member(jsii_name="putOnSchemaObject")
    def put_on_schema_object(
        self,
        *,
        all: typing.Optional[typing.Union["GrantPrivilegesToRoleOnSchemaObjectAll", typing.Dict[builtins.str, typing.Any]]] = None,
        future: typing.Optional[typing.Union["GrantPrivilegesToRoleOnSchemaObjectFuture", typing.Dict[builtins.str, typing.Any]]] = None,
        object_name: typing.Optional[builtins.str] = None,
        object_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param all: all block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#all GrantPrivilegesToRole#all}
        :param future: future block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#future GrantPrivilegesToRole#future}
        :param object_name: The fully qualified name of the object on which privileges will be granted. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#object_name GrantPrivilegesToRole#object_name}
        :param object_type: The object type of the schema object on which privileges will be granted. Valid values are: ALERT | DYNAMIC TABLE | EVENT TABLE | FILE FORMAT | FUNCTION | ICEBERG TABLE | PROCEDURE | SECRET | SEQUENCE | PIPE | MASKING POLICY | PASSWORD POLICY | ROW ACCESS POLICY | SESSION POLICY | TAG | STAGE | STREAM | TABLE | EXTERNAL TABLE | TASK | VIEW | MATERIALIZED VIEW Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#object_type GrantPrivilegesToRole#object_type}
        '''
        value = GrantPrivilegesToRoleOnSchemaObject(
            all=all, future=future, object_name=object_name, object_type=object_type
        )

        return typing.cast(None, jsii.invoke(self, "putOnSchemaObject", [value]))

    @jsii.member(jsii_name="resetAllPrivileges")
    def reset_all_privileges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllPrivileges", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOnAccount")
    def reset_on_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnAccount", []))

    @jsii.member(jsii_name="resetOnAccountObject")
    def reset_on_account_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnAccountObject", []))

    @jsii.member(jsii_name="resetOnSchema")
    def reset_on_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnSchema", []))

    @jsii.member(jsii_name="resetOnSchemaObject")
    def reset_on_schema_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnSchemaObject", []))

    @jsii.member(jsii_name="resetPrivileges")
    def reset_privileges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivileges", []))

    @jsii.member(jsii_name="resetWithGrantOption")
    def reset_with_grant_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWithGrantOption", []))

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
    @jsii.member(jsii_name="onAccountObject")
    def on_account_object(
        self,
    ) -> "GrantPrivilegesToRoleOnAccountObjectOutputReference":
        return typing.cast("GrantPrivilegesToRoleOnAccountObjectOutputReference", jsii.get(self, "onAccountObject"))

    @builtins.property
    @jsii.member(jsii_name="onSchema")
    def on_schema(self) -> "GrantPrivilegesToRoleOnSchemaOutputReference":
        return typing.cast("GrantPrivilegesToRoleOnSchemaOutputReference", jsii.get(self, "onSchema"))

    @builtins.property
    @jsii.member(jsii_name="onSchemaObject")
    def on_schema_object(self) -> "GrantPrivilegesToRoleOnSchemaObjectOutputReference":
        return typing.cast("GrantPrivilegesToRoleOnSchemaObjectOutputReference", jsii.get(self, "onSchemaObject"))

    @builtins.property
    @jsii.member(jsii_name="allPrivilegesInput")
    def all_privileges_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allPrivilegesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="onAccountInput")
    def on_account_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "onAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="onAccountObjectInput")
    def on_account_object_input(
        self,
    ) -> typing.Optional["GrantPrivilegesToRoleOnAccountObject"]:
        return typing.cast(typing.Optional["GrantPrivilegesToRoleOnAccountObject"], jsii.get(self, "onAccountObjectInput"))

    @builtins.property
    @jsii.member(jsii_name="onSchemaInput")
    def on_schema_input(self) -> typing.Optional["GrantPrivilegesToRoleOnSchema"]:
        return typing.cast(typing.Optional["GrantPrivilegesToRoleOnSchema"], jsii.get(self, "onSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="onSchemaObjectInput")
    def on_schema_object_input(
        self,
    ) -> typing.Optional["GrantPrivilegesToRoleOnSchemaObject"]:
        return typing.cast(typing.Optional["GrantPrivilegesToRoleOnSchemaObject"], jsii.get(self, "onSchemaObjectInput"))

    @builtins.property
    @jsii.member(jsii_name="privilegesInput")
    def privileges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "privilegesInput"))

    @builtins.property
    @jsii.member(jsii_name="roleNameInput")
    def role_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="withGrantOptionInput")
    def with_grant_option_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "withGrantOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="allPrivileges")
    def all_privileges(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allPrivileges"))

    @all_privileges.setter
    def all_privileges(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae2d0fb93445e52b92165c6a295ba8250d2313624055eab84a10146d174ba01c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allPrivileges", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8501f18eab60fb6ab7783788c55cd870cdc25c8c85764ff33e07efd01e65d2d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="onAccount")
    def on_account(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "onAccount"))

    @on_account.setter
    def on_account(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad8485be078d691a540591323a275a507a034eec5afb40342cc2946a4923a190)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onAccount", value)

    @builtins.property
    @jsii.member(jsii_name="privileges")
    def privileges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "privileges"))

    @privileges.setter
    def privileges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99a08e24e5d78c580d7e8493388217245f932fdca73c51ed949542040b227ba3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privileges", value)

    @builtins.property
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleName"))

    @role_name.setter
    def role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c3fc6e1b88460e0bcd4b85a1d51f18504928917047070ed7149f014ba7068a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleName", value)

    @builtins.property
    @jsii.member(jsii_name="withGrantOption")
    def with_grant_option(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "withGrantOption"))

    @with_grant_option.setter
    def with_grant_option(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1498c1b7fa3eab727be362fbfdc0bad741b1a50b92c9b990ce2adb708c37565c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "withGrantOption", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.grantPrivilegesToRole.GrantPrivilegesToRoleConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "role_name": "roleName",
        "all_privileges": "allPrivileges",
        "id": "id",
        "on_account": "onAccount",
        "on_account_object": "onAccountObject",
        "on_schema": "onSchema",
        "on_schema_object": "onSchemaObject",
        "privileges": "privileges",
        "with_grant_option": "withGrantOption",
    },
)
class GrantPrivilegesToRoleConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        role_name: builtins.str,
        all_privileges: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        on_account: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        on_account_object: typing.Optional[typing.Union["GrantPrivilegesToRoleOnAccountObject", typing.Dict[builtins.str, typing.Any]]] = None,
        on_schema: typing.Optional[typing.Union["GrantPrivilegesToRoleOnSchema", typing.Dict[builtins.str, typing.Any]]] = None,
        on_schema_object: typing.Optional[typing.Union["GrantPrivilegesToRoleOnSchemaObject", typing.Dict[builtins.str, typing.Any]]] = None,
        privileges: typing.Optional[typing.Sequence[builtins.str]] = None,
        with_grant_option: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param role_name: The fully qualified name of the role to which privileges will be granted. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#role_name GrantPrivilegesToRole#role_name}
        :param all_privileges: Grant all privileges on the account role. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#all_privileges GrantPrivilegesToRole#all_privileges}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#id GrantPrivilegesToRole#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param on_account: If true, the privileges will be granted on the account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#on_account GrantPrivilegesToRole#on_account}
        :param on_account_object: on_account_object block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#on_account_object GrantPrivilegesToRole#on_account_object}
        :param on_schema: on_schema block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#on_schema GrantPrivilegesToRole#on_schema}
        :param on_schema_object: on_schema_object block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#on_schema_object GrantPrivilegesToRole#on_schema_object}
        :param privileges: The privileges to grant on the account role. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#privileges GrantPrivilegesToRole#privileges}
        :param with_grant_option: Specifies whether the grantee can grant the privileges to other users. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#with_grant_option GrantPrivilegesToRole#with_grant_option}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(on_account_object, dict):
            on_account_object = GrantPrivilegesToRoleOnAccountObject(**on_account_object)
        if isinstance(on_schema, dict):
            on_schema = GrantPrivilegesToRoleOnSchema(**on_schema)
        if isinstance(on_schema_object, dict):
            on_schema_object = GrantPrivilegesToRoleOnSchemaObject(**on_schema_object)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a5ee16345c8b0c6f3c0384a76deedd8d755a73f999a1c40ba515563077a3514)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
            check_type(argname="argument all_privileges", value=all_privileges, expected_type=type_hints["all_privileges"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument on_account", value=on_account, expected_type=type_hints["on_account"])
            check_type(argname="argument on_account_object", value=on_account_object, expected_type=type_hints["on_account_object"])
            check_type(argname="argument on_schema", value=on_schema, expected_type=type_hints["on_schema"])
            check_type(argname="argument on_schema_object", value=on_schema_object, expected_type=type_hints["on_schema_object"])
            check_type(argname="argument privileges", value=privileges, expected_type=type_hints["privileges"])
            check_type(argname="argument with_grant_option", value=with_grant_option, expected_type=type_hints["with_grant_option"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_name": role_name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if all_privileges is not None:
            self._values["all_privileges"] = all_privileges
        if id is not None:
            self._values["id"] = id
        if on_account is not None:
            self._values["on_account"] = on_account
        if on_account_object is not None:
            self._values["on_account_object"] = on_account_object
        if on_schema is not None:
            self._values["on_schema"] = on_schema
        if on_schema_object is not None:
            self._values["on_schema_object"] = on_schema_object
        if privileges is not None:
            self._values["privileges"] = privileges
        if with_grant_option is not None:
            self._values["with_grant_option"] = with_grant_option

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def role_name(self) -> builtins.str:
        '''The fully qualified name of the role to which privileges will be granted.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#role_name GrantPrivilegesToRole#role_name}
        '''
        result = self._values.get("role_name")
        assert result is not None, "Required property 'role_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def all_privileges(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Grant all privileges on the account role.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#all_privileges GrantPrivilegesToRole#all_privileges}
        '''
        result = self._values.get("all_privileges")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#id GrantPrivilegesToRole#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_account(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, the privileges will be granted on the account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#on_account GrantPrivilegesToRole#on_account}
        '''
        result = self._values.get("on_account")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def on_account_object(
        self,
    ) -> typing.Optional["GrantPrivilegesToRoleOnAccountObject"]:
        '''on_account_object block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#on_account_object GrantPrivilegesToRole#on_account_object}
        '''
        result = self._values.get("on_account_object")
        return typing.cast(typing.Optional["GrantPrivilegesToRoleOnAccountObject"], result)

    @builtins.property
    def on_schema(self) -> typing.Optional["GrantPrivilegesToRoleOnSchema"]:
        '''on_schema block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#on_schema GrantPrivilegesToRole#on_schema}
        '''
        result = self._values.get("on_schema")
        return typing.cast(typing.Optional["GrantPrivilegesToRoleOnSchema"], result)

    @builtins.property
    def on_schema_object(
        self,
    ) -> typing.Optional["GrantPrivilegesToRoleOnSchemaObject"]:
        '''on_schema_object block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#on_schema_object GrantPrivilegesToRole#on_schema_object}
        '''
        result = self._values.get("on_schema_object")
        return typing.cast(typing.Optional["GrantPrivilegesToRoleOnSchemaObject"], result)

    @builtins.property
    def privileges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The privileges to grant on the account role.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#privileges GrantPrivilegesToRole#privileges}
        '''
        result = self._values.get("privileges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def with_grant_option(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specifies whether the grantee can grant the privileges to other users.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#with_grant_option GrantPrivilegesToRole#with_grant_option}
        '''
        result = self._values.get("with_grant_option")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrantPrivilegesToRoleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.grantPrivilegesToRole.GrantPrivilegesToRoleOnAccountObject",
    jsii_struct_bases=[],
    name_mapping={"object_name": "objectName", "object_type": "objectType"},
)
class GrantPrivilegesToRoleOnAccountObject:
    def __init__(self, *, object_name: builtins.str, object_type: builtins.str) -> None:
        '''
        :param object_name: The fully qualified name of the object on which privileges will be granted. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#object_name GrantPrivilegesToRole#object_name}
        :param object_type: The object type of the account object on which privileges will be granted. Valid values are: USER | RESOURCE MONITOR | WAREHOUSE | DATABASE | INTEGRATION | FAILOVER GROUP | REPLICATION GROUP | EXTERNAL VOLUME Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#object_type GrantPrivilegesToRole#object_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e2b940dca629c72f603127fe6a29409e15e2652a00195bd24f1a71e719057e2)
            check_type(argname="argument object_name", value=object_name, expected_type=type_hints["object_name"])
            check_type(argname="argument object_type", value=object_type, expected_type=type_hints["object_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object_name": object_name,
            "object_type": object_type,
        }

    @builtins.property
    def object_name(self) -> builtins.str:
        '''The fully qualified name of the object on which privileges will be granted.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#object_name GrantPrivilegesToRole#object_name}
        '''
        result = self._values.get("object_name")
        assert result is not None, "Required property 'object_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object_type(self) -> builtins.str:
        '''The object type of the account object on which privileges will be granted.

        Valid values are: USER | RESOURCE MONITOR | WAREHOUSE | DATABASE | INTEGRATION | FAILOVER GROUP | REPLICATION GROUP | EXTERNAL VOLUME

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#object_type GrantPrivilegesToRole#object_type}
        '''
        result = self._values.get("object_type")
        assert result is not None, "Required property 'object_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrantPrivilegesToRoleOnAccountObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GrantPrivilegesToRoleOnAccountObjectOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.grantPrivilegesToRole.GrantPrivilegesToRoleOnAccountObjectOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04b50230cccb35126081e3572b5f1c597bc59735fa7523942670edb722bb79d9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="objectNameInput")
    def object_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectNameInput"))

    @builtins.property
    @jsii.member(jsii_name="objectTypeInput")
    def object_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="objectName")
    def object_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectName"))

    @object_name.setter
    def object_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b182b48843436ead4ac2a8e07bfe08b6034b475bb6614d3c9c2362a17f14543)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectName", value)

    @builtins.property
    @jsii.member(jsii_name="objectType")
    def object_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectType"))

    @object_type.setter
    def object_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76fc8587e6d9b2238cfd63640e9b8e85423aa05f80aad5d7a3a57fd3f1a67fef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GrantPrivilegesToRoleOnAccountObject]:
        return typing.cast(typing.Optional[GrantPrivilegesToRoleOnAccountObject], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GrantPrivilegesToRoleOnAccountObject],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2d74bb9e5fcab7bd1dcc8cf0a91f524a2d695a3f51786e135cc7f4e8e62d313)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.grantPrivilegesToRole.GrantPrivilegesToRoleOnSchema",
    jsii_struct_bases=[],
    name_mapping={
        "all_schemas_in_database": "allSchemasInDatabase",
        "future_schemas_in_database": "futureSchemasInDatabase",
        "schema_name": "schemaName",
    },
)
class GrantPrivilegesToRoleOnSchema:
    def __init__(
        self,
        *,
        all_schemas_in_database: typing.Optional[builtins.str] = None,
        future_schemas_in_database: typing.Optional[builtins.str] = None,
        schema_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param all_schemas_in_database: The fully qualified name of the database. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#all_schemas_in_database GrantPrivilegesToRole#all_schemas_in_database}
        :param future_schemas_in_database: The fully qualified name of the database. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#future_schemas_in_database GrantPrivilegesToRole#future_schemas_in_database}
        :param schema_name: The fully qualified name of the schema. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#schema_name GrantPrivilegesToRole#schema_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce19377181accfbda92f741a0364170e08f650d7dc9ffc12bcf1337d71093c9e)
            check_type(argname="argument all_schemas_in_database", value=all_schemas_in_database, expected_type=type_hints["all_schemas_in_database"])
            check_type(argname="argument future_schemas_in_database", value=future_schemas_in_database, expected_type=type_hints["future_schemas_in_database"])
            check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if all_schemas_in_database is not None:
            self._values["all_schemas_in_database"] = all_schemas_in_database
        if future_schemas_in_database is not None:
            self._values["future_schemas_in_database"] = future_schemas_in_database
        if schema_name is not None:
            self._values["schema_name"] = schema_name

    @builtins.property
    def all_schemas_in_database(self) -> typing.Optional[builtins.str]:
        '''The fully qualified name of the database.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#all_schemas_in_database GrantPrivilegesToRole#all_schemas_in_database}
        '''
        result = self._values.get("all_schemas_in_database")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def future_schemas_in_database(self) -> typing.Optional[builtins.str]:
        '''The fully qualified name of the database.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#future_schemas_in_database GrantPrivilegesToRole#future_schemas_in_database}
        '''
        result = self._values.get("future_schemas_in_database")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_name(self) -> typing.Optional[builtins.str]:
        '''The fully qualified name of the schema.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#schema_name GrantPrivilegesToRole#schema_name}
        '''
        result = self._values.get("schema_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrantPrivilegesToRoleOnSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.grantPrivilegesToRole.GrantPrivilegesToRoleOnSchemaObject",
    jsii_struct_bases=[],
    name_mapping={
        "all": "all",
        "future": "future",
        "object_name": "objectName",
        "object_type": "objectType",
    },
)
class GrantPrivilegesToRoleOnSchemaObject:
    def __init__(
        self,
        *,
        all: typing.Optional[typing.Union["GrantPrivilegesToRoleOnSchemaObjectAll", typing.Dict[builtins.str, typing.Any]]] = None,
        future: typing.Optional[typing.Union["GrantPrivilegesToRoleOnSchemaObjectFuture", typing.Dict[builtins.str, typing.Any]]] = None,
        object_name: typing.Optional[builtins.str] = None,
        object_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param all: all block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#all GrantPrivilegesToRole#all}
        :param future: future block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#future GrantPrivilegesToRole#future}
        :param object_name: The fully qualified name of the object on which privileges will be granted. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#object_name GrantPrivilegesToRole#object_name}
        :param object_type: The object type of the schema object on which privileges will be granted. Valid values are: ALERT | DYNAMIC TABLE | EVENT TABLE | FILE FORMAT | FUNCTION | ICEBERG TABLE | PROCEDURE | SECRET | SEQUENCE | PIPE | MASKING POLICY | PASSWORD POLICY | ROW ACCESS POLICY | SESSION POLICY | TAG | STAGE | STREAM | TABLE | EXTERNAL TABLE | TASK | VIEW | MATERIALIZED VIEW Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#object_type GrantPrivilegesToRole#object_type}
        '''
        if isinstance(all, dict):
            all = GrantPrivilegesToRoleOnSchemaObjectAll(**all)
        if isinstance(future, dict):
            future = GrantPrivilegesToRoleOnSchemaObjectFuture(**future)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49a2c95a580eaf0ee6738063936b4fef69c97fede091faa3ca0214c9e97b79f8)
            check_type(argname="argument all", value=all, expected_type=type_hints["all"])
            check_type(argname="argument future", value=future, expected_type=type_hints["future"])
            check_type(argname="argument object_name", value=object_name, expected_type=type_hints["object_name"])
            check_type(argname="argument object_type", value=object_type, expected_type=type_hints["object_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if all is not None:
            self._values["all"] = all
        if future is not None:
            self._values["future"] = future
        if object_name is not None:
            self._values["object_name"] = object_name
        if object_type is not None:
            self._values["object_type"] = object_type

    @builtins.property
    def all(self) -> typing.Optional["GrantPrivilegesToRoleOnSchemaObjectAll"]:
        '''all block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#all GrantPrivilegesToRole#all}
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional["GrantPrivilegesToRoleOnSchemaObjectAll"], result)

    @builtins.property
    def future(self) -> typing.Optional["GrantPrivilegesToRoleOnSchemaObjectFuture"]:
        '''future block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#future GrantPrivilegesToRole#future}
        '''
        result = self._values.get("future")
        return typing.cast(typing.Optional["GrantPrivilegesToRoleOnSchemaObjectFuture"], result)

    @builtins.property
    def object_name(self) -> typing.Optional[builtins.str]:
        '''The fully qualified name of the object on which privileges will be granted.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#object_name GrantPrivilegesToRole#object_name}
        '''
        result = self._values.get("object_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_type(self) -> typing.Optional[builtins.str]:
        '''The object type of the schema object on which privileges will be granted.

        Valid values are: ALERT | DYNAMIC TABLE | EVENT TABLE | FILE FORMAT | FUNCTION | ICEBERG TABLE | PROCEDURE | SECRET | SEQUENCE | PIPE | MASKING POLICY | PASSWORD POLICY | ROW ACCESS POLICY | SESSION POLICY | TAG | STAGE | STREAM | TABLE | EXTERNAL TABLE | TASK | VIEW | MATERIALIZED VIEW

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#object_type GrantPrivilegesToRole#object_type}
        '''
        result = self._values.get("object_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrantPrivilegesToRoleOnSchemaObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.grantPrivilegesToRole.GrantPrivilegesToRoleOnSchemaObjectAll",
    jsii_struct_bases=[],
    name_mapping={
        "object_type_plural": "objectTypePlural",
        "in_database": "inDatabase",
        "in_schema": "inSchema",
    },
)
class GrantPrivilegesToRoleOnSchemaObjectAll:
    def __init__(
        self,
        *,
        object_type_plural: builtins.str,
        in_database: typing.Optional[builtins.str] = None,
        in_schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param object_type_plural: The plural object type of the schema object on which privileges will be granted. Valid values are: ALERTS | DYNAMIC TABLES | EVENT TABLES | FILE FORMATS | FUNCTIONS | ICEBERG TABLES | PROCEDURES | SECRETS | SEQUENCES | PIPES | MASKING POLICIES | PASSWORD POLICIES | ROW ACCESS POLICIES | SESSION POLICIES | TAGS | STAGES | STREAMS | TABLES | EXTERNAL TABLES | TASKS | VIEWS | MATERIALIZED VIEWS Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#object_type_plural GrantPrivilegesToRole#object_type_plural}
        :param in_database: The fully qualified name of the database. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#in_database GrantPrivilegesToRole#in_database}
        :param in_schema: The fully qualified name of the schema. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#in_schema GrantPrivilegesToRole#in_schema}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a78345955dd2a438762ae789a5161393c47155a724d3f7031b9d187b7a38aca)
            check_type(argname="argument object_type_plural", value=object_type_plural, expected_type=type_hints["object_type_plural"])
            check_type(argname="argument in_database", value=in_database, expected_type=type_hints["in_database"])
            check_type(argname="argument in_schema", value=in_schema, expected_type=type_hints["in_schema"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object_type_plural": object_type_plural,
        }
        if in_database is not None:
            self._values["in_database"] = in_database
        if in_schema is not None:
            self._values["in_schema"] = in_schema

    @builtins.property
    def object_type_plural(self) -> builtins.str:
        '''The plural object type of the schema object on which privileges will be granted.

        Valid values are: ALERTS | DYNAMIC TABLES | EVENT TABLES | FILE FORMATS | FUNCTIONS | ICEBERG TABLES | PROCEDURES | SECRETS | SEQUENCES | PIPES | MASKING POLICIES | PASSWORD POLICIES | ROW ACCESS POLICIES | SESSION POLICIES | TAGS | STAGES | STREAMS | TABLES | EXTERNAL TABLES | TASKS | VIEWS | MATERIALIZED VIEWS

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#object_type_plural GrantPrivilegesToRole#object_type_plural}
        '''
        result = self._values.get("object_type_plural")
        assert result is not None, "Required property 'object_type_plural' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def in_database(self) -> typing.Optional[builtins.str]:
        '''The fully qualified name of the database.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#in_database GrantPrivilegesToRole#in_database}
        '''
        result = self._values.get("in_database")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def in_schema(self) -> typing.Optional[builtins.str]:
        '''The fully qualified name of the schema.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#in_schema GrantPrivilegesToRole#in_schema}
        '''
        result = self._values.get("in_schema")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrantPrivilegesToRoleOnSchemaObjectAll(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GrantPrivilegesToRoleOnSchemaObjectAllOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.grantPrivilegesToRole.GrantPrivilegesToRoleOnSchemaObjectAllOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91b52dbcb08941435a4d64a4078887926b61df6a885912b999aa2dba57c4ba3a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInDatabase")
    def reset_in_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInDatabase", []))

    @jsii.member(jsii_name="resetInSchema")
    def reset_in_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInSchema", []))

    @builtins.property
    @jsii.member(jsii_name="inDatabaseInput")
    def in_database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inDatabaseInput"))

    @builtins.property
    @jsii.member(jsii_name="inSchemaInput")
    def in_schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="objectTypePluralInput")
    def object_type_plural_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectTypePluralInput"))

    @builtins.property
    @jsii.member(jsii_name="inDatabase")
    def in_database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inDatabase"))

    @in_database.setter
    def in_database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5988d10133134091f19761ea487cd1306ef84b23a0573e386806c8e3b970e26d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inDatabase", value)

    @builtins.property
    @jsii.member(jsii_name="inSchema")
    def in_schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inSchema"))

    @in_schema.setter
    def in_schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffd6066af8b0c1195500de025d1940ced1ac7890d7b836d0ab8f7c6f0ebe0e09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inSchema", value)

    @builtins.property
    @jsii.member(jsii_name="objectTypePlural")
    def object_type_plural(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectTypePlural"))

    @object_type_plural.setter
    def object_type_plural(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06ab70d0b240379a72a9d0a97ea2644edf5bfc1a9dfb0539d6fe9cc72d5152ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectTypePlural", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GrantPrivilegesToRoleOnSchemaObjectAll]:
        return typing.cast(typing.Optional[GrantPrivilegesToRoleOnSchemaObjectAll], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GrantPrivilegesToRoleOnSchemaObjectAll],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c919a2915e109109fc271c4aae63b898a7ddc76852ca1b4622f035831274ce3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.grantPrivilegesToRole.GrantPrivilegesToRoleOnSchemaObjectFuture",
    jsii_struct_bases=[],
    name_mapping={
        "object_type_plural": "objectTypePlural",
        "in_database": "inDatabase",
        "in_schema": "inSchema",
    },
)
class GrantPrivilegesToRoleOnSchemaObjectFuture:
    def __init__(
        self,
        *,
        object_type_plural: builtins.str,
        in_database: typing.Optional[builtins.str] = None,
        in_schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param object_type_plural: The plural object type of the schema object on which privileges will be granted. Valid values are: ALERTS | DYNAMIC TABLES | EVENT TABLES | FILE FORMATS | FUNCTIONS | ICEBERG TABLES | PROCEDURES | SECRETS | SEQUENCES | PIPES | MASKING POLICIES | PASSWORD POLICIES | ROW ACCESS POLICIES | SESSION POLICIES | TAGS | STAGES | STREAMS | TABLES | EXTERNAL TABLES | TASKS | VIEWS | MATERIALIZED VIEWS Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#object_type_plural GrantPrivilegesToRole#object_type_plural}
        :param in_database: The fully qualified name of the database. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#in_database GrantPrivilegesToRole#in_database}
        :param in_schema: The fully qualified name of the schema. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#in_schema GrantPrivilegesToRole#in_schema}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bebb066b98cbf145907bc2aad286413d5a9af2e5923bf69482efed25e1265763)
            check_type(argname="argument object_type_plural", value=object_type_plural, expected_type=type_hints["object_type_plural"])
            check_type(argname="argument in_database", value=in_database, expected_type=type_hints["in_database"])
            check_type(argname="argument in_schema", value=in_schema, expected_type=type_hints["in_schema"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object_type_plural": object_type_plural,
        }
        if in_database is not None:
            self._values["in_database"] = in_database
        if in_schema is not None:
            self._values["in_schema"] = in_schema

    @builtins.property
    def object_type_plural(self) -> builtins.str:
        '''The plural object type of the schema object on which privileges will be granted.

        Valid values are: ALERTS | DYNAMIC TABLES | EVENT TABLES | FILE FORMATS | FUNCTIONS | ICEBERG TABLES | PROCEDURES | SECRETS | SEQUENCES | PIPES | MASKING POLICIES | PASSWORD POLICIES | ROW ACCESS POLICIES | SESSION POLICIES | TAGS | STAGES | STREAMS | TABLES | EXTERNAL TABLES | TASKS | VIEWS | MATERIALIZED VIEWS

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#object_type_plural GrantPrivilegesToRole#object_type_plural}
        '''
        result = self._values.get("object_type_plural")
        assert result is not None, "Required property 'object_type_plural' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def in_database(self) -> typing.Optional[builtins.str]:
        '''The fully qualified name of the database.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#in_database GrantPrivilegesToRole#in_database}
        '''
        result = self._values.get("in_database")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def in_schema(self) -> typing.Optional[builtins.str]:
        '''The fully qualified name of the schema.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#in_schema GrantPrivilegesToRole#in_schema}
        '''
        result = self._values.get("in_schema")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrantPrivilegesToRoleOnSchemaObjectFuture(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GrantPrivilegesToRoleOnSchemaObjectFutureOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.grantPrivilegesToRole.GrantPrivilegesToRoleOnSchemaObjectFutureOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94d27973acbbfc48efc6278f590b2d0f6fd2c662d6cc3dfe68b0a552498b33df)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInDatabase")
    def reset_in_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInDatabase", []))

    @jsii.member(jsii_name="resetInSchema")
    def reset_in_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInSchema", []))

    @builtins.property
    @jsii.member(jsii_name="inDatabaseInput")
    def in_database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inDatabaseInput"))

    @builtins.property
    @jsii.member(jsii_name="inSchemaInput")
    def in_schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="objectTypePluralInput")
    def object_type_plural_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectTypePluralInput"))

    @builtins.property
    @jsii.member(jsii_name="inDatabase")
    def in_database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inDatabase"))

    @in_database.setter
    def in_database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cf29d2a89db7765549ca4a2f735982395dfd731b2c7da88be3f5f23da2e544f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inDatabase", value)

    @builtins.property
    @jsii.member(jsii_name="inSchema")
    def in_schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inSchema"))

    @in_schema.setter
    def in_schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2242ae018689f76b3afe88d3ab2e8833f11b087de69e05de9ddef722ba34074)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inSchema", value)

    @builtins.property
    @jsii.member(jsii_name="objectTypePlural")
    def object_type_plural(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectTypePlural"))

    @object_type_plural.setter
    def object_type_plural(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a1784a67a66ed16fd66a7fb2ba1117c858f57dabdf4d4ed68d00a8f2db84567)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectTypePlural", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GrantPrivilegesToRoleOnSchemaObjectFuture]:
        return typing.cast(typing.Optional[GrantPrivilegesToRoleOnSchemaObjectFuture], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GrantPrivilegesToRoleOnSchemaObjectFuture],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__972ae2e364890acdbadafbf89145bf5ad9c87c2cfd97a054f403bd8eb865e913)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GrantPrivilegesToRoleOnSchemaObjectOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.grantPrivilegesToRole.GrantPrivilegesToRoleOnSchemaObjectOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8e83d6cd40736f9207e84cc72c752ed7018db58eb74c116f38759914ce89588)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAll")
    def put_all(
        self,
        *,
        object_type_plural: builtins.str,
        in_database: typing.Optional[builtins.str] = None,
        in_schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param object_type_plural: The plural object type of the schema object on which privileges will be granted. Valid values are: ALERTS | DYNAMIC TABLES | EVENT TABLES | FILE FORMATS | FUNCTIONS | ICEBERG TABLES | PROCEDURES | SECRETS | SEQUENCES | PIPES | MASKING POLICIES | PASSWORD POLICIES | ROW ACCESS POLICIES | SESSION POLICIES | TAGS | STAGES | STREAMS | TABLES | EXTERNAL TABLES | TASKS | VIEWS | MATERIALIZED VIEWS Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#object_type_plural GrantPrivilegesToRole#object_type_plural}
        :param in_database: The fully qualified name of the database. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#in_database GrantPrivilegesToRole#in_database}
        :param in_schema: The fully qualified name of the schema. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#in_schema GrantPrivilegesToRole#in_schema}
        '''
        value = GrantPrivilegesToRoleOnSchemaObjectAll(
            object_type_plural=object_type_plural,
            in_database=in_database,
            in_schema=in_schema,
        )

        return typing.cast(None, jsii.invoke(self, "putAll", [value]))

    @jsii.member(jsii_name="putFuture")
    def put_future(
        self,
        *,
        object_type_plural: builtins.str,
        in_database: typing.Optional[builtins.str] = None,
        in_schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param object_type_plural: The plural object type of the schema object on which privileges will be granted. Valid values are: ALERTS | DYNAMIC TABLES | EVENT TABLES | FILE FORMATS | FUNCTIONS | ICEBERG TABLES | PROCEDURES | SECRETS | SEQUENCES | PIPES | MASKING POLICIES | PASSWORD POLICIES | ROW ACCESS POLICIES | SESSION POLICIES | TAGS | STAGES | STREAMS | TABLES | EXTERNAL TABLES | TASKS | VIEWS | MATERIALIZED VIEWS Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#object_type_plural GrantPrivilegesToRole#object_type_plural}
        :param in_database: The fully qualified name of the database. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#in_database GrantPrivilegesToRole#in_database}
        :param in_schema: The fully qualified name of the schema. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/grant_privileges_to_role#in_schema GrantPrivilegesToRole#in_schema}
        '''
        value = GrantPrivilegesToRoleOnSchemaObjectFuture(
            object_type_plural=object_type_plural,
            in_database=in_database,
            in_schema=in_schema,
        )

        return typing.cast(None, jsii.invoke(self, "putFuture", [value]))

    @jsii.member(jsii_name="resetAll")
    def reset_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAll", []))

    @jsii.member(jsii_name="resetFuture")
    def reset_future(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFuture", []))

    @jsii.member(jsii_name="resetObjectName")
    def reset_object_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectName", []))

    @jsii.member(jsii_name="resetObjectType")
    def reset_object_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectType", []))

    @builtins.property
    @jsii.member(jsii_name="all")
    def all(self) -> GrantPrivilegesToRoleOnSchemaObjectAllOutputReference:
        return typing.cast(GrantPrivilegesToRoleOnSchemaObjectAllOutputReference, jsii.get(self, "all"))

    @builtins.property
    @jsii.member(jsii_name="future")
    def future(self) -> GrantPrivilegesToRoleOnSchemaObjectFutureOutputReference:
        return typing.cast(GrantPrivilegesToRoleOnSchemaObjectFutureOutputReference, jsii.get(self, "future"))

    @builtins.property
    @jsii.member(jsii_name="allInput")
    def all_input(self) -> typing.Optional[GrantPrivilegesToRoleOnSchemaObjectAll]:
        return typing.cast(typing.Optional[GrantPrivilegesToRoleOnSchemaObjectAll], jsii.get(self, "allInput"))

    @builtins.property
    @jsii.member(jsii_name="futureInput")
    def future_input(
        self,
    ) -> typing.Optional[GrantPrivilegesToRoleOnSchemaObjectFuture]:
        return typing.cast(typing.Optional[GrantPrivilegesToRoleOnSchemaObjectFuture], jsii.get(self, "futureInput"))

    @builtins.property
    @jsii.member(jsii_name="objectNameInput")
    def object_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectNameInput"))

    @builtins.property
    @jsii.member(jsii_name="objectTypeInput")
    def object_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="objectName")
    def object_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectName"))

    @object_name.setter
    def object_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b35e3c5337bed8f57f685a1ba20743248e5012fe6cad62ad9084994b349e934d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectName", value)

    @builtins.property
    @jsii.member(jsii_name="objectType")
    def object_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectType"))

    @object_type.setter
    def object_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2f0810f0321e585ddc691b620d8457d63489c59904dc0ae7e0f51f2a37af191)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GrantPrivilegesToRoleOnSchemaObject]:
        return typing.cast(typing.Optional[GrantPrivilegesToRoleOnSchemaObject], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GrantPrivilegesToRoleOnSchemaObject],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab012cbcbfb24d462cc9243a13719d703264fe6703385a7453575606e73fd794)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GrantPrivilegesToRoleOnSchemaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.grantPrivilegesToRole.GrantPrivilegesToRoleOnSchemaOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee31efba5e60af4723ca7667d32503ae34df8d3791464bf32e6d27cdb357ff03)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllSchemasInDatabase")
    def reset_all_schemas_in_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllSchemasInDatabase", []))

    @jsii.member(jsii_name="resetFutureSchemasInDatabase")
    def reset_future_schemas_in_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFutureSchemasInDatabase", []))

    @jsii.member(jsii_name="resetSchemaName")
    def reset_schema_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaName", []))

    @builtins.property
    @jsii.member(jsii_name="allSchemasInDatabaseInput")
    def all_schemas_in_database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allSchemasInDatabaseInput"))

    @builtins.property
    @jsii.member(jsii_name="futureSchemasInDatabaseInput")
    def future_schemas_in_database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "futureSchemasInDatabaseInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaNameInput")
    def schema_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaNameInput"))

    @builtins.property
    @jsii.member(jsii_name="allSchemasInDatabase")
    def all_schemas_in_database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allSchemasInDatabase"))

    @all_schemas_in_database.setter
    def all_schemas_in_database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__882de92b3793c0bb0d2e7563fa4f3746f3b451700d4492e6c8516911234cd285)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allSchemasInDatabase", value)

    @builtins.property
    @jsii.member(jsii_name="futureSchemasInDatabase")
    def future_schemas_in_database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "futureSchemasInDatabase"))

    @future_schemas_in_database.setter
    def future_schemas_in_database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3576a871f8f87e60aede310ea2dadfc47a3cc0028bb7b9187855f6659e499a25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "futureSchemasInDatabase", value)

    @builtins.property
    @jsii.member(jsii_name="schemaName")
    def schema_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaName"))

    @schema_name.setter
    def schema_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf341a0afaa542dd30aca7ec4e443f71099bf8b86a477bfdbf8acc02284b4038)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GrantPrivilegesToRoleOnSchema]:
        return typing.cast(typing.Optional[GrantPrivilegesToRoleOnSchema], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GrantPrivilegesToRoleOnSchema],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19f1218636c7b861b319928bfdcfd6d7fe778ba8bedad7480e8c611cafc06449)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GrantPrivilegesToRole",
    "GrantPrivilegesToRoleConfig",
    "GrantPrivilegesToRoleOnAccountObject",
    "GrantPrivilegesToRoleOnAccountObjectOutputReference",
    "GrantPrivilegesToRoleOnSchema",
    "GrantPrivilegesToRoleOnSchemaObject",
    "GrantPrivilegesToRoleOnSchemaObjectAll",
    "GrantPrivilegesToRoleOnSchemaObjectAllOutputReference",
    "GrantPrivilegesToRoleOnSchemaObjectFuture",
    "GrantPrivilegesToRoleOnSchemaObjectFutureOutputReference",
    "GrantPrivilegesToRoleOnSchemaObjectOutputReference",
    "GrantPrivilegesToRoleOnSchemaOutputReference",
]

publication.publish()

def _typecheckingstub__df9b6bac89d7b7dd746aef9ebbff86facffbdbd9cbbcc1b272c36297b61ff96b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    role_name: builtins.str,
    all_privileges: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    on_account: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    on_account_object: typing.Optional[typing.Union[GrantPrivilegesToRoleOnAccountObject, typing.Dict[builtins.str, typing.Any]]] = None,
    on_schema: typing.Optional[typing.Union[GrantPrivilegesToRoleOnSchema, typing.Dict[builtins.str, typing.Any]]] = None,
    on_schema_object: typing.Optional[typing.Union[GrantPrivilegesToRoleOnSchemaObject, typing.Dict[builtins.str, typing.Any]]] = None,
    privileges: typing.Optional[typing.Sequence[builtins.str]] = None,
    with_grant_option: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da59db44f797e9bc59ec58ecb3d276fbdad3c41cb534f937d8a01b79cdad2508(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae2d0fb93445e52b92165c6a295ba8250d2313624055eab84a10146d174ba01c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8501f18eab60fb6ab7783788c55cd870cdc25c8c85764ff33e07efd01e65d2d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad8485be078d691a540591323a275a507a034eec5afb40342cc2946a4923a190(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99a08e24e5d78c580d7e8493388217245f932fdca73c51ed949542040b227ba3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c3fc6e1b88460e0bcd4b85a1d51f18504928917047070ed7149f014ba7068a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1498c1b7fa3eab727be362fbfdc0bad741b1a50b92c9b990ce2adb708c37565c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a5ee16345c8b0c6f3c0384a76deedd8d755a73f999a1c40ba515563077a3514(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    role_name: builtins.str,
    all_privileges: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    on_account: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    on_account_object: typing.Optional[typing.Union[GrantPrivilegesToRoleOnAccountObject, typing.Dict[builtins.str, typing.Any]]] = None,
    on_schema: typing.Optional[typing.Union[GrantPrivilegesToRoleOnSchema, typing.Dict[builtins.str, typing.Any]]] = None,
    on_schema_object: typing.Optional[typing.Union[GrantPrivilegesToRoleOnSchemaObject, typing.Dict[builtins.str, typing.Any]]] = None,
    privileges: typing.Optional[typing.Sequence[builtins.str]] = None,
    with_grant_option: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e2b940dca629c72f603127fe6a29409e15e2652a00195bd24f1a71e719057e2(
    *,
    object_name: builtins.str,
    object_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04b50230cccb35126081e3572b5f1c597bc59735fa7523942670edb722bb79d9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b182b48843436ead4ac2a8e07bfe08b6034b475bb6614d3c9c2362a17f14543(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76fc8587e6d9b2238cfd63640e9b8e85423aa05f80aad5d7a3a57fd3f1a67fef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2d74bb9e5fcab7bd1dcc8cf0a91f524a2d695a3f51786e135cc7f4e8e62d313(
    value: typing.Optional[GrantPrivilegesToRoleOnAccountObject],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce19377181accfbda92f741a0364170e08f650d7dc9ffc12bcf1337d71093c9e(
    *,
    all_schemas_in_database: typing.Optional[builtins.str] = None,
    future_schemas_in_database: typing.Optional[builtins.str] = None,
    schema_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49a2c95a580eaf0ee6738063936b4fef69c97fede091faa3ca0214c9e97b79f8(
    *,
    all: typing.Optional[typing.Union[GrantPrivilegesToRoleOnSchemaObjectAll, typing.Dict[builtins.str, typing.Any]]] = None,
    future: typing.Optional[typing.Union[GrantPrivilegesToRoleOnSchemaObjectFuture, typing.Dict[builtins.str, typing.Any]]] = None,
    object_name: typing.Optional[builtins.str] = None,
    object_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a78345955dd2a438762ae789a5161393c47155a724d3f7031b9d187b7a38aca(
    *,
    object_type_plural: builtins.str,
    in_database: typing.Optional[builtins.str] = None,
    in_schema: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91b52dbcb08941435a4d64a4078887926b61df6a885912b999aa2dba57c4ba3a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5988d10133134091f19761ea487cd1306ef84b23a0573e386806c8e3b970e26d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffd6066af8b0c1195500de025d1940ced1ac7890d7b836d0ab8f7c6f0ebe0e09(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06ab70d0b240379a72a9d0a97ea2644edf5bfc1a9dfb0539d6fe9cc72d5152ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c919a2915e109109fc271c4aae63b898a7ddc76852ca1b4622f035831274ce3f(
    value: typing.Optional[GrantPrivilegesToRoleOnSchemaObjectAll],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bebb066b98cbf145907bc2aad286413d5a9af2e5923bf69482efed25e1265763(
    *,
    object_type_plural: builtins.str,
    in_database: typing.Optional[builtins.str] = None,
    in_schema: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94d27973acbbfc48efc6278f590b2d0f6fd2c662d6cc3dfe68b0a552498b33df(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cf29d2a89db7765549ca4a2f735982395dfd731b2c7da88be3f5f23da2e544f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2242ae018689f76b3afe88d3ab2e8833f11b087de69e05de9ddef722ba34074(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a1784a67a66ed16fd66a7fb2ba1117c858f57dabdf4d4ed68d00a8f2db84567(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__972ae2e364890acdbadafbf89145bf5ad9c87c2cfd97a054f403bd8eb865e913(
    value: typing.Optional[GrantPrivilegesToRoleOnSchemaObjectFuture],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8e83d6cd40736f9207e84cc72c752ed7018db58eb74c116f38759914ce89588(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b35e3c5337bed8f57f685a1ba20743248e5012fe6cad62ad9084994b349e934d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2f0810f0321e585ddc691b620d8457d63489c59904dc0ae7e0f51f2a37af191(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab012cbcbfb24d462cc9243a13719d703264fe6703385a7453575606e73fd794(
    value: typing.Optional[GrantPrivilegesToRoleOnSchemaObject],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee31efba5e60af4723ca7667d32503ae34df8d3791464bf32e6d27cdb357ff03(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__882de92b3793c0bb0d2e7563fa4f3746f3b451700d4492e6c8516911234cd285(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3576a871f8f87e60aede310ea2dadfc47a3cc0028bb7b9187855f6659e499a25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf341a0afaa542dd30aca7ec4e443f71099bf8b86a477bfdbf8acc02284b4038(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19f1218636c7b861b319928bfdcfd6d7fe778ba8bedad7480e8c611cafc06449(
    value: typing.Optional[GrantPrivilegesToRoleOnSchema],
) -> None:
    """Type checking stubs"""
    pass

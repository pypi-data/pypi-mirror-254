'''
# `snowflake_procedure_grant`

Refer to the Terraform Registry for docs: [`snowflake_procedure_grant`](https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant).
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


class ProcedureGrant(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.procedureGrant.ProcedureGrant",
):
    '''Represents a {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant snowflake_procedure_grant}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        database_name: builtins.str,
        roles: typing.Sequence[builtins.str],
        argument_data_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_multiple_grants: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        on_all: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        on_future: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        privilege: typing.Optional[builtins.str] = None,
        procedure_name: typing.Optional[builtins.str] = None,
        revert_ownership_to_role_name: typing.Optional[builtins.str] = None,
        schema_name: typing.Optional[builtins.str] = None,
        shares: typing.Optional[typing.Sequence[builtins.str]] = None,
        with_grant_option: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant snowflake_procedure_grant} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param database_name: The name of the database containing the current or future procedures on which to grant privileges. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#database_name ProcedureGrant#database_name}
        :param roles: Grants privilege to these roles. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#roles ProcedureGrant#roles}
        :param argument_data_types: List of the argument data types for the procedure (must be present if procedure has arguments and procedure_name is present). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#argument_data_types ProcedureGrant#argument_data_types}
        :param enable_multiple_grants: When this is set to true, multiple grants of the same type can be created. This will cause Terraform to not revoke grants applied to roles and objects outside Terraform. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#enable_multiple_grants ProcedureGrant#enable_multiple_grants}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#id ProcedureGrant#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param on_all: When this is set to true and a schema_name is provided, apply this grant on all procedures in the given schema. When this is true and no schema_name is provided apply this grant on all procedures in the given database. The procedure_name and shares fields must be unset in order to use on_all. Cannot be used together with on_future. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#on_all ProcedureGrant#on_all}
        :param on_future: When this is set to true and a schema_name is provided, apply this grant on all future procedures in the given schema. When this is true and no schema_name is provided apply this grant on all future procedures in the given database. The procedure_name and shares fields must be unset in order to use on_future. Cannot be used together with on_all. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#on_future ProcedureGrant#on_future}
        :param privilege: The privilege to grant on the current or future procedure. To grant all privileges, use the value ``ALL PRIVILEGES``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#privilege ProcedureGrant#privilege}
        :param procedure_name: The name of the procedure on which to grant privileges immediately (only valid if on_future is false). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#procedure_name ProcedureGrant#procedure_name}
        :param revert_ownership_to_role_name: The name of the role to revert ownership to on destroy. Has no effect unless ``privilege`` is set to ``OWNERSHIP`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#revert_ownership_to_role_name ProcedureGrant#revert_ownership_to_role_name}
        :param schema_name: The name of the schema containing the current or future procedures on which to grant privileges. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#schema_name ProcedureGrant#schema_name}
        :param shares: Grants privilege to these shares (only valid if on_future is false). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#shares ProcedureGrant#shares}
        :param with_grant_option: When this is set to true, allows the recipient role to grant the privileges to other roles. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#with_grant_option ProcedureGrant#with_grant_option}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eea9fb09d8b1ff9dc8b0801d6c5a7ecce837ed2b4bb6040d4a7a7637842b562d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ProcedureGrantConfig(
            database_name=database_name,
            roles=roles,
            argument_data_types=argument_data_types,
            enable_multiple_grants=enable_multiple_grants,
            id=id,
            on_all=on_all,
            on_future=on_future,
            privilege=privilege,
            procedure_name=procedure_name,
            revert_ownership_to_role_name=revert_ownership_to_role_name,
            schema_name=schema_name,
            shares=shares,
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
        '''Generates CDKTF code for importing a ProcedureGrant resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the ProcedureGrant to import.
        :param import_from_id: The id of the existing ProcedureGrant that should be imported. Refer to the {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the ProcedureGrant to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22c0174350b0f8fcf23f9abda4c38106a385658a501017346ca3f804dfe4916e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetArgumentDataTypes")
    def reset_argument_data_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgumentDataTypes", []))

    @jsii.member(jsii_name="resetEnableMultipleGrants")
    def reset_enable_multiple_grants(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableMultipleGrants", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOnAll")
    def reset_on_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnAll", []))

    @jsii.member(jsii_name="resetOnFuture")
    def reset_on_future(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnFuture", []))

    @jsii.member(jsii_name="resetPrivilege")
    def reset_privilege(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivilege", []))

    @jsii.member(jsii_name="resetProcedureName")
    def reset_procedure_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcedureName", []))

    @jsii.member(jsii_name="resetRevertOwnershipToRoleName")
    def reset_revert_ownership_to_role_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRevertOwnershipToRoleName", []))

    @jsii.member(jsii_name="resetSchemaName")
    def reset_schema_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaName", []))

    @jsii.member(jsii_name="resetShares")
    def reset_shares(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShares", []))

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
    @jsii.member(jsii_name="argumentDataTypesInput")
    def argument_data_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argumentDataTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="enableMultipleGrantsInput")
    def enable_multiple_grants_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableMultipleGrantsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="onAllInput")
    def on_all_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "onAllInput"))

    @builtins.property
    @jsii.member(jsii_name="onFutureInput")
    def on_future_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "onFutureInput"))

    @builtins.property
    @jsii.member(jsii_name="privilegeInput")
    def privilege_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privilegeInput"))

    @builtins.property
    @jsii.member(jsii_name="procedureNameInput")
    def procedure_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "procedureNameInput"))

    @builtins.property
    @jsii.member(jsii_name="revertOwnershipToRoleNameInput")
    def revert_ownership_to_role_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "revertOwnershipToRoleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rolesInput")
    def roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rolesInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaNameInput")
    def schema_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sharesInput")
    def shares_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sharesInput"))

    @builtins.property
    @jsii.member(jsii_name="withGrantOptionInput")
    def with_grant_option_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "withGrantOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="argumentDataTypes")
    def argument_data_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "argumentDataTypes"))

    @argument_data_types.setter
    def argument_data_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__477872943ea6b32946bb10b04970130d696b742bd05b28673a9f70681b865208)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "argumentDataTypes", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b23216d64b34c19775f37d6cfe40d33ef813ee65dc3b63f6f516e07e07c29e91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="enableMultipleGrants")
    def enable_multiple_grants(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableMultipleGrants"))

    @enable_multiple_grants.setter
    def enable_multiple_grants(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28769524a7a9f38da40ac7919dd9e7abfec45a8cfb43db6679ea474240cb8bd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableMultipleGrants", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da492f9958dd943273d3ebf8f7e3f6030e75521a71269256b653bda4d6a3bfe5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="onAll")
    def on_all(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "onAll"))

    @on_all.setter
    def on_all(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f2096e8fb62c8cf59b62f7bd7be0773cc83e6dfb34f981505366837c2643384)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onAll", value)

    @builtins.property
    @jsii.member(jsii_name="onFuture")
    def on_future(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "onFuture"))

    @on_future.setter
    def on_future(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c81511bd4c6c5402db21d2c246a6a5c0b38b6a496c539dbde98fcc750f4cbac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onFuture", value)

    @builtins.property
    @jsii.member(jsii_name="privilege")
    def privilege(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privilege"))

    @privilege.setter
    def privilege(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a72600493a7d2b2cf4f16e233e1bda2077151e4856d93f93bd823846a6a9ee30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privilege", value)

    @builtins.property
    @jsii.member(jsii_name="procedureName")
    def procedure_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "procedureName"))

    @procedure_name.setter
    def procedure_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a49d69a85b8d6cd73301a1672b2301cc44da76f1df447cd9ddd8254613e9a4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "procedureName", value)

    @builtins.property
    @jsii.member(jsii_name="revertOwnershipToRoleName")
    def revert_ownership_to_role_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "revertOwnershipToRoleName"))

    @revert_ownership_to_role_name.setter
    def revert_ownership_to_role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dc58f3ffda4845e161073bca75a4d5f2d6e33bb6c410a1a0b35767fe15ec652)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revertOwnershipToRoleName", value)

    @builtins.property
    @jsii.member(jsii_name="roles")
    def roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "roles"))

    @roles.setter
    def roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daad52cb2eadc29b512d171826fd187ee4eb9d9c25124fd09a27a7c77fea6c31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roles", value)

    @builtins.property
    @jsii.member(jsii_name="schemaName")
    def schema_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaName"))

    @schema_name.setter
    def schema_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__536a91cc5c7fc56789240a07ca8e1622794fc8ec6f8c6de320101380d6a0646a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaName", value)

    @builtins.property
    @jsii.member(jsii_name="shares")
    def shares(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "shares"))

    @shares.setter
    def shares(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__777be50f830ccd058b97c42948834efdd742ba110e1e31eeda7b2aec61c0aaf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shares", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__7e1df775962bbf04a2f31ffd35df467ae29a636c2de616df9e00355165411e65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "withGrantOption", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.procedureGrant.ProcedureGrantConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "database_name": "databaseName",
        "roles": "roles",
        "argument_data_types": "argumentDataTypes",
        "enable_multiple_grants": "enableMultipleGrants",
        "id": "id",
        "on_all": "onAll",
        "on_future": "onFuture",
        "privilege": "privilege",
        "procedure_name": "procedureName",
        "revert_ownership_to_role_name": "revertOwnershipToRoleName",
        "schema_name": "schemaName",
        "shares": "shares",
        "with_grant_option": "withGrantOption",
    },
)
class ProcedureGrantConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        database_name: builtins.str,
        roles: typing.Sequence[builtins.str],
        argument_data_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_multiple_grants: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        on_all: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        on_future: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        privilege: typing.Optional[builtins.str] = None,
        procedure_name: typing.Optional[builtins.str] = None,
        revert_ownership_to_role_name: typing.Optional[builtins.str] = None,
        schema_name: typing.Optional[builtins.str] = None,
        shares: typing.Optional[typing.Sequence[builtins.str]] = None,
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
        :param database_name: The name of the database containing the current or future procedures on which to grant privileges. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#database_name ProcedureGrant#database_name}
        :param roles: Grants privilege to these roles. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#roles ProcedureGrant#roles}
        :param argument_data_types: List of the argument data types for the procedure (must be present if procedure has arguments and procedure_name is present). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#argument_data_types ProcedureGrant#argument_data_types}
        :param enable_multiple_grants: When this is set to true, multiple grants of the same type can be created. This will cause Terraform to not revoke grants applied to roles and objects outside Terraform. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#enable_multiple_grants ProcedureGrant#enable_multiple_grants}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#id ProcedureGrant#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param on_all: When this is set to true and a schema_name is provided, apply this grant on all procedures in the given schema. When this is true and no schema_name is provided apply this grant on all procedures in the given database. The procedure_name and shares fields must be unset in order to use on_all. Cannot be used together with on_future. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#on_all ProcedureGrant#on_all}
        :param on_future: When this is set to true and a schema_name is provided, apply this grant on all future procedures in the given schema. When this is true and no schema_name is provided apply this grant on all future procedures in the given database. The procedure_name and shares fields must be unset in order to use on_future. Cannot be used together with on_all. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#on_future ProcedureGrant#on_future}
        :param privilege: The privilege to grant on the current or future procedure. To grant all privileges, use the value ``ALL PRIVILEGES``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#privilege ProcedureGrant#privilege}
        :param procedure_name: The name of the procedure on which to grant privileges immediately (only valid if on_future is false). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#procedure_name ProcedureGrant#procedure_name}
        :param revert_ownership_to_role_name: The name of the role to revert ownership to on destroy. Has no effect unless ``privilege`` is set to ``OWNERSHIP`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#revert_ownership_to_role_name ProcedureGrant#revert_ownership_to_role_name}
        :param schema_name: The name of the schema containing the current or future procedures on which to grant privileges. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#schema_name ProcedureGrant#schema_name}
        :param shares: Grants privilege to these shares (only valid if on_future is false). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#shares ProcedureGrant#shares}
        :param with_grant_option: When this is set to true, allows the recipient role to grant the privileges to other roles. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#with_grant_option ProcedureGrant#with_grant_option}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52f975c538217df3f4b6a74404d122fb0d457a1b28e6320f05c9a8228dbfa30f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument argument_data_types", value=argument_data_types, expected_type=type_hints["argument_data_types"])
            check_type(argname="argument enable_multiple_grants", value=enable_multiple_grants, expected_type=type_hints["enable_multiple_grants"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument on_all", value=on_all, expected_type=type_hints["on_all"])
            check_type(argname="argument on_future", value=on_future, expected_type=type_hints["on_future"])
            check_type(argname="argument privilege", value=privilege, expected_type=type_hints["privilege"])
            check_type(argname="argument procedure_name", value=procedure_name, expected_type=type_hints["procedure_name"])
            check_type(argname="argument revert_ownership_to_role_name", value=revert_ownership_to_role_name, expected_type=type_hints["revert_ownership_to_role_name"])
            check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
            check_type(argname="argument shares", value=shares, expected_type=type_hints["shares"])
            check_type(argname="argument with_grant_option", value=with_grant_option, expected_type=type_hints["with_grant_option"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
            "roles": roles,
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
        if argument_data_types is not None:
            self._values["argument_data_types"] = argument_data_types
        if enable_multiple_grants is not None:
            self._values["enable_multiple_grants"] = enable_multiple_grants
        if id is not None:
            self._values["id"] = id
        if on_all is not None:
            self._values["on_all"] = on_all
        if on_future is not None:
            self._values["on_future"] = on_future
        if privilege is not None:
            self._values["privilege"] = privilege
        if procedure_name is not None:
            self._values["procedure_name"] = procedure_name
        if revert_ownership_to_role_name is not None:
            self._values["revert_ownership_to_role_name"] = revert_ownership_to_role_name
        if schema_name is not None:
            self._values["schema_name"] = schema_name
        if shares is not None:
            self._values["shares"] = shares
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
    def database_name(self) -> builtins.str:
        '''The name of the database containing the current or future procedures on which to grant privileges.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#database_name ProcedureGrant#database_name}
        '''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def roles(self) -> typing.List[builtins.str]:
        '''Grants privilege to these roles.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#roles ProcedureGrant#roles}
        '''
        result = self._values.get("roles")
        assert result is not None, "Required property 'roles' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def argument_data_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of the argument data types for the procedure (must be present if procedure has arguments and procedure_name is present).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#argument_data_types ProcedureGrant#argument_data_types}
        '''
        result = self._values.get("argument_data_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enable_multiple_grants(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When this is set to true, multiple grants of the same type can be created.

        This will cause Terraform to not revoke grants applied to roles and objects outside Terraform.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#enable_multiple_grants ProcedureGrant#enable_multiple_grants}
        '''
        result = self._values.get("enable_multiple_grants")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#id ProcedureGrant#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_all(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When this is set to true and a schema_name is provided, apply this grant on all procedures in the given schema.

        When this is true and no schema_name is provided apply this grant on all procedures in the given database. The procedure_name and shares fields must be unset in order to use on_all. Cannot be used together with on_future.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#on_all ProcedureGrant#on_all}
        '''
        result = self._values.get("on_all")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def on_future(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When this is set to true and a schema_name is provided, apply this grant on all future procedures in the given schema.

        When this is true and no schema_name is provided apply this grant on all future procedures in the given database. The procedure_name and shares fields must be unset in order to use on_future. Cannot be used together with on_all.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#on_future ProcedureGrant#on_future}
        '''
        result = self._values.get("on_future")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def privilege(self) -> typing.Optional[builtins.str]:
        '''The privilege to grant on the current or future procedure. To grant all privileges, use the value ``ALL PRIVILEGES``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#privilege ProcedureGrant#privilege}
        '''
        result = self._values.get("privilege")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def procedure_name(self) -> typing.Optional[builtins.str]:
        '''The name of the procedure on which to grant privileges immediately (only valid if on_future is false).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#procedure_name ProcedureGrant#procedure_name}
        '''
        result = self._values.get("procedure_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def revert_ownership_to_role_name(self) -> typing.Optional[builtins.str]:
        '''The name of the role to revert ownership to on destroy.

        Has no effect unless ``privilege`` is set to ``OWNERSHIP``

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#revert_ownership_to_role_name ProcedureGrant#revert_ownership_to_role_name}
        '''
        result = self._values.get("revert_ownership_to_role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_name(self) -> typing.Optional[builtins.str]:
        '''The name of the schema containing the current or future procedures on which to grant privileges.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#schema_name ProcedureGrant#schema_name}
        '''
        result = self._values.get("schema_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shares(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Grants privilege to these shares (only valid if on_future is false).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#shares ProcedureGrant#shares}
        '''
        result = self._values.get("shares")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def with_grant_option(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When this is set to true, allows the recipient role to grant the privileges to other roles.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/procedure_grant#with_grant_option ProcedureGrant#with_grant_option}
        '''
        result = self._values.get("with_grant_option")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProcedureGrantConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ProcedureGrant",
    "ProcedureGrantConfig",
]

publication.publish()

def _typecheckingstub__eea9fb09d8b1ff9dc8b0801d6c5a7ecce837ed2b4bb6040d4a7a7637842b562d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    database_name: builtins.str,
    roles: typing.Sequence[builtins.str],
    argument_data_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    enable_multiple_grants: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    on_all: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    on_future: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    privilege: typing.Optional[builtins.str] = None,
    procedure_name: typing.Optional[builtins.str] = None,
    revert_ownership_to_role_name: typing.Optional[builtins.str] = None,
    schema_name: typing.Optional[builtins.str] = None,
    shares: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__22c0174350b0f8fcf23f9abda4c38106a385658a501017346ca3f804dfe4916e(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__477872943ea6b32946bb10b04970130d696b742bd05b28673a9f70681b865208(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b23216d64b34c19775f37d6cfe40d33ef813ee65dc3b63f6f516e07e07c29e91(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28769524a7a9f38da40ac7919dd9e7abfec45a8cfb43db6679ea474240cb8bd8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da492f9958dd943273d3ebf8f7e3f6030e75521a71269256b653bda4d6a3bfe5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f2096e8fb62c8cf59b62f7bd7be0773cc83e6dfb34f981505366837c2643384(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c81511bd4c6c5402db21d2c246a6a5c0b38b6a496c539dbde98fcc750f4cbac(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a72600493a7d2b2cf4f16e233e1bda2077151e4856d93f93bd823846a6a9ee30(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a49d69a85b8d6cd73301a1672b2301cc44da76f1df447cd9ddd8254613e9a4c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dc58f3ffda4845e161073bca75a4d5f2d6e33bb6c410a1a0b35767fe15ec652(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daad52cb2eadc29b512d171826fd187ee4eb9d9c25124fd09a27a7c77fea6c31(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__536a91cc5c7fc56789240a07ca8e1622794fc8ec6f8c6de320101380d6a0646a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__777be50f830ccd058b97c42948834efdd742ba110e1e31eeda7b2aec61c0aaf0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e1df775962bbf04a2f31ffd35df467ae29a636c2de616df9e00355165411e65(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52f975c538217df3f4b6a74404d122fb0d457a1b28e6320f05c9a8228dbfa30f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    database_name: builtins.str,
    roles: typing.Sequence[builtins.str],
    argument_data_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    enable_multiple_grants: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    on_all: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    on_future: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    privilege: typing.Optional[builtins.str] = None,
    procedure_name: typing.Optional[builtins.str] = None,
    revert_ownership_to_role_name: typing.Optional[builtins.str] = None,
    schema_name: typing.Optional[builtins.str] = None,
    shares: typing.Optional[typing.Sequence[builtins.str]] = None,
    with_grant_option: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

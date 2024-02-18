'''
# `snowflake_user`

Refer to the Terraform Registry for docs: [`snowflake_user`](https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user).
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


class User(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.user.User",
):
    '''Represents a {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user snowflake_user}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        default_namespace: typing.Optional[builtins.str] = None,
        default_role: typing.Optional[builtins.str] = None,
        default_secondary_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_warehouse: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        display_name: typing.Optional[builtins.str] = None,
        email: typing.Optional[builtins.str] = None,
        first_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        last_name: typing.Optional[builtins.str] = None,
        login_name: typing.Optional[builtins.str] = None,
        must_change_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        password: typing.Optional[builtins.str] = None,
        rsa_public_key: typing.Optional[builtins.str] = None,
        rsa_public_key2: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user snowflake_user} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the user. Note that if you do not supply login_name this will be used as login_name. `doc <https://docs.snowflake.net/manuals/sql-reference/sql/create-user.html#required-parameters>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#name User#name}
        :param comment: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#comment User#comment}.
        :param default_namespace: Specifies the namespace (database only or database and schema) that is active by default for the user’s session upon login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#default_namespace User#default_namespace}
        :param default_role: Specifies the role that is active by default for the user’s session upon login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#default_role User#default_role}
        :param default_secondary_roles: Specifies the set of secondary roles that are active for the user’s session upon login. Currently only ["ALL"] value is supported - more information can be found in `doc <https://docs.snowflake.com/en/sql-reference/sql/create-user#optional-object-properties-objectproperties>`_ Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#default_secondary_roles User#default_secondary_roles}
        :param default_warehouse: Specifies the virtual warehouse that is active by default for the user’s session upon login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#default_warehouse User#default_warehouse}
        :param disabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#disabled User#disabled}.
        :param display_name: Name displayed for the user in the Snowflake web interface. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#display_name User#display_name}
        :param email: Email address for the user. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#email User#email}
        :param first_name: First name of the user. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#first_name User#first_name}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#id User#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param last_name: Last name of the user. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#last_name User#last_name}
        :param login_name: The name users use to log in. If not supplied, snowflake will use name instead. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#login_name User#login_name}
        :param must_change_password: Specifies whether the user is forced to change their password on next login (including their first/initial login) into the system. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#must_change_password User#must_change_password}
        :param password: **WARNING:** this will put the password in the terraform state file. Use carefully. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#password User#password}
        :param rsa_public_key: Specifies the user’s RSA public key; used for key-pair authentication. Must be on 1 line without header and trailer. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#rsa_public_key User#rsa_public_key}
        :param rsa_public_key2: Specifies the user’s second RSA public key; used to rotate the public and private keys for key-pair authentication based on an expiration schedule set by your organization. Must be on 1 line without header and trailer. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#rsa_public_key_2 User#rsa_public_key_2}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d84baddd02b2eb7d700b468bb97ddf9f5a11245bd45b1f2245c8755de57d049b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = UserConfig(
            name=name,
            comment=comment,
            default_namespace=default_namespace,
            default_role=default_role,
            default_secondary_roles=default_secondary_roles,
            default_warehouse=default_warehouse,
            disabled=disabled,
            display_name=display_name,
            email=email,
            first_name=first_name,
            id=id,
            last_name=last_name,
            login_name=login_name,
            must_change_password=must_change_password,
            password=password,
            rsa_public_key=rsa_public_key,
            rsa_public_key2=rsa_public_key2,
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
        '''Generates CDKTF code for importing a User resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the User to import.
        :param import_from_id: The id of the existing User that should be imported. Refer to the {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the User to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72414f2a9320dd73073a9cfd82d56b9f7c834226827c1ef0171ee81418205d13)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetDefaultNamespace")
    def reset_default_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultNamespace", []))

    @jsii.member(jsii_name="resetDefaultRole")
    def reset_default_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultRole", []))

    @jsii.member(jsii_name="resetDefaultSecondaryRoles")
    def reset_default_secondary_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultSecondaryRoles", []))

    @jsii.member(jsii_name="resetDefaultWarehouse")
    def reset_default_warehouse(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultWarehouse", []))

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetFirstName")
    def reset_first_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirstName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLastName")
    def reset_last_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastName", []))

    @jsii.member(jsii_name="resetLoginName")
    def reset_login_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginName", []))

    @jsii.member(jsii_name="resetMustChangePassword")
    def reset_must_change_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMustChangePassword", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetRsaPublicKey")
    def reset_rsa_public_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRsaPublicKey", []))

    @jsii.member(jsii_name="resetRsaPublicKey2")
    def reset_rsa_public_key2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRsaPublicKey2", []))

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
    @jsii.member(jsii_name="hasRsaPublicKey")
    def has_rsa_public_key(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "hasRsaPublicKey"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultNamespaceInput")
    def default_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultRoleInput")
    def default_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultSecondaryRolesInput")
    def default_secondary_roles_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "defaultSecondaryRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultWarehouseInput")
    def default_warehouse_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultWarehouseInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="firstNameInput")
    def first_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firstNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lastNameInput")
    def last_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastNameInput"))

    @builtins.property
    @jsii.member(jsii_name="loginNameInput")
    def login_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="mustChangePasswordInput")
    def must_change_password_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "mustChangePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="rsaPublicKey2Input")
    def rsa_public_key2_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rsaPublicKey2Input"))

    @builtins.property
    @jsii.member(jsii_name="rsaPublicKeyInput")
    def rsa_public_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rsaPublicKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c70d58a7dde72cf09c0145b794bb011cb77822b7c8d91de012cabddf0dc2f22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="defaultNamespace")
    def default_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultNamespace"))

    @default_namespace.setter
    def default_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__214a9ff205ee25636ec25f2fd215554275c9a32ac3378657ae75588682eed3f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="defaultRole")
    def default_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultRole"))

    @default_role.setter
    def default_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e767c3f4ed95e67d76786727e22e4670c693d1487eb2d8932b27be46669dd0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRole", value)

    @builtins.property
    @jsii.member(jsii_name="defaultSecondaryRoles")
    def default_secondary_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "defaultSecondaryRoles"))

    @default_secondary_roles.setter
    def default_secondary_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96d9ba76d0357a3a8d9bc943745d407c82f947929e8a54cddcd2bbbee1755977)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSecondaryRoles", value)

    @builtins.property
    @jsii.member(jsii_name="defaultWarehouse")
    def default_warehouse(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultWarehouse"))

    @default_warehouse.setter
    def default_warehouse(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04f64251ded505f4cefd6d4d5a15536f93689a9c0ad81a5cdc2f1af931991f0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultWarehouse", value)

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a755af3704f43753f2f278203f460cef46dcfaf3983e2953def6f033c7ec4c7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9b1a168967696bb92a92bf73717f80fa6aac4e483681eb8903630ad5a692161)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3322d98011bab95439fe965e9f7921436ff80ae4534133e91799adc6d07a6903)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="firstName")
    def first_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstName"))

    @first_name.setter
    def first_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b80b44a9d175599c1710c1ea47900e135b503a5f2a7b488e134a8149de564bf3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee534fe04b85b73ab500205e9b2d0a244d624b079ae8eb269c0d80ae790dd1e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="lastName")
    def last_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastName"))

    @last_name.setter
    def last_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0530543bda1184a7d929f8715889576a41c54bd5c8644b766fe2fc19dd25a36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastName", value)

    @builtins.property
    @jsii.member(jsii_name="loginName")
    def login_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loginName"))

    @login_name.setter
    def login_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abd62b8766f563c8bbaaf20c2117ac094fe19bf602c1dc6abca677209db98a0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginName", value)

    @builtins.property
    @jsii.member(jsii_name="mustChangePassword")
    def must_change_password(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "mustChangePassword"))

    @must_change_password.setter
    def must_change_password(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e87ca7689a8a9fc7bd76f1cc4572091cc8d1cd7db878cb8216171610932cb84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mustChangePassword", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__554b40f61c913aa67692d8d1364c59a569973014f8481649a24b270d88673a96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c384735f0ac2a22cda9e91e8ccb6aef7e481039f3eff75233e4d931bd764d63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="rsaPublicKey")
    def rsa_public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rsaPublicKey"))

    @rsa_public_key.setter
    def rsa_public_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bfab7a98ff160c89e43e23358130c93fe0eacfcf22f37020938d9cdef3270d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rsaPublicKey", value)

    @builtins.property
    @jsii.member(jsii_name="rsaPublicKey2")
    def rsa_public_key2(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rsaPublicKey2"))

    @rsa_public_key2.setter
    def rsa_public_key2(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e609e3a1336017dda59d661522b3f1323545c41e3aa80da6eb0016a37a52ffa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rsaPublicKey2", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.user.UserConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "comment": "comment",
        "default_namespace": "defaultNamespace",
        "default_role": "defaultRole",
        "default_secondary_roles": "defaultSecondaryRoles",
        "default_warehouse": "defaultWarehouse",
        "disabled": "disabled",
        "display_name": "displayName",
        "email": "email",
        "first_name": "firstName",
        "id": "id",
        "last_name": "lastName",
        "login_name": "loginName",
        "must_change_password": "mustChangePassword",
        "password": "password",
        "rsa_public_key": "rsaPublicKey",
        "rsa_public_key2": "rsaPublicKey2",
    },
)
class UserConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        default_namespace: typing.Optional[builtins.str] = None,
        default_role: typing.Optional[builtins.str] = None,
        default_secondary_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_warehouse: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        display_name: typing.Optional[builtins.str] = None,
        email: typing.Optional[builtins.str] = None,
        first_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        last_name: typing.Optional[builtins.str] = None,
        login_name: typing.Optional[builtins.str] = None,
        must_change_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        password: typing.Optional[builtins.str] = None,
        rsa_public_key: typing.Optional[builtins.str] = None,
        rsa_public_key2: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the user. Note that if you do not supply login_name this will be used as login_name. `doc <https://docs.snowflake.net/manuals/sql-reference/sql/create-user.html#required-parameters>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#name User#name}
        :param comment: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#comment User#comment}.
        :param default_namespace: Specifies the namespace (database only or database and schema) that is active by default for the user’s session upon login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#default_namespace User#default_namespace}
        :param default_role: Specifies the role that is active by default for the user’s session upon login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#default_role User#default_role}
        :param default_secondary_roles: Specifies the set of secondary roles that are active for the user’s session upon login. Currently only ["ALL"] value is supported - more information can be found in `doc <https://docs.snowflake.com/en/sql-reference/sql/create-user#optional-object-properties-objectproperties>`_ Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#default_secondary_roles User#default_secondary_roles}
        :param default_warehouse: Specifies the virtual warehouse that is active by default for the user’s session upon login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#default_warehouse User#default_warehouse}
        :param disabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#disabled User#disabled}.
        :param display_name: Name displayed for the user in the Snowflake web interface. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#display_name User#display_name}
        :param email: Email address for the user. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#email User#email}
        :param first_name: First name of the user. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#first_name User#first_name}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#id User#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param last_name: Last name of the user. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#last_name User#last_name}
        :param login_name: The name users use to log in. If not supplied, snowflake will use name instead. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#login_name User#login_name}
        :param must_change_password: Specifies whether the user is forced to change their password on next login (including their first/initial login) into the system. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#must_change_password User#must_change_password}
        :param password: **WARNING:** this will put the password in the terraform state file. Use carefully. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#password User#password}
        :param rsa_public_key: Specifies the user’s RSA public key; used for key-pair authentication. Must be on 1 line without header and trailer. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#rsa_public_key User#rsa_public_key}
        :param rsa_public_key2: Specifies the user’s second RSA public key; used to rotate the public and private keys for key-pair authentication based on an expiration schedule set by your organization. Must be on 1 line without header and trailer. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#rsa_public_key_2 User#rsa_public_key_2}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04bcd50566d7e5a0f6a888a622822b1bb2e90816ef4e28ff46370e9a97874f2c)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument default_namespace", value=default_namespace, expected_type=type_hints["default_namespace"])
            check_type(argname="argument default_role", value=default_role, expected_type=type_hints["default_role"])
            check_type(argname="argument default_secondary_roles", value=default_secondary_roles, expected_type=type_hints["default_secondary_roles"])
            check_type(argname="argument default_warehouse", value=default_warehouse, expected_type=type_hints["default_warehouse"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
            check_type(argname="argument login_name", value=login_name, expected_type=type_hints["login_name"])
            check_type(argname="argument must_change_password", value=must_change_password, expected_type=type_hints["must_change_password"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument rsa_public_key", value=rsa_public_key, expected_type=type_hints["rsa_public_key"])
            check_type(argname="argument rsa_public_key2", value=rsa_public_key2, expected_type=type_hints["rsa_public_key2"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
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
        if comment is not None:
            self._values["comment"] = comment
        if default_namespace is not None:
            self._values["default_namespace"] = default_namespace
        if default_role is not None:
            self._values["default_role"] = default_role
        if default_secondary_roles is not None:
            self._values["default_secondary_roles"] = default_secondary_roles
        if default_warehouse is not None:
            self._values["default_warehouse"] = default_warehouse
        if disabled is not None:
            self._values["disabled"] = disabled
        if display_name is not None:
            self._values["display_name"] = display_name
        if email is not None:
            self._values["email"] = email
        if first_name is not None:
            self._values["first_name"] = first_name
        if id is not None:
            self._values["id"] = id
        if last_name is not None:
            self._values["last_name"] = last_name
        if login_name is not None:
            self._values["login_name"] = login_name
        if must_change_password is not None:
            self._values["must_change_password"] = must_change_password
        if password is not None:
            self._values["password"] = password
        if rsa_public_key is not None:
            self._values["rsa_public_key"] = rsa_public_key
        if rsa_public_key2 is not None:
            self._values["rsa_public_key2"] = rsa_public_key2

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
    def name(self) -> builtins.str:
        '''Name of the user. Note that if you do not supply login_name this will be used as login_name. `doc <https://docs.snowflake.net/manuals/sql-reference/sql/create-user.html#required-parameters>`_.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#name User#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#comment User#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_namespace(self) -> typing.Optional[builtins.str]:
        '''Specifies the namespace (database only or database and schema) that is active by default for the user’s session upon login.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#default_namespace User#default_namespace}
        '''
        result = self._values.get("default_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_role(self) -> typing.Optional[builtins.str]:
        '''Specifies the role that is active by default for the user’s session upon login.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#default_role User#default_role}
        '''
        result = self._values.get("default_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_secondary_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the set of secondary roles that are active for the user’s session upon login.

        Currently only ["ALL"] value is supported - more information can be found in `doc <https://docs.snowflake.com/en/sql-reference/sql/create-user#optional-object-properties-objectproperties>`_

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#default_secondary_roles User#default_secondary_roles}
        '''
        result = self._values.get("default_secondary_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_warehouse(self) -> typing.Optional[builtins.str]:
        '''Specifies the virtual warehouse that is active by default for the user’s session upon login.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#default_warehouse User#default_warehouse}
        '''
        result = self._values.get("default_warehouse")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#disabled User#disabled}.'''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''Name displayed for the user in the Snowflake web interface.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#display_name User#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''Email address for the user.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#email User#email}
        '''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def first_name(self) -> typing.Optional[builtins.str]:
        '''First name of the user.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#first_name User#first_name}
        '''
        result = self._values.get("first_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#id User#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_name(self) -> typing.Optional[builtins.str]:
        '''Last name of the user.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#last_name User#last_name}
        '''
        result = self._values.get("last_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def login_name(self) -> typing.Optional[builtins.str]:
        '''The name users use to log in. If not supplied, snowflake will use name instead.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#login_name User#login_name}
        '''
        result = self._values.get("login_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def must_change_password(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specifies whether the user is forced to change their password on next login (including their first/initial login) into the system.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#must_change_password User#must_change_password}
        '''
        result = self._values.get("must_change_password")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''**WARNING:** this will put the password in the terraform state file. Use carefully.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#password User#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rsa_public_key(self) -> typing.Optional[builtins.str]:
        '''Specifies the user’s RSA public key; used for key-pair authentication. Must be on 1 line without header and trailer.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#rsa_public_key User#rsa_public_key}
        '''
        result = self._values.get("rsa_public_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rsa_public_key2(self) -> typing.Optional[builtins.str]:
        '''Specifies the user’s second RSA public key;

        used to rotate the public and private keys for key-pair authentication based on an expiration schedule set by your organization. Must be on 1 line without header and trailer.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.85.0/docs/resources/user#rsa_public_key_2 User#rsa_public_key_2}
        '''
        result = self._values.get("rsa_public_key2")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "User",
    "UserConfig",
]

publication.publish()

def _typecheckingstub__d84baddd02b2eb7d700b468bb97ddf9f5a11245bd45b1f2245c8755de57d049b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    default_namespace: typing.Optional[builtins.str] = None,
    default_role: typing.Optional[builtins.str] = None,
    default_secondary_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    default_warehouse: typing.Optional[builtins.str] = None,
    disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    display_name: typing.Optional[builtins.str] = None,
    email: typing.Optional[builtins.str] = None,
    first_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    last_name: typing.Optional[builtins.str] = None,
    login_name: typing.Optional[builtins.str] = None,
    must_change_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    password: typing.Optional[builtins.str] = None,
    rsa_public_key: typing.Optional[builtins.str] = None,
    rsa_public_key2: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__72414f2a9320dd73073a9cfd82d56b9f7c834226827c1ef0171ee81418205d13(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c70d58a7dde72cf09c0145b794bb011cb77822b7c8d91de012cabddf0dc2f22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__214a9ff205ee25636ec25f2fd215554275c9a32ac3378657ae75588682eed3f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e767c3f4ed95e67d76786727e22e4670c693d1487eb2d8932b27be46669dd0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96d9ba76d0357a3a8d9bc943745d407c82f947929e8a54cddcd2bbbee1755977(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04f64251ded505f4cefd6d4d5a15536f93689a9c0ad81a5cdc2f1af931991f0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a755af3704f43753f2f278203f460cef46dcfaf3983e2953def6f033c7ec4c7b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9b1a168967696bb92a92bf73717f80fa6aac4e483681eb8903630ad5a692161(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3322d98011bab95439fe965e9f7921436ff80ae4534133e91799adc6d07a6903(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b80b44a9d175599c1710c1ea47900e135b503a5f2a7b488e134a8149de564bf3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee534fe04b85b73ab500205e9b2d0a244d624b079ae8eb269c0d80ae790dd1e4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0530543bda1184a7d929f8715889576a41c54bd5c8644b766fe2fc19dd25a36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abd62b8766f563c8bbaaf20c2117ac094fe19bf602c1dc6abca677209db98a0d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e87ca7689a8a9fc7bd76f1cc4572091cc8d1cd7db878cb8216171610932cb84(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__554b40f61c913aa67692d8d1364c59a569973014f8481649a24b270d88673a96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c384735f0ac2a22cda9e91e8ccb6aef7e481039f3eff75233e4d931bd764d63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bfab7a98ff160c89e43e23358130c93fe0eacfcf22f37020938d9cdef3270d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e609e3a1336017dda59d661522b3f1323545c41e3aa80da6eb0016a37a52ffa3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04bcd50566d7e5a0f6a888a622822b1bb2e90816ef4e28ff46370e9a97874f2c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    default_namespace: typing.Optional[builtins.str] = None,
    default_role: typing.Optional[builtins.str] = None,
    default_secondary_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    default_warehouse: typing.Optional[builtins.str] = None,
    disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    display_name: typing.Optional[builtins.str] = None,
    email: typing.Optional[builtins.str] = None,
    first_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    last_name: typing.Optional[builtins.str] = None,
    login_name: typing.Optional[builtins.str] = None,
    must_change_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    password: typing.Optional[builtins.str] = None,
    rsa_public_key: typing.Optional[builtins.str] = None,
    rsa_public_key2: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

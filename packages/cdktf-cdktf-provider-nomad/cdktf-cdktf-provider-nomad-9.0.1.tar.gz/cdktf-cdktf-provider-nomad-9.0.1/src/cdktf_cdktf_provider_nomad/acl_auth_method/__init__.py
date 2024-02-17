'''
# `nomad_acl_auth_method`

Refer to the Terraform Registry for docs: [`nomad_acl_auth_method`](https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method).
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


class AclAuthMethod(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.aclAuthMethod.AclAuthMethod",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method nomad_acl_auth_method}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        config: typing.Union["AclAuthMethodConfigA", typing.Dict[builtins.str, typing.Any]],
        max_token_ttl: builtins.str,
        name: builtins.str,
        token_locality: builtins.str,
        type: builtins.str,
        default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        token_name_format: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method nomad_acl_auth_method} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param config: config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#config AclAuthMethod#config}
        :param max_token_ttl: Defines the maximum life of a token created by this method. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#max_token_ttl AclAuthMethod#max_token_ttl}
        :param name: The identifier of the ACL Auth Method. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#name AclAuthMethod#name}
        :param token_locality: Defines whether the ACL Auth Method creates a local or global token when performing SSO login. This field must be set to either "local" or "global". Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#token_locality AclAuthMethod#token_locality}
        :param type: ACL Auth Method SSO workflow type. Currently, the only supported type is "OIDC.". Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#type AclAuthMethod#type}
        :param default: Defines whether this ACL Auth Method is to be set as default. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#default AclAuthMethod#default}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#id AclAuthMethod#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param token_name_format: Defines the token format for the authenticated users. This can be lightly templated using HIL '${foo}' syntax. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#token_name_format AclAuthMethod#token_name_format}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88e5e1175a243f6912e5cc0a978f498ad783f5331b4aa12703ed9829e4b6f791)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config_ = AclAuthMethodConfig(
            config=config,
            max_token_ttl=max_token_ttl,
            name=name,
            token_locality=token_locality,
            type=type,
            default=default,
            id=id,
            token_name_format=token_name_format,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config_])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a AclAuthMethod resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the AclAuthMethod to import.
        :param import_from_id: The id of the existing AclAuthMethod that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the AclAuthMethod to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e991f027a417fd71ec449e59eab0028db7d507dd7c20c4f784bf7f4886353db)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putConfig")
    def put_config(
        self,
        *,
        allowed_redirect_uris: typing.Sequence[builtins.str],
        oidc_client_id: builtins.str,
        oidc_client_secret: builtins.str,
        oidc_discovery_url: builtins.str,
        bound_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        claim_mappings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        discovery_ca_pem: typing.Optional[typing.Sequence[builtins.str]] = None,
        list_claim_mappings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        oidc_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        signing_algs: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param allowed_redirect_uris: A list of allowed values that can be used for the redirect URI. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#allowed_redirect_uris AclAuthMethod#allowed_redirect_uris}
        :param oidc_client_id: The OAuth Client ID configured with the OIDC provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#oidc_client_id AclAuthMethod#oidc_client_id}
        :param oidc_client_secret: The OAuth Client Secret configured with the OIDC provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#oidc_client_secret AclAuthMethod#oidc_client_secret}
        :param oidc_discovery_url: The OIDC Discovery URL, without any .well-known component (base path). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#oidc_discovery_url AclAuthMethod#oidc_discovery_url}
        :param bound_audiences: List of auth claims that are valid for login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#bound_audiences AclAuthMethod#bound_audiences}
        :param claim_mappings: Mappings of claims (key) that will be copied to a metadata field (value). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#claim_mappings AclAuthMethod#claim_mappings}
        :param discovery_ca_pem: PEM encoded CA certs for use by the TLS client used to talk with the OIDC Discovery URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#discovery_ca_pem AclAuthMethod#discovery_ca_pem}
        :param list_claim_mappings: Mappings of list claims (key) that will be copied to a metadata field (value). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#list_claim_mappings AclAuthMethod#list_claim_mappings}
        :param oidc_scopes: List of OIDC scopes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#oidc_scopes AclAuthMethod#oidc_scopes}
        :param signing_algs: A list of supported signing algorithms. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#signing_algs AclAuthMethod#signing_algs}
        '''
        value = AclAuthMethodConfigA(
            allowed_redirect_uris=allowed_redirect_uris,
            oidc_client_id=oidc_client_id,
            oidc_client_secret=oidc_client_secret,
            oidc_discovery_url=oidc_discovery_url,
            bound_audiences=bound_audiences,
            claim_mappings=claim_mappings,
            discovery_ca_pem=discovery_ca_pem,
            list_claim_mappings=list_claim_mappings,
            oidc_scopes=oidc_scopes,
            signing_algs=signing_algs,
        )

        return typing.cast(None, jsii.invoke(self, "putConfig", [value]))

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTokenNameFormat")
    def reset_token_name_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenNameFormat", []))

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
    @jsii.member(jsii_name="config")
    def config(self) -> "AclAuthMethodConfigAOutputReference":
        return typing.cast("AclAuthMethodConfigAOutputReference", jsii.get(self, "config"))

    @builtins.property
    @jsii.member(jsii_name="configInput")
    def config_input(self) -> typing.Optional["AclAuthMethodConfigA"]:
        return typing.cast(typing.Optional["AclAuthMethodConfigA"], jsii.get(self, "configInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTokenTtlInput")
    def max_token_ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxTokenTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenLocalityInput")
    def token_locality_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenLocalityInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenNameFormatInput")
    def token_name_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenNameFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "default"))

    @default.setter
    def default(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__874f660ea3ddbf1c73fffeaab17d193d5e6d48ff3f5f8716bd9ddcc49cb94edf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f32dde41415211740dd5a6c9ef230400f520d9a34ce1df7ed9ff0102fa386149)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maxTokenTtl")
    def max_token_ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxTokenTtl"))

    @max_token_ttl.setter
    def max_token_ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be346925ec08d59afc244cdf08358c5cddc35c9a6481a1575c62add0de39591f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTokenTtl", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0366dc74861723b8324b57cbbfafb5d109b3951b4d5f721069d5a334f158249)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tokenLocality")
    def token_locality(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenLocality"))

    @token_locality.setter
    def token_locality(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a47177f31deef12a5653bec19bfc71cf83a83f71c0ac42083a67d7ffa1982df1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenLocality", value)

    @builtins.property
    @jsii.member(jsii_name="tokenNameFormat")
    def token_name_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenNameFormat"))

    @token_name_format.setter
    def token_name_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e037d609120502442e896f26318c9012a7e84f4c5903793789947743a6351be0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenNameFormat", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff887f1006e7e39f2298eebc35f93c98f81c647f24c0c9dedc3bfd3ff3f17e3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.aclAuthMethod.AclAuthMethodConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "config": "config",
        "max_token_ttl": "maxTokenTtl",
        "name": "name",
        "token_locality": "tokenLocality",
        "type": "type",
        "default": "default",
        "id": "id",
        "token_name_format": "tokenNameFormat",
    },
)
class AclAuthMethodConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        config: typing.Union["AclAuthMethodConfigA", typing.Dict[builtins.str, typing.Any]],
        max_token_ttl: builtins.str,
        name: builtins.str,
        token_locality: builtins.str,
        type: builtins.str,
        default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        token_name_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param config: config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#config AclAuthMethod#config}
        :param max_token_ttl: Defines the maximum life of a token created by this method. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#max_token_ttl AclAuthMethod#max_token_ttl}
        :param name: The identifier of the ACL Auth Method. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#name AclAuthMethod#name}
        :param token_locality: Defines whether the ACL Auth Method creates a local or global token when performing SSO login. This field must be set to either "local" or "global". Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#token_locality AclAuthMethod#token_locality}
        :param type: ACL Auth Method SSO workflow type. Currently, the only supported type is "OIDC.". Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#type AclAuthMethod#type}
        :param default: Defines whether this ACL Auth Method is to be set as default. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#default AclAuthMethod#default}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#id AclAuthMethod#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param token_name_format: Defines the token format for the authenticated users. This can be lightly templated using HIL '${foo}' syntax. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#token_name_format AclAuthMethod#token_name_format}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(config, dict):
            config = AclAuthMethodConfigA(**config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ef4f91358041c3bf59857d24ac90f1be8c39fc9517b566fbfaeb4e118df2d44)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument max_token_ttl", value=max_token_ttl, expected_type=type_hints["max_token_ttl"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument token_locality", value=token_locality, expected_type=type_hints["token_locality"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument token_name_format", value=token_name_format, expected_type=type_hints["token_name_format"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config": config,
            "max_token_ttl": max_token_ttl,
            "name": name,
            "token_locality": token_locality,
            "type": type,
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
        if default is not None:
            self._values["default"] = default
        if id is not None:
            self._values["id"] = id
        if token_name_format is not None:
            self._values["token_name_format"] = token_name_format

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
    def config(self) -> "AclAuthMethodConfigA":
        '''config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#config AclAuthMethod#config}
        '''
        result = self._values.get("config")
        assert result is not None, "Required property 'config' is missing"
        return typing.cast("AclAuthMethodConfigA", result)

    @builtins.property
    def max_token_ttl(self) -> builtins.str:
        '''Defines the maximum life of a token created by this method.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#max_token_ttl AclAuthMethod#max_token_ttl}
        '''
        result = self._values.get("max_token_ttl")
        assert result is not None, "Required property 'max_token_ttl' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The identifier of the ACL Auth Method.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#name AclAuthMethod#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token_locality(self) -> builtins.str:
        '''Defines whether the ACL Auth Method creates a local or global token when performing SSO login.

        This field must be set to either "local" or "global".

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#token_locality AclAuthMethod#token_locality}
        '''
        result = self._values.get("token_locality")
        assert result is not None, "Required property 'token_locality' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''ACL Auth Method SSO workflow type. Currently, the only supported type is "OIDC.".

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#type AclAuthMethod#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Defines whether this ACL Auth Method is to be set as default.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#default AclAuthMethod#default}
        '''
        result = self._values.get("default")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#id AclAuthMethod#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_name_format(self) -> typing.Optional[builtins.str]:
        '''Defines the token format for the authenticated users. This can be lightly templated using HIL '${foo}' syntax.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#token_name_format AclAuthMethod#token_name_format}
        '''
        result = self._values.get("token_name_format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AclAuthMethodConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.aclAuthMethod.AclAuthMethodConfigA",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_redirect_uris": "allowedRedirectUris",
        "oidc_client_id": "oidcClientId",
        "oidc_client_secret": "oidcClientSecret",
        "oidc_discovery_url": "oidcDiscoveryUrl",
        "bound_audiences": "boundAudiences",
        "claim_mappings": "claimMappings",
        "discovery_ca_pem": "discoveryCaPem",
        "list_claim_mappings": "listClaimMappings",
        "oidc_scopes": "oidcScopes",
        "signing_algs": "signingAlgs",
    },
)
class AclAuthMethodConfigA:
    def __init__(
        self,
        *,
        allowed_redirect_uris: typing.Sequence[builtins.str],
        oidc_client_id: builtins.str,
        oidc_client_secret: builtins.str,
        oidc_discovery_url: builtins.str,
        bound_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        claim_mappings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        discovery_ca_pem: typing.Optional[typing.Sequence[builtins.str]] = None,
        list_claim_mappings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        oidc_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        signing_algs: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param allowed_redirect_uris: A list of allowed values that can be used for the redirect URI. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#allowed_redirect_uris AclAuthMethod#allowed_redirect_uris}
        :param oidc_client_id: The OAuth Client ID configured with the OIDC provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#oidc_client_id AclAuthMethod#oidc_client_id}
        :param oidc_client_secret: The OAuth Client Secret configured with the OIDC provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#oidc_client_secret AclAuthMethod#oidc_client_secret}
        :param oidc_discovery_url: The OIDC Discovery URL, without any .well-known component (base path). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#oidc_discovery_url AclAuthMethod#oidc_discovery_url}
        :param bound_audiences: List of auth claims that are valid for login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#bound_audiences AclAuthMethod#bound_audiences}
        :param claim_mappings: Mappings of claims (key) that will be copied to a metadata field (value). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#claim_mappings AclAuthMethod#claim_mappings}
        :param discovery_ca_pem: PEM encoded CA certs for use by the TLS client used to talk with the OIDC Discovery URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#discovery_ca_pem AclAuthMethod#discovery_ca_pem}
        :param list_claim_mappings: Mappings of list claims (key) that will be copied to a metadata field (value). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#list_claim_mappings AclAuthMethod#list_claim_mappings}
        :param oidc_scopes: List of OIDC scopes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#oidc_scopes AclAuthMethod#oidc_scopes}
        :param signing_algs: A list of supported signing algorithms. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#signing_algs AclAuthMethod#signing_algs}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdf814662741aef41134aaad0673de2654a0b04aa478103f3a5714ba9205daa8)
            check_type(argname="argument allowed_redirect_uris", value=allowed_redirect_uris, expected_type=type_hints["allowed_redirect_uris"])
            check_type(argname="argument oidc_client_id", value=oidc_client_id, expected_type=type_hints["oidc_client_id"])
            check_type(argname="argument oidc_client_secret", value=oidc_client_secret, expected_type=type_hints["oidc_client_secret"])
            check_type(argname="argument oidc_discovery_url", value=oidc_discovery_url, expected_type=type_hints["oidc_discovery_url"])
            check_type(argname="argument bound_audiences", value=bound_audiences, expected_type=type_hints["bound_audiences"])
            check_type(argname="argument claim_mappings", value=claim_mappings, expected_type=type_hints["claim_mappings"])
            check_type(argname="argument discovery_ca_pem", value=discovery_ca_pem, expected_type=type_hints["discovery_ca_pem"])
            check_type(argname="argument list_claim_mappings", value=list_claim_mappings, expected_type=type_hints["list_claim_mappings"])
            check_type(argname="argument oidc_scopes", value=oidc_scopes, expected_type=type_hints["oidc_scopes"])
            check_type(argname="argument signing_algs", value=signing_algs, expected_type=type_hints["signing_algs"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allowed_redirect_uris": allowed_redirect_uris,
            "oidc_client_id": oidc_client_id,
            "oidc_client_secret": oidc_client_secret,
            "oidc_discovery_url": oidc_discovery_url,
        }
        if bound_audiences is not None:
            self._values["bound_audiences"] = bound_audiences
        if claim_mappings is not None:
            self._values["claim_mappings"] = claim_mappings
        if discovery_ca_pem is not None:
            self._values["discovery_ca_pem"] = discovery_ca_pem
        if list_claim_mappings is not None:
            self._values["list_claim_mappings"] = list_claim_mappings
        if oidc_scopes is not None:
            self._values["oidc_scopes"] = oidc_scopes
        if signing_algs is not None:
            self._values["signing_algs"] = signing_algs

    @builtins.property
    def allowed_redirect_uris(self) -> typing.List[builtins.str]:
        '''A list of allowed values that can be used for the redirect URI.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#allowed_redirect_uris AclAuthMethod#allowed_redirect_uris}
        '''
        result = self._values.get("allowed_redirect_uris")
        assert result is not None, "Required property 'allowed_redirect_uris' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def oidc_client_id(self) -> builtins.str:
        '''The OAuth Client ID configured with the OIDC provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#oidc_client_id AclAuthMethod#oidc_client_id}
        '''
        result = self._values.get("oidc_client_id")
        assert result is not None, "Required property 'oidc_client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oidc_client_secret(self) -> builtins.str:
        '''The OAuth Client Secret configured with the OIDC provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#oidc_client_secret AclAuthMethod#oidc_client_secret}
        '''
        result = self._values.get("oidc_client_secret")
        assert result is not None, "Required property 'oidc_client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oidc_discovery_url(self) -> builtins.str:
        '''The OIDC Discovery URL, without any .well-known component (base path).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#oidc_discovery_url AclAuthMethod#oidc_discovery_url}
        '''
        result = self._values.get("oidc_discovery_url")
        assert result is not None, "Required property 'oidc_discovery_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bound_audiences(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of auth claims that are valid for login.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#bound_audiences AclAuthMethod#bound_audiences}
        '''
        result = self._values.get("bound_audiences")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def claim_mappings(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Mappings of claims (key) that will be copied to a metadata field (value).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#claim_mappings AclAuthMethod#claim_mappings}
        '''
        result = self._values.get("claim_mappings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def discovery_ca_pem(self) -> typing.Optional[typing.List[builtins.str]]:
        '''PEM encoded CA certs for use by the TLS client used to talk with the OIDC Discovery URL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#discovery_ca_pem AclAuthMethod#discovery_ca_pem}
        '''
        result = self._values.get("discovery_ca_pem")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def list_claim_mappings(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Mappings of list claims (key) that will be copied to a metadata field (value).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#list_claim_mappings AclAuthMethod#list_claim_mappings}
        '''
        result = self._values.get("list_claim_mappings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def oidc_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of OIDC scopes.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#oidc_scopes AclAuthMethod#oidc_scopes}
        '''
        result = self._values.get("oidc_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def signing_algs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of supported signing algorithms.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/nomad/2.1.1/docs/resources/acl_auth_method#signing_algs AclAuthMethod#signing_algs}
        '''
        result = self._values.get("signing_algs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AclAuthMethodConfigA(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AclAuthMethodConfigAOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.aclAuthMethod.AclAuthMethodConfigAOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6e1f3cb6d40cd42ba3feb184212321b36f13a09ad639358b7f94f04fc0b55e92)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBoundAudiences")
    def reset_bound_audiences(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBoundAudiences", []))

    @jsii.member(jsii_name="resetClaimMappings")
    def reset_claim_mappings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClaimMappings", []))

    @jsii.member(jsii_name="resetDiscoveryCaPem")
    def reset_discovery_ca_pem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiscoveryCaPem", []))

    @jsii.member(jsii_name="resetListClaimMappings")
    def reset_list_claim_mappings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetListClaimMappings", []))

    @jsii.member(jsii_name="resetOidcScopes")
    def reset_oidc_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOidcScopes", []))

    @jsii.member(jsii_name="resetSigningAlgs")
    def reset_signing_algs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigningAlgs", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRedirectUrisInput")
    def allowed_redirect_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRedirectUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="boundAudiencesInput")
    def bound_audiences_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "boundAudiencesInput"))

    @builtins.property
    @jsii.member(jsii_name="claimMappingsInput")
    def claim_mappings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "claimMappingsInput"))

    @builtins.property
    @jsii.member(jsii_name="discoveryCaPemInput")
    def discovery_ca_pem_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "discoveryCaPemInput"))

    @builtins.property
    @jsii.member(jsii_name="listClaimMappingsInput")
    def list_claim_mappings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "listClaimMappingsInput"))

    @builtins.property
    @jsii.member(jsii_name="oidcClientIdInput")
    def oidc_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oidcClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="oidcClientSecretInput")
    def oidc_client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oidcClientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="oidcDiscoveryUrlInput")
    def oidc_discovery_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oidcDiscoveryUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="oidcScopesInput")
    def oidc_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "oidcScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="signingAlgsInput")
    def signing_algs_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "signingAlgsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRedirectUris")
    def allowed_redirect_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRedirectUris"))

    @allowed_redirect_uris.setter
    def allowed_redirect_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f3813ddd9811f2f8521e5e70f2d8c7f4b27729883a58964148ad311454b2c3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRedirectUris", value)

    @builtins.property
    @jsii.member(jsii_name="boundAudiences")
    def bound_audiences(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "boundAudiences"))

    @bound_audiences.setter
    def bound_audiences(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e1abdfdaf8b95e8ca43bc15656db572b05f1cb080c37fb19e8c8f3ac4413c2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "boundAudiences", value)

    @builtins.property
    @jsii.member(jsii_name="claimMappings")
    def claim_mappings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "claimMappings"))

    @claim_mappings.setter
    def claim_mappings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e0fc8cf67658e546bdc1303d703b65d49f3ffeda2a8f6b487e2aaa8bf88e4f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "claimMappings", value)

    @builtins.property
    @jsii.member(jsii_name="discoveryCaPem")
    def discovery_ca_pem(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "discoveryCaPem"))

    @discovery_ca_pem.setter
    def discovery_ca_pem(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a51fc63187bc29f2e6cd275c276dcbe940a867f9d5ec431d74bcff44168ddd7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "discoveryCaPem", value)

    @builtins.property
    @jsii.member(jsii_name="listClaimMappings")
    def list_claim_mappings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "listClaimMappings"))

    @list_claim_mappings.setter
    def list_claim_mappings(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4516d781fe1e8bc8f518f37d26716577836564c44e443db3c7f8379f98c45fc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listClaimMappings", value)

    @builtins.property
    @jsii.member(jsii_name="oidcClientId")
    def oidc_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oidcClientId"))

    @oidc_client_id.setter
    def oidc_client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fee9aac5ec2f4252aff0c8419dcd9c9d23379996c4af771af47a690e5b4fab6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oidcClientId", value)

    @builtins.property
    @jsii.member(jsii_name="oidcClientSecret")
    def oidc_client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oidcClientSecret"))

    @oidc_client_secret.setter
    def oidc_client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f006e856f57ebc1f767bbf60bab9bfb1bd05f7062fd99b700c07531ffdb2077e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oidcClientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="oidcDiscoveryUrl")
    def oidc_discovery_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oidcDiscoveryUrl"))

    @oidc_discovery_url.setter
    def oidc_discovery_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d08fc806e59b4b273f16d87da2bcde9a076cb4ee30251b071b89f4a8dff5f60d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oidcDiscoveryUrl", value)

    @builtins.property
    @jsii.member(jsii_name="oidcScopes")
    def oidc_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oidcScopes"))

    @oidc_scopes.setter
    def oidc_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__748f78180c8079b4aebad3a822b131f71deaee6bfa338acc6e61e77ac9728d0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oidcScopes", value)

    @builtins.property
    @jsii.member(jsii_name="signingAlgs")
    def signing_algs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "signingAlgs"))

    @signing_algs.setter
    def signing_algs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ad32103935369bb305a4460c52d4609cb201ca65812645eb8c155124b146dde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signingAlgs", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AclAuthMethodConfigA]:
        return typing.cast(typing.Optional[AclAuthMethodConfigA], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AclAuthMethodConfigA]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8634cefe5196e1065a07b1e65202964388dae125936c71050d9cee663c46451d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AclAuthMethod",
    "AclAuthMethodConfig",
    "AclAuthMethodConfigA",
    "AclAuthMethodConfigAOutputReference",
]

publication.publish()

def _typecheckingstub__88e5e1175a243f6912e5cc0a978f498ad783f5331b4aa12703ed9829e4b6f791(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    config: typing.Union[AclAuthMethodConfigA, typing.Dict[builtins.str, typing.Any]],
    max_token_ttl: builtins.str,
    name: builtins.str,
    token_locality: builtins.str,
    type: builtins.str,
    default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    token_name_format: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__2e991f027a417fd71ec449e59eab0028db7d507dd7c20c4f784bf7f4886353db(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__874f660ea3ddbf1c73fffeaab17d193d5e6d48ff3f5f8716bd9ddcc49cb94edf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f32dde41415211740dd5a6c9ef230400f520d9a34ce1df7ed9ff0102fa386149(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be346925ec08d59afc244cdf08358c5cddc35c9a6481a1575c62add0de39591f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0366dc74861723b8324b57cbbfafb5d109b3951b4d5f721069d5a334f158249(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a47177f31deef12a5653bec19bfc71cf83a83f71c0ac42083a67d7ffa1982df1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e037d609120502442e896f26318c9012a7e84f4c5903793789947743a6351be0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff887f1006e7e39f2298eebc35f93c98f81c647f24c0c9dedc3bfd3ff3f17e3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ef4f91358041c3bf59857d24ac90f1be8c39fc9517b566fbfaeb4e118df2d44(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    config: typing.Union[AclAuthMethodConfigA, typing.Dict[builtins.str, typing.Any]],
    max_token_ttl: builtins.str,
    name: builtins.str,
    token_locality: builtins.str,
    type: builtins.str,
    default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    token_name_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdf814662741aef41134aaad0673de2654a0b04aa478103f3a5714ba9205daa8(
    *,
    allowed_redirect_uris: typing.Sequence[builtins.str],
    oidc_client_id: builtins.str,
    oidc_client_secret: builtins.str,
    oidc_discovery_url: builtins.str,
    bound_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
    claim_mappings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    discovery_ca_pem: typing.Optional[typing.Sequence[builtins.str]] = None,
    list_claim_mappings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    oidc_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    signing_algs: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e1f3cb6d40cd42ba3feb184212321b36f13a09ad639358b7f94f04fc0b55e92(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f3813ddd9811f2f8521e5e70f2d8c7f4b27729883a58964148ad311454b2c3a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e1abdfdaf8b95e8ca43bc15656db572b05f1cb080c37fb19e8c8f3ac4413c2e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e0fc8cf67658e546bdc1303d703b65d49f3ffeda2a8f6b487e2aaa8bf88e4f7(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a51fc63187bc29f2e6cd275c276dcbe940a867f9d5ec431d74bcff44168ddd7a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4516d781fe1e8bc8f518f37d26716577836564c44e443db3c7f8379f98c45fc5(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fee9aac5ec2f4252aff0c8419dcd9c9d23379996c4af771af47a690e5b4fab6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f006e856f57ebc1f767bbf60bab9bfb1bd05f7062fd99b700c07531ffdb2077e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d08fc806e59b4b273f16d87da2bcde9a076cb4ee30251b071b89f4a8dff5f60d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__748f78180c8079b4aebad3a822b131f71deaee6bfa338acc6e61e77ac9728d0d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ad32103935369bb305a4460c52d4609cb201ca65812645eb8c155124b146dde(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8634cefe5196e1065a07b1e65202964388dae125936c71050d9cee663c46451d(
    value: typing.Optional[AclAuthMethodConfigA],
) -> None:
    """Type checking stubs"""
    pass

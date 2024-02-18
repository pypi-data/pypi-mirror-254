'''
# AWS::SSMGuiConnect Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_ssmguiconnect as ssmguiconnect
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SSMGuiConnect construct libraries](https://constructs.dev/search?q=ssmguiconnect)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::SSMGuiConnect resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSMGuiConnect.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SSMGuiConnect](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSMGuiConnect.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
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

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnPreferences(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssmguiconnect.CfnPreferences",
):
    '''Definition of AWS::SSMGuiConnect::Preferences Resource Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmguiconnect-preferences.html
    :cloudformationResource: AWS::SSMGuiConnect::Preferences
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssmguiconnect as ssmguiconnect
        
        cfn_preferences = ssmguiconnect.CfnPreferences(self, "MyCfnPreferences",
            idle_connection=[ssmguiconnect.CfnPreferences.IdleConnectionPreferencesProperty(
                alert=ssmguiconnect.CfnPreferences.IdleConnectionAlertProperty(
                    value=123,
        
                    # the properties below are optional
                    type="type"
                ),
                timeout=ssmguiconnect.CfnPreferences.IdleConnectionTimeoutProperty(
                    value=123,
        
                    # the properties below are optional
                    type="type"
                )
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        idle_connection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPreferences.IdleConnectionPreferencesProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param idle_connection: A map for Idle Connection Preferences.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__045e31f70bcabcaa4437ed6c7e11fb8462233ba15c60675b143088abfe090752)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPreferencesProps(idle_connection=idle_connection)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59c7a3e2f3cdd2e9d3e4372020a482f624a989ea6d129be44dbf7f070aacda70)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3749ba458af11bbb5fb93542c69a8b02362071d74426f5a7f030e9ea0836efac)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAccountId")
    def attr_account_id(self) -> builtins.str:
        '''The AWS Account Id that the preference is associated with, used as the unique identifier for this resource.

        :cloudformationAttribute: AccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccountId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="idleConnection")
    def idle_connection(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPreferences.IdleConnectionPreferencesProperty"]]]]:
        '''A map for Idle Connection Preferences.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPreferences.IdleConnectionPreferencesProperty"]]]], jsii.get(self, "idleConnection"))

    @idle_connection.setter
    def idle_connection(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPreferences.IdleConnectionPreferencesProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab719a036cfee03bd05bd1268ec5770183d8de99f212a67f9c1350bdfb6c57f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleConnection", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmguiconnect.CfnPreferences.IdleConnectionAlertProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value", "type": "type"},
    )
    class IdleConnectionAlertProperty:
        def __init__(
            self,
            *,
            value: jsii.Number,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param value: Default: - 1
            :param type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmguiconnect-preferences-idleconnectionalert.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmguiconnect as ssmguiconnect
                
                idle_connection_alert_property = ssmguiconnect.CfnPreferences.IdleConnectionAlertProperty(
                    value=123,
                
                    # the properties below are optional
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bbe4925665d6f7ea3d8bc552c5d56c3cb572c9238e6022235242e81ee5dd87a7)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "value": value,
            }
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def value(self) -> jsii.Number:
            '''
            :default: - 1

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmguiconnect-preferences-idleconnectionalert.html#cfn-ssmguiconnect-preferences-idleconnectionalert-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmguiconnect-preferences-idleconnectionalert.html#cfn-ssmguiconnect-preferences-idleconnectionalert-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdleConnectionAlertProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmguiconnect.CfnPreferences.IdleConnectionPreferencesProperty",
        jsii_struct_bases=[],
        name_mapping={"alert": "alert", "timeout": "timeout"},
    )
    class IdleConnectionPreferencesProperty:
        def __init__(
            self,
            *,
            alert: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPreferences.IdleConnectionAlertProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            timeout: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPreferences.IdleConnectionTimeoutProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Idle Connection Preferences.

            :param alert: 
            :param timeout: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmguiconnect-preferences-idleconnectionpreferences.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmguiconnect as ssmguiconnect
                
                idle_connection_preferences_property = ssmguiconnect.CfnPreferences.IdleConnectionPreferencesProperty(
                    alert=ssmguiconnect.CfnPreferences.IdleConnectionAlertProperty(
                        value=123,
                
                        # the properties below are optional
                        type="type"
                    ),
                    timeout=ssmguiconnect.CfnPreferences.IdleConnectionTimeoutProperty(
                        value=123,
                
                        # the properties below are optional
                        type="type"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__41c010404bc38fc03000ecbd3228c89dc9f1e752b2f500a711fd5b8c9ed77a1a)
                check_type(argname="argument alert", value=alert, expected_type=type_hints["alert"])
                check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if alert is not None:
                self._values["alert"] = alert
            if timeout is not None:
                self._values["timeout"] = timeout

        @builtins.property
        def alert(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPreferences.IdleConnectionAlertProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmguiconnect-preferences-idleconnectionpreferences.html#cfn-ssmguiconnect-preferences-idleconnectionpreferences-alert
            '''
            result = self._values.get("alert")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPreferences.IdleConnectionAlertProperty"]], result)

        @builtins.property
        def timeout(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPreferences.IdleConnectionTimeoutProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmguiconnect-preferences-idleconnectionpreferences.html#cfn-ssmguiconnect-preferences-idleconnectionpreferences-timeout
            '''
            result = self._values.get("timeout")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPreferences.IdleConnectionTimeoutProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdleConnectionPreferencesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmguiconnect.CfnPreferences.IdleConnectionTimeoutProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value", "type": "type"},
    )
    class IdleConnectionTimeoutProperty:
        def __init__(
            self,
            *,
            value: jsii.Number,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param value: Default: - 10
            :param type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmguiconnect-preferences-idleconnectiontimeout.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmguiconnect as ssmguiconnect
                
                idle_connection_timeout_property = ssmguiconnect.CfnPreferences.IdleConnectionTimeoutProperty(
                    value=123,
                
                    # the properties below are optional
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3c76c83a3db9620d5734254439f4d906cfcdeecbf44afb4b7473d610bef05ca)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "value": value,
            }
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def value(self) -> jsii.Number:
            '''
            :default: - 10

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmguiconnect-preferences-idleconnectiontimeout.html#cfn-ssmguiconnect-preferences-idleconnectiontimeout-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmguiconnect-preferences-idleconnectiontimeout.html#cfn-ssmguiconnect-preferences-idleconnectiontimeout-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdleConnectionTimeoutProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssmguiconnect.CfnPreferencesProps",
    jsii_struct_bases=[],
    name_mapping={"idle_connection": "idleConnection"},
)
class CfnPreferencesProps:
    def __init__(
        self,
        *,
        idle_connection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPreferences.IdleConnectionPreferencesProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPreferences``.

        :param idle_connection: A map for Idle Connection Preferences.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmguiconnect-preferences.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssmguiconnect as ssmguiconnect
            
            cfn_preferences_props = ssmguiconnect.CfnPreferencesProps(
                idle_connection=[ssmguiconnect.CfnPreferences.IdleConnectionPreferencesProperty(
                    alert=ssmguiconnect.CfnPreferences.IdleConnectionAlertProperty(
                        value=123,
            
                        # the properties below are optional
                        type="type"
                    ),
                    timeout=ssmguiconnect.CfnPreferences.IdleConnectionTimeoutProperty(
                        value=123,
            
                        # the properties below are optional
                        type="type"
                    )
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98cae01e7635c618ff7b373fa87c04c806f9ee04274631cc3ad753469d5b8661)
            check_type(argname="argument idle_connection", value=idle_connection, expected_type=type_hints["idle_connection"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if idle_connection is not None:
            self._values["idle_connection"] = idle_connection

    @builtins.property
    def idle_connection(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPreferences.IdleConnectionPreferencesProperty]]]]:
        '''A map for Idle Connection Preferences.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmguiconnect-preferences.html#cfn-ssmguiconnect-preferences-idleconnection
        '''
        result = self._values.get("idle_connection")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPreferences.IdleConnectionPreferencesProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPreferencesProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnPreferences",
    "CfnPreferencesProps",
]

publication.publish()

def _typecheckingstub__045e31f70bcabcaa4437ed6c7e11fb8462233ba15c60675b143088abfe090752(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    idle_connection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPreferences.IdleConnectionPreferencesProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59c7a3e2f3cdd2e9d3e4372020a482f624a989ea6d129be44dbf7f070aacda70(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3749ba458af11bbb5fb93542c69a8b02362071d74426f5a7f030e9ea0836efac(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab719a036cfee03bd05bd1268ec5770183d8de99f212a67f9c1350bdfb6c57f7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPreferences.IdleConnectionPreferencesProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbe4925665d6f7ea3d8bc552c5d56c3cb572c9238e6022235242e81ee5dd87a7(
    *,
    value: jsii.Number,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41c010404bc38fc03000ecbd3228c89dc9f1e752b2f500a711fd5b8c9ed77a1a(
    *,
    alert: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPreferences.IdleConnectionAlertProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    timeout: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPreferences.IdleConnectionTimeoutProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3c76c83a3db9620d5734254439f4d906cfcdeecbf44afb4b7473d610bef05ca(
    *,
    value: jsii.Number,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98cae01e7635c618ff7b373fa87c04c806f9ee04274631cc3ad753469d5b8661(
    *,
    idle_connection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPreferences.IdleConnectionPreferencesProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

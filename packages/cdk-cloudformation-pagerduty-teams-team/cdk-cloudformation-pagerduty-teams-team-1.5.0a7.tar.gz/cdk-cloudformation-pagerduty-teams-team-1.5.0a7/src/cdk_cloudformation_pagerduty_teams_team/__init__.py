'''
# pagerduty-teams-team

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `PagerDuty::Teams::Team` v1.5.0.

## Description

Manage a team in PagerDuty.

## References

* [Documentation](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers)
* [Source](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name PagerDuty::Teams::Team \
  --publisher-id c830e97710da0c9954d80ba8df021e5439e7134b \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/c830e97710da0c9954d80ba8df021e5439e7134b/PagerDuty-Teams-Team \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `PagerDuty::Teams::Team`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fpagerduty-teams-team+v1.5.0).
* Issues related to `PagerDuty::Teams::Team` should be reported to the [publisher](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers).

## License

Distributed under the Apache-2.0 License.
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

from ._jsii import *

import aws_cdk as _aws_cdk_ceddda9d
import constructs as _constructs_77d1e7e8


class CfnTeam(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/pagerduty-teams-team.CfnTeam",
):
    '''A CloudFormation ``PagerDuty::Teams::Team``.

    :cloudformationResource: PagerDuty::Teams::Team
    :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        html_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``PagerDuty::Teams::Team``.

        :param scope: - scope in which this resource is defined.
        :param id_: - scoped id of the resource.
        :param name: 
        :param description: 
        :param html_url: 
        :param id: 
        :param summary: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e56ff3fe49b475c2443818c137629422f31ae314f53701ac1503818040b6516)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        props = CfnTeamProps(
            name=name,
            description=description,
            html_url=html_url,
            id=id,
            summary=summary,
        )

        jsii.create(self.__class__, self, [scope, id_, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''Attribute ``PagerDuty::Teams::Team.Type``.

        :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnTeamProps":
        '''Resource props.'''
        return typing.cast("CfnTeamProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-teams-team.CfnTeamProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "html_url": "htmlUrl",
        "id": "id",
        "summary": "summary",
    },
)
class CfnTeamProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        html_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Manage a team in PagerDuty.

        :param name: 
        :param description: 
        :param html_url: 
        :param id: 
        :param summary: 

        :schema: CfnTeamProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9042d5c8807c42bc8c3a16450ad5e7801c36b28617aac8b38bec0dd05d472aab)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument html_url", value=html_url, expected_type=type_hints["html_url"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if html_url is not None:
            self._values["html_url"] = html_url
        if id is not None:
            self._values["id"] = id
        if summary is not None:
            self._values["summary"] = summary

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :schema: CfnTeamProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnTeamProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def html_url(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnTeamProps#HtmlUrl
        '''
        result = self._values.get("html_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnTeamProps#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnTeamProps#Summary
        '''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTeamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnTeam",
    "CfnTeamProps",
]

publication.publish()

def _typecheckingstub__9e56ff3fe49b475c2443818c137629422f31ae314f53701ac1503818040b6516(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    html_url: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    summary: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9042d5c8807c42bc8c3a16450ad5e7801c36b28617aac8b38bec0dd05d472aab(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    html_url: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    summary: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

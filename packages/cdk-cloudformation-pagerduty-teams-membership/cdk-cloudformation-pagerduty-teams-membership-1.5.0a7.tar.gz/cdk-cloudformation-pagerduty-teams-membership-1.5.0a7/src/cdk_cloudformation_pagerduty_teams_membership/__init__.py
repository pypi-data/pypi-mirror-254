'''
# pagerduty-teams-membership

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `PagerDuty::Teams::Membership` v1.5.0.

## Description

Manage a membership of a user into a team in PagerDuty.

## References

* [Documentation](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers)
* [Source](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name PagerDuty::Teams::Membership \
  --publisher-id c830e97710da0c9954d80ba8df021e5439e7134b \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/c830e97710da0c9954d80ba8df021e5439e7134b/PagerDuty-Teams-Membership \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `PagerDuty::Teams::Membership`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fpagerduty-teams-membership+v1.5.0).
* Issues related to `PagerDuty::Teams::Membership` should be reported to the [publisher](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers).

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


class CfnMembership(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/pagerduty-teams-membership.CfnMembership",
):
    '''A CloudFormation ``PagerDuty::Teams::Membership``.

    :cloudformationResource: PagerDuty::Teams::Membership
    :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        team_id: builtins.str,
        user_id: builtins.str,
        role: typing.Optional["Role"] = None,
    ) -> None:
        '''Create a new ``PagerDuty::Teams::Membership``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param team_id: 
        :param user_id: 
        :param role: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81c6179d24a5599b4734c5002b2df1e12e4b3741496e41517d6ec777df9e1c45)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMembershipProps(team_id=team_id, user_id=user_id, role=role)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnMembershipProps":
        '''Resource props.'''
        return typing.cast("CfnMembershipProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-teams-membership.CfnMembershipProps",
    jsii_struct_bases=[],
    name_mapping={"team_id": "teamId", "user_id": "userId", "role": "role"},
)
class CfnMembershipProps:
    def __init__(
        self,
        *,
        team_id: builtins.str,
        user_id: builtins.str,
        role: typing.Optional["Role"] = None,
    ) -> None:
        '''Manage a membership of a user into a team in PagerDuty.

        :param team_id: 
        :param user_id: 
        :param role: 

        :schema: CfnMembershipProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e847e4af26a86df21aaffbeebed6a4cce360301b2191cdf81946fe45d963b0e3)
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "team_id": team_id,
            "user_id": user_id,
        }
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def team_id(self) -> builtins.str:
        '''
        :schema: CfnMembershipProps#TeamId
        '''
        result = self._values.get("team_id")
        assert result is not None, "Required property 'team_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_id(self) -> builtins.str:
        '''
        :schema: CfnMembershipProps#UserId
        '''
        result = self._values.get("user_id")
        assert result is not None, "Required property 'user_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> typing.Optional["Role"]:
        '''
        :schema: CfnMembershipProps#Role
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional["Role"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMembershipProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@cdk-cloudformation/pagerduty-teams-membership.Role")
class Role(enum.Enum):
    '''The role of the user on the team.

    :schema: Role
    '''

    OBSERVER = "OBSERVER"
    '''observer.'''
    RESPONDER = "RESPONDER"
    '''responder.'''
    MANAGER = "MANAGER"
    '''manager.'''


__all__ = [
    "CfnMembership",
    "CfnMembershipProps",
    "Role",
]

publication.publish()

def _typecheckingstub__81c6179d24a5599b4734c5002b2df1e12e4b3741496e41517d6ec777df9e1c45(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    team_id: builtins.str,
    user_id: builtins.str,
    role: typing.Optional[Role] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e847e4af26a86df21aaffbeebed6a4cce360301b2191cdf81946fe45d963b0e3(
    *,
    team_id: builtins.str,
    user_id: builtins.str,
    role: typing.Optional[Role] = None,
) -> None:
    """Type checking stubs"""
    pass

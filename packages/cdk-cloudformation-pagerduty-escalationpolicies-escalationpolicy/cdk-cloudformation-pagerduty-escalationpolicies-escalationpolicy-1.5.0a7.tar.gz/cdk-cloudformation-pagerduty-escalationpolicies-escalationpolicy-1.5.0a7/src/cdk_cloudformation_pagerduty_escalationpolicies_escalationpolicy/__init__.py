'''
# pagerduty-escalationpolicies-escalationpolicy

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `PagerDuty::EscalationPolicies::EscalationPolicy` v1.5.0.

## Description

Manage an escalation policy in PagerDuty.

## References

* [Documentation](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers)
* [Source](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name PagerDuty::EscalationPolicies::EscalationPolicy \
  --publisher-id c830e97710da0c9954d80ba8df021e5439e7134b \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/c830e97710da0c9954d80ba8df021e5439e7134b/PagerDuty-EscalationPolicies-EscalationPolicy \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `PagerDuty::EscalationPolicies::EscalationPolicy`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fpagerduty-escalationpolicies-escalationpolicy+v1.5.0).
* Issues related to `PagerDuty::EscalationPolicies::EscalationPolicy` should be reported to the [publisher](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers).

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


class CfnEscalationPolicy(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/pagerduty-escalationpolicies-escalationpolicy.CfnEscalationPolicy",
):
    '''A CloudFormation ``PagerDuty::EscalationPolicies::EscalationPolicy``.

    :cloudformationResource: PagerDuty::EscalationPolicies::EscalationPolicy
    :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        escalation_rules: typing.Sequence[typing.Union["EscalationRule", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        html_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        num_loops: typing.Optional[jsii.Number] = None,
        on_call_handoff_notifications: typing.Optional["CfnEscalationPolicyPropsOnCallHandoffNotifications"] = None,
        summary: typing.Optional[builtins.str] = None,
        teams: typing.Optional[typing.Sequence[typing.Union["Team", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``PagerDuty::EscalationPolicies::EscalationPolicy``.

        :param scope: - scope in which this resource is defined.
        :param id_: - scoped id of the resource.
        :param escalation_rules: 
        :param name: The name of the escalation policy.
        :param description: Escalation policy description.
        :param html_url: 
        :param id: 
        :param num_loops: The number of times the escalation policy will repeat after reaching the end of its escalation.
        :param on_call_handoff_notifications: Determines how on call handoff notifications will be sent for users on the escalation policy. Defaults to "if_has_services". Default: if_has_services".
        :param summary: 
        :param teams: Teams associated with the policy. Account must have the teams ability to use this parameter.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4af38613008cf95ad6b9b0f104dd40d81df2d462b4247975ef94e04ad7875aa9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        props = CfnEscalationPolicyProps(
            escalation_rules=escalation_rules,
            name=name,
            description=description,
            html_url=html_url,
            id=id,
            num_loops=num_loops,
            on_call_handoff_notifications=on_call_handoff_notifications,
            summary=summary,
            teams=teams,
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
        '''Attribute ``PagerDuty::EscalationPolicies::EscalationPolicy.Type``.

        :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnEscalationPolicyProps":
        '''Resource props.'''
        return typing.cast("CfnEscalationPolicyProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-escalationpolicies-escalationpolicy.CfnEscalationPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "escalation_rules": "escalationRules",
        "name": "name",
        "description": "description",
        "html_url": "htmlUrl",
        "id": "id",
        "num_loops": "numLoops",
        "on_call_handoff_notifications": "onCallHandoffNotifications",
        "summary": "summary",
        "teams": "teams",
    },
)
class CfnEscalationPolicyProps:
    def __init__(
        self,
        *,
        escalation_rules: typing.Sequence[typing.Union["EscalationRule", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        html_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        num_loops: typing.Optional[jsii.Number] = None,
        on_call_handoff_notifications: typing.Optional["CfnEscalationPolicyPropsOnCallHandoffNotifications"] = None,
        summary: typing.Optional[builtins.str] = None,
        teams: typing.Optional[typing.Sequence[typing.Union["Team", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Manage an escalation policy in PagerDuty.

        :param escalation_rules: 
        :param name: The name of the escalation policy.
        :param description: Escalation policy description.
        :param html_url: 
        :param id: 
        :param num_loops: The number of times the escalation policy will repeat after reaching the end of its escalation.
        :param on_call_handoff_notifications: Determines how on call handoff notifications will be sent for users on the escalation policy. Defaults to "if_has_services". Default: if_has_services".
        :param summary: 
        :param teams: Teams associated with the policy. Account must have the teams ability to use this parameter.

        :schema: CfnEscalationPolicyProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebc265f42fa9b9c467f1db75ddd03cad8db839008562dcf4678f59b870570d97)
            check_type(argname="argument escalation_rules", value=escalation_rules, expected_type=type_hints["escalation_rules"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument html_url", value=html_url, expected_type=type_hints["html_url"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument num_loops", value=num_loops, expected_type=type_hints["num_loops"])
            check_type(argname="argument on_call_handoff_notifications", value=on_call_handoff_notifications, expected_type=type_hints["on_call_handoff_notifications"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument teams", value=teams, expected_type=type_hints["teams"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "escalation_rules": escalation_rules,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if html_url is not None:
            self._values["html_url"] = html_url
        if id is not None:
            self._values["id"] = id
        if num_loops is not None:
            self._values["num_loops"] = num_loops
        if on_call_handoff_notifications is not None:
            self._values["on_call_handoff_notifications"] = on_call_handoff_notifications
        if summary is not None:
            self._values["summary"] = summary
        if teams is not None:
            self._values["teams"] = teams

    @builtins.property
    def escalation_rules(self) -> typing.List["EscalationRule"]:
        '''
        :schema: CfnEscalationPolicyProps#EscalationRules
        '''
        result = self._values.get("escalation_rules")
        assert result is not None, "Required property 'escalation_rules' is missing"
        return typing.cast(typing.List["EscalationRule"], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the escalation policy.

        :schema: CfnEscalationPolicyProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Escalation policy description.

        :schema: CfnEscalationPolicyProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def html_url(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnEscalationPolicyProps#HtmlUrl
        '''
        result = self._values.get("html_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnEscalationPolicyProps#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_loops(self) -> typing.Optional[jsii.Number]:
        '''The number of times the escalation policy will repeat after reaching the end of its escalation.

        :schema: CfnEscalationPolicyProps#NumLoops
        '''
        result = self._values.get("num_loops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def on_call_handoff_notifications(
        self,
    ) -> typing.Optional["CfnEscalationPolicyPropsOnCallHandoffNotifications"]:
        '''Determines how on call handoff notifications will be sent for users on the escalation policy.

        Defaults to "if_has_services".

        :default: if_has_services".

        :schema: CfnEscalationPolicyProps#OnCallHandoffNotifications
        '''
        result = self._values.get("on_call_handoff_notifications")
        return typing.cast(typing.Optional["CfnEscalationPolicyPropsOnCallHandoffNotifications"], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnEscalationPolicyProps#Summary
        '''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def teams(self) -> typing.Optional[typing.List["Team"]]:
        '''Teams associated with the policy.

        Account must have the teams ability to use this parameter.

        :schema: CfnEscalationPolicyProps#Teams
        '''
        result = self._values.get("teams")
        return typing.cast(typing.Optional[typing.List["Team"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEscalationPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-escalationpolicies-escalationpolicy.CfnEscalationPolicyPropsOnCallHandoffNotifications"
)
class CfnEscalationPolicyPropsOnCallHandoffNotifications(enum.Enum):
    '''Determines how on call handoff notifications will be sent for users on the escalation policy.

    Defaults to "if_has_services".

    :default: if_has_services".

    :schema: CfnEscalationPolicyPropsOnCallHandoffNotifications
    '''

    IF_UNDERSCORE_HAS_UNDERSCORE_SERVICES = "IF_UNDERSCORE_HAS_UNDERSCORE_SERVICES"
    '''if_has_services.'''
    ALWAYS = "ALWAYS"
    '''always.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-escalationpolicies-escalationpolicy.EscalationRule",
    jsii_struct_bases=[],
    name_mapping={
        "escalation_delay_in_minutes": "escalationDelayInMinutes",
        "targets": "targets",
    },
)
class EscalationRule:
    def __init__(
        self,
        *,
        escalation_delay_in_minutes: jsii.Number,
        targets: typing.Sequence[typing.Union["Target", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param escalation_delay_in_minutes: The number of minutes before an unacknowledged incident escalates away from this rule.
        :param targets: The targets an incident should be assigned to upon reaching this rule.

        :schema: EscalationRule
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a22f1469250781fd48e052a0b4acd54103ce760e31f4cbffd88ce1629e261c3)
            check_type(argname="argument escalation_delay_in_minutes", value=escalation_delay_in_minutes, expected_type=type_hints["escalation_delay_in_minutes"])
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "escalation_delay_in_minutes": escalation_delay_in_minutes,
            "targets": targets,
        }

    @builtins.property
    def escalation_delay_in_minutes(self) -> jsii.Number:
        '''The number of minutes before an unacknowledged incident escalates away from this rule.

        :schema: EscalationRule#EscalationDelayInMinutes
        '''
        result = self._values.get("escalation_delay_in_minutes")
        assert result is not None, "Required property 'escalation_delay_in_minutes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def targets(self) -> typing.List["Target"]:
        '''The targets an incident should be assigned to upon reaching this rule.

        :schema: EscalationRule#Targets
        '''
        result = self._values.get("targets")
        assert result is not None, "Required property 'targets' is missing"
        return typing.cast(typing.List["Target"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EscalationRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-escalationpolicies-escalationpolicy.Target",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "type": "type"},
)
class Target:
    def __init__(self, *, id: builtins.str, type: "TargetType") -> None:
        '''
        :param id: 
        :param type: A string that determines the schema of the object. This must be the standard name for the entity, suffixed by _reference if the object is a reference./, =, +, and -.

        :schema: Target
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1a6e42b299f79edfd4ae3a73f334408a6989184c37cdc412551fd6e15012a66)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "type": type,
        }

    @builtins.property
    def id(self) -> builtins.str:
        '''
        :schema: Target#Id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> "TargetType":
        '''A string that determines the schema of the object.

        This must be the standard name for the entity, suffixed by _reference if the object is a reference./, =, +, and -.

        :schema: Target#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("TargetType", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Target(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-escalationpolicies-escalationpolicy.TargetType"
)
class TargetType(enum.Enum):
    '''A string that determines the schema of the object.

    This must be the standard name for the entity, suffixed by _reference if the object is a reference./, =, +, and -.

    :schema: TargetType
    '''

    USER = "USER"
    '''user.'''
    SCHEDULE = "SCHEDULE"
    '''schedule.'''
    USER_UNDERSCORE_REFERENCE = "USER_UNDERSCORE_REFERENCE"
    '''user_reference.'''
    SCHEDULE_UNDERSCORE_REFERENCE = "SCHEDULE_UNDERSCORE_REFERENCE"
    '''schedule_reference.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-escalationpolicies-escalationpolicy.Team",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "type": "type"},
)
class Team:
    def __init__(self, *, id: builtins.str, type: "TeamType") -> None:
        '''
        :param id: 
        :param type: A string that determines the schema of the object. This must be the standard name for the entity, suffixed by _reference if the object is a reference./, =, +, and -.

        :schema: Team
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13a35a57ca050fe003f9727ac29b5601cd1235935a9fac4e69dfed4b1d3c8fbc)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "type": type,
        }

    @builtins.property
    def id(self) -> builtins.str:
        '''
        :schema: Team#Id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> "TeamType":
        '''A string that determines the schema of the object.

        This must be the standard name for the entity, suffixed by _reference if the object is a reference./, =, +, and -.

        :schema: Team#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("TeamType", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Team(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-escalationpolicies-escalationpolicy.TeamType"
)
class TeamType(enum.Enum):
    '''A string that determines the schema of the object.

    This must be the standard name for the entity, suffixed by _reference if the object is a reference./, =, +, and -.

    :schema: TeamType
    '''

    TEAM_UNDERSCORE_REFERENCE = "TEAM_UNDERSCORE_REFERENCE"
    '''team_reference.'''


__all__ = [
    "CfnEscalationPolicy",
    "CfnEscalationPolicyProps",
    "CfnEscalationPolicyPropsOnCallHandoffNotifications",
    "EscalationRule",
    "Target",
    "TargetType",
    "Team",
    "TeamType",
]

publication.publish()

def _typecheckingstub__4af38613008cf95ad6b9b0f104dd40d81df2d462b4247975ef94e04ad7875aa9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    escalation_rules: typing.Sequence[typing.Union[EscalationRule, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    html_url: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    num_loops: typing.Optional[jsii.Number] = None,
    on_call_handoff_notifications: typing.Optional[CfnEscalationPolicyPropsOnCallHandoffNotifications] = None,
    summary: typing.Optional[builtins.str] = None,
    teams: typing.Optional[typing.Sequence[typing.Union[Team, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebc265f42fa9b9c467f1db75ddd03cad8db839008562dcf4678f59b870570d97(
    *,
    escalation_rules: typing.Sequence[typing.Union[EscalationRule, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    html_url: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    num_loops: typing.Optional[jsii.Number] = None,
    on_call_handoff_notifications: typing.Optional[CfnEscalationPolicyPropsOnCallHandoffNotifications] = None,
    summary: typing.Optional[builtins.str] = None,
    teams: typing.Optional[typing.Sequence[typing.Union[Team, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a22f1469250781fd48e052a0b4acd54103ce760e31f4cbffd88ce1629e261c3(
    *,
    escalation_delay_in_minutes: jsii.Number,
    targets: typing.Sequence[typing.Union[Target, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1a6e42b299f79edfd4ae3a73f334408a6989184c37cdc412551fd6e15012a66(
    *,
    id: builtins.str,
    type: TargetType,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13a35a57ca050fe003f9727ac29b5601cd1235935a9fac4e69dfed4b1d3c8fbc(
    *,
    id: builtins.str,
    type: TeamType,
) -> None:
    """Type checking stubs"""
    pass

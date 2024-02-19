'''
# pagerduty-users-user

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `PagerDuty::Users::User` v1.5.0.

## Description

Manage a user in PagerDuty.

## References

* [Documentation](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers)
* [Source](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name PagerDuty::Users::User \
  --publisher-id c830e97710da0c9954d80ba8df021e5439e7134b \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/c830e97710da0c9954d80ba8df021e5439e7134b/PagerDuty-Users-User \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `PagerDuty::Users::User`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fpagerduty-users-user+v1.5.0).
* Issues related to `PagerDuty::Users::User` should be reported to the [publisher](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers).

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


class CfnUser(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/pagerduty-users-user.CfnUser",
):
    '''A CloudFormation ``PagerDuty::Users::User``.

    :cloudformationResource: PagerDuty::Users::User
    :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        email: builtins.str,
        name: builtins.str,
        color: typing.Optional[builtins.str] = None,
        contact_methods: typing.Optional[typing.Sequence[typing.Union["ContactMethod", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        job_title: typing.Optional[builtins.str] = None,
        notification_rules: typing.Optional[typing.Sequence[typing.Union["NotificationRule", typing.Dict[builtins.str, typing.Any]]]] = None,
        role: typing.Optional["CfnUserPropsRole"] = None,
        time_zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``PagerDuty::Users::User``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param email: The user's email address.
        :param name: The name of the user.
        :param color: The schedule color.
        :param contact_methods: The list of contact methods for the user.
        :param description: The user's bio.
        :param job_title: The user's title.
        :param notification_rules: The list of notification rules for the user.
        :param role: The user role. Account must have the read_only_users ability to set a user as a read_only_user or a read_only_limited_user, and must have advanced permissions abilities to set a user as observer or restricted_access.
        :param time_zone: The preferred time zone name. If null, the account's time zone will be used.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6f8f0f348954a36e5664628f525999f2763ea5a7a57224324cc8245be70f791)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserProps(
            email=email,
            name=name,
            color=color,
            contact_methods=contact_methods,
            description=description,
            job_title=job_title,
            notification_rules=notification_rules,
            role=role,
            time_zone=time_zone,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAvatarUrl")
    def attr_avatar_url(self) -> builtins.str:
        '''Attribute ``PagerDuty::Users::User.AvatarUrl``.

        :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAvatarUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrHtmlUrl")
    def attr_html_url(self) -> builtins.str:
        '''Attribute ``PagerDuty::Users::User.HtmlUrl``.

        :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHtmlUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``PagerDuty::Users::User.Id``.

        :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrInvitationSent")
    def attr_invitation_sent(self) -> _aws_cdk_ceddda9d.IResolvable:
        '''Attribute ``PagerDuty::Users::User.InvitationSent``.

        :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
        '''
        return typing.cast(_aws_cdk_ceddda9d.IResolvable, jsii.get(self, "attrInvitationSent"))

    @builtins.property
    @jsii.member(jsii_name="attrSummary")
    def attr_summary(self) -> builtins.str:
        '''Attribute ``PagerDuty::Users::User.Summary``.

        :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSummary"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''Attribute ``PagerDuty::Users::User.Type``.

        :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnUserProps":
        '''Resource props.'''
        return typing.cast("CfnUserProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-users-user.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "email": "email",
        "name": "name",
        "color": "color",
        "contact_methods": "contactMethods",
        "description": "description",
        "job_title": "jobTitle",
        "notification_rules": "notificationRules",
        "role": "role",
        "time_zone": "timeZone",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        email: builtins.str,
        name: builtins.str,
        color: typing.Optional[builtins.str] = None,
        contact_methods: typing.Optional[typing.Sequence[typing.Union["ContactMethod", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        job_title: typing.Optional[builtins.str] = None,
        notification_rules: typing.Optional[typing.Sequence[typing.Union["NotificationRule", typing.Dict[builtins.str, typing.Any]]]] = None,
        role: typing.Optional["CfnUserPropsRole"] = None,
        time_zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Manage a user in PagerDuty.

        :param email: The user's email address.
        :param name: The name of the user.
        :param color: The schedule color.
        :param contact_methods: The list of contact methods for the user.
        :param description: The user's bio.
        :param job_title: The user's title.
        :param notification_rules: The list of notification rules for the user.
        :param role: The user role. Account must have the read_only_users ability to set a user as a read_only_user or a read_only_limited_user, and must have advanced permissions abilities to set a user as observer or restricted_access.
        :param time_zone: The preferred time zone name. If null, the account's time zone will be used.

        :schema: CfnUserProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7335cb4a9eed73448ef72c314c8047d4a2cecd3fc94931dd4dd4f70a428f241a)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument color", value=color, expected_type=type_hints["color"])
            check_type(argname="argument contact_methods", value=contact_methods, expected_type=type_hints["contact_methods"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument job_title", value=job_title, expected_type=type_hints["job_title"])
            check_type(argname="argument notification_rules", value=notification_rules, expected_type=type_hints["notification_rules"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "email": email,
            "name": name,
        }
        if color is not None:
            self._values["color"] = color
        if contact_methods is not None:
            self._values["contact_methods"] = contact_methods
        if description is not None:
            self._values["description"] = description
        if job_title is not None:
            self._values["job_title"] = job_title
        if notification_rules is not None:
            self._values["notification_rules"] = notification_rules
        if role is not None:
            self._values["role"] = role
        if time_zone is not None:
            self._values["time_zone"] = time_zone

    @builtins.property
    def email(self) -> builtins.str:
        '''The user's email address.

        :schema: CfnUserProps#Email
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the user.

        :schema: CfnUserProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def color(self) -> typing.Optional[builtins.str]:
        '''The schedule color.

        :schema: CfnUserProps#Color
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def contact_methods(self) -> typing.Optional[typing.List["ContactMethod"]]:
        '''The list of contact methods for the user.

        :schema: CfnUserProps#ContactMethods
        '''
        result = self._values.get("contact_methods")
        return typing.cast(typing.Optional[typing.List["ContactMethod"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The user's bio.

        :schema: CfnUserProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_title(self) -> typing.Optional[builtins.str]:
        '''The user's title.

        :schema: CfnUserProps#JobTitle
        '''
        result = self._values.get("job_title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_rules(self) -> typing.Optional[typing.List["NotificationRule"]]:
        '''The list of notification rules for the user.

        :schema: CfnUserProps#NotificationRules
        '''
        result = self._values.get("notification_rules")
        return typing.cast(typing.Optional[typing.List["NotificationRule"]], result)

    @builtins.property
    def role(self) -> typing.Optional["CfnUserPropsRole"]:
        '''The user role.

        Account must have the read_only_users ability to set a user as a read_only_user or a read_only_limited_user, and must have advanced permissions abilities to set a user as observer or restricted_access.

        :schema: CfnUserProps#Role
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional["CfnUserPropsRole"], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''The preferred time zone name.

        If null, the account's time zone will be used.

        :schema: CfnUserProps#TimeZone
        '''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@cdk-cloudformation/pagerduty-users-user.CfnUserPropsRole")
class CfnUserPropsRole(enum.Enum):
    '''The user role.

    Account must have the read_only_users ability to set a user as a read_only_user or a read_only_limited_user, and must have advanced permissions abilities to set a user as observer or restricted_access.

    :schema: CfnUserPropsRole
    '''

    ADMIN = "ADMIN"
    '''admin.'''
    LIMITED_UNDERSCORE_USER = "LIMITED_UNDERSCORE_USER"
    '''limited_user.'''
    OBSERVER = "OBSERVER"
    '''observer.'''
    OWNER = "OWNER"
    '''owner.'''
    READ_UNDERSCORE_ONLY_UNDERSCORE_USER = "READ_UNDERSCORE_ONLY_UNDERSCORE_USER"
    '''read_only_user.'''
    RESTRICTED_UNDERSCORE_ACCESS = "RESTRICTED_UNDERSCORE_ACCESS"
    '''restricted_access.'''
    READ_UNDERSCORE_ONLY_UNDERSCORE_LIMITED_UNDERSCORE_USER = "READ_UNDERSCORE_ONLY_UNDERSCORE_LIMITED_UNDERSCORE_USER"
    '''read_only_limited_user.'''
    USER = "USER"
    '''user.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-users-user.ContactMethod",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "summary": "summary", "type": "type"},
)
class ContactMethod:
    def __init__(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
        type: typing.Optional["ContactMethodType"] = None,
    ) -> None:
        '''
        :param id: 
        :param summary: A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to name, though it is not intended to be an identifier.
        :param type: A string that determines the schema of the object. This must be the standard name for the entity, suffixed by _reference if the object is a reference.

        :schema: ContactMethod
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db2d4ae0ddc172bd8ba45dddde8e83634f3a8646d1b0a54108523931ffba6f34)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if summary is not None:
            self._values["summary"] = summary
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ContactMethod#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client.

        In many cases, this will be identical to name, though it is not intended to be an identifier.

        :schema: ContactMethod#Summary
        '''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional["ContactMethodType"]:
        '''A string that determines the schema of the object.

        This must be the standard name for the entity, suffixed by _reference if the object is a reference.

        :schema: ContactMethod#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["ContactMethodType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactMethod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@cdk-cloudformation/pagerduty-users-user.ContactMethodType")
class ContactMethodType(enum.Enum):
    '''A string that determines the schema of the object.

    This must be the standard name for the entity, suffixed by _reference if the object is a reference.

    :schema: ContactMethodType
    '''

    EMAIL_UNDERSCORE_CONTACT_UNDERSCORE_METHOD_UNDERSCORE_REFERENCE = "EMAIL_UNDERSCORE_CONTACT_UNDERSCORE_METHOD_UNDERSCORE_REFERENCE"
    '''email_contact_method_reference.'''
    PHONE_UNDERSCORE_CONTACT_UNDERSCORE_METHOD_UNDERSCORE_REFERENCE = "PHONE_UNDERSCORE_CONTACT_UNDERSCORE_METHOD_UNDERSCORE_REFERENCE"
    '''phone_contact_method_reference.'''
    PUSH_UNDERSCORE_NOTIFICATION_UNDERSCORE_CONTACT_UNDERSCORE_METHOD_UNDERSCORE_REFERENCE = "PUSH_UNDERSCORE_NOTIFICATION_UNDERSCORE_CONTACT_UNDERSCORE_METHOD_UNDERSCORE_REFERENCE"
    '''push_notification_contact_method_reference.'''
    SMS_UNDERSCORE_CONTACT_UNDERSCORE_METHOD_UNDERSCORE_REFERENCE = "SMS_UNDERSCORE_CONTACT_UNDERSCORE_METHOD_UNDERSCORE_REFERENCE"
    '''sms_contact_method_reference.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-users-user.NotificationRule",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "summary": "summary", "type": "type"},
)
class NotificationRule:
    def __init__(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
        type: typing.Optional["NotificationRuleType"] = None,
    ) -> None:
        '''
        :param id: 
        :param summary: A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to name, though it is not intended to be an identifier.
        :param type: A string that determines the schema of the object. This must be the standard name for the entity, suffixed by _reference if the object is a reference.

        :schema: NotificationRule
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f877ff5418245abcbdb9db3d79685b1eea766e0d24ba3cec59762bf0fff4fbe0)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if summary is not None:
            self._values["summary"] = summary
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: NotificationRule#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client.

        In many cases, this will be identical to name, though it is not intended to be an identifier.

        :schema: NotificationRule#Summary
        '''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional["NotificationRuleType"]:
        '''A string that determines the schema of the object.

        This must be the standard name for the entity, suffixed by _reference if the object is a reference.

        :schema: NotificationRule#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["NotificationRuleType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@cdk-cloudformation/pagerduty-users-user.NotificationRuleType")
class NotificationRuleType(enum.Enum):
    '''A string that determines the schema of the object.

    This must be the standard name for the entity, suffixed by _reference if the object is a reference.

    :schema: NotificationRuleType
    '''

    ASSIGNMENT_UNDERSCORE_NOTIFICATION_UNDERSCORE_RULE_UNDERSCORE_REFERENCE = "ASSIGNMENT_UNDERSCORE_NOTIFICATION_UNDERSCORE_RULE_UNDERSCORE_REFERENCE"
    '''assignment_notification_rule_reference.'''


__all__ = [
    "CfnUser",
    "CfnUserProps",
    "CfnUserPropsRole",
    "ContactMethod",
    "ContactMethodType",
    "NotificationRule",
    "NotificationRuleType",
]

publication.publish()

def _typecheckingstub__a6f8f0f348954a36e5664628f525999f2763ea5a7a57224324cc8245be70f791(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    email: builtins.str,
    name: builtins.str,
    color: typing.Optional[builtins.str] = None,
    contact_methods: typing.Optional[typing.Sequence[typing.Union[ContactMethod, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    job_title: typing.Optional[builtins.str] = None,
    notification_rules: typing.Optional[typing.Sequence[typing.Union[NotificationRule, typing.Dict[builtins.str, typing.Any]]]] = None,
    role: typing.Optional[CfnUserPropsRole] = None,
    time_zone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7335cb4a9eed73448ef72c314c8047d4a2cecd3fc94931dd4dd4f70a428f241a(
    *,
    email: builtins.str,
    name: builtins.str,
    color: typing.Optional[builtins.str] = None,
    contact_methods: typing.Optional[typing.Sequence[typing.Union[ContactMethod, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    job_title: typing.Optional[builtins.str] = None,
    notification_rules: typing.Optional[typing.Sequence[typing.Union[NotificationRule, typing.Dict[builtins.str, typing.Any]]]] = None,
    role: typing.Optional[CfnUserPropsRole] = None,
    time_zone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db2d4ae0ddc172bd8ba45dddde8e83634f3a8646d1b0a54108523931ffba6f34(
    *,
    id: typing.Optional[builtins.str] = None,
    summary: typing.Optional[builtins.str] = None,
    type: typing.Optional[ContactMethodType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f877ff5418245abcbdb9db3d79685b1eea766e0d24ba3cec59762bf0fff4fbe0(
    *,
    id: typing.Optional[builtins.str] = None,
    summary: typing.Optional[builtins.str] = None,
    type: typing.Optional[NotificationRuleType] = None,
) -> None:
    """Type checking stubs"""
    pass

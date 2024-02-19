'''
# pagerduty-responseplays-responseplay

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `PagerDuty::ResponsePlays::ResponsePlay` v1.5.0.

## Description

Manage a response play in PagerDuty

## References

* [Documentation](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers)
* [Source](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name PagerDuty::ResponsePlays::ResponsePlay \
  --publisher-id c830e97710da0c9954d80ba8df021e5439e7134b \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/c830e97710da0c9954d80ba8df021e5439e7134b/PagerDuty-ResponsePlays-ResponsePlay \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `PagerDuty::ResponsePlays::ResponsePlay`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fpagerduty-responseplays-responseplay+v1.5.0).
* Issues related to `PagerDuty::ResponsePlays::ResponsePlay` should be reported to the [publisher](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers).

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


class CfnResponsePlay(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/pagerduty-responseplays-responseplay.CfnResponsePlay",
):
    '''A CloudFormation ``PagerDuty::ResponsePlays::ResponsePlay``.

    :cloudformationResource: PagerDuty::ResponsePlays::ResponsePlay
    :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        from_email: builtins.str,
        conference_number: typing.Optional[builtins.str] = None,
        conference_type: typing.Optional["CfnResponsePlayPropsConferenceType"] = None,
        conference_url: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        html_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        responders: typing.Optional[typing.Sequence[typing.Union["Responder", typing.Dict[builtins.str, typing.Any]]]] = None,
        responders_message: typing.Optional[builtins.str] = None,
        runnability: typing.Optional["CfnResponsePlayPropsRunnability"] = None,
        subscribers: typing.Optional[typing.Sequence[typing.Union["Subscriber", typing.Dict[builtins.str, typing.Any]]]] = None,
        subscribers_message: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
        team: typing.Any = None,
    ) -> None:
        '''Create a new ``PagerDuty::ResponsePlays::ResponsePlay``.

        :param scope: - scope in which this resource is defined.
        :param id_: - scoped id of the resource.
        :param from_email: The email address of a valid user associated with the account making the request.
        :param conference_number: The telephone number that will be set as the conference number for any incident on which this response play is run.
        :param conference_type: This field has three possible values and indicates how the response play was created. none : The response play had no conference_number or conference_url set at time of creation. manual : The response play had one or both of conference_number and conference_url set at time of creation. zoom : Customers with the Zoom-Integration Entitelment can use this value to dynamicly configure conference number and url for zoom
        :param conference_url: The URL that will be set as the conference URL for any incident on which this response play is run.
        :param description: The description of the response play.
        :param html_url: 
        :param id: 
        :param name: The name of the response play.
        :param responders: 
        :param responders_message: The content of the notification that will be sent to all incident subscribers upon the running of this response play. Note that this includes any users who may have already been subscribed to the incident prior to the running of this response play. If empty, no notifications will be sent.
        :param runnability: String representing how this response play is allowed to be run. Valid options are:. services: This response play cannot be manually run by any users. It will run automatically for new incidents triggered on any services that are configured with this response play. teams: This response play can be run manually on an incident only by members of its configured team. This option can only be selected when the team property for this response play is not empty. responders: This response play can be run manually on an incident by any responders in this account.
        :param subscribers: 
        :param subscribers_message: The content of the notification that will be sent to all incident subscribers upon the running of this response play. Note that this includes any users who may have already been subscribed to the incident prior to the running of this response play. If empty, no notifications will be sent.
        :param summary: 
        :param team: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f73632f823949feaa29e0bb15b99dd878c6acc70816f2326678e2e055f68537)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        props = CfnResponsePlayProps(
            from_email=from_email,
            conference_number=conference_number,
            conference_type=conference_type,
            conference_url=conference_url,
            description=description,
            html_url=html_url,
            id=id,
            name=name,
            responders=responders,
            responders_message=responders_message,
            runnability=runnability,
            subscribers=subscribers,
            subscribers_message=subscribers_message,
            summary=summary,
            team=team,
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
        '''Attribute ``PagerDuty::ResponsePlays::ResponsePlay.Type``.

        :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnResponsePlayProps":
        '''Resource props.'''
        return typing.cast("CfnResponsePlayProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-responseplays-responseplay.CfnResponsePlayProps",
    jsii_struct_bases=[],
    name_mapping={
        "from_email": "fromEmail",
        "conference_number": "conferenceNumber",
        "conference_type": "conferenceType",
        "conference_url": "conferenceUrl",
        "description": "description",
        "html_url": "htmlUrl",
        "id": "id",
        "name": "name",
        "responders": "responders",
        "responders_message": "respondersMessage",
        "runnability": "runnability",
        "subscribers": "subscribers",
        "subscribers_message": "subscribersMessage",
        "summary": "summary",
        "team": "team",
    },
)
class CfnResponsePlayProps:
    def __init__(
        self,
        *,
        from_email: builtins.str,
        conference_number: typing.Optional[builtins.str] = None,
        conference_type: typing.Optional["CfnResponsePlayPropsConferenceType"] = None,
        conference_url: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        html_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        responders: typing.Optional[typing.Sequence[typing.Union["Responder", typing.Dict[builtins.str, typing.Any]]]] = None,
        responders_message: typing.Optional[builtins.str] = None,
        runnability: typing.Optional["CfnResponsePlayPropsRunnability"] = None,
        subscribers: typing.Optional[typing.Sequence[typing.Union["Subscriber", typing.Dict[builtins.str, typing.Any]]]] = None,
        subscribers_message: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
        team: typing.Any = None,
    ) -> None:
        '''Manage a response play in PagerDuty.

        :param from_email: The email address of a valid user associated with the account making the request.
        :param conference_number: The telephone number that will be set as the conference number for any incident on which this response play is run.
        :param conference_type: This field has three possible values and indicates how the response play was created. none : The response play had no conference_number or conference_url set at time of creation. manual : The response play had one or both of conference_number and conference_url set at time of creation. zoom : Customers with the Zoom-Integration Entitelment can use this value to dynamicly configure conference number and url for zoom
        :param conference_url: The URL that will be set as the conference URL for any incident on which this response play is run.
        :param description: The description of the response play.
        :param html_url: 
        :param id: 
        :param name: The name of the response play.
        :param responders: 
        :param responders_message: The content of the notification that will be sent to all incident subscribers upon the running of this response play. Note that this includes any users who may have already been subscribed to the incident prior to the running of this response play. If empty, no notifications will be sent.
        :param runnability: String representing how this response play is allowed to be run. Valid options are:. services: This response play cannot be manually run by any users. It will run automatically for new incidents triggered on any services that are configured with this response play. teams: This response play can be run manually on an incident only by members of its configured team. This option can only be selected when the team property for this response play is not empty. responders: This response play can be run manually on an incident by any responders in this account.
        :param subscribers: 
        :param subscribers_message: The content of the notification that will be sent to all incident subscribers upon the running of this response play. Note that this includes any users who may have already been subscribed to the incident prior to the running of this response play. If empty, no notifications will be sent.
        :param summary: 
        :param team: 

        :schema: CfnResponsePlayProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__481c44139b056738eeb7e19669f2d1414b61c99653b1eb037770490ecb3fcda7)
            check_type(argname="argument from_email", value=from_email, expected_type=type_hints["from_email"])
            check_type(argname="argument conference_number", value=conference_number, expected_type=type_hints["conference_number"])
            check_type(argname="argument conference_type", value=conference_type, expected_type=type_hints["conference_type"])
            check_type(argname="argument conference_url", value=conference_url, expected_type=type_hints["conference_url"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument html_url", value=html_url, expected_type=type_hints["html_url"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument responders", value=responders, expected_type=type_hints["responders"])
            check_type(argname="argument responders_message", value=responders_message, expected_type=type_hints["responders_message"])
            check_type(argname="argument runnability", value=runnability, expected_type=type_hints["runnability"])
            check_type(argname="argument subscribers", value=subscribers, expected_type=type_hints["subscribers"])
            check_type(argname="argument subscribers_message", value=subscribers_message, expected_type=type_hints["subscribers_message"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument team", value=team, expected_type=type_hints["team"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "from_email": from_email,
        }
        if conference_number is not None:
            self._values["conference_number"] = conference_number
        if conference_type is not None:
            self._values["conference_type"] = conference_type
        if conference_url is not None:
            self._values["conference_url"] = conference_url
        if description is not None:
            self._values["description"] = description
        if html_url is not None:
            self._values["html_url"] = html_url
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if responders is not None:
            self._values["responders"] = responders
        if responders_message is not None:
            self._values["responders_message"] = responders_message
        if runnability is not None:
            self._values["runnability"] = runnability
        if subscribers is not None:
            self._values["subscribers"] = subscribers
        if subscribers_message is not None:
            self._values["subscribers_message"] = subscribers_message
        if summary is not None:
            self._values["summary"] = summary
        if team is not None:
            self._values["team"] = team

    @builtins.property
    def from_email(self) -> builtins.str:
        '''The email address of a valid user associated with the account making the request.

        :schema: CfnResponsePlayProps#FromEmail
        '''
        result = self._values.get("from_email")
        assert result is not None, "Required property 'from_email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def conference_number(self) -> typing.Optional[builtins.str]:
        '''The telephone number that will be set as the conference number for any incident on which this response play is run.

        :schema: CfnResponsePlayProps#ConferenceNumber
        '''
        result = self._values.get("conference_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def conference_type(self) -> typing.Optional["CfnResponsePlayPropsConferenceType"]:
        '''This field has three possible values and indicates how the response play was created.

        none : The response play had no conference_number or conference_url set at time of creation.
        manual : The response play had one or both of conference_number and conference_url set at time of creation.
        zoom : Customers with the Zoom-Integration Entitelment can use this value to dynamicly configure conference number and url for zoom

        :schema: CfnResponsePlayProps#ConferenceType
        '''
        result = self._values.get("conference_type")
        return typing.cast(typing.Optional["CfnResponsePlayPropsConferenceType"], result)

    @builtins.property
    def conference_url(self) -> typing.Optional[builtins.str]:
        '''The URL that will be set as the conference URL for any incident on which this response play is run.

        :schema: CfnResponsePlayProps#ConferenceUrl
        '''
        result = self._values.get("conference_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the response play.

        :schema: CfnResponsePlayProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def html_url(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnResponsePlayProps#HtmlUrl
        '''
        result = self._values.get("html_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnResponsePlayProps#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the response play.

        :schema: CfnResponsePlayProps#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def responders(self) -> typing.Optional[typing.List["Responder"]]:
        '''
        :schema: CfnResponsePlayProps#Responders
        '''
        result = self._values.get("responders")
        return typing.cast(typing.Optional[typing.List["Responder"]], result)

    @builtins.property
    def responders_message(self) -> typing.Optional[builtins.str]:
        '''The content of the notification that will be sent to all incident subscribers upon the running of this response play.

        Note that this includes any users who may have already been subscribed to the incident prior to the running of this response play. If empty, no notifications will be sent.

        :schema: CfnResponsePlayProps#RespondersMessage
        '''
        result = self._values.get("responders_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runnability(self) -> typing.Optional["CfnResponsePlayPropsRunnability"]:
        '''String representing how this response play is allowed to be run. Valid options are:.

        services: This response play cannot be manually run by any users. It will run automatically for new incidents triggered on any services that are configured with this response play.
        teams: This response play can be run manually on an incident only by members of its configured team. This option can only be selected when the team property for this response play is not empty.
        responders: This response play can be run manually on an incident by any responders in this account.

        :schema: CfnResponsePlayProps#Runnability
        '''
        result = self._values.get("runnability")
        return typing.cast(typing.Optional["CfnResponsePlayPropsRunnability"], result)

    @builtins.property
    def subscribers(self) -> typing.Optional[typing.List["Subscriber"]]:
        '''
        :schema: CfnResponsePlayProps#Subscribers
        '''
        result = self._values.get("subscribers")
        return typing.cast(typing.Optional[typing.List["Subscriber"]], result)

    @builtins.property
    def subscribers_message(self) -> typing.Optional[builtins.str]:
        '''The content of the notification that will be sent to all incident subscribers upon the running of this response play.

        Note that this includes any users who may have already been subscribed to the incident prior to the running of this response play. If empty, no notifications will be sent.

        :schema: CfnResponsePlayProps#SubscribersMessage
        '''
        result = self._values.get("subscribers_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnResponsePlayProps#Summary
        '''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def team(self) -> typing.Any:
        '''
        :schema: CfnResponsePlayProps#Team
        '''
        result = self._values.get("team")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResponsePlayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-responseplays-responseplay.CfnResponsePlayPropsConferenceType"
)
class CfnResponsePlayPropsConferenceType(enum.Enum):
    '''This field has three possible values and indicates how the response play was created.

    none : The response play had no conference_number or conference_url set at time of creation.
    manual : The response play had one or both of conference_number and conference_url set at time of creation.
    zoom : Customers with the Zoom-Integration Entitelment can use this value to dynamicly configure conference number and url for zoom

    :schema: CfnResponsePlayPropsConferenceType
    '''

    NONE = "NONE"
    '''none.'''
    MANUAL = "MANUAL"
    '''manual.'''
    ZOOM = "ZOOM"
    '''zoom.'''


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-responseplays-responseplay.CfnResponsePlayPropsRunnability"
)
class CfnResponsePlayPropsRunnability(enum.Enum):
    '''String representing how this response play is allowed to be run. Valid options are:.

    services: This response play cannot be manually run by any users. It will run automatically for new incidents triggered on any services that are configured with this response play.
    teams: This response play can be run manually on an incident only by members of its configured team. This option can only be selected when the team property for this response play is not empty.
    responders: This response play can be run manually on an incident by any responders in this account.

    :schema: CfnResponsePlayPropsRunnability
    '''

    SERVICES = "SERVICES"
    '''services.'''
    TEAMS = "TEAMS"
    '''teams.'''
    RESPONDERS = "RESPONDERS"
    '''responders.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-responseplays-responseplay.Responder",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "type": "type"},
)
class Responder:
    def __init__(self, *, id: builtins.str, type: "ResponderType") -> None:
        '''
        :param id: 
        :param type: A string that determines the schema of the object. This must be the standard name for the entity, suffixed by _reference if the object is a reference.

        :schema: Responder
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6d75d3a8d880393d9093834dd77885f8199169096ee7bcb5cbd93a7566b819d)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "type": type,
        }

    @builtins.property
    def id(self) -> builtins.str:
        '''
        :schema: Responder#Id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> "ResponderType":
        '''A string that determines the schema of the object.

        This must be the standard name for the entity, suffixed by _reference if the object is a reference.

        :schema: Responder#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("ResponderType", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Responder(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-responseplays-responseplay.ResponderType"
)
class ResponderType(enum.Enum):
    '''A string that determines the schema of the object.

    This must be the standard name for the entity, suffixed by _reference if the object is a reference.

    :schema: ResponderType
    '''

    USER_UNDERSCORE_REFERENCE = "USER_UNDERSCORE_REFERENCE"
    '''user_reference.'''
    ESCALATION_UNDERSCORE_POLICY_UNDERSCORE_REFERENCE = "ESCALATION_UNDERSCORE_POLICY_UNDERSCORE_REFERENCE"
    '''escalation_policy_reference.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-responseplays-responseplay.Subscriber",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "type": "type"},
)
class Subscriber:
    def __init__(self, *, id: builtins.str, type: "SubscriberType") -> None:
        '''
        :param id: 
        :param type: A string that determines the schema of the object. This must be the standard name for the entity, suffixed by _reference if the object is a reference.

        :schema: Subscriber
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd006e22a109acac888714b8078ecea18741c22ccf916b1b2a78a4c94db22d00)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "type": type,
        }

    @builtins.property
    def id(self) -> builtins.str:
        '''
        :schema: Subscriber#Id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> "SubscriberType":
        '''A string that determines the schema of the object.

        This must be the standard name for the entity, suffixed by _reference if the object is a reference.

        :schema: Subscriber#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("SubscriberType", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Subscriber(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-responseplays-responseplay.SubscriberType"
)
class SubscriberType(enum.Enum):
    '''A string that determines the schema of the object.

    This must be the standard name for the entity, suffixed by _reference if the object is a reference.

    :schema: SubscriberType
    '''

    USER_UNDERSCORE_REFERENCE = "USER_UNDERSCORE_REFERENCE"
    '''user_reference.'''
    TEAM_UNDERSCORE_REFERENCE = "TEAM_UNDERSCORE_REFERENCE"
    '''team_reference.'''


__all__ = [
    "CfnResponsePlay",
    "CfnResponsePlayProps",
    "CfnResponsePlayPropsConferenceType",
    "CfnResponsePlayPropsRunnability",
    "Responder",
    "ResponderType",
    "Subscriber",
    "SubscriberType",
]

publication.publish()

def _typecheckingstub__8f73632f823949feaa29e0bb15b99dd878c6acc70816f2326678e2e055f68537(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    from_email: builtins.str,
    conference_number: typing.Optional[builtins.str] = None,
    conference_type: typing.Optional[CfnResponsePlayPropsConferenceType] = None,
    conference_url: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    html_url: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    responders: typing.Optional[typing.Sequence[typing.Union[Responder, typing.Dict[builtins.str, typing.Any]]]] = None,
    responders_message: typing.Optional[builtins.str] = None,
    runnability: typing.Optional[CfnResponsePlayPropsRunnability] = None,
    subscribers: typing.Optional[typing.Sequence[typing.Union[Subscriber, typing.Dict[builtins.str, typing.Any]]]] = None,
    subscribers_message: typing.Optional[builtins.str] = None,
    summary: typing.Optional[builtins.str] = None,
    team: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__481c44139b056738eeb7e19669f2d1414b61c99653b1eb037770490ecb3fcda7(
    *,
    from_email: builtins.str,
    conference_number: typing.Optional[builtins.str] = None,
    conference_type: typing.Optional[CfnResponsePlayPropsConferenceType] = None,
    conference_url: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    html_url: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    responders: typing.Optional[typing.Sequence[typing.Union[Responder, typing.Dict[builtins.str, typing.Any]]]] = None,
    responders_message: typing.Optional[builtins.str] = None,
    runnability: typing.Optional[CfnResponsePlayPropsRunnability] = None,
    subscribers: typing.Optional[typing.Sequence[typing.Union[Subscriber, typing.Dict[builtins.str, typing.Any]]]] = None,
    subscribers_message: typing.Optional[builtins.str] = None,
    summary: typing.Optional[builtins.str] = None,
    team: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6d75d3a8d880393d9093834dd77885f8199169096ee7bcb5cbd93a7566b819d(
    *,
    id: builtins.str,
    type: ResponderType,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd006e22a109acac888714b8078ecea18741c22ccf916b1b2a78a4c94db22d00(
    *,
    id: builtins.str,
    type: SubscriberType,
) -> None:
    """Type checking stubs"""
    pass

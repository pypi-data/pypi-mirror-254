'''
# pagerduty-services-service

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `PagerDuty::Services::Service` v1.1.0.

## Description

Manage a Service in PagerDuty.

## References

* [Documentation](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers)
* [Source](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name PagerDuty::Services::Service \
  --publisher-id c830e97710da0c9954d80ba8df021e5439e7134b \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/c830e97710da0c9954d80ba8df021e5439e7134b/PagerDuty-Services-Service \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `PagerDuty::Services::Service`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fpagerduty-services-service+v1.1.0).
* Issues related to `PagerDuty::Services::Service` should be reported to the [publisher](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers).

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


class CfnService(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/pagerduty-services-service.CfnService",
):
    '''A CloudFormation ``PagerDuty::Services::Service``.

    :cloudformationResource: PagerDuty::Services::Service
    :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        escalation_policy_id: builtins.str,
        name: builtins.str,
        acknowledgement_timeout: typing.Optional[jsii.Number] = None,
        alert_creation: typing.Optional["CfnServicePropsAlertCreation"] = None,
        alert_grouping_parameters: typing.Optional[typing.Union["CfnServicePropsAlertGroupingParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        auto_pause_notifications_parameters: typing.Optional[typing.Union["CfnServicePropsAutoPauseNotificationsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        auto_resolve_timeout: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        html_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        incident_urgency_rule: typing.Optional[typing.Union["CfnServicePropsIncidentUrgencyRule", typing.Dict[builtins.str, typing.Any]]] = None,
        scheduled_actions: typing.Optional[typing.Sequence["ScheduledActionAt"]] = None,
        status: typing.Optional["CfnServicePropsStatus"] = None,
        summary: typing.Optional[builtins.str] = None,
        support_hours: typing.Optional[typing.Union["CfnServicePropsSupportHours", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``PagerDuty::Services::Service``.

        :param scope: - scope in which this resource is defined.
        :param id_: - scoped id of the resource.
        :param escalation_policy_id: The ID of the Escalation Policy.
        :param name: The name of the service.
        :param acknowledgement_timeout: A number that determines time in seconds that an incident changes to the Triggered State after being Acknowledged.
        :param alert_creation: String representing whether a service creates only incidents, or both alerts and incidents.
        :param alert_grouping_parameters: Object that defines how alerts on this service will be automatically grouped into incidents.
        :param auto_pause_notifications_parameters: Object that defines how alerts on this service are automatically suspended for a period of time before triggering, when identified as likely being transient.
        :param auto_resolve_timeout: A number that determines time in seconds that an incident is automatically resolved if left open for that long.
        :param description: The user-provided description of the service.
        :param html_url: 
        :param id: 
        :param incident_urgency_rule: Object representing the Incident Urgency Rule.
        :param scheduled_actions: The list of scheduled actions for the service.
        :param status: A string that represent the current state of the Service, allowed values are: active, warning, critical, maintenance, disabled.
        :param summary: 
        :param support_hours: Object representing Support Hours.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a791f1867f80d07ba5154dc405060728820ef0dfe16dd793ce8ab6d47385aa5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        props = CfnServiceProps(
            escalation_policy_id=escalation_policy_id,
            name=name,
            acknowledgement_timeout=acknowledgement_timeout,
            alert_creation=alert_creation,
            alert_grouping_parameters=alert_grouping_parameters,
            auto_pause_notifications_parameters=auto_pause_notifications_parameters,
            auto_resolve_timeout=auto_resolve_timeout,
            description=description,
            html_url=html_url,
            id=id,
            incident_urgency_rule=incident_urgency_rule,
            scheduled_actions=scheduled_actions,
            status=status,
            summary=summary,
            support_hours=support_hours,
        )

        jsii.create(self.__class__, self, [scope, id_, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrSelf")
    def attr_self(self) -> builtins.str:
        '''Attribute ``PagerDuty::Services::Service.Self``.

        :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSelf"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''Attribute ``PagerDuty::Services::Service.Type``.

        :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnServiceProps":
        '''Resource props.'''
        return typing.cast("CfnServiceProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-services-service.CfnServiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "escalation_policy_id": "escalationPolicyId",
        "name": "name",
        "acknowledgement_timeout": "acknowledgementTimeout",
        "alert_creation": "alertCreation",
        "alert_grouping_parameters": "alertGroupingParameters",
        "auto_pause_notifications_parameters": "autoPauseNotificationsParameters",
        "auto_resolve_timeout": "autoResolveTimeout",
        "description": "description",
        "html_url": "htmlUrl",
        "id": "id",
        "incident_urgency_rule": "incidentUrgencyRule",
        "scheduled_actions": "scheduledActions",
        "status": "status",
        "summary": "summary",
        "support_hours": "supportHours",
    },
)
class CfnServiceProps:
    def __init__(
        self,
        *,
        escalation_policy_id: builtins.str,
        name: builtins.str,
        acknowledgement_timeout: typing.Optional[jsii.Number] = None,
        alert_creation: typing.Optional["CfnServicePropsAlertCreation"] = None,
        alert_grouping_parameters: typing.Optional[typing.Union["CfnServicePropsAlertGroupingParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        auto_pause_notifications_parameters: typing.Optional[typing.Union["CfnServicePropsAutoPauseNotificationsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        auto_resolve_timeout: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        html_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        incident_urgency_rule: typing.Optional[typing.Union["CfnServicePropsIncidentUrgencyRule", typing.Dict[builtins.str, typing.Any]]] = None,
        scheduled_actions: typing.Optional[typing.Sequence["ScheduledActionAt"]] = None,
        status: typing.Optional["CfnServicePropsStatus"] = None,
        summary: typing.Optional[builtins.str] = None,
        support_hours: typing.Optional[typing.Union["CfnServicePropsSupportHours", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Manage a Service in PagerDuty.

        :param escalation_policy_id: The ID of the Escalation Policy.
        :param name: The name of the service.
        :param acknowledgement_timeout: A number that determines time in seconds that an incident changes to the Triggered State after being Acknowledged.
        :param alert_creation: String representing whether a service creates only incidents, or both alerts and incidents.
        :param alert_grouping_parameters: Object that defines how alerts on this service will be automatically grouped into incidents.
        :param auto_pause_notifications_parameters: Object that defines how alerts on this service are automatically suspended for a period of time before triggering, when identified as likely being transient.
        :param auto_resolve_timeout: A number that determines time in seconds that an incident is automatically resolved if left open for that long.
        :param description: The user-provided description of the service.
        :param html_url: 
        :param id: 
        :param incident_urgency_rule: Object representing the Incident Urgency Rule.
        :param scheduled_actions: The list of scheduled actions for the service.
        :param status: A string that represent the current state of the Service, allowed values are: active, warning, critical, maintenance, disabled.
        :param summary: 
        :param support_hours: Object representing Support Hours.

        :schema: CfnServiceProps
        '''
        if isinstance(alert_grouping_parameters, dict):
            alert_grouping_parameters = CfnServicePropsAlertGroupingParameters(**alert_grouping_parameters)
        if isinstance(auto_pause_notifications_parameters, dict):
            auto_pause_notifications_parameters = CfnServicePropsAutoPauseNotificationsParameters(**auto_pause_notifications_parameters)
        if isinstance(incident_urgency_rule, dict):
            incident_urgency_rule = CfnServicePropsIncidentUrgencyRule(**incident_urgency_rule)
        if isinstance(support_hours, dict):
            support_hours = CfnServicePropsSupportHours(**support_hours)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98f282e236a7f47acd8379b4bab3ccbe7e639835a523b5c8abf2fd2509e06d32)
            check_type(argname="argument escalation_policy_id", value=escalation_policy_id, expected_type=type_hints["escalation_policy_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument acknowledgement_timeout", value=acknowledgement_timeout, expected_type=type_hints["acknowledgement_timeout"])
            check_type(argname="argument alert_creation", value=alert_creation, expected_type=type_hints["alert_creation"])
            check_type(argname="argument alert_grouping_parameters", value=alert_grouping_parameters, expected_type=type_hints["alert_grouping_parameters"])
            check_type(argname="argument auto_pause_notifications_parameters", value=auto_pause_notifications_parameters, expected_type=type_hints["auto_pause_notifications_parameters"])
            check_type(argname="argument auto_resolve_timeout", value=auto_resolve_timeout, expected_type=type_hints["auto_resolve_timeout"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument html_url", value=html_url, expected_type=type_hints["html_url"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument incident_urgency_rule", value=incident_urgency_rule, expected_type=type_hints["incident_urgency_rule"])
            check_type(argname="argument scheduled_actions", value=scheduled_actions, expected_type=type_hints["scheduled_actions"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument support_hours", value=support_hours, expected_type=type_hints["support_hours"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "escalation_policy_id": escalation_policy_id,
            "name": name,
        }
        if acknowledgement_timeout is not None:
            self._values["acknowledgement_timeout"] = acknowledgement_timeout
        if alert_creation is not None:
            self._values["alert_creation"] = alert_creation
        if alert_grouping_parameters is not None:
            self._values["alert_grouping_parameters"] = alert_grouping_parameters
        if auto_pause_notifications_parameters is not None:
            self._values["auto_pause_notifications_parameters"] = auto_pause_notifications_parameters
        if auto_resolve_timeout is not None:
            self._values["auto_resolve_timeout"] = auto_resolve_timeout
        if description is not None:
            self._values["description"] = description
        if html_url is not None:
            self._values["html_url"] = html_url
        if id is not None:
            self._values["id"] = id
        if incident_urgency_rule is not None:
            self._values["incident_urgency_rule"] = incident_urgency_rule
        if scheduled_actions is not None:
            self._values["scheduled_actions"] = scheduled_actions
        if status is not None:
            self._values["status"] = status
        if summary is not None:
            self._values["summary"] = summary
        if support_hours is not None:
            self._values["support_hours"] = support_hours

    @builtins.property
    def escalation_policy_id(self) -> builtins.str:
        '''The ID of the Escalation Policy.

        :schema: CfnServiceProps#EscalationPolicyId
        '''
        result = self._values.get("escalation_policy_id")
        assert result is not None, "Required property 'escalation_policy_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the service.

        :schema: CfnServiceProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def acknowledgement_timeout(self) -> typing.Optional[jsii.Number]:
        '''A number that determines time in seconds that an incident changes to the Triggered State after being Acknowledged.

        :schema: CfnServiceProps#AcknowledgementTimeout
        '''
        result = self._values.get("acknowledgement_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def alert_creation(self) -> typing.Optional["CfnServicePropsAlertCreation"]:
        '''String representing whether a service creates only incidents, or both alerts and incidents.

        :schema: CfnServiceProps#AlertCreation
        '''
        result = self._values.get("alert_creation")
        return typing.cast(typing.Optional["CfnServicePropsAlertCreation"], result)

    @builtins.property
    def alert_grouping_parameters(
        self,
    ) -> typing.Optional["CfnServicePropsAlertGroupingParameters"]:
        '''Object that defines how alerts on this service will be automatically grouped into incidents.

        :schema: CfnServiceProps#AlertGroupingParameters
        '''
        result = self._values.get("alert_grouping_parameters")
        return typing.cast(typing.Optional["CfnServicePropsAlertGroupingParameters"], result)

    @builtins.property
    def auto_pause_notifications_parameters(
        self,
    ) -> typing.Optional["CfnServicePropsAutoPauseNotificationsParameters"]:
        '''Object that defines how alerts on this service are automatically suspended for a period of time before triggering, when identified as likely being transient.

        :schema: CfnServiceProps#AutoPauseNotificationsParameters
        '''
        result = self._values.get("auto_pause_notifications_parameters")
        return typing.cast(typing.Optional["CfnServicePropsAutoPauseNotificationsParameters"], result)

    @builtins.property
    def auto_resolve_timeout(self) -> typing.Optional[jsii.Number]:
        '''A number that determines time in seconds that an incident is automatically resolved if left open for that long.

        :schema: CfnServiceProps#AutoResolveTimeout
        '''
        result = self._values.get("auto_resolve_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The user-provided description of the service.

        :schema: CfnServiceProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def html_url(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnServiceProps#HtmlUrl
        '''
        result = self._values.get("html_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnServiceProps#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def incident_urgency_rule(
        self,
    ) -> typing.Optional["CfnServicePropsIncidentUrgencyRule"]:
        '''Object representing the Incident Urgency Rule.

        :schema: CfnServiceProps#IncidentUrgencyRule
        '''
        result = self._values.get("incident_urgency_rule")
        return typing.cast(typing.Optional["CfnServicePropsIncidentUrgencyRule"], result)

    @builtins.property
    def scheduled_actions(self) -> typing.Optional[typing.List["ScheduledActionAt"]]:
        '''The list of scheduled actions for the service.

        :schema: CfnServiceProps#ScheduledActions
        '''
        result = self._values.get("scheduled_actions")
        return typing.cast(typing.Optional[typing.List["ScheduledActionAt"]], result)

    @builtins.property
    def status(self) -> typing.Optional["CfnServicePropsStatus"]:
        '''A string that represent the current state of the Service, allowed values are: active, warning, critical, maintenance, disabled.

        :schema: CfnServiceProps#Status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional["CfnServicePropsStatus"], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnServiceProps#Summary
        '''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def support_hours(self) -> typing.Optional["CfnServicePropsSupportHours"]:
        '''Object representing Support Hours.

        :schema: CfnServiceProps#SupportHours
        '''
        result = self._values.get("support_hours")
        return typing.cast(typing.Optional["CfnServicePropsSupportHours"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-service.CfnServicePropsAlertCreation"
)
class CfnServicePropsAlertCreation(enum.Enum):
    '''String representing whether a service creates only incidents, or both alerts and incidents.

    :schema: CfnServicePropsAlertCreation
    '''

    CREATE_UNDERSCORE_INCIDENTS = "CREATE_UNDERSCORE_INCIDENTS"
    '''create_incidents.'''
    CREATE_UNDERSCORE_ALERTS_UNDERSCORE_AND_UNDERSCORE_INCIDENTS = "CREATE_UNDERSCORE_ALERTS_UNDERSCORE_AND_UNDERSCORE_INCIDENTS"
    '''create_alerts_and_incidents.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-services-service.CfnServicePropsAlertGroupingParameters",
    jsii_struct_bases=[],
    name_mapping={"config": "config", "type": "type"},
)
class CfnServicePropsAlertGroupingParameters:
    def __init__(
        self,
        *,
        config: typing.Optional[typing.Union["CfnServicePropsAlertGroupingParametersConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional["CfnServicePropsAlertGroupingParametersType"] = None,
    ) -> None:
        '''Object that defines how alerts on this service will be automatically grouped into incidents.

        :param config: Object representing configuration of the Alert Grouping.
        :param type: String representing the type of alert grouping, allowed values are: time, intelligent, content_based.

        :schema: CfnServicePropsAlertGroupingParameters
        '''
        if isinstance(config, dict):
            config = CfnServicePropsAlertGroupingParametersConfig(**config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79ec0a071ee7b8d6e1b2bfd87aaf42e3194ac9d38ab734deb7bb5c6f869d22e2)
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if config is not None:
            self._values["config"] = config
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def config(self) -> typing.Optional["CfnServicePropsAlertGroupingParametersConfig"]:
        '''Object representing configuration of the Alert Grouping.

        :schema: CfnServicePropsAlertGroupingParameters#Config
        '''
        result = self._values.get("config")
        return typing.cast(typing.Optional["CfnServicePropsAlertGroupingParametersConfig"], result)

    @builtins.property
    def type(self) -> typing.Optional["CfnServicePropsAlertGroupingParametersType"]:
        '''String representing the type of alert grouping, allowed values are: time, intelligent, content_based.

        :schema: CfnServicePropsAlertGroupingParameters#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["CfnServicePropsAlertGroupingParametersType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServicePropsAlertGroupingParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-services-service.CfnServicePropsAlertGroupingParametersConfig",
    jsii_struct_bases=[],
    name_mapping={"timeout": "timeout"},
)
class CfnServicePropsAlertGroupingParametersConfig:
    def __init__(self, *, timeout: typing.Optional[jsii.Number] = None) -> None:
        '''Object representing configuration of the Alert Grouping.

        :param timeout: Number representing the timeout of timeout for the Alert Grouping.

        :schema: CfnServicePropsAlertGroupingParametersConfig
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4841996ead4df4e17bc1605933a6229673692fda585e259c3284e706bf49787a)
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''Number representing the timeout of timeout for the Alert Grouping.

        :schema: CfnServicePropsAlertGroupingParametersConfig#Timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServicePropsAlertGroupingParametersConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-service.CfnServicePropsAlertGroupingParametersType"
)
class CfnServicePropsAlertGroupingParametersType(enum.Enum):
    '''String representing the type of alert grouping, allowed values are: time, intelligent, content_based.

    :schema: CfnServicePropsAlertGroupingParametersType
    '''

    TIME = "TIME"
    '''time.'''
    INTELLIGENT = "INTELLIGENT"
    '''intelligent.'''
    CONTENT_UNDERSCORE_BASED = "CONTENT_UNDERSCORE_BASED"
    '''content_based.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-services-service.CfnServicePropsAutoPauseNotificationsParameters",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "timeout": "timeout"},
)
class CfnServicePropsAutoPauseNotificationsParameters:
    def __init__(
        self,
        *,
        enabled: typing.Optional[builtins.bool] = None,
        timeout: typing.Optional["CfnServicePropsAutoPauseNotificationsParametersTimeout"] = None,
    ) -> None:
        '''Object that defines how alerts on this service are automatically suspended for a period of time before triggering, when identified as likely being transient.

        :param enabled: Boolean indicating if the Auto Pause Notification is enabled.
        :param timeout: Number representing the timeout for Auto Pause Notification, valid values are: 120, 180, 300, 600, 900.

        :schema: CfnServicePropsAutoPauseNotificationsParameters
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a0d59d818bef979d9bfdcbd02e10c3789f13c21a07998e9e7acd77f900ab8c2)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Boolean indicating if the Auto Pause Notification is enabled.

        :schema: CfnServicePropsAutoPauseNotificationsParameters#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def timeout(
        self,
    ) -> typing.Optional["CfnServicePropsAutoPauseNotificationsParametersTimeout"]:
        '''Number representing the timeout for Auto Pause Notification, valid values are: 120, 180, 300, 600, 900.

        :schema: CfnServicePropsAutoPauseNotificationsParameters#Timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["CfnServicePropsAutoPauseNotificationsParametersTimeout"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServicePropsAutoPauseNotificationsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-service.CfnServicePropsAutoPauseNotificationsParametersTimeout"
)
class CfnServicePropsAutoPauseNotificationsParametersTimeout(enum.Enum):
    '''Number representing the timeout for Auto Pause Notification, valid values are: 120, 180, 300, 600, 900.

    :schema: CfnServicePropsAutoPauseNotificationsParametersTimeout
    '''

    VALUE_120 = "VALUE_120"
    '''120.'''
    VALUE_180 = "VALUE_180"
    '''180.'''
    VALUE_300 = "VALUE_300"
    '''300.'''
    VALUE_600 = "VALUE_600"
    '''600.'''
    VALUE_900 = "VALUE_900"
    '''900.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-services-service.CfnServicePropsIncidentUrgencyRule",
    jsii_struct_bases=[],
    name_mapping={
        "during_support_hours": "duringSupportHours",
        "outside_support_hours": "outsideSupportHours",
        "type": "type",
        "urgency": "urgency",
    },
)
class CfnServicePropsIncidentUrgencyRule:
    def __init__(
        self,
        *,
        during_support_hours: typing.Optional[typing.Union["CfnServicePropsIncidentUrgencyRuleDuringSupportHours", typing.Dict[builtins.str, typing.Any]]] = None,
        outside_support_hours: typing.Optional[typing.Union["CfnServicePropsIncidentUrgencyRuleOutsideSupportHours", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional["UrgencyType"] = None,
        urgency: typing.Optional["Urgency"] = None,
    ) -> None:
        '''Object representing the Incident Urgency Rule.

        :param during_support_hours: Object representing the Incident Urgency Rule during support hours.
        :param outside_support_hours: Object representing the Incident Urgency Rule outside support hours.
        :param type: 
        :param urgency: 

        :schema: CfnServicePropsIncidentUrgencyRule
        '''
        if isinstance(during_support_hours, dict):
            during_support_hours = CfnServicePropsIncidentUrgencyRuleDuringSupportHours(**during_support_hours)
        if isinstance(outside_support_hours, dict):
            outside_support_hours = CfnServicePropsIncidentUrgencyRuleOutsideSupportHours(**outside_support_hours)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__662569dc4e7e6bfba66dfe7b2403644e9bcb17d057a493b1124cfee9c5c7bfc5)
            check_type(argname="argument during_support_hours", value=during_support_hours, expected_type=type_hints["during_support_hours"])
            check_type(argname="argument outside_support_hours", value=outside_support_hours, expected_type=type_hints["outside_support_hours"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument urgency", value=urgency, expected_type=type_hints["urgency"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if during_support_hours is not None:
            self._values["during_support_hours"] = during_support_hours
        if outside_support_hours is not None:
            self._values["outside_support_hours"] = outside_support_hours
        if type is not None:
            self._values["type"] = type
        if urgency is not None:
            self._values["urgency"] = urgency

    @builtins.property
    def during_support_hours(
        self,
    ) -> typing.Optional["CfnServicePropsIncidentUrgencyRuleDuringSupportHours"]:
        '''Object representing the Incident Urgency Rule during support hours.

        :schema: CfnServicePropsIncidentUrgencyRule#DuringSupportHours
        '''
        result = self._values.get("during_support_hours")
        return typing.cast(typing.Optional["CfnServicePropsIncidentUrgencyRuleDuringSupportHours"], result)

    @builtins.property
    def outside_support_hours(
        self,
    ) -> typing.Optional["CfnServicePropsIncidentUrgencyRuleOutsideSupportHours"]:
        '''Object representing the Incident Urgency Rule outside support hours.

        :schema: CfnServicePropsIncidentUrgencyRule#OutsideSupportHours
        '''
        result = self._values.get("outside_support_hours")
        return typing.cast(typing.Optional["CfnServicePropsIncidentUrgencyRuleOutsideSupportHours"], result)

    @builtins.property
    def type(self) -> typing.Optional["UrgencyType"]:
        '''
        :schema: CfnServicePropsIncidentUrgencyRule#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["UrgencyType"], result)

    @builtins.property
    def urgency(self) -> typing.Optional["Urgency"]:
        '''
        :schema: CfnServicePropsIncidentUrgencyRule#Urgency
        '''
        result = self._values.get("urgency")
        return typing.cast(typing.Optional["Urgency"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServicePropsIncidentUrgencyRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-services-service.CfnServicePropsIncidentUrgencyRuleDuringSupportHours",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "urgency": "urgency"},
)
class CfnServicePropsIncidentUrgencyRuleDuringSupportHours:
    def __init__(
        self,
        *,
        type: typing.Optional["UrgencyType"] = None,
        urgency: typing.Optional["Urgency"] = None,
    ) -> None:
        '''Object representing the Incident Urgency Rule during support hours.

        :param type: 
        :param urgency: 

        :schema: CfnServicePropsIncidentUrgencyRuleDuringSupportHours
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c31fe8fe04a57c08816b0c096f7ddefe2a7902ad73b5a7c47c84afcba36eec51)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument urgency", value=urgency, expected_type=type_hints["urgency"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if type is not None:
            self._values["type"] = type
        if urgency is not None:
            self._values["urgency"] = urgency

    @builtins.property
    def type(self) -> typing.Optional["UrgencyType"]:
        '''
        :schema: CfnServicePropsIncidentUrgencyRuleDuringSupportHours#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["UrgencyType"], result)

    @builtins.property
    def urgency(self) -> typing.Optional["Urgency"]:
        '''
        :schema: CfnServicePropsIncidentUrgencyRuleDuringSupportHours#Urgency
        '''
        result = self._values.get("urgency")
        return typing.cast(typing.Optional["Urgency"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServicePropsIncidentUrgencyRuleDuringSupportHours(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-services-service.CfnServicePropsIncidentUrgencyRuleOutsideSupportHours",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "urgency": "urgency"},
)
class CfnServicePropsIncidentUrgencyRuleOutsideSupportHours:
    def __init__(
        self,
        *,
        type: typing.Optional["UrgencyType"] = None,
        urgency: typing.Optional["Urgency"] = None,
    ) -> None:
        '''Object representing the Incident Urgency Rule outside support hours.

        :param type: 
        :param urgency: 

        :schema: CfnServicePropsIncidentUrgencyRuleOutsideSupportHours
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ad3d2ce85bc1c77bed47cda23c60921dd582cabb34e957ccc35a165e8711dfd)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument urgency", value=urgency, expected_type=type_hints["urgency"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if type is not None:
            self._values["type"] = type
        if urgency is not None:
            self._values["urgency"] = urgency

    @builtins.property
    def type(self) -> typing.Optional["UrgencyType"]:
        '''
        :schema: CfnServicePropsIncidentUrgencyRuleOutsideSupportHours#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["UrgencyType"], result)

    @builtins.property
    def urgency(self) -> typing.Optional["Urgency"]:
        '''
        :schema: CfnServicePropsIncidentUrgencyRuleOutsideSupportHours#Urgency
        '''
        result = self._values.get("urgency")
        return typing.cast(typing.Optional["Urgency"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServicePropsIncidentUrgencyRuleOutsideSupportHours(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-service.CfnServicePropsStatus"
)
class CfnServicePropsStatus(enum.Enum):
    '''A string that represent the current state of the Service, allowed values are: active, warning, critical, maintenance, disabled.

    :schema: CfnServicePropsStatus
    '''

    ACTIVE = "ACTIVE"
    '''active.'''
    WARNING = "WARNING"
    '''warning.'''
    CRITICAL = "CRITICAL"
    '''critical.'''
    MAINTENANCE = "MAINTENANCE"
    '''maintenance.'''
    DISABLED = "DISABLED"
    '''disabled.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-services-service.CfnServicePropsSupportHours",
    jsii_struct_bases=[],
    name_mapping={
        "days_of_week": "daysOfWeek",
        "end_time": "endTime",
        "start_time": "startTime",
        "time_zone": "timeZone",
        "type": "type",
    },
)
class CfnServicePropsSupportHours:
    def __init__(
        self,
        *,
        days_of_week: typing.Optional[typing.Sequence[jsii.Number]] = None,
        end_time: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        time_zone: typing.Optional[builtins.str] = None,
        type: typing.Optional["CfnServicePropsSupportHoursType"] = None,
    ) -> None:
        '''Object representing Support Hours.

        :param days_of_week: Array representing the days of the week for support hours.
        :param end_time: String representing the support hours' ending time of day (date portion is ignored).
        :param start_time: String representing the support hours' starting time of day (date portion is ignored).
        :param time_zone: String representing the time zone for the support hours.
        :param type: String representing the type of support hours, value must be fixed_time_per_day.

        :schema: CfnServicePropsSupportHours
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bd85a541d4f56b74b5c938934876fd65f2e8093b790fbba4a7dc9ce6112ee8a)
            check_type(argname="argument days_of_week", value=days_of_week, expected_type=type_hints["days_of_week"])
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if days_of_week is not None:
            self._values["days_of_week"] = days_of_week
        if end_time is not None:
            self._values["end_time"] = end_time
        if start_time is not None:
            self._values["start_time"] = start_time
        if time_zone is not None:
            self._values["time_zone"] = time_zone
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def days_of_week(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Array representing the days of the week for support hours.

        :schema: CfnServicePropsSupportHours#DaysOfWeek
        '''
        result = self._values.get("days_of_week")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def end_time(self) -> typing.Optional[builtins.str]:
        '''String representing the support hours' ending time of day (date portion is ignored).

        :schema: CfnServicePropsSupportHours#EndTime
        '''
        result = self._values.get("end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''String representing the support hours' starting time of day (date portion is ignored).

        :schema: CfnServicePropsSupportHours#StartTime
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''String representing the time zone for the support hours.

        :schema: CfnServicePropsSupportHours#TimeZone
        '''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional["CfnServicePropsSupportHoursType"]:
        '''String representing the type of support hours, value must be fixed_time_per_day.

        :schema: CfnServicePropsSupportHours#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["CfnServicePropsSupportHoursType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServicePropsSupportHours(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-service.CfnServicePropsSupportHoursType"
)
class CfnServicePropsSupportHoursType(enum.Enum):
    '''String representing the type of support hours, value must be fixed_time_per_day.

    :schema: CfnServicePropsSupportHoursType
    '''

    FIXED_UNDERSCORE_TIME_UNDERSCORE_PER_UNDERSCORE_DAY = "FIXED_UNDERSCORE_TIME_UNDERSCORE_PER_UNDERSCORE_DAY"
    '''fixed_time_per_day.'''


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-service.ScheduledActionAt"
)
class ScheduledActionAt(enum.Enum):
    '''Represents when scheduled action will occur, allowed values are: support_hours_start, support_hours_end.

    :schema: ScheduledActionAt
    '''

    SUPPORT_UNDERSCORE_HOURS_UNDERSCORE_START = "SUPPORT_UNDERSCORE_HOURS_UNDERSCORE_START"
    '''support_hours_start.'''
    SUPPORT_UNDERSCORE_HOURS_UNDERSCORE_END = "SUPPORT_UNDERSCORE_HOURS_UNDERSCORE_END"
    '''support_hours_end.'''


@jsii.enum(jsii_type="@cdk-cloudformation/pagerduty-services-service.Urgency")
class Urgency(enum.Enum):
    '''String representing the incidents' urgency, if type is constant, allowed values are: low, high, severity_based.

    :schema: Urgency
    '''

    LOW = "LOW"
    '''low.'''
    HIGH = "HIGH"
    '''high.'''
    SEVERITY_UNDERSCORE_BASED = "SEVERITY_UNDERSCORE_BASED"
    '''severity_based.'''


@jsii.enum(jsii_type="@cdk-cloudformation/pagerduty-services-service.UrgencyType")
class UrgencyType(enum.Enum):
    '''String representing the type of incident urgency: whether it's constant, or it's dependent on the support hours.

    :schema: UrgencyType
    '''

    CONSTANT = "CONSTANT"
    '''constant.'''
    USE_UNDERSCORE_SUPPORT_UNDERSCORE_HOURS = "USE_UNDERSCORE_SUPPORT_UNDERSCORE_HOURS"
    '''use_support_hours.'''


__all__ = [
    "CfnService",
    "CfnServiceProps",
    "CfnServicePropsAlertCreation",
    "CfnServicePropsAlertGroupingParameters",
    "CfnServicePropsAlertGroupingParametersConfig",
    "CfnServicePropsAlertGroupingParametersType",
    "CfnServicePropsAutoPauseNotificationsParameters",
    "CfnServicePropsAutoPauseNotificationsParametersTimeout",
    "CfnServicePropsIncidentUrgencyRule",
    "CfnServicePropsIncidentUrgencyRuleDuringSupportHours",
    "CfnServicePropsIncidentUrgencyRuleOutsideSupportHours",
    "CfnServicePropsStatus",
    "CfnServicePropsSupportHours",
    "CfnServicePropsSupportHoursType",
    "ScheduledActionAt",
    "Urgency",
    "UrgencyType",
]

publication.publish()

def _typecheckingstub__7a791f1867f80d07ba5154dc405060728820ef0dfe16dd793ce8ab6d47385aa5(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    escalation_policy_id: builtins.str,
    name: builtins.str,
    acknowledgement_timeout: typing.Optional[jsii.Number] = None,
    alert_creation: typing.Optional[CfnServicePropsAlertCreation] = None,
    alert_grouping_parameters: typing.Optional[typing.Union[CfnServicePropsAlertGroupingParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_pause_notifications_parameters: typing.Optional[typing.Union[CfnServicePropsAutoPauseNotificationsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_resolve_timeout: typing.Optional[jsii.Number] = None,
    description: typing.Optional[builtins.str] = None,
    html_url: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    incident_urgency_rule: typing.Optional[typing.Union[CfnServicePropsIncidentUrgencyRule, typing.Dict[builtins.str, typing.Any]]] = None,
    scheduled_actions: typing.Optional[typing.Sequence[ScheduledActionAt]] = None,
    status: typing.Optional[CfnServicePropsStatus] = None,
    summary: typing.Optional[builtins.str] = None,
    support_hours: typing.Optional[typing.Union[CfnServicePropsSupportHours, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98f282e236a7f47acd8379b4bab3ccbe7e639835a523b5c8abf2fd2509e06d32(
    *,
    escalation_policy_id: builtins.str,
    name: builtins.str,
    acknowledgement_timeout: typing.Optional[jsii.Number] = None,
    alert_creation: typing.Optional[CfnServicePropsAlertCreation] = None,
    alert_grouping_parameters: typing.Optional[typing.Union[CfnServicePropsAlertGroupingParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_pause_notifications_parameters: typing.Optional[typing.Union[CfnServicePropsAutoPauseNotificationsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_resolve_timeout: typing.Optional[jsii.Number] = None,
    description: typing.Optional[builtins.str] = None,
    html_url: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    incident_urgency_rule: typing.Optional[typing.Union[CfnServicePropsIncidentUrgencyRule, typing.Dict[builtins.str, typing.Any]]] = None,
    scheduled_actions: typing.Optional[typing.Sequence[ScheduledActionAt]] = None,
    status: typing.Optional[CfnServicePropsStatus] = None,
    summary: typing.Optional[builtins.str] = None,
    support_hours: typing.Optional[typing.Union[CfnServicePropsSupportHours, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79ec0a071ee7b8d6e1b2bfd87aaf42e3194ac9d38ab734deb7bb5c6f869d22e2(
    *,
    config: typing.Optional[typing.Union[CfnServicePropsAlertGroupingParametersConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[CfnServicePropsAlertGroupingParametersType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4841996ead4df4e17bc1605933a6229673692fda585e259c3284e706bf49787a(
    *,
    timeout: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a0d59d818bef979d9bfdcbd02e10c3789f13c21a07998e9e7acd77f900ab8c2(
    *,
    enabled: typing.Optional[builtins.bool] = None,
    timeout: typing.Optional[CfnServicePropsAutoPauseNotificationsParametersTimeout] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__662569dc4e7e6bfba66dfe7b2403644e9bcb17d057a493b1124cfee9c5c7bfc5(
    *,
    during_support_hours: typing.Optional[typing.Union[CfnServicePropsIncidentUrgencyRuleDuringSupportHours, typing.Dict[builtins.str, typing.Any]]] = None,
    outside_support_hours: typing.Optional[typing.Union[CfnServicePropsIncidentUrgencyRuleOutsideSupportHours, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[UrgencyType] = None,
    urgency: typing.Optional[Urgency] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c31fe8fe04a57c08816b0c096f7ddefe2a7902ad73b5a7c47c84afcba36eec51(
    *,
    type: typing.Optional[UrgencyType] = None,
    urgency: typing.Optional[Urgency] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ad3d2ce85bc1c77bed47cda23c60921dd582cabb34e957ccc35a165e8711dfd(
    *,
    type: typing.Optional[UrgencyType] = None,
    urgency: typing.Optional[Urgency] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bd85a541d4f56b74b5c938934876fd65f2e8093b790fbba4a7dc9ce6112ee8a(
    *,
    days_of_week: typing.Optional[typing.Sequence[jsii.Number]] = None,
    end_time: typing.Optional[builtins.str] = None,
    start_time: typing.Optional[builtins.str] = None,
    time_zone: typing.Optional[builtins.str] = None,
    type: typing.Optional[CfnServicePropsSupportHoursType] = None,
) -> None:
    """Type checking stubs"""
    pass

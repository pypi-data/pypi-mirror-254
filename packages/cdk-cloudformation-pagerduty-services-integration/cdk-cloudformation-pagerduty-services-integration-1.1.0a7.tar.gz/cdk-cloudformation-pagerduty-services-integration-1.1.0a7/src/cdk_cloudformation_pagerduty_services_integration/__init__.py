'''
# pagerduty-services-integration

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `PagerDuty::Services::Integration` v1.1.0.

## Description

A resource schema representing a PagerDuty Integration belonging to a Service.

## References

* [Source](https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name PagerDuty::Services::Integration \
  --publisher-id c830e97710da0c9954d80ba8df021e5439e7134b \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/c830e97710da0c9954d80ba8df021e5439e7134b/PagerDuty-Services-Integration \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `PagerDuty::Services::Integration`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fpagerduty-services-integration+v1.1.0).
* Issues related to `PagerDuty::Services::Integration` should be reported to the [publisher](https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git).

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


class CfnIntegration(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.CfnIntegration",
):
    '''A CloudFormation ``PagerDuty::Services::Integration``.

    :cloudformationResource: PagerDuty::Services::Integration
    :link: https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git
    '''

    def __init__(
        self_,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        service_id: builtins.str,
        type: "CfnIntegrationPropsType",
        email_filter_mode: typing.Optional["CfnIntegrationPropsEmailFilterMode"] = None,
        email_filters: typing.Optional[typing.Sequence[typing.Union["EmailFilter", typing.Dict[builtins.str, typing.Any]]]] = None,
        email_incident_creation: typing.Optional["CfnIntegrationPropsEmailIncidentCreation"] = None,
        email_parsers: typing.Optional[typing.Sequence[typing.Union["EmailParser", typing.Dict[builtins.str, typing.Any]]]] = None,
        email_parsing_fallback: typing.Optional["CfnIntegrationPropsEmailParsingFallback"] = None,
        html_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        integration_email: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        self: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
        vendor_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``PagerDuty::Services::Integration``.

        :param scope: - scope in which this resource is defined.
        :param id_: - scoped id of the resource.
        :param service_id: The ID of the service integration should be associated with.
        :param type: The type of integration to be created. Refer to the API documentation for list of allowed values.
        :param email_filter_mode: Email filter mode. Specified only for generic_email_inbound_integration integrations.
        :param email_filters: Email filters. Specified only for generic_email_inbound_integration integrations.
        :param email_incident_creation: Email incident creation. Specified only for generic_email_inbound_integration integrations.
        :param email_parsers: Email parsers. Specified only for generic_email_inbound_integration integrations.
        :param email_parsing_fallback: Email Parsing Fallback. Specified only for generic_email_inbound_integration integrations.
        :param html_url: 
        :param id: 
        :param integration_email: Email address for the integration - must be set to an email address @your-subdomain.pagerduty.com. Specified only for generic_email_inbound_integration integrations.
        :param name: The name of integration to be created.
        :param self: 
        :param summary: 
        :param vendor_id: The ID of a third party vendor integration. Used for existing integrations.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5c315d74c1cf374637e7cd234d393c5dbd8aa739b0e24e0e8ff45de60c2833c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        props = CfnIntegrationProps(
            service_id=service_id,
            type=type,
            email_filter_mode=email_filter_mode,
            email_filters=email_filters,
            email_incident_creation=email_incident_creation,
            email_parsers=email_parsers,
            email_parsing_fallback=email_parsing_fallback,
            html_url=html_url,
            id=id,
            integration_email=integration_email,
            name=name,
            self=self,
            summary=summary,
            vendor_id=vendor_id,
        )

        jsii.create(self_.__class__, self_, [scope, id_, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrIntegrationUrl")
    def attr_integration_url(self) -> builtins.str:
        '''Attribute ``PagerDuty::Services::Integration.IntegrationUrl``.

        :link: https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIntegrationUrl"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnIntegrationProps":
        '''Resource props.'''
        return typing.cast("CfnIntegrationProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.CfnIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "service_id": "serviceId",
        "type": "type",
        "email_filter_mode": "emailFilterMode",
        "email_filters": "emailFilters",
        "email_incident_creation": "emailIncidentCreation",
        "email_parsers": "emailParsers",
        "email_parsing_fallback": "emailParsingFallback",
        "html_url": "htmlUrl",
        "id": "id",
        "integration_email": "integrationEmail",
        "name": "name",
        "self": "self",
        "summary": "summary",
        "vendor_id": "vendorId",
    },
)
class CfnIntegrationProps:
    def __init__(
        self_,
        *,
        service_id: builtins.str,
        type: "CfnIntegrationPropsType",
        email_filter_mode: typing.Optional["CfnIntegrationPropsEmailFilterMode"] = None,
        email_filters: typing.Optional[typing.Sequence[typing.Union["EmailFilter", typing.Dict[builtins.str, typing.Any]]]] = None,
        email_incident_creation: typing.Optional["CfnIntegrationPropsEmailIncidentCreation"] = None,
        email_parsers: typing.Optional[typing.Sequence[typing.Union["EmailParser", typing.Dict[builtins.str, typing.Any]]]] = None,
        email_parsing_fallback: typing.Optional["CfnIntegrationPropsEmailParsingFallback"] = None,
        html_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        integration_email: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        self: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
        vendor_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''A resource schema representing a PagerDuty Integration belonging to a Service.

        :param service_id: The ID of the service integration should be associated with.
        :param type: The type of integration to be created. Refer to the API documentation for list of allowed values.
        :param email_filter_mode: Email filter mode. Specified only for generic_email_inbound_integration integrations.
        :param email_filters: Email filters. Specified only for generic_email_inbound_integration integrations.
        :param email_incident_creation: Email incident creation. Specified only for generic_email_inbound_integration integrations.
        :param email_parsers: Email parsers. Specified only for generic_email_inbound_integration integrations.
        :param email_parsing_fallback: Email Parsing Fallback. Specified only for generic_email_inbound_integration integrations.
        :param html_url: 
        :param id: 
        :param integration_email: Email address for the integration - must be set to an email address @your-subdomain.pagerduty.com. Specified only for generic_email_inbound_integration integrations.
        :param name: The name of integration to be created.
        :param self: 
        :param summary: 
        :param vendor_id: The ID of a third party vendor integration. Used for existing integrations.

        :schema: CfnIntegrationProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25905378a05454df064a9176ef7f71e81084b77a73aec7c712e2649fb8f08db5)
            check_type(argname="argument service_id", value=service_id, expected_type=type_hints["service_id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument email_filter_mode", value=email_filter_mode, expected_type=type_hints["email_filter_mode"])
            check_type(argname="argument email_filters", value=email_filters, expected_type=type_hints["email_filters"])
            check_type(argname="argument email_incident_creation", value=email_incident_creation, expected_type=type_hints["email_incident_creation"])
            check_type(argname="argument email_parsers", value=email_parsers, expected_type=type_hints["email_parsers"])
            check_type(argname="argument email_parsing_fallback", value=email_parsing_fallback, expected_type=type_hints["email_parsing_fallback"])
            check_type(argname="argument html_url", value=html_url, expected_type=type_hints["html_url"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument integration_email", value=integration_email, expected_type=type_hints["integration_email"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument self", value=self, expected_type=type_hints["self"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument vendor_id", value=vendor_id, expected_type=type_hints["vendor_id"])
        self_._values: typing.Dict[builtins.str, typing.Any] = {
            "service_id": service_id,
            "type": type,
        }
        if email_filter_mode is not None:
            self_._values["email_filter_mode"] = email_filter_mode
        if email_filters is not None:
            self_._values["email_filters"] = email_filters
        if email_incident_creation is not None:
            self_._values["email_incident_creation"] = email_incident_creation
        if email_parsers is not None:
            self_._values["email_parsers"] = email_parsers
        if email_parsing_fallback is not None:
            self_._values["email_parsing_fallback"] = email_parsing_fallback
        if html_url is not None:
            self_._values["html_url"] = html_url
        if id is not None:
            self_._values["id"] = id
        if integration_email is not None:
            self_._values["integration_email"] = integration_email
        if name is not None:
            self_._values["name"] = name
        if self is not None:
            self_._values["self"] = self
        if summary is not None:
            self_._values["summary"] = summary
        if vendor_id is not None:
            self_._values["vendor_id"] = vendor_id

    @builtins.property
    def service_id(self) -> builtins.str:
        '''The ID of the service integration should be associated with.

        :schema: CfnIntegrationProps#ServiceId
        '''
        result = self._values.get("service_id")
        assert result is not None, "Required property 'service_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> "CfnIntegrationPropsType":
        '''The type of integration to be created.

        Refer to the API documentation for list of allowed values.

        :schema: CfnIntegrationProps#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("CfnIntegrationPropsType", result)

    @builtins.property
    def email_filter_mode(
        self,
    ) -> typing.Optional["CfnIntegrationPropsEmailFilterMode"]:
        '''Email filter mode.

        Specified only for generic_email_inbound_integration integrations.

        :schema: CfnIntegrationProps#EmailFilterMode
        '''
        result = self._values.get("email_filter_mode")
        return typing.cast(typing.Optional["CfnIntegrationPropsEmailFilterMode"], result)

    @builtins.property
    def email_filters(self) -> typing.Optional[typing.List["EmailFilter"]]:
        '''Email filters.

        Specified only for generic_email_inbound_integration integrations.

        :schema: CfnIntegrationProps#EmailFilters
        '''
        result = self._values.get("email_filters")
        return typing.cast(typing.Optional[typing.List["EmailFilter"]], result)

    @builtins.property
    def email_incident_creation(
        self,
    ) -> typing.Optional["CfnIntegrationPropsEmailIncidentCreation"]:
        '''Email incident creation.

        Specified only for generic_email_inbound_integration integrations.

        :schema: CfnIntegrationProps#EmailIncidentCreation
        '''
        result = self._values.get("email_incident_creation")
        return typing.cast(typing.Optional["CfnIntegrationPropsEmailIncidentCreation"], result)

    @builtins.property
    def email_parsers(self) -> typing.Optional[typing.List["EmailParser"]]:
        '''Email parsers.

        Specified only for generic_email_inbound_integration integrations.

        :schema: CfnIntegrationProps#EmailParsers
        '''
        result = self._values.get("email_parsers")
        return typing.cast(typing.Optional[typing.List["EmailParser"]], result)

    @builtins.property
    def email_parsing_fallback(
        self,
    ) -> typing.Optional["CfnIntegrationPropsEmailParsingFallback"]:
        '''Email Parsing Fallback.

        Specified only for generic_email_inbound_integration integrations.

        :schema: CfnIntegrationProps#EmailParsingFallback
        '''
        result = self._values.get("email_parsing_fallback")
        return typing.cast(typing.Optional["CfnIntegrationPropsEmailParsingFallback"], result)

    @builtins.property
    def html_url(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnIntegrationProps#HtmlUrl
        '''
        result = self._values.get("html_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnIntegrationProps#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_email(self) -> typing.Optional[builtins.str]:
        '''Email address for the integration - must be set to an email address @your-subdomain.pagerduty.com. Specified only for generic_email_inbound_integration integrations.

        :schema: CfnIntegrationProps#IntegrationEmail
        '''
        result = self._values.get("integration_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of integration to be created.

        :schema: CfnIntegrationProps#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def self(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnIntegrationProps#Self
        '''
        result = self._values.get("self")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnIntegrationProps#Summary
        '''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vendor_id(self) -> typing.Optional[builtins.str]:
        '''The ID of a third party vendor integration.

        Used for existing integrations.

        :schema: CfnIntegrationProps#VendorId
        '''
        result = self._values.get("vendor_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.CfnIntegrationPropsEmailFilterMode"
)
class CfnIntegrationPropsEmailFilterMode(enum.Enum):
    '''Email filter mode.

    Specified only for generic_email_inbound_integration integrations.

    :schema: CfnIntegrationPropsEmailFilterMode
    '''

    EMAIL = "EMAIL"
    '''email.'''
    OR_HYPHEN_RULES_HYPHEN_EMAIL = "OR_HYPHEN_RULES_HYPHEN_EMAIL"
    '''or-rules-email.'''
    AND_HYPHEN_RULES_HYPHEN_EMAIL = "AND_HYPHEN_RULES_HYPHEN_EMAIL"
    '''and-rules-email.'''


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.CfnIntegrationPropsEmailIncidentCreation"
)
class CfnIntegrationPropsEmailIncidentCreation(enum.Enum):
    '''Email incident creation.

    Specified only for generic_email_inbound_integration integrations.

    :schema: CfnIntegrationPropsEmailIncidentCreation
    '''

    ON_UNDERSCORE_NEW_UNDERSCORE_EMAIL = "ON_UNDERSCORE_NEW_UNDERSCORE_EMAIL"
    '''on_new_email.'''
    ON_UNDERSCORE_NEW_UNDERSCORE_EMAIL_UNDERSCORE_SUBJECT = "ON_UNDERSCORE_NEW_UNDERSCORE_EMAIL_UNDERSCORE_SUBJECT"
    '''on_new_email_subject.'''
    ONLY_UNDERSCORE_IF_UNDERSCORE_NO_UNDERSCORE_OPEN_UNDERSCORE_INCIDENTS = "ONLY_UNDERSCORE_IF_UNDERSCORE_NO_UNDERSCORE_OPEN_UNDERSCORE_INCIDENTS"
    '''only_if_no_open_incidents.'''
    USE_UNDERSCORE_RULES = "USE_UNDERSCORE_RULES"
    '''use_rules.'''


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.CfnIntegrationPropsEmailParsingFallback"
)
class CfnIntegrationPropsEmailParsingFallback(enum.Enum):
    '''Email Parsing Fallback.

    Specified only for generic_email_inbound_integration integrations.

    :schema: CfnIntegrationPropsEmailParsingFallback
    '''

    OPEN_UNDERSCORE_NEW_UNDERSCORE_INCIDENT = "OPEN_UNDERSCORE_NEW_UNDERSCORE_INCIDENT"
    '''open_new_incident.'''
    DISCARD = "DISCARD"
    '''discard.'''


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.CfnIntegrationPropsType"
)
class CfnIntegrationPropsType(enum.Enum):
    '''The type of integration to be created.

    Refer to the API documentation for list of allowed values.

    :schema: CfnIntegrationPropsType
    '''

    AWS_UNDERSCORE_CLOUDWATCH_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION = "AWS_UNDERSCORE_CLOUDWATCH_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION"
    '''aws_cloudwatch_inbound_integration.'''
    CLOUDKICK_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION = "CLOUDKICK_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION"
    '''cloudkick_inbound_integration.'''
    EVENT_UNDERSCORE_TRANSFORMER_UNDERSCORE_API_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION = "EVENT_UNDERSCORE_TRANSFORMER_UNDERSCORE_API_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION"
    '''event_transformer_api_inbound_integration.'''
    GENERIC_UNDERSCORE_EMAIL_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION = "GENERIC_UNDERSCORE_EMAIL_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION"
    '''generic_email_inbound_integration.'''
    GENERIC_UNDERSCORE_EVENTS_UNDERSCORE_API_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION = "GENERIC_UNDERSCORE_EVENTS_UNDERSCORE_API_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION"
    '''generic_events_api_inbound_integration.'''
    KEYNOTE_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION = "KEYNOTE_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION"
    '''keynote_inbound_integration.'''
    NAGIOS_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION = "NAGIOS_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION"
    '''nagios_inbound_integration.'''
    PINGDOM_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION = "PINGDOM_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION"
    '''pingdom_inbound_integration.'''
    SQL_UNDERSCORE_MONITOR_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION = "SQL_UNDERSCORE_MONITOR_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION"
    '''sql_monitor_inbound_integration.'''
    EVENTS_UNDERSCORE_API_UNDERSCORE_V2_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION = "EVENTS_UNDERSCORE_API_UNDERSCORE_V2_UNDERSCORE_INBOUND_UNDERSCORE_INTEGRATION"
    '''events_api_v2_inbound_integration.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.EmailFilter",
    jsii_struct_bases=[],
    name_mapping={
        "body_mode": "bodyMode",
        "body_regex": "bodyRegex",
        "from_email_mode": "fromEmailMode",
        "from_email_regex": "fromEmailRegex",
        "subject_mode": "subjectMode",
        "subject_regex": "subjectRegex",
    },
)
class EmailFilter:
    def __init__(
        self,
        *,
        body_mode: typing.Optional["EmailFilterBodyMode"] = None,
        body_regex: typing.Optional[builtins.str] = None,
        from_email_mode: typing.Optional["EmailFilterFromEmailMode"] = None,
        from_email_regex: typing.Optional[builtins.str] = None,
        subject_mode: typing.Optional["EmailFilterSubjectMode"] = None,
        subject_regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param body_mode: 
        :param body_regex: 
        :param from_email_mode: 
        :param from_email_regex: 
        :param subject_mode: 
        :param subject_regex: 

        :schema: EmailFilter
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__654d9141c74cc6d28ebd4c2515eefd1c4fc3de4406423633557122ad3dc43b8a)
            check_type(argname="argument body_mode", value=body_mode, expected_type=type_hints["body_mode"])
            check_type(argname="argument body_regex", value=body_regex, expected_type=type_hints["body_regex"])
            check_type(argname="argument from_email_mode", value=from_email_mode, expected_type=type_hints["from_email_mode"])
            check_type(argname="argument from_email_regex", value=from_email_regex, expected_type=type_hints["from_email_regex"])
            check_type(argname="argument subject_mode", value=subject_mode, expected_type=type_hints["subject_mode"])
            check_type(argname="argument subject_regex", value=subject_regex, expected_type=type_hints["subject_regex"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if body_mode is not None:
            self._values["body_mode"] = body_mode
        if body_regex is not None:
            self._values["body_regex"] = body_regex
        if from_email_mode is not None:
            self._values["from_email_mode"] = from_email_mode
        if from_email_regex is not None:
            self._values["from_email_regex"] = from_email_regex
        if subject_mode is not None:
            self._values["subject_mode"] = subject_mode
        if subject_regex is not None:
            self._values["subject_regex"] = subject_regex

    @builtins.property
    def body_mode(self) -> typing.Optional["EmailFilterBodyMode"]:
        '''
        :schema: EmailFilter#BodyMode
        '''
        result = self._values.get("body_mode")
        return typing.cast(typing.Optional["EmailFilterBodyMode"], result)

    @builtins.property
    def body_regex(self) -> typing.Optional[builtins.str]:
        '''
        :schema: EmailFilter#BodyRegex
        '''
        result = self._values.get("body_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def from_email_mode(self) -> typing.Optional["EmailFilterFromEmailMode"]:
        '''
        :schema: EmailFilter#FromEmailMode
        '''
        result = self._values.get("from_email_mode")
        return typing.cast(typing.Optional["EmailFilterFromEmailMode"], result)

    @builtins.property
    def from_email_regex(self) -> typing.Optional[builtins.str]:
        '''
        :schema: EmailFilter#FromEmailRegex
        '''
        result = self._values.get("from_email_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subject_mode(self) -> typing.Optional["EmailFilterSubjectMode"]:
        '''
        :schema: EmailFilter#SubjectMode
        '''
        result = self._values.get("subject_mode")
        return typing.cast(typing.Optional["EmailFilterSubjectMode"], result)

    @builtins.property
    def subject_regex(self) -> typing.Optional[builtins.str]:
        '''
        :schema: EmailFilter#SubjectRegex
        '''
        result = self._values.get("subject_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmailFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.EmailFilterBodyMode"
)
class EmailFilterBodyMode(enum.Enum):
    '''
    :schema: EmailFilterBodyMode
    '''

    MATCH = "MATCH"
    '''match.'''
    NO_HYPHEN_MATCH = "NO_HYPHEN_MATCH"
    '''no-match.'''
    ALWAYS = "ALWAYS"
    '''always.'''


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.EmailFilterFromEmailMode"
)
class EmailFilterFromEmailMode(enum.Enum):
    '''
    :schema: EmailFilterFromEmailMode
    '''

    MATCH = "MATCH"
    '''match.'''
    NO_HYPHEN_MATCH = "NO_HYPHEN_MATCH"
    '''no-match.'''
    ALWAYS = "ALWAYS"
    '''always.'''


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.EmailFilterSubjectMode"
)
class EmailFilterSubjectMode(enum.Enum):
    '''
    :schema: EmailFilterSubjectMode
    '''

    MATCH = "MATCH"
    '''match.'''
    NO_HYPHEN_MATCH = "NO_HYPHEN_MATCH"
    '''no-match.'''
    ALWAYS = "ALWAYS"
    '''always.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.EmailParser",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "match_predicate": "matchPredicate",
        "value_extractors": "valueExtractors",
    },
)
class EmailParser:
    def __init__(
        self,
        *,
        action: typing.Optional["EmailParserAction"] = None,
        match_predicate: typing.Optional[typing.Union["RootMatchPredicate", typing.Dict[builtins.str, typing.Any]]] = None,
        value_extractors: typing.Optional[typing.Sequence[typing.Union["ValueExtractor", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param action: 
        :param match_predicate: 
        :param value_extractors: 

        :schema: EmailParser
        '''
        if isinstance(match_predicate, dict):
            match_predicate = RootMatchPredicate(**match_predicate)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bc167d621a966f732f7471b88c206d9ab14ed9f798e70639d761dd832dd3c29)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument match_predicate", value=match_predicate, expected_type=type_hints["match_predicate"])
            check_type(argname="argument value_extractors", value=value_extractors, expected_type=type_hints["value_extractors"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if match_predicate is not None:
            self._values["match_predicate"] = match_predicate
        if value_extractors is not None:
            self._values["value_extractors"] = value_extractors

    @builtins.property
    def action(self) -> typing.Optional["EmailParserAction"]:
        '''
        :schema: EmailParser#Action
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional["EmailParserAction"], result)

    @builtins.property
    def match_predicate(self) -> typing.Optional["RootMatchPredicate"]:
        '''
        :schema: EmailParser#MatchPredicate
        '''
        result = self._values.get("match_predicate")
        return typing.cast(typing.Optional["RootMatchPredicate"], result)

    @builtins.property
    def value_extractors(self) -> typing.Optional[typing.List["ValueExtractor"]]:
        '''
        :schema: EmailParser#ValueExtractors
        '''
        result = self._values.get("value_extractors")
        return typing.cast(typing.Optional[typing.List["ValueExtractor"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmailParser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.EmailParserAction"
)
class EmailParserAction(enum.Enum):
    '''
    :schema: EmailParserAction
    '''

    TRIGGER = "TRIGGER"
    '''trigger.'''
    RESOLVE = "RESOLVE"
    '''resolve.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.MatchPredicate",
    jsii_struct_bases=[],
    name_mapping={"matcher": "matcher", "part": "part", "type": "type"},
)
class MatchPredicate:
    def __init__(
        self,
        *,
        matcher: typing.Optional[builtins.str] = None,
        part: typing.Optional["MatchPredicatePart"] = None,
        type: typing.Optional["MatchPredicateType"] = None,
    ) -> None:
        '''
        :param matcher: 
        :param part: 
        :param type: 

        :schema: MatchPredicate
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7a39e81c1da7d6ea61f0e86deb98ca91c03d49016446a7d12aa2a7468339ae0)
            check_type(argname="argument matcher", value=matcher, expected_type=type_hints["matcher"])
            check_type(argname="argument part", value=part, expected_type=type_hints["part"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if matcher is not None:
            self._values["matcher"] = matcher
        if part is not None:
            self._values["part"] = part
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def matcher(self) -> typing.Optional[builtins.str]:
        '''
        :schema: MatchPredicate#Matcher
        '''
        result = self._values.get("matcher")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def part(self) -> typing.Optional["MatchPredicatePart"]:
        '''
        :schema: MatchPredicate#Part
        '''
        result = self._values.get("part")
        return typing.cast(typing.Optional["MatchPredicatePart"], result)

    @builtins.property
    def type(self) -> typing.Optional["MatchPredicateType"]:
        '''
        :schema: MatchPredicate#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["MatchPredicateType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MatchPredicate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.MatchPredicatePart"
)
class MatchPredicatePart(enum.Enum):
    '''
    :schema: MatchPredicatePart
    '''

    BODY = "BODY"
    '''body.'''
    SUBJECT = "SUBJECT"
    '''subject.'''
    FROM_UNDERSCORE_ADDRESS = "FROM_UNDERSCORE_ADDRESS"
    '''from_address.'''


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.MatchPredicateType"
)
class MatchPredicateType(enum.Enum):
    '''
    :schema: MatchPredicateType
    '''

    ALL = "ALL"
    '''all.'''
    ANY = "ANY"
    '''any.'''
    NOT = "NOT"
    '''not.'''
    CONTAINS = "CONTAINS"
    '''contains.'''
    EXACTLY = "EXACTLY"
    '''exactly.'''
    REGEX = "REGEX"
    '''regex.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.RootMatchPredicate",
    jsii_struct_bases=[],
    name_mapping={"children": "children", "type": "type"},
)
class RootMatchPredicate:
    def __init__(
        self,
        *,
        children: typing.Optional[typing.Sequence[typing.Union[MatchPredicate, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional["RootMatchPredicateType"] = None,
    ) -> None:
        '''
        :param children: 
        :param type: 

        :schema: RootMatchPredicate
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25da52e7580f2f5fc0aed95511d9723338d701051fce23bc64e1b84bb12607ec)
            check_type(argname="argument children", value=children, expected_type=type_hints["children"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if children is not None:
            self._values["children"] = children
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def children(self) -> typing.Optional[typing.List[MatchPredicate]]:
        '''
        :schema: RootMatchPredicate#Children
        '''
        result = self._values.get("children")
        return typing.cast(typing.Optional[typing.List[MatchPredicate]], result)

    @builtins.property
    def type(self) -> typing.Optional["RootMatchPredicateType"]:
        '''
        :schema: RootMatchPredicate#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["RootMatchPredicateType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RootMatchPredicate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.RootMatchPredicateType"
)
class RootMatchPredicateType(enum.Enum):
    '''
    :schema: RootMatchPredicateType
    '''

    ALL = "ALL"
    '''all.'''
    ANY = "ANY"
    '''any.'''
    NOT = "NOT"
    '''not.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.ValueExtractor",
    jsii_struct_bases=[],
    name_mapping={
        "ends_before": "endsBefore",
        "part": "part",
        "regex": "regex",
        "starts_after": "startsAfter",
        "type": "type",
        "value_name": "valueName",
    },
)
class ValueExtractor:
    def __init__(
        self,
        *,
        ends_before: typing.Optional[builtins.str] = None,
        part: typing.Optional["ValueExtractorPart"] = None,
        regex: typing.Optional[builtins.str] = None,
        starts_after: typing.Optional[builtins.str] = None,
        type: typing.Optional["ValueExtractorType"] = None,
        value_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ends_before: 
        :param part: 
        :param regex: 
        :param starts_after: 
        :param type: 
        :param value_name: 

        :schema: ValueExtractor
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dfe332b3be3c39f29dd06554c5fa096c305cbc1ed5a3d020e5dc4dc928ef22a)
            check_type(argname="argument ends_before", value=ends_before, expected_type=type_hints["ends_before"])
            check_type(argname="argument part", value=part, expected_type=type_hints["part"])
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
            check_type(argname="argument starts_after", value=starts_after, expected_type=type_hints["starts_after"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value_name", value=value_name, expected_type=type_hints["value_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ends_before is not None:
            self._values["ends_before"] = ends_before
        if part is not None:
            self._values["part"] = part
        if regex is not None:
            self._values["regex"] = regex
        if starts_after is not None:
            self._values["starts_after"] = starts_after
        if type is not None:
            self._values["type"] = type
        if value_name is not None:
            self._values["value_name"] = value_name

    @builtins.property
    def ends_before(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ValueExtractor#EndsBefore
        '''
        result = self._values.get("ends_before")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def part(self) -> typing.Optional["ValueExtractorPart"]:
        '''
        :schema: ValueExtractor#Part
        '''
        result = self._values.get("part")
        return typing.cast(typing.Optional["ValueExtractorPart"], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ValueExtractor#Regex
        '''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def starts_after(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ValueExtractor#StartsAfter
        '''
        result = self._values.get("starts_after")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional["ValueExtractorType"]:
        '''
        :schema: ValueExtractor#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["ValueExtractorType"], result)

    @builtins.property
    def value_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ValueExtractor#ValueName
        '''
        result = self._values.get("value_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValueExtractor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.ValueExtractorPart"
)
class ValueExtractorPart(enum.Enum):
    '''
    :schema: ValueExtractorPart
    '''

    BODY = "BODY"
    '''body.'''
    SUBJECT = "SUBJECT"
    '''subject.'''
    FROM_UNDERSCORE_ADDRESS = "FROM_UNDERSCORE_ADDRESS"
    '''from_address.'''


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-services-integration.ValueExtractorType"
)
class ValueExtractorType(enum.Enum):
    '''
    :schema: ValueExtractorType
    '''

    ENTIRE = "ENTIRE"
    '''entire.'''
    REGEX = "REGEX"
    '''regex.'''
    BETWEEN = "BETWEEN"
    '''between.'''


__all__ = [
    "CfnIntegration",
    "CfnIntegrationProps",
    "CfnIntegrationPropsEmailFilterMode",
    "CfnIntegrationPropsEmailIncidentCreation",
    "CfnIntegrationPropsEmailParsingFallback",
    "CfnIntegrationPropsType",
    "EmailFilter",
    "EmailFilterBodyMode",
    "EmailFilterFromEmailMode",
    "EmailFilterSubjectMode",
    "EmailParser",
    "EmailParserAction",
    "MatchPredicate",
    "MatchPredicatePart",
    "MatchPredicateType",
    "RootMatchPredicate",
    "RootMatchPredicateType",
    "ValueExtractor",
    "ValueExtractorPart",
    "ValueExtractorType",
]

publication.publish()

def _typecheckingstub__a5c315d74c1cf374637e7cd234d393c5dbd8aa739b0e24e0e8ff45de60c2833c(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    service_id: builtins.str,
    type: CfnIntegrationPropsType,
    email_filter_mode: typing.Optional[CfnIntegrationPropsEmailFilterMode] = None,
    email_filters: typing.Optional[typing.Sequence[typing.Union[EmailFilter, typing.Dict[builtins.str, typing.Any]]]] = None,
    email_incident_creation: typing.Optional[CfnIntegrationPropsEmailIncidentCreation] = None,
    email_parsers: typing.Optional[typing.Sequence[typing.Union[EmailParser, typing.Dict[builtins.str, typing.Any]]]] = None,
    email_parsing_fallback: typing.Optional[CfnIntegrationPropsEmailParsingFallback] = None,
    html_url: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    integration_email: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    self: typing.Optional[builtins.str] = None,
    summary: typing.Optional[builtins.str] = None,
    vendor_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25905378a05454df064a9176ef7f71e81084b77a73aec7c712e2649fb8f08db5(
    *,
    service_id: builtins.str,
    type: CfnIntegrationPropsType,
    email_filter_mode: typing.Optional[CfnIntegrationPropsEmailFilterMode] = None,
    email_filters: typing.Optional[typing.Sequence[typing.Union[EmailFilter, typing.Dict[builtins.str, typing.Any]]]] = None,
    email_incident_creation: typing.Optional[CfnIntegrationPropsEmailIncidentCreation] = None,
    email_parsers: typing.Optional[typing.Sequence[typing.Union[EmailParser, typing.Dict[builtins.str, typing.Any]]]] = None,
    email_parsing_fallback: typing.Optional[CfnIntegrationPropsEmailParsingFallback] = None,
    html_url: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    integration_email: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    self: typing.Optional[builtins.str] = None,
    summary: typing.Optional[builtins.str] = None,
    vendor_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__654d9141c74cc6d28ebd4c2515eefd1c4fc3de4406423633557122ad3dc43b8a(
    *,
    body_mode: typing.Optional[EmailFilterBodyMode] = None,
    body_regex: typing.Optional[builtins.str] = None,
    from_email_mode: typing.Optional[EmailFilterFromEmailMode] = None,
    from_email_regex: typing.Optional[builtins.str] = None,
    subject_mode: typing.Optional[EmailFilterSubjectMode] = None,
    subject_regex: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bc167d621a966f732f7471b88c206d9ab14ed9f798e70639d761dd832dd3c29(
    *,
    action: typing.Optional[EmailParserAction] = None,
    match_predicate: typing.Optional[typing.Union[RootMatchPredicate, typing.Dict[builtins.str, typing.Any]]] = None,
    value_extractors: typing.Optional[typing.Sequence[typing.Union[ValueExtractor, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7a39e81c1da7d6ea61f0e86deb98ca91c03d49016446a7d12aa2a7468339ae0(
    *,
    matcher: typing.Optional[builtins.str] = None,
    part: typing.Optional[MatchPredicatePart] = None,
    type: typing.Optional[MatchPredicateType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25da52e7580f2f5fc0aed95511d9723338d701051fce23bc64e1b84bb12607ec(
    *,
    children: typing.Optional[typing.Sequence[typing.Union[MatchPredicate, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[RootMatchPredicateType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dfe332b3be3c39f29dd06554c5fa096c305cbc1ed5a3d020e5dc4dc928ef22a(
    *,
    ends_before: typing.Optional[builtins.str] = None,
    part: typing.Optional[ValueExtractorPart] = None,
    regex: typing.Optional[builtins.str] = None,
    starts_after: typing.Optional[builtins.str] = None,
    type: typing.Optional[ValueExtractorType] = None,
    value_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

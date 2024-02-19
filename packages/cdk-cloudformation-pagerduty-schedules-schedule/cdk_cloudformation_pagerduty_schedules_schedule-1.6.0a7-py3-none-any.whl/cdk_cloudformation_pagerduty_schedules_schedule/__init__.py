'''
# pagerduty-schedules-schedule

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `PagerDuty::Schedules::Schedule` v1.6.0.

## Description

Manage a on-call schedule in PagerDuty

## References

* [Documentation](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers)
* [Source](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name PagerDuty::Schedules::Schedule \
  --publisher-id c830e97710da0c9954d80ba8df021e5439e7134b \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/c830e97710da0c9954d80ba8df021e5439e7134b/PagerDuty-Schedules-Schedule \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `PagerDuty::Schedules::Schedule`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fpagerduty-schedules-schedule+v1.6.0).
* Issues related to `PagerDuty::Schedules::Schedule` should be reported to the [publisher](https://github.com/aws-ia/cloudformation-pagerduty-resource-providers).

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


class CfnSchedule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/pagerduty-schedules-schedule.CfnSchedule",
):
    '''A CloudFormation ``PagerDuty::Schedules::Schedule``.

    :cloudformationResource: PagerDuty::Schedules::Schedule
    :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
    '''

    def __init__(
        self_,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        time_zone: builtins.str,
        description: typing.Optional[builtins.str] = None,
        final_schedule: typing.Optional[typing.Union["SubSchedule", typing.Dict[builtins.str, typing.Any]]] = None,
        html_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        overrides_subschedule: typing.Optional[typing.Union["SubSchedule", typing.Dict[builtins.str, typing.Any]]] = None,
        schedule_layers: typing.Optional[typing.Sequence[typing.Union["ScheduleLayer", typing.Dict[builtins.str, typing.Any]]]] = None,
        self: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
        teams: typing.Optional[typing.Sequence[typing.Union["Team", typing.Dict[builtins.str, typing.Any]]]] = None,
        users: typing.Optional[typing.Sequence[typing.Union["User", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``PagerDuty::Schedules::Schedule``.

        :param scope: - scope in which this resource is defined.
        :param id_: - scoped id of the resource.
        :param time_zone: The time zone of the schedule.
        :param description: The description of the schedule.
        :param final_schedule: 
        :param html_url: 
        :param id: 
        :param name: The name of the schedule.
        :param overrides_subschedule: 
        :param schedule_layers: A list of schedule layers.
        :param self: 
        :param summary: 
        :param teams: An array of all of the teams on the schedule.
        :param users: An array of all of the users on the schedule.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9fbe972890587dc3ae9b58557591f436d047fa6a4fd85d4d0aecf9fd8224bc7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        props = CfnScheduleProps(
            time_zone=time_zone,
            description=description,
            final_schedule=final_schedule,
            html_url=html_url,
            id=id,
            name=name,
            overrides_subschedule=overrides_subschedule,
            schedule_layers=schedule_layers,
            self=self,
            summary=summary,
            teams=teams,
            users=users,
        )

        jsii.create(self_.__class__, self_, [scope, id_, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''Attribute ``PagerDuty::Schedules::Schedule.Type``.

        :link: https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnScheduleProps":
        '''Resource props.'''
        return typing.cast("CfnScheduleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-schedules-schedule.CfnScheduleProps",
    jsii_struct_bases=[],
    name_mapping={
        "time_zone": "timeZone",
        "description": "description",
        "final_schedule": "finalSchedule",
        "html_url": "htmlUrl",
        "id": "id",
        "name": "name",
        "overrides_subschedule": "overridesSubschedule",
        "schedule_layers": "scheduleLayers",
        "self": "self",
        "summary": "summary",
        "teams": "teams",
        "users": "users",
    },
)
class CfnScheduleProps:
    def __init__(
        self_,
        *,
        time_zone: builtins.str,
        description: typing.Optional[builtins.str] = None,
        final_schedule: typing.Optional[typing.Union["SubSchedule", typing.Dict[builtins.str, typing.Any]]] = None,
        html_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        overrides_subschedule: typing.Optional[typing.Union["SubSchedule", typing.Dict[builtins.str, typing.Any]]] = None,
        schedule_layers: typing.Optional[typing.Sequence[typing.Union["ScheduleLayer", typing.Dict[builtins.str, typing.Any]]]] = None,
        self: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
        teams: typing.Optional[typing.Sequence[typing.Union["Team", typing.Dict[builtins.str, typing.Any]]]] = None,
        users: typing.Optional[typing.Sequence[typing.Union["User", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Manage a on-call schedule in PagerDuty.

        :param time_zone: The time zone of the schedule.
        :param description: The description of the schedule.
        :param final_schedule: 
        :param html_url: 
        :param id: 
        :param name: The name of the schedule.
        :param overrides_subschedule: 
        :param schedule_layers: A list of schedule layers.
        :param self: 
        :param summary: 
        :param teams: An array of all of the teams on the schedule.
        :param users: An array of all of the users on the schedule.

        :schema: CfnScheduleProps
        '''
        if isinstance(final_schedule, dict):
            final_schedule = SubSchedule(**final_schedule)
        if isinstance(overrides_subschedule, dict):
            overrides_subschedule = SubSchedule(**overrides_subschedule)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2b65aa3b728efc90f161a0683b3bae44af0185d0b042bc0e95f3d633d4d26c8)
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument final_schedule", value=final_schedule, expected_type=type_hints["final_schedule"])
            check_type(argname="argument html_url", value=html_url, expected_type=type_hints["html_url"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument overrides_subschedule", value=overrides_subschedule, expected_type=type_hints["overrides_subschedule"])
            check_type(argname="argument schedule_layers", value=schedule_layers, expected_type=type_hints["schedule_layers"])
            check_type(argname="argument self", value=self, expected_type=type_hints["self"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument teams", value=teams, expected_type=type_hints["teams"])
            check_type(argname="argument users", value=users, expected_type=type_hints["users"])
        self_._values: typing.Dict[builtins.str, typing.Any] = {
            "time_zone": time_zone,
        }
        if description is not None:
            self_._values["description"] = description
        if final_schedule is not None:
            self_._values["final_schedule"] = final_schedule
        if html_url is not None:
            self_._values["html_url"] = html_url
        if id is not None:
            self_._values["id"] = id
        if name is not None:
            self_._values["name"] = name
        if overrides_subschedule is not None:
            self_._values["overrides_subschedule"] = overrides_subschedule
        if schedule_layers is not None:
            self_._values["schedule_layers"] = schedule_layers
        if self is not None:
            self_._values["self"] = self
        if summary is not None:
            self_._values["summary"] = summary
        if teams is not None:
            self_._values["teams"] = teams
        if users is not None:
            self_._values["users"] = users

    @builtins.property
    def time_zone(self) -> builtins.str:
        '''The time zone of the schedule.

        :schema: CfnScheduleProps#TimeZone
        '''
        result = self._values.get("time_zone")
        assert result is not None, "Required property 'time_zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the schedule.

        :schema: CfnScheduleProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def final_schedule(self) -> typing.Optional["SubSchedule"]:
        '''
        :schema: CfnScheduleProps#FinalSchedule
        '''
        result = self._values.get("final_schedule")
        return typing.cast(typing.Optional["SubSchedule"], result)

    @builtins.property
    def html_url(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnScheduleProps#HtmlUrl
        '''
        result = self._values.get("html_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnScheduleProps#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the schedule.

        :schema: CfnScheduleProps#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def overrides_subschedule(self) -> typing.Optional["SubSchedule"]:
        '''
        :schema: CfnScheduleProps#OverridesSubschedule
        '''
        result = self._values.get("overrides_subschedule")
        return typing.cast(typing.Optional["SubSchedule"], result)

    @builtins.property
    def schedule_layers(self) -> typing.Optional[typing.List["ScheduleLayer"]]:
        '''A list of schedule layers.

        :schema: CfnScheduleProps#ScheduleLayers
        '''
        result = self._values.get("schedule_layers")
        return typing.cast(typing.Optional[typing.List["ScheduleLayer"]], result)

    @builtins.property
    def self(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnScheduleProps#Self
        '''
        result = self._values.get("self")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnScheduleProps#Summary
        '''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def teams(self) -> typing.Optional[typing.List["Team"]]:
        '''An array of all of the teams on the schedule.

        :schema: CfnScheduleProps#Teams
        '''
        result = self._values.get("teams")
        return typing.cast(typing.Optional[typing.List["Team"]], result)

    @builtins.property
    def users(self) -> typing.Optional[typing.List["User"]]:
        '''An array of all of the users on the schedule.

        :schema: CfnScheduleProps#Users
        '''
        result = self._values.get("users")
        return typing.cast(typing.Optional[typing.List["User"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScheduleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-schedules-schedule.RenderedScheduleEntries",
    jsii_struct_bases=[],
    name_mapping={"end": "end", "start": "start", "user": "user"},
)
class RenderedScheduleEntries:
    def __init__(
        self,
        *,
        end: datetime.datetime,
        start: datetime.datetime,
        user: typing.Optional[typing.Union["User", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param end: The end time of this entry. If null, the entry does not end.
        :param start: The start time of this entry.
        :param user: 

        :schema: RenderedScheduleEntries
        '''
        if isinstance(user, dict):
            user = User(**user)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0701b55cf8e72e606fee33bf0b308c0e17f9e8ddda121148c425af96f6cc1ab)
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "end": end,
            "start": start,
        }
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def end(self) -> datetime.datetime:
        '''The end time of this entry.

        If null, the entry does not end.

        :schema: RenderedScheduleEntries#End
        '''
        result = self._values.get("end")
        assert result is not None, "Required property 'end' is missing"
        return typing.cast(datetime.datetime, result)

    @builtins.property
    def start(self) -> datetime.datetime:
        '''The start time of this entry.

        :schema: RenderedScheduleEntries#Start
        '''
        result = self._values.get("start")
        assert result is not None, "Required property 'start' is missing"
        return typing.cast(datetime.datetime, result)

    @builtins.property
    def user(self) -> typing.Optional["User"]:
        '''
        :schema: RenderedScheduleEntries#User
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional["User"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RenderedScheduleEntries(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-schedules-schedule.Restriction",
    jsii_struct_bases=[],
    name_mapping={
        "duration_seconds": "durationSeconds",
        "start_time_of_day": "startTimeOfDay",
        "type": "type",
        "start_day_of_week": "startDayOfWeek",
    },
)
class Restriction:
    def __init__(
        self,
        *,
        duration_seconds: jsii.Number,
        start_time_of_day: builtins.str,
        type: "RestrictionType",
        start_day_of_week: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param duration_seconds: The duration of the restriction in seconds.
        :param start_time_of_day: The start time in HH:mm:ss format.
        :param type: Specify the types of restriction.
        :param start_day_of_week: Only required for use with a weekly_restriction restriction type. The first day of the weekly rotation schedule as ISO 8601 day (1 is Monday, etc.)

        :schema: Restriction
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c2ac24754743a5e54685ddfaff0f6a220a4041104b350558e60e8284ab87ae6)
            check_type(argname="argument duration_seconds", value=duration_seconds, expected_type=type_hints["duration_seconds"])
            check_type(argname="argument start_time_of_day", value=start_time_of_day, expected_type=type_hints["start_time_of_day"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument start_day_of_week", value=start_day_of_week, expected_type=type_hints["start_day_of_week"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "duration_seconds": duration_seconds,
            "start_time_of_day": start_time_of_day,
            "type": type,
        }
        if start_day_of_week is not None:
            self._values["start_day_of_week"] = start_day_of_week

    @builtins.property
    def duration_seconds(self) -> jsii.Number:
        '''The duration of the restriction in seconds.

        :schema: Restriction#DurationSeconds
        '''
        result = self._values.get("duration_seconds")
        assert result is not None, "Required property 'duration_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def start_time_of_day(self) -> builtins.str:
        '''The start time in HH:mm:ss format.

        :schema: Restriction#StartTimeOfDay
        '''
        result = self._values.get("start_time_of_day")
        assert result is not None, "Required property 'start_time_of_day' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> "RestrictionType":
        '''Specify the types of restriction.

        :schema: Restriction#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("RestrictionType", result)

    @builtins.property
    def start_day_of_week(self) -> typing.Optional[jsii.Number]:
        '''Only required for use with a weekly_restriction restriction type.

        The first day of the weekly rotation schedule as ISO 8601 day (1 is Monday, etc.)

        :schema: Restriction#StartDayOfWeek
        '''
        result = self._values.get("start_day_of_week")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Restriction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-schedules-schedule.RestrictionType"
)
class RestrictionType(enum.Enum):
    '''Specify the types of restriction.

    :schema: RestrictionType
    '''

    DAILY_UNDERSCORE_RESTRICTION = "DAILY_UNDERSCORE_RESTRICTION"
    '''daily_restriction.'''
    WEEKLY_UNDERSCORE_RESTRICTION = "WEEKLY_UNDERSCORE_RESTRICTION"
    '''weekly_restriction.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-schedules-schedule.ScheduleLayer",
    jsii_struct_bases=[],
    name_mapping={
        "rotation_turn_length_seconds": "rotationTurnLengthSeconds",
        "rotation_virtual_start": "rotationVirtualStart",
        "start": "start",
        "users": "users",
        "end": "end",
        "id": "id",
        "name": "name",
        "restrictions": "restrictions",
    },
)
class ScheduleLayer:
    def __init__(
        self,
        *,
        rotation_turn_length_seconds: jsii.Number,
        rotation_virtual_start: datetime.datetime,
        start: datetime.datetime,
        users: typing.Sequence[typing.Union["UserWrapper", typing.Dict[builtins.str, typing.Any]]],
        end: typing.Optional[datetime.datetime] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        restrictions: typing.Optional[typing.Sequence[typing.Union[Restriction, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param rotation_turn_length_seconds: The duration of each on-call shift in seconds.
        :param rotation_virtual_start: The effective start time of the layer. This can be before the start time of the schedule.
        :param start: The start time of this layer.
        :param users: The ordered list of users on this layer. The position of the user on the list determines their order in the layer.
        :param end: The end time of this layer. If null, the layer does not end.
        :param id: 
        :param name: The name of the schedule layer.
        :param restrictions: An array of restrictions for the layer. A restriction is a limit on which period of the day or week the schedule layer can accept assignments.

        :schema: ScheduleLayer
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdb579219b59f24dbe97333402380a98778ce90c92a3865c1eeafa5f6c0a1716)
            check_type(argname="argument rotation_turn_length_seconds", value=rotation_turn_length_seconds, expected_type=type_hints["rotation_turn_length_seconds"])
            check_type(argname="argument rotation_virtual_start", value=rotation_virtual_start, expected_type=type_hints["rotation_virtual_start"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            check_type(argname="argument users", value=users, expected_type=type_hints["users"])
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument restrictions", value=restrictions, expected_type=type_hints["restrictions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rotation_turn_length_seconds": rotation_turn_length_seconds,
            "rotation_virtual_start": rotation_virtual_start,
            "start": start,
            "users": users,
        }
        if end is not None:
            self._values["end"] = end
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if restrictions is not None:
            self._values["restrictions"] = restrictions

    @builtins.property
    def rotation_turn_length_seconds(self) -> jsii.Number:
        '''The duration of each on-call shift in seconds.

        :schema: ScheduleLayer#RotationTurnLengthSeconds
        '''
        result = self._values.get("rotation_turn_length_seconds")
        assert result is not None, "Required property 'rotation_turn_length_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def rotation_virtual_start(self) -> datetime.datetime:
        '''The effective start time of the layer.

        This can be before the start time of the schedule.

        :schema: ScheduleLayer#RotationVirtualStart
        '''
        result = self._values.get("rotation_virtual_start")
        assert result is not None, "Required property 'rotation_virtual_start' is missing"
        return typing.cast(datetime.datetime, result)

    @builtins.property
    def start(self) -> datetime.datetime:
        '''The start time of this layer.

        :schema: ScheduleLayer#Start
        '''
        result = self._values.get("start")
        assert result is not None, "Required property 'start' is missing"
        return typing.cast(datetime.datetime, result)

    @builtins.property
    def users(self) -> typing.List["UserWrapper"]:
        '''The ordered list of users on this layer.

        The position of the user on the list determines their order in the layer.

        :schema: ScheduleLayer#Users
        '''
        result = self._values.get("users")
        assert result is not None, "Required property 'users' is missing"
        return typing.cast(typing.List["UserWrapper"], result)

    @builtins.property
    def end(self) -> typing.Optional[datetime.datetime]:
        '''The end time of this layer.

        If null, the layer does not end.

        :schema: ScheduleLayer#End
        '''
        result = self._values.get("end")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScheduleLayer#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the schedule layer.

        :schema: ScheduleLayer#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restrictions(self) -> typing.Optional[typing.List[Restriction]]:
        '''An array of restrictions for the layer.

        A restriction is a limit on which period of the day or week the schedule layer can accept assignments.

        :schema: ScheduleLayer#Restrictions
        '''
        result = self._values.get("restrictions")
        return typing.cast(typing.Optional[typing.List[Restriction]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScheduleLayer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-schedules-schedule.SubSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "rendered_coverage_percentage": "renderedCoveragePercentage",
        "rendered_schedule_entries": "renderedScheduleEntries",
    },
)
class SubSchedule:
    def __init__(
        self,
        *,
        name: "SubScheduleName",
        rendered_coverage_percentage: typing.Optional[jsii.Number] = None,
        rendered_schedule_entries: typing.Optional[typing.Sequence[typing.Union[RenderedScheduleEntries, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param name: The name of the subschedule.
        :param rendered_coverage_percentage: 
        :param rendered_schedule_entries: This is a list of entries on the computed layer for the current time range. Since or until must be set in order for this field to be populated.

        :schema: SubSchedule
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68de761160fb28c2375cc8d7e0612d9cead5231b69111a198dcb511169f1047f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rendered_coverage_percentage", value=rendered_coverage_percentage, expected_type=type_hints["rendered_coverage_percentage"])
            check_type(argname="argument rendered_schedule_entries", value=rendered_schedule_entries, expected_type=type_hints["rendered_schedule_entries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if rendered_coverage_percentage is not None:
            self._values["rendered_coverage_percentage"] = rendered_coverage_percentage
        if rendered_schedule_entries is not None:
            self._values["rendered_schedule_entries"] = rendered_schedule_entries

    @builtins.property
    def name(self) -> "SubScheduleName":
        '''The name of the subschedule.

        :schema: SubSchedule#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast("SubScheduleName", result)

    @builtins.property
    def rendered_coverage_percentage(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: SubSchedule#RenderedCoveragePercentage
        '''
        result = self._values.get("rendered_coverage_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rendered_schedule_entries(
        self,
    ) -> typing.Optional[typing.List[RenderedScheduleEntries]]:
        '''This is a list of entries on the computed layer for the current time range.

        Since or until must be set in order for this field to be populated.

        :schema: SubSchedule#RenderedScheduleEntries
        '''
        result = self._values.get("rendered_schedule_entries")
        return typing.cast(typing.Optional[typing.List[RenderedScheduleEntries]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/pagerduty-schedules-schedule.SubScheduleName"
)
class SubScheduleName(enum.Enum):
    '''The name of the subschedule.

    :schema: SubScheduleName
    '''

    FINAL_SCHEDULED = "FINAL_SCHEDULED"
    '''Final Scheduled.'''
    OVERRIDES = "OVERRIDES"
    '''Overrides.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-schedules-schedule.Team",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "type": "type",
        "html_url": "htmlUrl",
        "self": "self",
        "summary": "summary",
    },
)
class Team:
    def __init__(
        self_,
        *,
        id: builtins.str,
        type: "TeamType",
        html_url: typing.Optional[builtins.str] = None,
        self: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: 
        :param type: A string that determines the schema of the object. This must be the standard name for the entity, suffixed by _reference if the object is a reference./, =, +, and -.
        :param html_url: 
        :param self: 
        :param summary: 

        :schema: Team
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b94d1f3c21be319e2ae58c0ce18161e5b0091c5c5e916ed888f159757ceb3db)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument html_url", value=html_url, expected_type=type_hints["html_url"])
            check_type(argname="argument self", value=self, expected_type=type_hints["self"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
        self_._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "type": type,
        }
        if html_url is not None:
            self_._values["html_url"] = html_url
        if self is not None:
            self_._values["self"] = self
        if summary is not None:
            self_._values["summary"] = summary

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

    @builtins.property
    def html_url(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Team#HtmlUrl
        '''
        result = self._values.get("html_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def self(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Team#Self
        '''
        result = self._values.get("self")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Team#Summary
        '''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Team(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@cdk-cloudformation/pagerduty-schedules-schedule.TeamType")
class TeamType(enum.Enum):
    '''A string that determines the schema of the object.

    This must be the standard name for the entity, suffixed by _reference if the object is a reference./, =, +, and -.

    :schema: TeamType
    '''

    TEAM_UNDERSCORE_REFERENCE = "TEAM_UNDERSCORE_REFERENCE"
    '''team_reference.'''
    TEAM = "TEAM"
    '''team.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-schedules-schedule.User",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "type": "type",
        "html_url": "htmlUrl",
        "self": "self",
        "summary": "summary",
    },
)
class User:
    def __init__(
        self_,
        *,
        id: builtins.str,
        type: "UserType",
        html_url: typing.Optional[builtins.str] = None,
        self: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: 
        :param type: A string that determines the schema of the object. This must be the standard name for the entity, suffixed by _reference if the object is a reference./, =, +, and -.
        :param html_url: 
        :param self: 
        :param summary: 

        :schema: User
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f6d366f8a9ff773898423c1e52a1a4a0489304eab953c214b907674831a9b0a)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument html_url", value=html_url, expected_type=type_hints["html_url"])
            check_type(argname="argument self", value=self, expected_type=type_hints["self"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
        self_._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "type": type,
        }
        if html_url is not None:
            self_._values["html_url"] = html_url
        if self is not None:
            self_._values["self"] = self
        if summary is not None:
            self_._values["summary"] = summary

    @builtins.property
    def id(self) -> builtins.str:
        '''
        :schema: User#Id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> "UserType":
        '''A string that determines the schema of the object.

        This must be the standard name for the entity, suffixed by _reference if the object is a reference./, =, +, and -.

        :schema: User#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("UserType", result)

    @builtins.property
    def html_url(self) -> typing.Optional[builtins.str]:
        '''
        :schema: User#HtmlUrl
        '''
        result = self._values.get("html_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def self(self) -> typing.Optional[builtins.str]:
        '''
        :schema: User#Self
        '''
        result = self._values.get("self")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''
        :schema: User#Summary
        '''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "User(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@cdk-cloudformation/pagerduty-schedules-schedule.UserType")
class UserType(enum.Enum):
    '''A string that determines the schema of the object.

    This must be the standard name for the entity, suffixed by _reference if the object is a reference./, =, +, and -.

    :schema: UserType
    '''

    USER_UNDERSCORE_REFERENCE = "USER_UNDERSCORE_REFERENCE"
    '''user_reference.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/pagerduty-schedules-schedule.UserWrapper",
    jsii_struct_bases=[],
    name_mapping={"user": "user"},
)
class UserWrapper:
    def __init__(
        self,
        *,
        user: typing.Union[User, typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param user: 

        :schema: UserWrapper
        '''
        if isinstance(user, dict):
            user = User(**user)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dca76cc62d54e70d826a96579fd7df8142e836ae3923bb23fc93bc56f232c09b)
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user": user,
        }

    @builtins.property
    def user(self) -> User:
        '''
        :schema: UserWrapper#User
        '''
        result = self._values.get("user")
        assert result is not None, "Required property 'user' is missing"
        return typing.cast(User, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserWrapper(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnSchedule",
    "CfnScheduleProps",
    "RenderedScheduleEntries",
    "Restriction",
    "RestrictionType",
    "ScheduleLayer",
    "SubSchedule",
    "SubScheduleName",
    "Team",
    "TeamType",
    "User",
    "UserType",
    "UserWrapper",
]

publication.publish()

def _typecheckingstub__c9fbe972890587dc3ae9b58557591f436d047fa6a4fd85d4d0aecf9fd8224bc7(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    time_zone: builtins.str,
    description: typing.Optional[builtins.str] = None,
    final_schedule: typing.Optional[typing.Union[SubSchedule, typing.Dict[builtins.str, typing.Any]]] = None,
    html_url: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    overrides_subschedule: typing.Optional[typing.Union[SubSchedule, typing.Dict[builtins.str, typing.Any]]] = None,
    schedule_layers: typing.Optional[typing.Sequence[typing.Union[ScheduleLayer, typing.Dict[builtins.str, typing.Any]]]] = None,
    self: typing.Optional[builtins.str] = None,
    summary: typing.Optional[builtins.str] = None,
    teams: typing.Optional[typing.Sequence[typing.Union[Team, typing.Dict[builtins.str, typing.Any]]]] = None,
    users: typing.Optional[typing.Sequence[typing.Union[User, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2b65aa3b728efc90f161a0683b3bae44af0185d0b042bc0e95f3d633d4d26c8(
    *,
    time_zone: builtins.str,
    description: typing.Optional[builtins.str] = None,
    final_schedule: typing.Optional[typing.Union[SubSchedule, typing.Dict[builtins.str, typing.Any]]] = None,
    html_url: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    overrides_subschedule: typing.Optional[typing.Union[SubSchedule, typing.Dict[builtins.str, typing.Any]]] = None,
    schedule_layers: typing.Optional[typing.Sequence[typing.Union[ScheduleLayer, typing.Dict[builtins.str, typing.Any]]]] = None,
    self: typing.Optional[builtins.str] = None,
    summary: typing.Optional[builtins.str] = None,
    teams: typing.Optional[typing.Sequence[typing.Union[Team, typing.Dict[builtins.str, typing.Any]]]] = None,
    users: typing.Optional[typing.Sequence[typing.Union[User, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0701b55cf8e72e606fee33bf0b308c0e17f9e8ddda121148c425af96f6cc1ab(
    *,
    end: datetime.datetime,
    start: datetime.datetime,
    user: typing.Optional[typing.Union[User, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c2ac24754743a5e54685ddfaff0f6a220a4041104b350558e60e8284ab87ae6(
    *,
    duration_seconds: jsii.Number,
    start_time_of_day: builtins.str,
    type: RestrictionType,
    start_day_of_week: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdb579219b59f24dbe97333402380a98778ce90c92a3865c1eeafa5f6c0a1716(
    *,
    rotation_turn_length_seconds: jsii.Number,
    rotation_virtual_start: datetime.datetime,
    start: datetime.datetime,
    users: typing.Sequence[typing.Union[UserWrapper, typing.Dict[builtins.str, typing.Any]]],
    end: typing.Optional[datetime.datetime] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    restrictions: typing.Optional[typing.Sequence[typing.Union[Restriction, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68de761160fb28c2375cc8d7e0612d9cead5231b69111a198dcb511169f1047f(
    *,
    name: SubScheduleName,
    rendered_coverage_percentage: typing.Optional[jsii.Number] = None,
    rendered_schedule_entries: typing.Optional[typing.Sequence[typing.Union[RenderedScheduleEntries, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b94d1f3c21be319e2ae58c0ce18161e5b0091c5c5e916ed888f159757ceb3db(
    *,
    id: builtins.str,
    type: TeamType,
    html_url: typing.Optional[builtins.str] = None,
    self: typing.Optional[builtins.str] = None,
    summary: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f6d366f8a9ff773898423c1e52a1a4a0489304eab953c214b907674831a9b0a(
    *,
    id: builtins.str,
    type: UserType,
    html_url: typing.Optional[builtins.str] = None,
    self: typing.Optional[builtins.str] = None,
    summary: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dca76cc62d54e70d826a96579fd7df8142e836ae3923bb23fc93bc56f232c09b(
    *,
    user: typing.Union[User, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

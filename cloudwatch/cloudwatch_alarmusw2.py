from aws_cdk import (
    Duration,
    Stack,
    RemovalPolicy,
    aws_cloudwatch as _cw,
    aws_cloudwatch_actions as _actions,
    aws_iam as _iam,
    aws_lambda as _lambda,
    aws_logs as _logs,
    aws_sns as _sns,
    aws_sns_subscriptions as _subs,
)

from constructs import Construct

class CloudwatchAlarmUsw2(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

    ### SNS TOPIC ###

        topic = _sns.Topic(
            self, 'topic',
            topic_name = 'ErrorAlarmUSW2',
            display_name = 'ErrorAlarmUSW2'
        )

        subscription = _subs.EmailSubscription('hello@lukach.io')

        topic.add_subscription(subscription)

    ### ERRORS METRIC ###

        errors = _cw.MathExpression(
            expression = 'SELECT SUM(Errors) FROM SCHEMA("AWS/Lambda", FunctionName) GROUP BY FunctionName ORDER BY SUM() DESC'
        )

    ### ERRORS ALARM ###

        alarm = _cw.Alarm(
            self, 'alarm',
            alarm_name = 'ErrorAlarmUSW2',
            alarm_description = 'USW2 Alarm for Lambda Errors',
            metric = errors,
            threshold = 1,
            evaluation_periods = 1,
            datapoints_to_alarm = 1,
            comparison_operator = _cw.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            treat_missing_data = _cw.TreatMissingData.NOT_BREACHING
        )

        alarm.add_alarm_action(_actions.SnsAction(topic))

    ### ERROR TEST ###

        role = _iam.Role(
            self, 'role',
            assumed_by = _iam.ServicePrincipal(
                'lambda.amazonaws.com'
            )
        )

        role.add_managed_policy(
            _iam.ManagedPolicy.from_aws_managed_policy_name(
                'service-role/AWSLambdaBasicExecutionRole'
            )
        )

        test = _lambda.Function(
            self, 'test',
            function_name = 'test',
            runtime = _lambda.Runtime.PYTHON_3_13,
            architecture = _lambda.Architecture.ARM_64,
            code = _lambda.Code.from_asset('test'),
            handler = 'test.handler',
            timeout = Duration.seconds(3),
            memory_size = 128,
            role = role
        )

        logs = _logs.LogGroup(
            self, 'logs',
            log_group_name = '/aws/lambda/'+test.function_name,
            retention = _logs.RetentionDays.ONE_WEEK,
            removal_policy = RemovalPolicy.DESTROY
        )

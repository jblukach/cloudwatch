#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cloudwatch.cloudwatch_alarmuse1 import CloudwatchAlarmUse1
from cloudwatch.cloudwatch_alarmuse2 import CloudwatchAlarmUse2
from cloudwatch.cloudwatch_alarmusw2 import CloudwatchAlarmUsw2
from cloudwatch.cloudwatch_stack import CloudwatchStack

app = cdk.App()

CloudwatchAlarmUse1(
    app, 'CloudwatchAlarmUse1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-east-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = 'lukach'
    )
)

CloudwatchAlarmUse2(
    app, 'CloudwatchAlarmUse2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-east-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = 'lukach'
    )
)

CloudwatchAlarmUsw2(
    app, 'CloudwatchAlarmUsw2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-west-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = 'lukach'
    )
)

CloudwatchStack(
    app, 'CloudwatchStack',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-east-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = 'lukach'
    )
)

cdk.Tags.of(app).add('Alias','cloudwatch')
cdk.Tags.of(app).add('GitHub','https://github.com/jblukach/cloudwatch')
cdk.Tags.of(app).add('Org','lukach.io')

app.synth()
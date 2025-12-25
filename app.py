#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cloudwatch.cloudwatch_stack import CloudwatchStack

app = cdk.App()

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
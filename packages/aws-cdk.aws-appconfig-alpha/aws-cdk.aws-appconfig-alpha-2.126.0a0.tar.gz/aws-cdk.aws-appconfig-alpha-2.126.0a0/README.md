# AWS AppConfig Construct Library

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be
> announced in the release notes. This means that while you may use them, you may need to update
> your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

Use AWS AppConfig, a capability of AWS Systems Manager, to create, manage, and quickly deploy application configurations. A configuration is a collection of settings that influence the behavior of your application. You can use AWS AppConfig with applications hosted on Amazon Elastic Compute Cloud (Amazon EC2) instances, AWS Lambda, containers, mobile applications, or IoT devices. To view examples of the types of configurations you can manage by using AWS AppConfig, see [Example configurations](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html#appconfig-creating-configuration-and-profile-examples).

## Application

In AWS AppConfig, an application is simply an organizational construct like a folder. This organizational construct has a
relationship with some unit of executable code. For example, you could create an application called MyMobileApp to organize and
manage configuration data for a mobile application installed by your users. Configurations and environments are associated with
the application.

The name and description of an application are optional.

Create a simple application:

```python
appconfig.Application(self, "MyApplication")
```

Create an application with a name and description:

```python
appconfig.Application(self, "MyApplication",
    application_name="App1",
    description="This is my application created through CDK."
)
```

## Deployment Strategy

A deployment strategy defines how a configuration will roll out. The roll out is defined by four parameters: deployment type,
step percentage, deployment time, and bake time.
See: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy.html

Deployment strategy with predefined values:

```python
appconfig.DeploymentStrategy(self, "MyDeploymentStrategy",
    rollout_strategy=appconfig.RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
)
```

Deployment strategy with custom values:

```python
appconfig.DeploymentStrategy(self, "MyDeploymentStrategy",
    rollout_strategy=appconfig.RolloutStrategy.linear(
        growth_factor=20,
        deployment_duration=Duration.minutes(30),
        final_bake_time=Duration.minutes(30)
    )
)
```

Importing a deployment strategy by ID:

```python
appconfig.DeploymentStrategy.from_deployment_strategy_id(self, "MyImportedDeploymentStrategy", appconfig.DeploymentStrategyId.from_string("abc123"))
```

Importing an AWS AppConfig predefined deployment strategy by ID:

```python
appconfig.DeploymentStrategy.from_deployment_strategy_id(self, "MyImportedPredefinedDeploymentStrategy", appconfig.DeploymentStrategyId.CANARY_10_PERCENT_20_MINUTES)
```

## Configuration

A configuration is a higher-level construct that can either be a `HostedConfiguration` (stored internally through AWS
AppConfig) or a `SourcedConfiguration` (stored in an Amazon S3 bucket, AWS Secrets Manager secrets, Systems Manager (SSM)
Parameter Store parameters, SSM documents, or AWS CodePipeline). This construct manages deployments on creation.

### HostedConfiguration

A hosted configuration represents configuration stored in the AWS AppConfig hosted configuration store. A hosted configuration
takes in the configuration content and associated AWS AppConfig application. On construction of a hosted configuration, the
configuration is deployed.

```python
# application: appconfig.Application


appconfig.HostedConfiguration(self, "MyHostedConfiguration",
    application=application,
    content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content.")
)
```

You can define hosted configuration content using any of the following ConfigurationContent methods:

* `fromFile` - Defines the hosted configuration content from a file (you can specify a relative path).
* `fromInlineText` - Defines the hosted configuration from inline text.
* `fromInlineJson` - Defines the hosted configuration from inline JSON.
* `fromInlineYaml` - Defines the hosted configuration from inline YAML.
* `fromInline` - Defines the hosted configuration from user-specified content types.

AWS AppConfig supports the following types of configuration profiles.

* **Feature flag**: Use a feature flag configuration to turn on new features that require a timely deployment, such as a product launch or announcement.
* **Freeform**: Use a freeform configuration to carefully introduce changes to your application.

A hosted configuration with type:

```python
# application: appconfig.Application


appconfig.HostedConfiguration(self, "MyHostedConfiguration",
    application=application,
    content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content."),
    type=appconfig.ConfigurationType.FEATURE_FLAGS
)
```

When you create a configuration and configuration profile, you can specify up to two validators. A validator ensures that your
configuration data is syntactically and semantically correct. You can create validators in either JSON Schema or as an AWS
Lambda function.
See [About validators](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html#appconfig-creating-configuration-and-profile-validators) for more information.

When you import a JSON Schema validator from a file, you can pass in a relative path.

A hosted configuration with validators:

```python
# application: appconfig.Application
# fn: lambda.Function


appconfig.HostedConfiguration(self, "MyHostedConfiguration",
    application=application,
    content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content."),
    validators=[
        appconfig.JsonSchemaValidator.from_file("schema.json"),
        appconfig.LambdaValidator.from_function(fn)
    ]
)
```

You can attach a deployment strategy (as described in the previous section) to your configuration to specify how you want your
configuration to roll out.

A hosted configuration with a deployment strategy:

```python
# application: appconfig.Application


appconfig.HostedConfiguration(self, "MyHostedConfiguration",
    application=application,
    content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content."),
    deployment_strategy=appconfig.DeploymentStrategy(self, "MyDeploymentStrategy",
        rollout_strategy=appconfig.RolloutStrategy.linear(
            growth_factor=15,
            deployment_duration=Duration.minutes(30),
            final_bake_time=Duration.minutes(15)
        )
    )
)
```

The `deployTo` parameter is used to specify which environments to deploy the configuration to. If this parameter is not
specified, there will not be a deployment.

A hosted configuration with `deployTo`:

```python
# application: appconfig.Application
# env: appconfig.Environment


appconfig.HostedConfiguration(self, "MyHostedConfiguration",
    application=application,
    content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content."),
    deploy_to=[env]
)
```

To deploy a configuration to an environment after initialization use the `deploy` method:

```python
# application: appconfig.Application
# env: appconfig.Environment


config = appconfig.HostedConfiguration(self, "MyHostedConfiguration",
    application=application,
    content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content.")
)

config.deploy(env)
```

### SourcedConfiguration

A sourced configuration represents configuration stored in an Amazon S3 bucket, AWS Secrets Manager secret, Systems Manager
(SSM) Parameter Store parameter, SSM document, or AWS CodePipeline. A sourced configuration takes in the location source
construct and optionally a version number to deploy. On construction of a sourced configuration, the configuration is deployed
only if a version number is specified.

### S3

Use an Amazon S3 bucket to store a configuration.

```python
# application: appconfig.Application


bucket = s3.Bucket(self, "MyBucket",
    versioned=True
)

appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_bucket(bucket, "path/to/file.json")
)
```

Use an encrypted bucket:

```python
# application: appconfig.Application


bucket = s3.Bucket(self, "MyBucket",
    versioned=True,
    encryption=s3.BucketEncryption.KMS
)

appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_bucket(bucket, "path/to/file.json")
)
```

### AWS Secrets Manager secret

Use a Secrets Manager secret to store a configuration.

```python
# application: appconfig.Application
# secret: secrets.Secret


appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_secret(secret)
)
```

### SSM Parameter Store parameter

Use an SSM parameter to store a configuration.

```python
# application: appconfig.Application
# parameter: ssm.StringParameter


appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_parameter(parameter),
    version_number="1"
)
```

### SSM document

Use an SSM document to store a configuration.

```python
# application: appconfig.Application
# document: ssm.CfnDocument


appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_cfn_document(document)
)
```

### AWS CodePipeline

Use an AWS CodePipeline pipeline to store a configuration.

```python
# application: appconfig.Application
# pipeline: codepipeline.Pipeline


appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_pipeline(pipeline)
)
```

Similar to a hosted configuration, a sourced configuration can optionally take in a type, validators, a `deployTo` parameter, and a deployment strategy.

A sourced configuration with type:

```python
# application: appconfig.Application
# bucket: s3.Bucket


appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_bucket(bucket, "path/to/file.json"),
    type=appconfig.ConfigurationType.FEATURE_FLAGS,
    name="MyConfig",
    description="This is my sourced configuration from CDK."
)
```

A sourced configuration with validators:

```python
# application: appconfig.Application
# bucket: s3.Bucket
# fn: lambda.Function


appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_bucket(bucket, "path/to/file.json"),
    validators=[
        appconfig.JsonSchemaValidator.from_file("schema.json"),
        appconfig.LambdaValidator.from_function(fn)
    ]
)
```

A sourced configuration with a deployment strategy:

```python
# application: appconfig.Application
# bucket: s3.Bucket


appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_bucket(bucket, "path/to/file.json"),
    deployment_strategy=appconfig.DeploymentStrategy(self, "MyDeploymentStrategy",
        rollout_strategy=appconfig.RolloutStrategy.linear(
            growth_factor=15,
            deployment_duration=Duration.minutes(30),
            final_bake_time=Duration.minutes(15)
        )
    )
)
```

The `deployTo` parameter is used to specify which environments to deploy the configuration to. If this parameter is not
specified, there will not be a deployment.

A sourced configuration with `deployTo`:

```python
# application: appconfig.Application
# bucket: s3.Bucket
# env: appconfig.Environment


appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_bucket(bucket, "path/to/file.json"),
    deploy_to=[env]
)
```

## Environment

For each AWS AppConfig application, you define one or more environments. An environment is a logical deployment group of AWS
AppConfig targets, such as applications in a Beta or Production environment. You can also define environments for application
subcomponents such as the Web, Mobile, and Back-end components for your application. You can configure Amazon CloudWatch alarms
for each environment. The system monitors alarms during a configuration deployment. If an alarm is triggered, the system rolls
back the configuration.

Basic environment with monitors:

```python
# application: appconfig.Application
# alarm: cloudwatch.Alarm
# composite_alarm: cloudwatch.CompositeAlarm


appconfig.Environment(self, "MyEnvironment",
    application=application,
    monitors=[
        appconfig.Monitor.from_cloud_watch_alarm(alarm),
        appconfig.Monitor.from_cloud_watch_alarm(composite_alarm)
    ]
)
```

Environment monitors also support L1 CfnEnvironment.MonitorsProperty constructs. However, this is not the recommended approach
for CloudWatch alarms because a role will not be auto-generated if not provided.

## Extension

An extension augments your ability to inject logic or behavior at different points during the AWS AppConfig workflow of
creating or deploying a configuration.
See: https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html

### AWS Lambda destination

Use an AWS Lambda as the event destination for an extension.

```python
# fn: lambda.Function


appconfig.Extension(self, "MyExtension",
    actions=[
        appconfig.Action(
            action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
            event_destination=appconfig.LambdaDestination(fn)
        )
    ]
)
```

Lambda extension with parameters:

```python
# fn: lambda.Function


appconfig.Extension(self, "MyExtension",
    actions=[
        appconfig.Action(
            action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
            event_destination=appconfig.LambdaDestination(fn)
        )
    ],
    parameters=[
        appconfig.Parameter.required("testParam", "true"),
        appconfig.Parameter.not_required("testNotRequiredParam")
    ]
)
```

### Amazon Simple Queue Service (SQS) destination

Use a queue as the event destination for an extension.

```python
# queue: sqs.Queue


appconfig.Extension(self, "MyExtension",
    actions=[
        appconfig.Action(
            action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
            event_destination=appconfig.SqsDestination(queue)
        )
    ]
)
```

### Amazon Simple Notification Service (SNS) destination

Use an SNS topic as the event destination for an extension.

```python
# topic: sns.Topic


appconfig.Extension(self, "MyExtension",
    actions=[
        appconfig.Action(
            action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
            event_destination=appconfig.SnsDestination(topic)
        )
    ]
)
```

### Amazon EventBridge destination

Use the default event bus as the event destination for an extension.

```python
bus = events.EventBus.from_event_bus_name(self, "MyEventBus", "default")

appconfig.Extension(self, "MyExtension",
    actions=[
        appconfig.Action(
            action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
            event_destination=appconfig.EventBridgeDestination(bus)
        )
    ]
)
```

You can also add extensions and their associations directly by calling `onDeploymentComplete()` or any other action point
method on the AWS AppConfig application, configuration, or environment resource. To add an association to an existing
extension, you can call `addExtension()` on the resource.

Adding an association to an AWS AppConfig application:

```python
# application: appconfig.Application
# extension: appconfig.Extension
# lambda_destination: appconfig.LambdaDestination


application.add_extension(extension)
application.on_deployment_complete(lambda_destination)
```

---
id: usage
title: Usage
---

## Usage

### One shot 
```shell
monitapi monitor {targets.yaml}
```

### Run with FastAPI
You need to put targets.yaml in the current directory.

```shell
monitapi serve
```

### Deploy to serverless
```shell
monitapi deploy {platform} --name {function-name} --file {targets.yaml} --options {deploy-option}
```

* platform
    - cloud_functions
    - aws_lambda
* function-name
    - Function name to deploy
* targets.yaml
    - Definition file as YAML
* deploy-option
    - Official deployment options

#### Example

* Cloud Functions
```shell
monitapi deploy cloud_functions --name monitapi --file targets.yaml --options '{"--region": "asia-northeast1"}'
```

* AWS Lambda
```shell
monitapi deploy aws_lambda --name monitapi --file targets.yaml --options '{"--role": "{ARN}"}'
```

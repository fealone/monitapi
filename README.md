# monitapi
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

## What is this
monitapi is something to monitor API(URL) by a serverless.  
It supports hosting with FastAPI, running with CLI, and deploying to serverless.

## Getting Started

### Installation
monitapi is made by Python, so can you install it via PyPI.

```shell
pip install monitapi
```

### Definition
The monitoring target and notification target can be defined using YAML.  
It's defined as one file.

#### Monitoring target
```yaml
monitor_targets:
    - {monitor-name}
      method: {http-method}
      url: {monitoring-url}
      headers:
          {header-name}: {header-value}
      status_code: {expected-status-code}
      timeout: {timeout}
```

* monitor-name
    - Monitor name
* http-method
    - HEAD, GET, POST, PUT, DELETE, OPTIONS, PATCH
* monitoring-url
    - URL to monitor
* header-name, header-value
    - HTTP headers
* expected-status-code
    - The status code you expect from the monitored target.
* timeout
    - Read timeout and connection timeout.

#### Notification target
```yaml
notification_targets
    - {notification-name}
      type: {notification-type}
      endpoint: {notification-endpoint}
      payload:
          {request-payload}
```

* notification-name
    - Notification name
* notification-type
    - slack
* notification-endpoint
    - The endpoint that sends the notification request.
* request-payload
    - The POST payload to send to the endpoint.
    - You can use {{url}}, {{status_code}}, {{expected status_code}} and {{message}} as variables.

#### Example
```yaml
monitor_targets:
    - github-monitapi
      method: "GET"
      url: https://github.com/fealone/monitapi
      status_code: 200
      timeout: 5

notification_targets:
    - notification-to-slack:
      type: slack
      endpoint: {Slack Incoming Webhooks endpoint}
      payload:
          blocks:
              -
                type: section
                text:
                    type: mrkdwn
                    text: "Target: {{url}}, Status: {{status_code}}, Expect: {{expected_status_code}}, Message: {{message}}"

```

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
* function-name
    - Function name to deploy
* targets.yaml
    - Definition file as YAML
* deploy-option
    - Official deployment options

#### Example
```shell
monitapi deploy cloud_functions --name monitapi --file targets.yaml --options '{"--region": "asia-northeast1"}'
```

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://lonesec.com"><img src="https://avatars1.githubusercontent.com/u/57695598?v=4" width="100px;" alt=""/><br /><sub><b>fealone</b></sub></a><br /><a href="https://github.com/fealone/monitapi/commits?author=fealone" title="Code">💻</a> <a href="#content-fealone" title="Content">🖋</a> <a href="#design-fealone" title="Design">🎨</a> <a href="#example-fealone" title="Examples">💡</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details

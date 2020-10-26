---
id: definition
title: Definition
---

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
      retry: {retry}
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
    - The status code you expect from the monitored target
* timeout
    - Read timeout and connection timeout
* retry
    - Number of retries

#### Notification target
```yaml
notification_targets:
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
    - The endpoint that sends the notification request
* request-payload
    - The POST payload to send to the endpoint
    - You can use {{url}}, {{status_code}}, {{expected status_code}} and {{message}} as variables

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

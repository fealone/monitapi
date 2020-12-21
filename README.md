# monitapi

<img src="https://raw.githubusercontent.com/fealone/monitapi/master/website/static/img/logo.png" width="600px">

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

---

## What is this
monitapi is something to monitor API(URL) by a serverless.  
It supports hosting with FastAPI, running with CLI, and deploying to serverless.

## Getting Started
Please refer to the documents created by Docusaurus.  
A rich README and website are in preparation.

https://fealone.github.io/monitapi

## Image of operating environment

### GCP

<img src="https://raw.githubusercontent.com/fealone/monitapi/master/website/static/img/gcp.rediagram.png" width="600px">

### AWS

<img src="https://raw.githubusercontent.com/fealone/monitapi/master/website/static/img/aws.rediagram.png" width="600px">

### Installation
monitapi is made by Python, so can you install it via PyPI.

```shell
pip install monitapi
```

### Example targets file
```yaml
monitor_targets:
    - github-monitapi
      method: "GET"
      url: https://github.com/fealone/monitapi
      status_code: 200
      timeout: 5
      retry: 1
      retry_wait: 5

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

### Usage

#### One shot 
```shell
monitapi monitor {targets.yaml}
```

#### Run with FastAPI
You need to put targets.yaml in the current directory.

```shell
monitapi serve
```

#### Deploy to serverless
```shell
monitapi deploy {platform} --name {function-name} --file {targets.yaml} --options {deploy-option}
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

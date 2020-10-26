(window.webpackJsonp=window.webpackJsonp||[]).push([[5],{62:function(e,t,n){"use strict";n.r(t),n.d(t,"frontMatter",(function(){return r})),n.d(t,"metadata",(function(){return c})),n.d(t,"rightToc",(function(){return l})),n.d(t,"default",(function(){return u}));var a=n(2),i=n(6),o=(n(0),n(77)),r={id:"definition",title:"Definition"},c={unversionedId:"definition",id:"definition",isDocsHomePage:!1,title:"Definition",description:"Definition",source:"@site/docs/definition.md",slug:"/definition",permalink:"/docs/definition",editUrl:"https://github.com/fealone/monitapi/edit/master/website/docs/definition.md",version:"current",sidebar:"someSidebar",previous:{title:"Usage",permalink:"/docs/usage"}},l=[{value:"Definition",id:"definition",children:[]}],b={rightToc:l};function u(e){var t=e.components,n=Object(i.a)(e,["components"]);return Object(o.b)("wrapper",Object(a.a)({},b,n,{components:t,mdxType:"MDXLayout"}),Object(o.b)("h3",{id:"definition"},"Definition"),Object(o.b)("p",null,"The monitoring target and notification target can be defined using YAML.",Object(o.b)("br",{parentName:"p"}),"\n","It's defined as one file."),Object(o.b)("h4",{id:"monitoring-target"},"Monitoring target"),Object(o.b)("pre",null,Object(o.b)("code",Object(a.a)({parentName:"pre"},{className:"language-yaml"}),"monitor_targets:\n    - {monitor-name}\n      method: {http-method}\n      url: {monitoring-url}\n      headers:\n          {header-name}: {header-value}\n      status_code: {expected-status-code}\n      timeout: {timeout}\n      retry: {retry}\n")),Object(o.b)("ul",null,Object(o.b)("li",{parentName:"ul"},"monitor-name",Object(o.b)("ul",{parentName:"li"},Object(o.b)("li",{parentName:"ul"},"Monitor name"))),Object(o.b)("li",{parentName:"ul"},"http-method",Object(o.b)("ul",{parentName:"li"},Object(o.b)("li",{parentName:"ul"},"HEAD, GET, POST, PUT, DELETE, OPTIONS, PATCH"))),Object(o.b)("li",{parentName:"ul"},"monitoring-url",Object(o.b)("ul",{parentName:"li"},Object(o.b)("li",{parentName:"ul"},"URL to monitor"))),Object(o.b)("li",{parentName:"ul"},"header-name, header-value",Object(o.b)("ul",{parentName:"li"},Object(o.b)("li",{parentName:"ul"},"HTTP headers"))),Object(o.b)("li",{parentName:"ul"},"expected-status-code",Object(o.b)("ul",{parentName:"li"},Object(o.b)("li",{parentName:"ul"},"The status code you expect from the monitored target"))),Object(o.b)("li",{parentName:"ul"},"timeout",Object(o.b)("ul",{parentName:"li"},Object(o.b)("li",{parentName:"ul"},"Read timeout and connection timeout"))),Object(o.b)("li",{parentName:"ul"},"retry",Object(o.b)("ul",{parentName:"li"},Object(o.b)("li",{parentName:"ul"},"Number of retries")))),Object(o.b)("h4",{id:"notification-target"},"Notification target"),Object(o.b)("pre",null,Object(o.b)("code",Object(a.a)({parentName:"pre"},{className:"language-yaml"}),"notification_targets:\n    - {notification-name}\n      type: {notification-type}\n      endpoint: {notification-endpoint}\n      payload:\n          {request-payload}\n")),Object(o.b)("ul",null,Object(o.b)("li",{parentName:"ul"},"notification-name",Object(o.b)("ul",{parentName:"li"},Object(o.b)("li",{parentName:"ul"},"Notification name"))),Object(o.b)("li",{parentName:"ul"},"notification-type",Object(o.b)("ul",{parentName:"li"},Object(o.b)("li",{parentName:"ul"},"slack"))),Object(o.b)("li",{parentName:"ul"},"notification-endpoint",Object(o.b)("ul",{parentName:"li"},Object(o.b)("li",{parentName:"ul"},"The endpoint that sends the notification request"))),Object(o.b)("li",{parentName:"ul"},"request-payload",Object(o.b)("ul",{parentName:"li"},Object(o.b)("li",{parentName:"ul"},"The POST payload to send to the endpoint"),Object(o.b)("li",{parentName:"ul"},"You can use {{url}}, {{status_code}}, {{expected status_code}} and {{message}} as variables")))),Object(o.b)("h4",{id:"example"},"Example"),Object(o.b)("pre",null,Object(o.b)("code",Object(a.a)({parentName:"pre"},{className:"language-yaml"}),'monitor_targets:\n    - github-monitapi\n      method: "GET"\n      url: https://github.com/fealone/monitapi\n      status_code: 200\n      timeout: 5\n\nnotification_targets:\n    - notification-to-slack:\n      type: slack\n      endpoint: {Slack Incoming Webhooks endpoint}\n      payload:\n          blocks:\n              -\n                type: section\n                text:\n                    type: mrkdwn\n                    text: "Target: {{url}}, Status: {{status_code}}, Expect: {{expected_status_code}}, Message: {{message}}"\n\n')))}u.isMDXComponent=!0}}]);
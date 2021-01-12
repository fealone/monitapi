(window.webpackJsonp=window.webpackJsonp||[]).push([[4],{61:function(e,t,a){"use strict";a.r(t),a.d(t,"frontMatter",(function(){return o})),a.d(t,"metadata",(function(){return s})),a.d(t,"rightToc",(function(){return r})),a.d(t,"default",(function(){return b}));var n=a(2),l=a(6),i=(a(0),a(76)),o={id:"usage",title:"Usage"},s={unversionedId:"usage",id:"usage",isDocsHomePage:!1,title:"Usage",description:"Usage",source:"@site/docs/usage.md",slug:"/usage",permalink:"/monitapi/docs/usage",editUrl:"https://github.com/fealone/monitapi/edit/master/website/docs/usage.md",version:"current",sidebar:"someSidebar",previous:{title:"Definition",permalink:"/monitapi/docs/definition"}},r=[{value:"Usage",id:"usage",children:[{value:"One shot",id:"one-shot",children:[]},{value:"Run with FastAPI",id:"run-with-fastapi",children:[]},{value:"Deploy to serverless",id:"deploy-to-serverless",children:[]}]}],c={rightToc:r};function b(e){var t=e.components,a=Object(l.a)(e,["components"]);return Object(i.b)("wrapper",Object(n.a)({},c,a,{components:t,mdxType:"MDXLayout"}),Object(i.b)("h2",{id:"usage"},"Usage"),Object(i.b)("h3",{id:"one-shot"},"One shot"),Object(i.b)("pre",null,Object(i.b)("code",Object(n.a)({parentName:"pre"},{className:"language-shell"}),"monitapi monitor {targets.yaml}\n")),Object(i.b)("h3",{id:"run-with-fastapi"},"Run with FastAPI"),Object(i.b)("p",null,"You need to put targets.yaml in the current directory."),Object(i.b)("pre",null,Object(i.b)("code",Object(n.a)({parentName:"pre"},{className:"language-shell"}),"monitapi serve\n")),Object(i.b)("h3",{id:"deploy-to-serverless"},"Deploy to serverless"),Object(i.b)("pre",null,Object(i.b)("code",Object(n.a)({parentName:"pre"},{className:"language-shell"}),"monitapi deploy {platform} --name {function-name} --file {targets.yaml} --options {deploy-option}\n")),Object(i.b)("ul",null,Object(i.b)("li",{parentName:"ul"},"platform",Object(i.b)("ul",{parentName:"li"},Object(i.b)("li",{parentName:"ul"},"cloud_functions"),Object(i.b)("li",{parentName:"ul"},"aws_lambda"))),Object(i.b)("li",{parentName:"ul"},"function-name",Object(i.b)("ul",{parentName:"li"},Object(i.b)("li",{parentName:"ul"},"Function name to deploy"))),Object(i.b)("li",{parentName:"ul"},"targets.yaml",Object(i.b)("ul",{parentName:"li"},Object(i.b)("li",{parentName:"ul"},"Definition file as YAML"))),Object(i.b)("li",{parentName:"ul"},"deploy-option",Object(i.b)("ul",{parentName:"li"},Object(i.b)("li",{parentName:"ul"},"Official deployment options")))),Object(i.b)("h4",{id:"example"},"Example"),Object(i.b)("ul",null,Object(i.b)("li",{parentName:"ul"},"Cloud Functions")),Object(i.b)("pre",null,Object(i.b)("code",Object(n.a)({parentName:"pre"},{className:"language-shell"}),'monitapi deploy cloud_functions --name monitapi --file targets.yaml --options \'{"--region": "asia-northeast1"}\'\n')),Object(i.b)("ul",null,Object(i.b)("li",{parentName:"ul"},"AWS Lambda")),Object(i.b)("pre",null,Object(i.b)("code",Object(n.a)({parentName:"pre"},{className:"language-shell"}),'monitapi deploy aws_lambda --name monitapi --file targets.yaml --options \'{"--role": "{ARN}"}\'\n')))}b.isMDXComponent=!0}}]);
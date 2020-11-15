import React from 'react';
import { PNG, Diagram, GeneralIcon } from 'rediagram';
import { AWS, InvizAWS, Lambda, APIGateway, SimpleNotificationService, CloudWatch} from '@rediagram/aws';

PNG(
  <Diagram title="monitapi with AWS">
    <InvizAWS>
      <AWS>
        <CloudWatch name="Event with Cron" upstream={["HTTPS"]}/>
        <SimpleNotificationService name="HTTPS" upstream={["monitapi Endpoint"]}/>
        <APIGateway name="monitapi Endpoint" upstream={["monitapi"]} />
        <Lambda name="monitapi" upstream={["Monitoring Target"]}/>
      </AWS>
      <GeneralIcon name="Monitoring Target" type="Traditional server" />
    </InvizAWS>
  </Diagram>,
);
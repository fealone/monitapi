import React from 'react';
import { PNG, Diagram, GeneralIcon } from 'rediagram';
import {GCP, InvizGCP, CloudScheduler, CloudFunctions} from '@rediagram/gcp'

PNG(
  <Diagram title="monitapi with GCP">
    <GCP>
      <InvizGCP>
        <CloudScheduler name="Scheduler" upstream={["monitapi"]}/>
        <CloudFunctions name="monitapi" upstream={["Monitoring Target"]}/>
      </InvizGCP>
      </GCP>
      <GeneralIcon name="Monitoring Target" type="Traditional server" />
  </Diagram>,
);
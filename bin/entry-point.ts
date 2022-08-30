#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { PipelineStack } from '../lib/pipeline-stack';
import { dev } from '../environment';

// CDK Application
const app = new cdk.App();

// Creating new pipeline
new PipelineStack(app, 'PipelineStack', {
  env: {                  // Current environment
    account:dev.account,  // environment
    region: dev.region    // region
  },
  appName: app.node.tryGetContext('app-name') // application name
});

app.synth(); // Synth application
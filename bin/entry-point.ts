#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { PipelineStack } from '../lib/pipeline-stack';
import { dev } from '../environment';

const app = new cdk.App();
new PipelineStack(app, 'PipelineStack', {
  env: {
    account:dev.account,
    region: dev.region
  }
});

app.synth();
import * as cdk from 'aws-cdk-lib';

import { AppStage } from './app-stage';
import { Construct } from 'constructs';

import { 
  CodePipeline, 
  CodePipelineSource, 
  ShellStep,
  ManualApprovalStep
} from 'aws-cdk-lib/pipelines'; 

export interface PipelineStackProps extends cdk.StackProps {
  env: cdk.Environment;
  appName: string;
}

export class PipelineStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props: PipelineStackProps) {
    super(scope, id, props);
  
  
    // Create new pipeline
    const pipeline = new CodePipeline(this, 'Pipeline', {
      pipelineName: 'MyPipeline',
      synth: new ShellStep('Synth',{
        input: CodePipelineSource.connection(
          'JohnCameron94/cdk-codepipeline',
          'master',
          {
            connectionArn: 'arn:aws:codestar-connections:ca-central-1:360070888501:connection/5199c46f-94d5-4428-b063-9513fed3c5e2'
          }
        ),
          commands: ['npm ci', 'npm run build', 'npx cdk synth']
      })
    });
    
    const testStage = pipeline.addStage(new AppStage(this, 'Testing', {
      env:props.env,
      appName:props.appName
    }));
    
    testStage.addPost(new ManualApprovalStep('approval'))
  }
}

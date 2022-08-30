import * as cdk from 'aws-cdk-lib';

import { DeployStage } from './deploy-stage';
import { Construct } from 'constructs';

import { 
  CodePipeline, 
  CodePipelineSource, 
  ShellStep 
} from 'aws-cdk-lib/pipelines'; 

export class PipelineStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
  
  
    // Create new pipeline
    const pipeline = new CodePipeline(this, 'Pipeline', {
      pipelineName: 'MyPipeline',
      synth: new ShellStep('Synth',{
        input: CodePipelineSource.connection(
          'JohnCameron94/cdk-codepipeline',
          'main',
          {
            connectionArn: 'arn:aws:codestar-connections:ca-central-1:360070888501:connection/5199c46f-94d5-4428-b063-9513fed3c5e2'
          }
        ),
          commands: ['npm ci', 'npm run build', 'npx cdk synth']
      })
    });
  }
}

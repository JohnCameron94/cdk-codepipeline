import * as cdk from 'aws-cdk-lib';
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
        input: CodePipelineSource.gitHub(
          'https://github.com/JohnCameron94/cdk-codepipeline.git','main'),
          commands: ['npm ci', 'npm run build', 'npx cdk synth']
      })
    });
  }
}

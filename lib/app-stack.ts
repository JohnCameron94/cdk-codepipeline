import * as cdk from 'aws-cdk-lib';
import { Function, Runtime, InlineCode } from 'aws-cdk-lib/aws-lambda';
import { Construct } from 'constructs';

export interface AppStackProps {
  env: cdk.Environment;
  appName: string;
  
}

export class AppStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props: AppStackProps){
      super(scope,id,props)
      
      const lambda = new Function(this, 'LambdaFunction', {
        functionName: `${props.appName}-lambda`,
        runtime: Runtime.NODEJS_16_X,
        handler: 'resp-lambda.handler',
        code: new InlineCode (
          'exports.handler = _ => "Hello from Lambda";'
        )
      });
      
    }
}
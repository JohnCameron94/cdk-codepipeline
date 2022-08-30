import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { AppStack } from './app-stack';

export interface AppStageProps extends cdk.StageProps{
    env: cdk.Environment;
    appName: string;
}

export class AppStage extends cdk.Stage {
    constructor(scope: Construct, id: string, props: AppStageProps){
       super(scope,id,props);
       
       new AppStack(this, 'ApplicationStack', {
           env: props.env,
           appName: this.node.tryGetContext('app-name')
       })
       
    }
}
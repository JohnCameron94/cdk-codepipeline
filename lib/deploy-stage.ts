import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { AppStack } from './app-stack';

export class DeployStage extends cdk.Stage {
    constructor(scope: Construct, id: string, props?: cdk.StageProps){
       super(scope,id,props);
       
       
       
    }
}
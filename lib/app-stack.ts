import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';

export interface AppStackProps {
    
}

export class AppStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props: AppStackProps){
      super(scope,id,props)
      
      
      
    }
}
from aws_cdk import (
    # Duration,
    Stack,
    aws_codepipeline_actions as cpactions,
    aws_codepipeline as codepipeline,
    aws_codebuild as code_build
)
from cdkpipeline.configurations import RawConfig,AppConfig,ResourceConfig

from constructs import Construct

class CdkPipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, raw_config: RawConfig, 
                app_config: AppConfig ,**kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self._app_config = app_config
        self._raw_config = raw_config
        
        
        source_output = codepipeline.Artifact()
         # Pipeline setup where app_config is used
        # ...
        source_action = cpactions.GitHubSourceAction(
            action_name='Source',
            owner=self._app_config.repo_name,
            branch=self._app_config.branch,
            repo=self._app_config.repo_url,
            oauth_token='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',
            output=source_output
        )
        # ...
        pipeline = codepipeline.Pipeline(
            self, 
            'pipeline',
            stages=[
                codepipeline.StageProps(stage_name="Source", actions=[source_action]),
                codepipeline.StageProps(
                    stage_name="Build",
                    actions=[
                        cpactions.CodeBuildAction(
                            action_name="Build",
                            project=codebuild.PipelineProject(self,"MyProject"),
                            input=source_output
                        )
                    ],
                ),
            ],
        )

        # DEVELOPMENT ENVIRONMENT
        dev_config = ResourceConfig.from_raw_config(self._raw_config.dev)
        dev_my_stage = MyStage(self, 'dev-my-stage', dev_config)
        dev_stage = pipeline.add_application_stage(dev_my_stage)

        # STAGING ENVIRONMENT
        staging_config = ResourceConfig.from_raw_config(self._raw_config.staging)
        staging_my_stage = MyStage(self, 'staging-my-stage', staging_config)
        staging_stage = pipeline.add_application_stage(staging_my_stage)

        # PRODUCTION ENVIRONMENT
        production_config = ResourceConfig.from_raw_config(self._raw_config.production)
        production_my_stage = MyStage(self, 'production-my-stage', production_config)
        production_stage = pipeline.add_application_stage(production_my_stage)
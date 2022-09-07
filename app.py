#!/usr/bin/env python3
import aws_cdk as cdk
import os
from pathlib import Path
from cdkpipeline.cdk_pipeline_stack import CdkPipelineStack
from cdkpipeline.configurations import (
    RawConfig,
    AppConfig
)


# Read config file
config_file = Path('./config/config.json')
# Load Raw Configurations
raw_config = RawConfig(config_file)
# Application Config
app_config = AppConfig.from_raw_config(raw_config.application)
# Cdk App
app = cdk.App()
# PipelineStack
CdkCodepipelineStack(
    app, 
    f"{app_config.app_name}-{app_config.branch}",
    env=app_config.build_environment,
    raw_config=raw_config,
    app_config=app_config
)

app.synth()

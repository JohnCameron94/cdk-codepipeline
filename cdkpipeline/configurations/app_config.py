from dataclasses import dataclass
from aws_cdk import ( Environment )
from typing import (
    Any,
    Dict,
    Type,
    TypeVar
)

AppConfigClass = TypeVar('AppConfigClass', bound='AppConfig')

@dataclass
class AppConfig () :
    app_name: str
    repo_name: str
    repo_url: str
    branch: str
    build_environment: Environment
    
    
    @classmethod
    def from_raw_config(cls: Type[AppConfigClass], raw_config: Dict[str, Any]) -> AppConfigClass:
        """
        Constructor from raw configuration.
        It will perform some conversion to CDK specific types and classes.
        """
        raw_config = cls.convert_to_cdk_constructs(raw_config)

        return cls(**raw_config)
        
     @staticmethod
    def convert_to_cdk_constructs(raw_config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Converts raw config to CDK specific constructs when required.
        This method can be used when overwriting the classmethod construct of
        an inherited class in order to preserve the conversions of the parent
        class.
        """
        raw_build_environment = raw_config.pop('build_environment')

        build_environment = Environment(**raw_build_environment)

        raw_config.update(build_environment=build_environment)

        return raw_config

        
            
    
            
            
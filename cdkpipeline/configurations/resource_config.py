from dataclasses import dataclass
from typing import Any, Dict, Type, TypeVar
from aws_cdk.core import Environment, RemovalPolicy

# https://mypy.readthedocs.io/en/stable/kinds_of_types.html#the-type-of-class-objects
# https://github.com/python/typing/issues/58
# Needed to return correct child class types in classmethod constructor
ResourceConfigClass = TypeVar('ResourceConfigClass', bound='ResourceConfig')


@dataclass
class ResourceConfig():
    """ Configuration of a single environment."""

    name: str
    environment: Environment
    tags: Dict[str, str]
    deletion_protection: bool
    removal_policy: RemovalPolicy
    minimum_auto_scaling_group: int
    maximum_auto_scaling_group: int

    @classmethod
    def from_raw_config(cls: Type[ResourceConfigClass], raw_config: Dict[str, Any]) -> ResourceConfigClass:
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
        an inherited class in order to preserved the conversions of the parent
        class.
        """
        raw_env = raw_config.pop('env')
        raw_removal_policy = raw_config.pop('removal_policy')

        env = Environment(**raw_env)
        removal_policy = RemovalPolicy[raw_removal_policy]

        raw_config.update(environment=env, removal_policy=removal_policy)

        return raw_config
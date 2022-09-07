from pathlib import Path
from dataclasses import dataclass
import json
from typing import ( 
    Any, 
    Dict, 
    Type, 
    TypeVar
)

class RawConfig:
    """
    Raw JSON configuration of the application and of all infrastructure resources for
    each environment and.
    """

    def __init__(self, config_file: Path):
        self._all_config: Any = self._read_config(config_file)
        self._environments_config: Any = self._all_config['environments']
        self._default: Any = self._environments_config['default']

        self.development: Any = self._get_config('development')
        self.staging: Any = self._get_config('staging')
        self.production: Any = self._get_config('production')

        self.application: Any = self._all_config['application']

    # Implementation of reading and parsing logic
    
    def _read_config(self,config_file: Path) -> dict:
        return json.load(config_file)
    
    
    def _get_config(self, env: str) -> Any:
        config = self._environments_config.get(env, None)
        return config
    
    
    
    
"""
----------------------------------------------------------------------------
COMMERCIAL IN CONFIDENCE

(c) Copyright Quosient Ltd. All Rights Reserved.

See LICENSE.txt in the repository root.
----------------------------------------------------------------------------
"""
from ebx.peristence.abstact_persistence import AbstractPersistence
from pathlib import Path
import json

class LocalFilePersistence(AbstractPersistence):
    """Local file system persistence."""
    def __init__(self, path):
        self.path = path

    def save(self,key:str, data):
        p = Path(self.path)
        p.mkdir(parents=True,exist_ok=True)
        with open(p/key,'w') as f:
            json.dump(data,f,indent=4)
        return self

    def exists(self, key: str) -> bool:
        p = Path(self.path)
        return (p/key).exists()
    
    def load(self, key: str):
        p = Path(self.path)
        with open(p/key,'r') as f:
            data = json.load(f)
        return data
    
    def set_path(self, path: str):
        self.path = path
        return self
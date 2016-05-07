import json
import os


__version__ = '0.0.0'
_metadata_file = os.path.join(os.path.dirname(__file__),'package_metadata.json')
if os.path.exists(_metadata_file):
    with open(_metadata_file) as _metadata_handle:
        _metadata = json.load(_metadata_handle)
        __version__ = _metadata['version']

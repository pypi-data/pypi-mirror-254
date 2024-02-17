import os
from typing import List, Optional
import json
import locale

METADATA_DIR = os.path.join('.junon')
DEFAULT_PARAMETERS_JSON_PATH = os.path.join(METADATA_DIR, f'default_params.json')
DEFAULT_MODEL = 'gpt-4-turbo-preview'


def save_default_parameters(default_parameters):
    with open(DEFAULT_PARAMETERS_JSON_PATH, 'w') as f:
        json.dump(default_parameters, f, indent=4, ensure_ascii=False)


def load_default_parameters() -> Optional[dict]:
    if not os.path.exists(DEFAULT_PARAMETERS_JSON_PATH):
        return dict(
            temperature=0.0,
            model=DEFAULT_MODEL,
            user_communication_language=locale.getdefaultlocale()[0],
        )
    with open(DEFAULT_PARAMETERS_JSON_PATH, 'r') as f:
        return json.load(f)

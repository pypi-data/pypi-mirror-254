#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
import os

from ...signer.errors import SignerConfigError
from .config_chapter import ConfigChapter


class State(ConfigChapter):

    def __init__(self, required, filename):
        self._state_required = required
        self._state_filename = filename

    @classmethod
    def from_yaml(cls, input_dict):
        if input_dict is None:
            return None

        state_chapter = State(input_dict.get('required'), input_dict.get('filename'))
        if state_chapter.validate(input_dict, validation_file='state_schema.json'):

            if state_chapter.state_required:
                if not state_chapter.state_filename:
                    raise SignerConfigError(
                        'configuration.state.required is set to True, but no configuration.state.filename is not set',
                    )

                if not os.path.exists(os.path.join('.src', state_chapter.state_filename)):
                    raise SignerConfigError('configuration.state.filename is set, but file not found')

            return state_chapter
        return None

    @property
    def state_filename(self):
        return self._state_filename

    @property
    def state_required(self):
        return self._state_required

import os

from beebot.config import config


class _Path:

    def join(self, *args):
        return os.path.join(config.root_dir, *args)


path = _Path()

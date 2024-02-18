import os
from typing import Optional

from uploader.exceptions import NotInCI


class UploadStructure:
    @property
    def user(self) -> Optional[str]:
        if 'GITHUB_REPOSITORY' in os.environ:
            return os.environ['GITHUB_REPOSITORY']
        raise NotInCI("GITHUB_REPOSITORY")

    @property
    def commit(self) -> Optional[str]:
        if 'GITHUB_SHA' in os.environ:
            return os.environ['GITHUB_SHA']
        raise NotInCI("GITHUB_SHA")

    @property
    def ref(self) -> Optional[str]:
        if 'GITHUB_REF' in os.environ:
            return os.environ['GITHUB_REF']
        raise NotInCI("GITHUB_REF")

    @property
    def token(self) -> Optional[str]:
        if 'TESTPULSE_TOKEN' in os.environ:
            return os.environ['TESTPULSE_TOKEN']
        raise NotInCI("TESTPULSE_TOKEN")

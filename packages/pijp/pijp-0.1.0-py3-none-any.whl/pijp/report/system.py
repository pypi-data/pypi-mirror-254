from typing import Optional
import os
import platform
import socket

from pydantic import BaseModel


class SystemReport(BaseModel):
    hostname: str = socket.gethostname()
    os_name: str = platform.system()
    os_version: str = platform.version()
    os_release: str = platform.release()
    cpu_architecture: str = platform.machine()
    cpu_cores: Optional[int] = os.cpu_count()

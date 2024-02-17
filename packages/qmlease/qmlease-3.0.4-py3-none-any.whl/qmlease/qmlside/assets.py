from __future__ import annotations

from os import getcwd
from os.path import basename

from lk_utils import normpath

from ..qtcore import QObject
from ..qtcore import slot


class Assets(QObject):
    
    def __init__(self):
        super().__init__()
        self._cwd = 'file:///' + getcwd().replace('\\', '/')
        self._src = self._cwd
        self._custom_sources = {}  # type: dict[str, str]
    
    def set_root(self, dir_: str) -> None:
        self._src = 'file:///' + normpath(dir_, force_abspath=True)
    
    def add_source(self, src: str, name: str = None) -> None:
        if name is None:
            name = basename(src)
        self._custom_sources[name] = \
            'file:///' + normpath(src, force_abspath=True)
    
    @slot(result=str)
    @slot(str, result=str)
    def src(self, relpath: str = '') -> str:
        if relpath == '':
            return self._src
        else:
            return normpath(f'{self._src}/{relpath}')
    
    @slot(result=str)
    @slot(str, result=str)
    def cwd(self, relpath: str = '') -> str:
        if relpath == '':
            return self._cwd
        else:
            return normpath(f'{self._cwd}/{relpath}')
    
    @slot(str, result=str)
    @slot(str, str, result=str)
    def get(self, src_name: str, relpath: str = '') -> str:
        return normpath(f'{self._custom_sources[src_name]}/{relpath}')


pyassets = Assets()

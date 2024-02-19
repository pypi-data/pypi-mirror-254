import sys 
from contextlib import contextmanager
import json
import os
from os import fspath
from platform import system
import stat
from subprocess import check_call
from typing import Optional,Dict
from .utils import AnyPath, temp_path
from os.path import join

@contextmanager
def make_map_file(tecmp_mapping: Optional[Dict[int, str]]):
    tecmp_mapping = tecmp_mapping or dict()
    with temp_path(suffix=".json") as tmpfile:
        mappings = list()
        for (chl_id, inf_name) in tecmp_mapping.items():
            mappings.append(dict(
                when=dict(chl_id=chl_id),
                change=dict(inf_name=inf_name)
            ))
        with open(tmpfile, 'w', encoding='utf-8') as f:
            data = dict(version=1, mappings=mappings)
            json.dump(data, f, indent=4)

        yield tmpfile


def tecmp_convert(infile: AnyPath, outfile: AnyPath, *, tecmp_mapping: Optional[Dict[int, str]] = None) -> None:
    """
    Remove TECMP packets from infile and write the result to outfile.
    """
    pkg_dir = os.path.dirname(os.path.abspath(__file__))
    bin_file = join(pkg_dir, 'binConverter', system().lower(), 'tecmp_converter')
    if system() == 'Linux':
        st = os.stat(bin_file)
        os.chmod(bin_file, st.st_mode | stat.S_IEXEC)

    with make_map_file(tecmp_mapping) as map_file:
        check_call([
            bin_file,
            "--tecmp-only",
            "--channel-map", map_file,
            fspath(infile),
            fspath(outfile)
        ])


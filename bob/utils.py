# -*- coding: utf-8 -*-

import os
import re
import tarfile
from subprocess import Popen, PIPE

def iter_marker_lines(marker, formula, strip=True):
    """Extracts any markers from a given formula."""

    with open(formula) as f:
        for line in f:
            if line.startswith(marker):

                if strip:
                    line = line[len(marker):]
                    line = line.strip()

                yield line


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError:
        pass


def process(cmd, cwd=None):
    """A simple wrapper around the subprocess module."""
    p = Popen(cmd, cwd=cwd, shell=False, stdout=PIPE, stderr=PIPE)
    return p


def pipe(a, b, indent=True):
    """Pipes stream A to stream B, with optional indentation."""

    for line in a:

        if indent:
            b.write('    ')

        b.write(line)


def targz_tree(dir, output):
    """Creates a tar.gz archive from a given directory."""
    with tarfile.open(output, 'w:gz') as tar:
        tar.add(dir, arcname=os.path.basename(dir))

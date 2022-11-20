#!/usr/bin/env python3

import os
import json
import pytest
import hashlib
import tempfile
from validata import simulate, error_check


def verifyHash(data: dict, readSize: int = 4096):
    tf = tempfile.NamedTemporaryFile(delete=False)
    with open(tf.name, 'w') as fh:
        fh.write(json.dumps(data))
    sha256Hash = hashlib.sha256()
    with open(tf.name, 'rb') as f:
        data = f.read(readSize)
        while data:
            sha256Hash.update(data)
            data = f.read(readSize)
    hash_ = sha256Hash.hexdigest()
    os.remove(tf.name)
    return hash_


def test_error_check():
    data = simulate(size=1000, mistake=True, error=0.01, seed=42)
    errors = error_check(data, error=0.01, outlier=3)
    hash_ = '7f270f6d428dcf0b3a575c81c6217b19dcd6692d92d6772435704d478d15d03b'
    assert verifyHash(errors) == hash_

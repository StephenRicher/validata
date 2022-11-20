# Validata - Utility for error checking

![build: status](https://github.com/StephenRicher/validata/actions/workflows/tests.yaml/badge.svg)

## Table of contents
  * [Installation](#installation)
    * [Docker](#docker)
  * [Python](#python)
    * [Pandas](#pandas)
    * [Files](#files)
  * [License](#license)
  * [Contact](#contact)

## Installation
```bash
pip install git+https://github.com/StephenRicher/validata.git
```

## Python
`DataCrypt` can be imported as a python module to encrypt and decrypt files.

### Pandas
If a Pandas DataFrame is provided to `datacrypt.encrypt` then it will be encrypted in `.parquet` format.
Following decryption, an in-memory buffer is returned which should be passed to `pd.read_parquet` to recover the dataframe and datatypes.

```python
import pandas as pd
from datacrypt import encrypt, decrypt

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['dog', 'cat', 'bat']
})

encrypt(df, 'df-encrypted.pq')

df = pd.read_parquet(decrypt('df-encrypted.pq'))
```

### Files
The command line functionality can also be achieved within Python.
In addition the `datacrypt.decrypt` function returns an in-memory buffer which can be read directly.

#### Encrypt and write encrypted data to file
```python
import pandas as pd
from datacrypt import encrypt, decrypt

with open('data.encrypted', 'wb') as fh:
    fh.write(encrypt('data.csv'))
```

#### Decrypt and write decrypted data to file
```python
with open('data.decrypted.csv', 'w') as fh:
    fh.write(decrypt('data.encrypted').getvalue())
```

#### Decrypt and read in-memory buffer to Pandas
```python
df = pd.read_csv(decrypt('data.encrypted'))
```

## License
Distributed under the MIT License. _See [LICENSE](./LICENSE) for more information._


## Contact
If you have any other questions please contact the author **[Stephen Richer](https://www.linkedin.com/in/stephenricher/)**
at stephen.richer@proton.me

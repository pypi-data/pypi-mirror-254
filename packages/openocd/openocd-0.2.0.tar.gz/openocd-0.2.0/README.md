# openocd

Python interface library for [OpenOCD](https://openocd.org/).


# Dependencies

* Python >= 3.6


# Installation

Prerequisites:

* Python 3.6 or higher

  * https://www.python.org/

* setuptools

  * https://pypi.org/project/setuptools/

To install this package, run:

```bash
python setup.py install
```


# Example

```python
from openocd import OpenOcd

with OpenOcd() as oocd:
    oocd.halt()
    registers = oocd.read_registers(['pc', 'sp'])

    print('Program counter: 0x%x' % registers['pc'])
    print('Stack pointer: 0x%x' % registers['sp'])

    oocd.resume()
```

# License

This project is licensed under the [GPLv3+](https://www.gnu.org/licenses/gpl-3.0.en.html) - see the [LICENSE](LICENSE) file for details.

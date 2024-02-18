# RUtil: Rust Utilities for Python

This code defines a library of Rust functions, and a Python middleman from which to call those functions. It is modelled on the `shutil` module from the Python standard library.

## Installation

### Installing the Python Code

* If you're installing remotely, **`pip install hosker-rutil`** should do the trick.
* If, on the other hand, you're installing locally, then use **`pip install .`** from this directory.

### Compiling the Rust Library

By installing the PIP package as described above, you will also have installed the command `hosker-rutil-install-specials`. Running this command will compile the Rust libraries from their source code, as well as installing Cargo, if you don't have it already.

## Examples

### Primes

This code should find whether a nine-digit number is prime or not - and do so far quicker than anything in pure Python:

```python
from hosker_rutil.primes import is_prime_i32

def run():
    print(is_prime_i32(188888881))

if __name__ == "__main__":
    run()
```

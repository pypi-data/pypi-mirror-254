"""
Entrypoint module.

Allows to use the package as main application:
``python -m byteblower.test_cases.low_latency``

Why does this file exist, and why ``__main__``? For more info, read:
- https://peps.python.org/pep-0338/
- https://docs.python.org/3/using/cmdline.html#cmdoption-m
"""
from .cli import main

if __name__ == "__main__":
    main()

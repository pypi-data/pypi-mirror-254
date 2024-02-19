from setuptools import setup

name = "types-pyserial"
description = "Typing stubs for pyserial"
long_description = '''
## Typing stubs for pyserial

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`pyserial`](https://github.com/pyserial/pyserial) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`pyserial`.

This version of `types-pyserial` aims to provide accurate annotations
for `pyserial==3.5.*`.
The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/pyserial. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `a2a6aee89213d87ed6f86cf723a7fc4ed3c219a2` and was tested
with mypy 1.8.0, pyright 1.1.342, and
pytype 2024.1.24.
'''.lstrip()

setup(name=name,
      version="3.5.0.20240205",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/pyserial.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['serial-stubs'],
      package_data={'serial-stubs': ['__init__.pyi', '__main__.pyi', 'rfc2217.pyi', 'rs485.pyi', 'serialcli.pyi', 'serialjava.pyi', 'serialposix.pyi', 'serialutil.pyi', 'serialwin32.pyi', 'threaded/__init__.pyi', 'tools/__init__.pyi', 'tools/hexlify_codec.pyi', 'tools/list_ports.pyi', 'tools/list_ports_common.pyi', 'tools/list_ports_linux.pyi', 'tools/list_ports_osx.pyi', 'tools/list_ports_posix.pyi', 'tools/list_ports_windows.pyi', 'tools/miniterm.pyi', 'urlhandler/__init__.pyi', 'urlhandler/protocol_alt.pyi', 'urlhandler/protocol_cp2110.pyi', 'urlhandler/protocol_hwgrep.pyi', 'urlhandler/protocol_loop.pyi', 'urlhandler/protocol_rfc2217.pyi', 'urlhandler/protocol_socket.pyi', 'urlhandler/protocol_spy.pyi', 'win32.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)

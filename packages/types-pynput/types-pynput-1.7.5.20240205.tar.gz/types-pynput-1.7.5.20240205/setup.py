from setuptools import setup

name = "types-pynput"
description = "Typing stubs for pynput"
long_description = '''
## Typing stubs for pynput

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`pynput`](https://github.com/moses-palmer/pynput) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`pynput`.

This version of `types-pynput` aims to provide accurate annotations
for `pynput==1.7.*`.
The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/pynput. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `a2a6aee89213d87ed6f86cf723a7fc4ed3c219a2` and was tested
with mypy 1.8.0, pyright 1.1.342, and
pytype 2024.1.24.
'''.lstrip()

setup(name=name,
      version="1.7.5.20240205",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/pynput.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['pynput-stubs'],
      package_data={'pynput-stubs': ['__init__.pyi', '_info.pyi', '_util.pyi', 'keyboard/__init__.pyi', 'keyboard/_base.pyi', 'keyboard/_dummy.pyi', 'mouse/__init__.pyi', 'mouse/_base.pyi', 'mouse/_dummy.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)

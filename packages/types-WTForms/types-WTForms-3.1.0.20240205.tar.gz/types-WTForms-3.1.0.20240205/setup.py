from setuptools import setup

name = "types-WTForms"
description = "Typing stubs for WTForms"
long_description = '''
## Typing stubs for WTForms

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`WTForms`](https://github.com/wtforms/wtforms) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`WTForms`.

This version of `types-WTForms` aims to provide accurate annotations
for `WTForms==3.1.*`.
The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/WTForms. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `a2a6aee89213d87ed6f86cf723a7fc4ed3c219a2` and was tested
with mypy 1.8.0, pyright 1.1.342, and
pytype 2024.1.24.
'''.lstrip()

setup(name=name,
      version="3.1.0.20240205",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/WTForms.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=['MarkupSafe'],
      packages=['wtforms-stubs'],
      package_data={'wtforms-stubs': ['__init__.pyi', 'csrf/__init__.pyi', 'csrf/core.pyi', 'csrf/session.pyi', 'fields/__init__.pyi', 'fields/choices.pyi', 'fields/core.pyi', 'fields/datetime.pyi', 'fields/form.pyi', 'fields/list.pyi', 'fields/numeric.pyi', 'fields/simple.pyi', 'form.pyi', 'i18n.pyi', 'meta.pyi', 'utils.pyi', 'validators.pyi', 'widgets/__init__.pyi', 'widgets/core.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)

Pathlib-cli is a command line interface for Python's pathlib library.
It focuses on extracting parts of paths (stem, suffixes, parents, etc).

Pathlib-cli also includes prefix and prefixes command which are not
in pathlib. These extricate a substring of the filename up to but
not including the nth '.'.

Example usage:

```
readlink -f * | pathlib-cli prefix
```

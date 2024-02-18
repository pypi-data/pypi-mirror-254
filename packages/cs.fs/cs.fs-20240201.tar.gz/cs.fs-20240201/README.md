Assorted filesystem related utility functions,
some of which have been bloating cs.fileutils for too long.

*Latest release 20240201*:
* FSPathBasedSingleton: drop the default_factory parameter/attribute, let default_attr specify a callable.
* Singleton._resolve_fspath: fix reference to class name.

## Function `atomic_directory(*da, **dkw)`

Decorator for a function which fills in a directory
which calls the function against a temporary directory
then renames the temporary to the target name on completion.

Parameters:
* `infill_func`: the function to fill in the target directory
* `make_placeholder`: optional flag, default `False`:
  if true an empty directory will be make at the target name
  and after completion it will be removed and the completed
  directory renamed to the target name

## Function `fnmatchdir(dirpath, fnglob)`

Return a list of the names in `dirpath` matching the glob `fnglob`.

## Class `FSPathBasedSingleton(cs.obj.SingletonMixin, HasFSPath)`

The basis for a `SingletonMixin` based on `realpath(self.fspath)`.

*Method `FSPathBasedSingleton.__init__(self, fspath: Optional[str] = None, lock=None)`*:
Initialise the singleton:

On the first call:
- set `.fspath` to `self._resolve_fspath(fspath)`
- set `._lock` to `lock` (or `threading.Lock()` if not specified)
- return `True`
On subsequent calls return `False`.

## Class `HasFSPath`

An object with a `.fspath` attribute representing a filesystem location.

*Method `HasFSPath.fnmatch(self, fnglob)`*:
Return a list of the names in `self.fspath` matching the glob `fnglob`.

*Method `HasFSPath.listdir(self)`*:
Return `os.listdir(self.fspath)`.

*Method `HasFSPath.pathto(self, *subpaths)`*:
The full path to `subpaths`, comprising a relative path
below `self.fspath`.
This is a shim for `os.path.join` which requires that all
the `subpaths` be relative paths.

*Property `HasFSPath.shortpath`*:
The short version of `self.fspath`.

## Function `is_valid_rpath(rpath, log=None) -> bool`

Test that `rpath` is a clean relative path with no funny business.

This is a Boolean wrapper for `validate_rpath()`.

## Function `longpath(path, prefixes=None)`

Return `path` with prefixes and environment variables substituted.
The converse of `shortpath()`.

## Function `needdir(dirpath, mode=511, *, use_makedirs=False, log=None)`

Create the directory `dirpath` if missing.

Parameters:
* `dirpath`: the required directory path
* `mode`: the permissions mode, default `0o777`
* `log`: log `makedirs` or `mkdir` call
* `use_makedirs`: optional creation mode, default `False`;
  if true, use `os.makedirs`, otherwise `os.mkdir`

## Function `rpaths(dirpath='.', *, only_suffixes=None, skip_suffixes=None, sort_paths=False)`

Yield relative file paths from a directory.

Parameters:
* `dirpath`: optional top directory, default `'.'`
* `only_suffixes`: optional iterable of suffixes of interest;
  if provided only files ending in these suffixes will be yielded
* `skip_suffixes`: optional iterable if suffixes to ignore;
  if provided files ending in these suffixes will not be yielded
* `sort_paths`: optional flag specifying that filenames should be sorted,
  default `False`

## Function `shortpath(path, prefixes=None)`

Return `path` with the first matching leading prefix replaced.

Parameters:
* `environ`: environment mapping if not os.environ
* `prefixes`: optional iterable of `(prefix,subst)` to consider for replacement;
  each `prefix` is subject to environment variable
  substitution before consideration
  The default considers "$HOME/" for replacement by "~/".

## Function `validate_rpath(rpath: str)`

Test that `rpath` is a clean relative path with no funny business;
raise `ValueError` if the test fails.

Tests:
- not empty or '.' or '..'
- not an absolute path
- normalised
- does not walk up out of its parent directory

Examples:

    >>> validate_rpath('')
    False
    >>> validate_rpath('.')

# Release Log



*Release 20240201*:
* FSPathBasedSingleton: drop the default_factory parameter/attribute, let default_attr specify a callable.
* Singleton._resolve_fspath: fix reference to class name.

*Release 20231129*:
* HasFSPath: new listdir method.
* HasFSPath.pathto: accept multiple relative subpaths.
* FSPathBasedSingleton: accept cls.FSPATH_FACTORY as a factory function for the default fspath, makes it possible to defer the path lookup.
* Replace is_clean_subpath with validate_rpath/is_valid_rpath pair.

*Release 20230806*:
* Reimplement fnmatchdir using fnmatch.filter.
* No longer claim Python 2 compatibility.

*Release 20230401*:
HasFSPath.shortpath: hand call before .fspath set.

*Release 20221221*:
Replace use of cs.env.envsub with os.path.expandvars and drop unused environ parameter.

*Release 20220918*:
* FSPathBasedSingleton.__init__: return True on the first call, False on subsequent calls.
* FSPathBasedSingleton.__init__: probe __dict__ for '_lock' instead of using hasattr (which plays poorly this early on with classes with their own __getattr__).
* needdir: accept optional `log` parameter to log mkdir or makedirs.
* HasFSPath: add a default __str__.

*Release 20220805*:
Doc update.

*Release 20220530*:
FSPathBasedSingleton._resolve_fspath: new `envvar` and `default_attr` parameters.

*Release 20220429*:
* New HasFSPath and FSPathBasedSingleton.
* Add longpath and shortpath from cs.fileutils.
* New is_clean_subpath(subpath).
* New needdir(path).
* New fnmatchdir(dirpath,fnglob) pulled out from HasFSPath.fnmatch(fnglob).

*Release 20220327*:
New module cs.fs to contain more filesystem focussed functions than cs.fileutils, which is feeling a bit bloated.

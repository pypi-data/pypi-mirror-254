Access the MacOS degfaults via the `defaults` command.

*Latest release 20240201*:
Initial PyPI release.

## Class `Defaults`

A view of the defaults.

*Property `Defaults.domains`*:
Return a list of the domains present in the defaults.

*Method `Defaults.run(self, argv, doit=True, quiet=False) -> str`*:
Run a `defaults` subcommand, return the output decoded from UTF-8.

## Function `defaults(argv, *, host=None, doit=True, **subp)`

Run the `defaults` command with the arguments `argv`.
If the optional `host` parameter is supplied,
a value of `'.'` uses the `-currentHost` option
and other values are used with the `-host` option.
Return the `CompletedProcess` result or `None` if `doit` is false.

## Class `DomainDefaults`

A view of the defaults for a particular domain.

*Method `DomainDefaults.as_dict(self)`*:
Return the current defaults as a `dict`.

*Method `DomainDefaults.flush(self)`*:
Forget any cached information.

# Release Log



*Release 20240201*:
Initial PyPI release.

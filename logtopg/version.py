# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

"""
Do not do anything in this file except define the __version__ variable!

The setup.py script reads this version from here during install.

In the past, I've defined the version in the setup.py file (A), or
defined it in the top of the project, like in logtopg/__init__.py (B).

Choice A is bad because it isn't easy to fire up a python session and
then do::

    >>> import logtopg
    >>> logtopg.__version__ # doctest: +SKIP

to look up the version.

And choice B is bad because the logtopg/__init__.py file might blow up
during install because it tries to import a some third-party module that
hasn't been imported yet.

"""

__version__ = "0.1.1"

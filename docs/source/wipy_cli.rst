wipy_cli
--------

The `wipy_cli` script is a command line utility to access the wipy board.  This script currently supports a number of
subcommands.

wipy_cli console
~~~~~~~~~~~~~~~~

The `wipy_cli console` command provides a console session on the wipy board via telent::

    $ wipy_cli console
    >>> import os
    >>> os.uname()
    (sysname='WiPy', nodename='WiPy', release='1.2.0', version='v1.6-89-g440d33a on 2016-02-27', machine='WiPy with CC3200')
    >>>

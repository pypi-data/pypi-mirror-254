"""
Pretty print package version.

The full version style has these components:
[base]-[revision].[release info].[build info]

You can override components via command line options.

EPILOG:
Examples:
Print version in default style, which is "internal"
  $ pdk-semver
  3.2.2-rev.3.git.b674019

Print version in default style, with release info "arch.aarch64"
  $ pdk-semver --rinfo-value arch.aarch64
  3.2.2-rev.3.arch.aarch64.git.b674019

Print all styles
  $ pdk-semver -s all --rinfo-value some.info
  internal 3.2.2-rev.3.some.info.git.b674019
    public 3.2.2-rev.3.some.info
   baserev 3.2.2-rev.3
      base 3.2.2
"""


import logging
import sys

import pydevkit.log.config  # noqa: F401
from pydevkit.argparse import ArgumentParser

from . import __version__
from .scm import get_scm_vals
from .ver import Version

log = logging.getLogger(__name__)


def get_cmd_vals(args) -> dict:
    vals = {}
    for k, v in vars(args).items():
        pfx = k.split("_", 1)[0]
        if pfx in ["rinfo"]:
            vals[k] = v
    return vals


def get_args():
    p = ArgumentParser(help=__doc__, version=__version__, usage="short")
    p.add_argument(
        "-C", help="path to git repo", dest="path", metavar="path", default="."
    )
    p.add_argument(
        "-r", help="git revision ref", dest="ref", metavar="ref", default="HEAD"
    )
    styles = [*list(Version.Styles.keys()), "all"]
    p.add_argument(
        "-s",
        help="style, one of %(choices)s",
        dest="style",
        metavar="name",
        default="internal",
        choices=styles,
    )
    p.add_argument(
        "--rinfo-value", help="release info component", metavar="txt", default=""
    )

    return p.parse_known_args()


def main():
    args, unknown_args = get_args()
    if unknown_args:
        log.warning("Unknown arguments: %s", unknown_args)
        sys.exit(1)

    ver = Version()
    cmd_vals = get_cmd_vals(args)
    scm_vals = get_scm_vals(args.path, args.ref)
    if args.style != "all":
        print(ver.fmt(Version.Styles[args.style], scm_vals, cmd_vals))
        return

    for k, v in Version.Styles.items():
        print("%8s" % k, ver.fmt(v, scm_vals, cmd_vals))


if __name__ == "__main__":
    main()

"""Git repo support."""

import logging

import pydevkit.log.config  # noqa: F401
from pydevkit.shell import Shell

log = logging.getLogger(__name__)


class GitVals:
    Name = "git"

    @staticmethod
    def supported(path):
        sh = Shell()
        sh["dir"] = path
        sh["git"] = 'git -C "%(dir)s"' % sh
        sh("%(git)s rev-parse --git-dir >& /dev/null")

    @staticmethod
    def get_vals(adir, aref) -> dict:
        sh = Shell()
        sh["dir"] = adir
        sh["ref"] = aref
        sh["git"] = 'git -C "%(dir)s"' % sh
        rc = {}
        # find closest tag
        val = sh.inp("%(git)s describe --abbrev=0 %(ref)s 2>/dev/null | cat")
        rc["base_value"] = val if val else "0.1.0"
        if val:
            val += ".."
        sh["tag"] = val
        val = int(sh.inp("%(git)s rev-list %(tag)s%(ref)s --count"))
        rc["rev_value"] = val
        val = sh.inp("%(git)s rev-parse --short %(ref)s")
        rc["binfo_value"] = ["git", val]
        return rc


def get_scm_vals(path, ref) -> dict:
    for cls in [GitVals]:
        try:
            cls.supported(path)
            log.debug("%s repo found at '%s'", cls.Name, path)
            return cls.get_vals(path, ref)
        except Exception:
            pass
    log.warning("no version control found at '%s", path)
    return {}

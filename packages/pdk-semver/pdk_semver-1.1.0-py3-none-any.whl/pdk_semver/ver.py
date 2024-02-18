"""Pretty print package version."""


import logging
import re
from types import MappingProxyType

log = logging.getLogger(__name__)


class Version:
    Styles = MappingProxyType(
        {
            "internal": {
                "base_show": True,
                "base_latest": False,
                "rev_show": True,
                "rev_show_zero": False,
                "rev_prefix": "rev",
                "rinfo_show": True,
                "binfo_show": True,
            },
            "public": {
                "base_show": True,
                "base_latest": False,
                "rev_show": True,
                "rev_show_zero": False,
                "rev_prefix": "rev",
                "rinfo_show": True,
                "binfo_show": False,
            },
            "baserev": {
                "base_show": True,
                "base_latest": False,
                "rev_show": True,
                "rev_show_zero": False,
                "rev_prefix": "rev",
                "rinfo_show": False,
                "binfo_show": False,
            },
            "base": {
                "base_show": True,
                "base_latest": False,
                "rev_show": False,
                "rev_show_zero": False,
                "rev_prefix": "rev",
                "rinfo_show": False,
                "binfo_show": False,
            },
        }
    )

    def str_sanitize(self, txt) -> str:
        if not (txt and isinstance(txt, str)):
            return ""
        return re.sub("[^0-9a-zA-Z_.-]", "", txt)

    def ver_sanitize(self, txt) -> str:
        if not (txt and isinstance(txt, str)):
            return ""
        txt = re.sub("([_.-])+", "\\1", txt)
        txt = re.sub("([_.-])+$", "", txt)
        log.debug("ver sanitize: return '%s'", txt)
        return txt

    def fmt_base(self, opts: dict) -> list:
        if not opts.get("base_show"):
            return []
        val = opts.get("base_value", "0.1.0")
        if opts.get("base_latest"):
            val = val.split(".")[:2]
            val = ".".join(val)
        return [val]

    def fmt_rev(self, opts: dict) -> list:
        if not opts.get("rev_show"):
            return []
        val = opts.get("rev_value", 0)
        if not (val or opts.get("rev_show_zero")):
            return []
        rc = []
        pfx = opts.get("rev_prefix")
        if pfx:
            rc.append(pfx)
        rc.append(str(val))
        return rc

    def fmt_rinfo(self, opts: dict) -> list:
        return self.fmt_info(opts, "rinfo")

    def fmt_binfo(self, opts: dict) -> list:
        return self.fmt_info(opts, "binfo")

    def fmt_info(self, opts: dict, pfx: str) -> list:
        pfx += "_"
        if not opts.get(pfx + "show"):
            return []
        val = opts.get(pfx + "value")
        if not val:
            return []
        if isinstance(val, str):
            val = [val]
        return val

    def fmt(self, *vals_list, **kwargs) -> str:
        log.debug("fmt: start")
        fvals = {}
        for vals in vals_list:
            log.debug("vals: %s", vals)
            fvals.update(vals)
        log.debug("kwargs: %s", kwargs)
        for k, v in kwargs.items():
            fvals[k] = v

        def call_plugin(name, func):
            log.debug("plugin '%s': start", name)
            rc = func(fvals)
            log.debug("plugin '%s': return %s", name, rc)
            return rc

        rc = []
        for p in ["rev", "rinfo", "binfo"]:
            func = getattr(self, "fmt_" + p, None)
            if not func:
                log.warning("unknown plugin '%s'", p)
                continue
            rc += call_plugin(p, func)
        rc = [self.str_sanitize(e) for e in rc]
        rc = [e for e in rc if e]
        log.debug("ver sanitize return: '%s'", rc)

        ver = call_plugin("base", self.fmt_base)
        if rc:
            ver.append(".".join(rc))
        ver = "-".join(ver)
        ver = self.ver_sanitize(ver)
        log.debug("fmt: return '%s'", ver)
        return ver

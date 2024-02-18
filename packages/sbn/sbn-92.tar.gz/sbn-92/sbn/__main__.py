# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0212,W0611,W0613,E0401


"runtime"


import getpass
import inspect
import os
import pwd
import readline
import sys
import termios
import time
import _thread


from . import Client, Command, Default, Error, Event, Object, Storage
from . import cdir, cmnd, debug, forever, launch, parse_command, spl, scan


def __dir__():
    return (
        'Cfg',
        'Console',
        'daemon',
        'daemoned',
        'main',
        'privileges',
        'wrap',
        'wrapped'
    )


__all__ = __dir__()


Cfg         = Default()
Cfg.name    = __file__.split(os.sep)[-2]
Cfg.wd      = os.path.expanduser(f"~/.{Cfg.name}")
Cfg.pidfile = os.path.join(Cfg.wd, f"{Cfg.name}.pid")
Cfg.user    = getpass.getuser()
Storage.wd  = Cfg.wd


from sbn import modules


class Console(Client):

    def announce(self, txt):
        pass

    def callback(self, evt):
        Client.callback(self, evt)
        evt.wait()

    def poll(self):
        evt = Event()
        evt.orig = object.__repr__(self)
        evt.txt = input("> ")
        evt.type = "command"
        return evt

    def say(self, channel, txt):
        txt = txt.encode('utf-8', 'replace').decode()
        print(txt)


def daemon(pidfile, verbose=False):
    pid = os.fork()
    if pid != 0:
        os._exit(0)
    os.setsid()
    pid2 = os.fork()
    if pid2 != 0:
        os._exit(0)
    if not verbose:
        with open('/dev/null', 'r', encoding="utf-8") as sis:
            os.dup2(sis.fileno(), sys.stdin.fileno())
        with open('/dev/null', 'a+', encoding="utf-8") as sos:
            os.dup2(sos.fileno(), sys.stdout.fileno())
        with open('/dev/null', 'a+', encoding="utf-8") as ses:
            os.dup2(ses.fileno(), sys.stderr.fileno())
    os.umask(0)
    os.chdir("/")
    if os.path.exists(pidfile):
        os.unlink(pidfile)
    cdir(os.path.dirname(pidfile))
    with open(pidfile, "w", encoding="utf-8") as fds:
        fds.write(str(os.getpid()))


def daemoned():
    Cfg.mod = ",".join(modules.__dir__())
    daemon(Cfg.pidfile)
    privileges(Cfg.user)
    scan(modules, Cfg.mod, True)
    forever()


def privileges(username):
    pwnam = pwd.getpwnam(username)
    os.setgid(pwnam.pw_gid)
    os.setuid(pwnam.pw_uid)


def wrap(func):
    old2 = None
    try:
        old2 = termios.tcgetattr(sys.stdin.fileno())
    except termios.error:
        pass
    try:
        func()
    except (KeyboardInterrupt, EOFError):
        print("")
    finally:
        if old2:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old2)


def main():
    Storage.skel()
    parse_command(Cfg, " ".join(sys.argv[1:]))
    if "x" in Cfg.opts:
        Cfg.mod += ",cmd,flt,man,mod,mre,pwd,req,thr"
    else:
        Cfg.mod = ",".join(modules.__dir__())
    if "v" in Cfg.opts:
        dte = time.ctime(time.time()).replace("  ", " ")
        debug(f"{Cfg.name.upper()} {Cfg.opts.upper()} started {dte}")
    if "d" in Cfg.opts:
        daemoned()
    csl = Console()
    if "h" in Cfg.opts:
        scan(modules, Cfg.mod)
        cmnd("man")
    if "c" in Cfg.opts:
        scan(modules, Cfg.mod, True, Cfg.sets.dis, True)
        csl.start()
        forever()
    if Cfg.otxt:
        scan(modules, Cfg.mod)
        return cmnd(Cfg.otxt)


def wrapped():
    wrap(main)
    Error.show()


if __name__ == "__main__":
    wrapped()

# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0613,W0212


"runtime"


import inspect
import time
import _thread


from .brokers import Broker
from .command import Command
from .handler import Event, Handler
from .objects import Object
from .parsers import spl
from .storage import Storage
from .threads import launch


class Client(Handler):

    def __init__(self):
        Handler.__init__(self)
        self.register("command", Command.handle)
        Broker.add(self)

    def announce(self, txt):
        self.raw(txt)

    def say(self, channel, txt):
        self.raw(txt)

    def raw(self, txt):
        pass


def cmnd(clt, txt):
    evn = Event()
    evn.orig = object.__repr__(clt)
    evn.txt = txt
    Command.handle(evn)
    evn.wait()
    return evn


def forever():
    while 1:
        try:
            time.sleep(1.0)
        except (KeyboardInterrupt, EOFError):
            _thread.interrupt_main()


def scan(pkg, modstr, initer=False, disable="", wait=True) -> []:
    mds = []
    for modname in spl(modstr):
        if modname in spl(disable):
            continue
        module = getattr(pkg, modname, None)
        if not module:
            continue
        for _key, cmd in inspect.getmembers(module, inspect.isfunction):
            if 'event' in cmd.__code__.co_varnames:
                Command.add(cmd)
        for _key, clz in inspect.getmembers(module, inspect.isclass):
            if not issubclass(clz, Object):
                continue
            Storage.add(clz)
        if initer and "init" in dir(module):
            module._thr = launch(module.init, name=f"init {modname}")
            mds.append(module)
    if wait and initer:
        for mod in mds:
            mod._thr.join()
    return mds

#    ____    ________  ___   _____ ____  __ __ 
#   / __ \  / ____/  |/  /  / ___// __ \/ //_/ 
#  / / / / / /_  / /|_/ /   \__ \/ / / / ,<    
# / /_/ / / __/ / /  / /   ___/ / /_/ / /| |   
# \___\_\/_/   /_/  /_/   /____/_____/_/ |_|   
#                                              
# python binding c libaray by ctypesgen
# Date: 2023.12.25
# ==============================================
__docformat__ = "restructuredtext"
# Begin preamble for Python

import ctypes
import sys
from ctypes import *


_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass
# End loader

# Load Libaray
libList = []
libName = "libQFM_SDK"
current_dir = os.path.dirname(os.path.abspath(__file__))

if sys.platform == 'win32' or sys.platform == 'cygwin':
    libList.append(os.path.join(current_dir, 'lib', 'win-x64'))
    libName = "QFM_SDK_DLL"
elif "aarch64" in os.uname()[4]:
    libList.append(os.path.join(current_dir, 'lib', 'arm64', 'release'))
elif ctypes.sizeof(ctypes.c_void_p) == 8:
    libList.append(os.path.join(current_dir, 'lib', 'x86_64', 'release'))
else:
    libList.append(os.path.join(current_dir, 'lib', 'arm', 'release'))

add_library_search_dirs(libList)
_libs["libQFM_SDK.so"] = load_library(libName)

__uint8_t = c_ubyte# /usr/include/aarch64-linux-gnu/bits/types.h: 38

__uint16_t = c_ushort# /usr/include/aarch64-linux-gnu/bits/types.h: 40

__uint32_t = c_uint# /usr/include/aarch64-linux-gnu/bits/types.h: 42

uint8_t = __uint8_t# /usr/include/aarch64-linux-gnu/bits/stdint-uintn.h: 24

uint16_t = __uint16_t# /usr/include/aarch64-linux-gnu/bits/stdint-uintn.h: 25

uint32_t = __uint32_t# /usr/include/aarch64-linux-gnu/bits/stdint-uintn.h: 26

DWORD = uint32_t# QF_Def.h: 61

WORD = uint16_t# QF_Def.h: 65

BYTE = uint8_t# QF_Def.h: 68

BOOL = c_bool# QF_Def.h: 73

UINT32 = uint32_t# QF_Def.h: 80

USHORT = uint16_t# QF_Def.h: 84

LONG = uint32_t# QF_Def.h: 88

HANDLE = POINTER(None)# QF_Def.h: 92

enum_anon_22 = c_int# QF_Error.h: 153

QF_RET_SUCCESS = 0# QF_Error.h: 153

QF_ERR_CANNOT_OPEN_SERIAL = (-1)# QF_Error.h: 153

QF_ERR_CANNOT_SETUP_SERIAL = (-2)# QF_Error.h: 153

QF_ERR_CANNOT_WRITE_SERIAL = (-3)# QF_Error.h: 153

QF_ERR_WRITE_SERIAL_TIMEOUT = (-4)# QF_Error.h: 153

QF_ERR_CANNOT_READ_SERIAL = (-5)# QF_Error.h: 153

QF_ERR_READ_SERIAL_TIMEOUT = (-6)# QF_Error.h: 153

QF_ERR_CHECKSUM_ERROR = (-7)# QF_Error.h: 153

QF_ERR_CANNOT_SET_TIMEOUT = (-8)# QF_Error.h: 153

QF_ERR_CANNOT_START_SOCKET = (-301)# QF_Error.h: 153

QF_ERR_CANNOT_OPEN_SOCKET = (-302)# QF_Error.h: 153

QF_ERR_CANNOT_CONNECT_SOCKET = (-303)# QF_Error.h: 153

QF_ERR_CANNOT_READ_SOCKET = (-304)# QF_Error.h: 153

QF_ERR_READ_SOCKET_TIMEOUT = (-305)# QF_Error.h: 153

QF_ERR_CANNOT_WRITE_SOCKET = (-306)# QF_Error.h: 153

QF_ERR_WRITE_SOCKET_TIMEOUT = (-307)# QF_Error.h: 153

QF_ERR_FAILED = (-100)# QF_Error.h: 153

QF_ERR_SCAN_FAIL = (-101)# QF_Error.h: 153

QF_ERR_NOT_FOUND = (-102)# QF_Error.h: 153

QF_ERR_NOT_MATCH = (-103)# QF_Error.h: 153

QF_ERR_TRY_AGAIN = (-104)# QF_Error.h: 153

QF_ERR_TIME_OUT = (-105)# QF_Error.h: 153

QF_ERR_MEM_FULL = (-106)# QF_Error.h: 153

QF_ERR_EXIST_ID = (-107)# QF_Error.h: 153

QF_ERR_FACE_TEMPLATE_LIMIT = (-108)# QF_Error.h: 153

QF_ERR_UNSUPPORTED = (-109)# QF_Error.h: 153

QF_ERR_INVALID_ID = (-110)# QF_Error.h: 153

QF_ERR_TIMEOUT_MATCH = (-111)# QF_Error.h: 153

QF_ERR_BUSY = (-112)# QF_Error.h: 153

QF_ERR_CANCELED = (-113)# QF_Error.h: 153

QF_ERR_DATA_ERROR = (-114)# QF_Error.h: 153

QF_ERR_EXIST_FACE = (-115)# QF_Error.h: 153

QF_ERR_FAKE_DETECTED = (-122)# QF_Error.h: 153

QF_ERR_OUT_OF_MEMORY = (-200)# QF_Error.h: 153

QF_ERR_INVALID_PARAMETER = (-201)# QF_Error.h: 153

QF_ERR_FILE_IO = (-202)# QF_Error.h: 153

QF_ERR_INVALID_FILE = (-203)# QF_Error.h: 153

QF_ERR_INVALID_FIRMWARE = (-204)# QF_Error.h: 153

QF_ERR_RECOVERY_MODE = (-401)# QF_Error.h: 153

QF_ERR_NO_SERIAL_NUMBER = (-402)# QF_Error.h: 153

QF_ERR_INVALID_DATABASE_FORMAT = (-403)# QF_Error.h: 153

QF_ERR_WRONG_IMAGE_FORMAT = (-404)# QF_Error.h: 153

QF_ERR_WRONG_IMAGE_SIZE = (-405)# QF_Error.h: 153

QF_ERR_SECURE_CODE_VERIFICATION_FAIL = (-501)# QF_Error.h: 153

QF_ERR_UNKNOWN = (-9999)# QF_Error.h: 153

QF_RET_CODE = enum_anon_22# QF_Error.h: 153

enum_anon_23 = c_int# QF_Error.h: 243

QF_PROTO_RET_FAILED = 0x60# QF_Error.h: 243

QF_PROTO_RET_SUCCESS = 0x61# QF_Error.h: 243

QF_PROTO_RET_SCAN_SUCCESS = 0x62# QF_Error.h: 243

QF_PROTO_RET_SCAN_FAIL = 0x63# QF_Error.h: 243

QF_PROTO_RET_NOT_FOUND = 0x69# QF_Error.h: 243

QF_PROTO_RET_NOT_MATCH = 0x6A# QF_Error.h: 243

QF_PROTO_RET_TRY_AGAIN = 0x6B# QF_Error.h: 243

QF_PROTO_RET_TIME_OUT = 0x6C# QF_Error.h: 243

QF_PROTO_RET_MEM_FULL = 0x6D# QF_Error.h: 243

QF_PROTO_RET_EXIST_ID = 0x6E# QF_Error.h: 243

QF_PROTO_RET_FACE_TEMPLATE_LIMIT = 0x72# QF_Error.h: 243

QF_PROTO_RET_CONTINUE = 0x74# QF_Error.h: 243

QF_PROTO_RET_UNSUPPORTED = 0x75# QF_Error.h: 243

QF_PROTO_RET_INVALID_ID = 0x76# QF_Error.h: 243

QF_PROTO_RET_TIMEOUT_MATCH = 0x7A# QF_Error.h: 243

QF_PROTO_RET_INVALID_FIRMWARE = 0x7C# QF_Error.h: 243

QF_PROTO_RET_BUSY = 0x80# QF_Error.h: 243

QF_PROTO_RET_CANCELED = 0x81# QF_Error.h: 243

QF_PROTO_RET_DATA_ERROR = 0x82# QF_Error.h: 243

QF_PROTO_RET_DATA_OK = 0x83# QF_Error.h: 243

QF_PROTO_RET_EXIST_FACE = 0x86# QF_Error.h: 243

QF_PROTO_RET_NO_SERIAL_NUMBER = 0xA2# QF_Error.h: 243

QF_PROTO_RET_FAKE_DETECTED = 0xB0# QF_Error.h: 243

QF_PROTO_RET_INVALID_DATABASE_FORMAT = 0xB2# QF_Error.h: 243

QF_PROTO_RET_WRONG_IMAGE_FORMAT = 0xB3# QF_Error.h: 243

QF_PROTO_RET_WRONG_IMAGE_SIZE = 0XB4# QF_Error.h: 243

QF_PROTO_RET_USER_FEEDBACK = 0xB5# QF_Error.h: 243

QF_PROTOCOL_RET_CODE = enum_anon_23# QF_Error.h: 243

# QF_Packet.h: 55
if _libs["libQFM_SDK.so"].has("QF_GetPacketValue", "cdecl"):
    QF_GetPacketValue = _libs["libQFM_SDK.so"].get("QF_GetPacketValue", "cdecl")
    QF_GetPacketValue.argtypes = [c_int, POINTER(BYTE)]
    QF_GetPacketValue.restype = UINT32

# QF_Packet.h: 57
if _libs["libQFM_SDK.so"].has("QF_ReadData", "cdecl"):
    QF_ReadData = _libs["libQFM_SDK.so"].get("QF_ReadData", "cdecl")
    QF_ReadData.argtypes = [POINTER(c_ubyte), c_int, c_int]
    QF_ReadData.restype = c_int

# QF_Packet.h: 58
if _libs["libQFM_SDK.so"].has("QF_WriteData", "cdecl"):
    QF_WriteData = _libs["libQFM_SDK.so"].get("QF_WriteData", "cdecl")
    QF_WriteData.argtypes = [POINTER(c_ubyte), c_int, c_int]
    QF_WriteData.restype = c_int

# QF_Packet.h: 60
if _libs["libQFM_SDK.so"].has("QF_ClearReadBuffer", "cdecl"):
    QF_ClearReadBuffer = _libs["libQFM_SDK.so"].get("QF_ClearReadBuffer", "cdecl")
    QF_ClearReadBuffer.argtypes = []
    QF_ClearReadBuffer.restype = c_int

# QF_Packet.h: 61
if _libs["libQFM_SDK.so"].has("QF_ClearWriteBuffer", "cdecl"):
    QF_ClearWriteBuffer = _libs["libQFM_SDK.so"].get("QF_ClearWriteBuffer", "cdecl")
    QF_ClearWriteBuffer.argtypes = []
    QF_ClearWriteBuffer.restype = c_int

enum_anon_24 = c_int# QF_Command.h: 58

QF_COM_SW = 0x01# QF_Command.h: 58

QF_COM_SF = 0x02# QF_Command.h: 58

QF_COM_SR = 0x03# QF_Command.h: 58

QF_COM_SS = 0x04# QF_Command.h: 58

QF_COM_ES = 0x05# QF_Command.h: 58

QF_COM_VS = 0x08# QF_Command.h: 58

QF_COM_VT = 0x10# QF_Command.h: 58

QF_COM_IS = 0x11# QF_Command.h: 58

QF_COM_IT = 0x13# QF_Command.h: 58

QF_COM_DT = 0x16# QF_Command.h: 58

QF_COM_DA = 0x17# QF_Command.h: 58

QF_COM_CT = 0x19# QF_Command.h: 58

QF_COM_DS = 0x1E# QF_Command.h: 58

QF_COM_CS = 0x1A# QF_Command.h: 58

QF_COM_ST = 0x21# QF_Command.h: 58

QF_COM_VH = 0x22# QF_Command.h: 58

QF_COM_FP = 0x23# QF_Command.h: 58

QF_COM_DP = 0x24# QF_Command.h: 58

QF_COM_PKE = 0x2A# QF_Command.h: 58

QF_COM_KW = 0x34# QF_Command.h: 58

QF_COM_KS = 0x35# QF_Command.h: 58

QF_COM_GR = 0x36# QF_Command.h: 58

QF_COM_GW = 0x37# QF_Command.h: 58

QF_COM_GC = 0x38# QF_Command.h: 58

QF_COM_GD = 0x39# QF_Command.h: 58

QF_COM_QR = 0x51# QF_Command.h: 58

QF_COM_SC = 0x52# QF_Command.h: 58

QF_COM_CA = 0x60# QF_Command.h: 58

QF_COM_UG = 0x62# QF_Command.h: 58

QF_COM_EIX = 0x80# QF_Command.h: 58

QF_COM_IIX = 0x81# QF_Command.h: 58

QF_COM_VIX = 0x82# QF_Command.h: 58

QF_COM_SIX = 0x83# QF_Command.h: 58

QF_COM_RIX = 0x84# QF_Command.h: 58

QF_COM_LTX = 0x86# QF_Command.h: 58

QF_COM_ETX = 0x87# QF_Command.h: 58

QF_COM_RTX = 0x89# QF_Command.h: 58

QF_COM_RS = 0xD0# QF_Command.h: 58

QF_COM_LDB = 0xD3# QF_Command.h: 58

QF_COM_SDB = 0xD4# QF_Command.h: 58

QF_COM_DFU = 0xDF# QF_Command.h: 58

QF_COM_FF = 0xFF# QF_Command.h: 58

QF_COM_FR = 0xFA# QF_Command.h: 58

QF_COMMAND = enum_anon_24# QF_Command.h: 58

# QF_Command.h: 60
if _libs["libQFM_SDK.so"].has("QF_CalculateTimeout", "cdecl"):
    QF_CalculateTimeout = _libs["libQFM_SDK.so"].get("QF_CalculateTimeout", "cdecl")
    QF_CalculateTimeout.argtypes = [c_int]
    QF_CalculateTimeout.restype = c_int

# QF_SysParameter.h: 20
class struct_anon_25(Structure):
    pass

struct_anon_25.__slots__ = [
    'parameter',
    'value',
]
struct_anon_25._fields_ = [
    ('parameter', c_int),
    ('value', UINT32),
]

SysParameter = struct_anon_25# QF_SysParameter.h: 20

# QF_SysParameter.h: 23
try:
    s_SysParameter = (POINTER(SysParameter)).in_dll(_libs["libQFM_SDK.so"], "s_SysParameter")
except:
    pass

# QF_SysParameter.h: 26
try:
    s_SysParameterList = (POINTER(c_char * int(30))).in_dll(_libs["libQFM_SDK.so"], "s_SysParameterList")
except:
    pass

enum_anon_26 = c_int# QF_SysParameter.h: 148

QF_SYS_TIMEOUT = 0x62# QF_SysParameter.h: 148

QF_SYS_TEMPLATE_SIZE = 0x64# QF_SysParameter.h: 148

QF_SYS_ENROLL_MODE = 0x65# QF_SysParameter.h: 148

QF_SYS_SECURITY_LEVEL = 0x66# QF_SysParameter.h: 148

QF_SYS_ENCRYPTION_MODE = 0x67# QF_SysParameter.h: 148

QF_SYS_FIRMWARE_VERSION = 0x6e# QF_SysParameter.h: 148

QF_SYS_SERIAL_NUMBER = 0x6f# QF_SysParameter.h: 148

QF_SYS_BAUDRATE = 0x71# QF_SysParameter.h: 148

QF_SYS_ENROLLED_TEMPLATES = 0x73# QF_SysParameter.h: 148

QF_SYS_AVAILABLE_TEMPLATES = 0x74# QF_SysParameter.h: 148

QF_SYS_SEND_SCAN_SUCCESS = 0x75# QF_SysParameter.h: 148

QF_SYS_ASCII_PACKET = 0x76# QF_SysParameter.h: 148

QF_SYS_ROTATE_IMAGE = 0x77# QF_SysParameter.h: 148

QF_SYS_SENSITIVITY = 0x80# QF_SysParameter.h: 148

QF_SYS_HORIZONTAL_SENSITIVITY = 0x80# QF_SysParameter.h: 148

QF_SYS_IMAGE_QUALITY = 0x81# QF_SysParameter.h: 148

QF_SYS_AUTO_RESPONSE = 0x82# QF_SysParameter.h: 148

QF_SYS_FREE_SCAN = 0x84# QF_SysParameter.h: 148

QF_SYS_PROVISIONAL_ENROLL = 0x85# QF_SysParameter.h: 148

QF_SYS_RESPONSE_DELAY = 0x87# QF_SysParameter.h: 148

QF_SYS_MATCHING_TIMEOUT = 0x88# QF_SysParameter.h: 148

QF_SYS_BUILD_NUMBER = 0x89# QF_SysParameter.h: 148

QF_SYS_LIGHTING_CONDITION = 0x90# QF_SysParameter.h: 148

QF_SYS_FREESCAN_DELAY = 0x91# QF_SysParameter.h: 148

QF_SYS_TEMPLATE_TYPE = 0x96# QF_SysParameter.h: 148

QF_SYS_FAKE_DETECTION = 0x98# QF_SysParameter.h: 148

QF_SYS_PROTOCOL_INTERFACE = 0X9e# QF_SysParameter.h: 148

QF_SYS_KERNEL_VERSION = 0xa3# QF_SysParameter.h: 148

QF_SYS_PACKET_SECURITY = 0xa5# QF_SysParameter.h: 148

QF_SYS_MASK_CHECK_LEVEL = 0xb1# QF_SysParameter.h: 148

QF_SYS_USER_FEEDBACK = 0xb2# QF_SysParameter.h: 148

QF_SYS_VERTICAL_SENSITIVITY = 0xb3# QF_SysParameter.h: 148

QF_SYS_QFACE_ENGINE_VERSION = 0xb4# QF_SysParameter.h: 148

QF_SYS_PATCH_VERSION = 0xb5# QF_SysParameter.h: 148

QF_SYS_ENROLLMENT_RESTRICTION = 0xb6# QF_SysParameter.h: 148

QF_SYS_NUMBER_OF_USER = 0xb7# QF_SysParameter.h: 148

QF_SYS_USER_DETECTION = 0xb8# QF_SysParameter.h: 148

QF_SYS_SCREEN_ORIENTATION = 0xb9# QF_SysParameter.h: 148

QF_SYS_RESERVED = 0xff# QF_SysParameter.h: 148

QF_SYS_PARAM = enum_anon_26# QF_SysParameter.h: 148

# QF_Template.h: 30
class struct_anon_27(Structure):
    pass

struct_anon_27.__slots__ = [
    'userID',
    'numOfTemplate',
    'reserved_0',
    'reserved_1',
    'reserved_2',
]
struct_anon_27._fields_ = [
    ('userID', UINT32),
    ('numOfTemplate', BYTE),
    ('reserved_0', BYTE),
    ('reserved_1', BYTE),
    ('reserved_2', BYTE),
]

QFUserInfo = struct_anon_27# QF_Template.h: 30

# QF_Template.h: 50
class struct_anon_28(Structure):
    pass

struct_anon_28.__slots__ = [
    'userID',
    'checksum',
    'numOfTemplate',
    'templateProperty',
    'encryptionMode',
    'subID',
    'mask',
    'reserved_0',
]
struct_anon_28._fields_ = [
    ('userID', UINT32),
    ('checksum', UINT32 * int(20)),
    ('numOfTemplate', BYTE),
    ('templateProperty', BYTE, 4),
    ('encryptionMode', BYTE, 4),
    ('subID', BYTE, 4),
    ('mask', BYTE, 4),
    ('reserved_0', BYTE),
]

QFUserInfoEx = struct_anon_28# QF_Template.h: 50

# QF_Template.h: 63
if _libs["libQFM_SDK.so"].has("QF_SortByUserID", "cdecl"):
    QF_SortByUserID = _libs["libQFM_SDK.so"].get("QF_SortByUserID", "cdecl")
    QF_SortByUserID.argtypes = [POINTER(None), POINTER(None)]
    QF_SortByUserID.restype = c_int

enum_anon_29 = c_int# QF_Module.h: 14

QF_MODULE_PRO = 0# QF_Module.h: 14

QF_MODULE_UNKNOWN = (-1)# QF_Module.h: 14

QF_MODULE_TYPE = enum_anon_29# QF_Module.h: 14

enum_anon_30 = c_int# QF_Module.h: 21

QF_VERSION_0_1 = 1# QF_Module.h: 21

QF_VERSION_1_0 = 10# QF_Module.h: 21

QF_VERSION_UNKNOWN = (-1)# QF_Module.h: 21

QF_MODULE_VERSION = enum_anon_30# QF_Module.h: 21

enum_anon_31 = c_int# QF_Module.h: 27

QF_HARDWARE_REVISION_A = 0# QF_Module.h: 27

QF_HARDWARE_UNKNOWN = (-1)# QF_Module.h: 27

QF_HARDWARE_REVISION = enum_anon_31# QF_Module.h: 27

enum_anon_32 = c_int# QF_Enroll.h: 15

QF_ENROLL_MODE_ONE_SHOT = 0x30# QF_Enroll.h: 15

QF_ENROLL_MODE = enum_anon_32# QF_Enroll.h: 15

enum_anon_33 = c_int# QF_Enroll.h: 37

QF_ENROLL_OPTION_ADD_NEW = 0x71# QF_Enroll.h: 37

QF_ENROLL_OPTION_AUTO_ID = 0x79# QF_Enroll.h: 37

QF_ENROLL_OPTION_CHECK_ID = 0x70# QF_Enroll.h: 37

QF_ENROLL_OPTION_CHECK_FACE = 0x84# QF_Enroll.h: 37

QF_ENROLL_OPTION_CHECK_FACE_AUTO_ID = 0x85# QF_Enroll.h: 37

QF_ENROLL_OPTION = enum_anon_33# QF_Enroll.h: 37

# QF_Image.h: 34
class struct_anon_34(Structure):
    pass

struct_anon_34.__slots__ = [
    'length',
    'data',
]
struct_anon_34._fields_ = [
    ('length', UINT32),
    ('data', POINTER(BYTE)),
]

QFImage = struct_anon_34# QF_Image.h: 34

enum_anon_35 = c_int# QF_Serial.h: 19

QF_SINGLE_PROTOCOL = 0# QF_Serial.h: 19

QF_PROTOCOL = enum_anon_35# QF_Serial.h: 19

enum_anon_36 = c_int# QF_Serial.h: 25

QF_SERIAL_CHANNEL = 0# QF_Serial.h: 25

QF_SOCKET_CHANNEL = 1# QF_Serial.h: 25

QF_CHANNEL_TYPE = enum_anon_36# QF_Serial.h: 25

# QF_Serial.h: 31
if _libs["libQFM_SDK.so"].has("QF_ReadSerial", "cdecl"):
    QF_ReadSerial = _libs["libQFM_SDK.so"].get("QF_ReadSerial", "cdecl")
    QF_ReadSerial.argtypes = [POINTER(c_ubyte), c_int, c_int]
    QF_ReadSerial.restype = c_int

# QF_Serial.h: 32
if _libs["libQFM_SDK.so"].has("QF_WriteSerial", "cdecl"):
    QF_WriteSerial = _libs["libQFM_SDK.so"].get("QF_WriteSerial", "cdecl")
    QF_WriteSerial.argtypes = [POINTER(c_ubyte), c_int, c_int]
    QF_WriteSerial.restype = c_int

# QF_Serial.h: 33
if _libs["libQFM_SDK.so"].has("QF_OpenSerial", "cdecl"):
    QF_OpenSerial = _libs["libQFM_SDK.so"].get("QF_OpenSerial", "cdecl")
    QF_OpenSerial.argtypes = [String]
    QF_OpenSerial.restype = c_int

# QF_Serial.h: 34
if _libs["libQFM_SDK.so"].has("QF_CloseSerial", "cdecl"):
    QF_CloseSerial = _libs["libQFM_SDK.so"].get("QF_CloseSerial", "cdecl")
    QF_CloseSerial.argtypes = []
    QF_CloseSerial.restype = c_int

# QF_Serial.h: 35
if _libs["libQFM_SDK.so"].has("QF_SetupSerial", "cdecl"):
    QF_SetupSerial = _libs["libQFM_SDK.so"].get("QF_SetupSerial", "cdecl")
    QF_SetupSerial.argtypes = [c_int]
    QF_SetupSerial.restype = c_int

# QF_Serial.h: 36
if _libs["libQFM_SDK.so"].has("QF_ClearSerialReadBuffer", "cdecl"):
    QF_ClearSerialReadBuffer = _libs["libQFM_SDK.so"].get("QF_ClearSerialReadBuffer", "cdecl")
    QF_ClearSerialReadBuffer.argtypes = []
    QF_ClearSerialReadBuffer.restype = c_int

# QF_Serial.h: 37
if _libs["libQFM_SDK.so"].has("QF_ClearSerialWriteBuffer", "cdecl"):
    QF_ClearSerialWriteBuffer = _libs["libQFM_SDK.so"].get("QF_ClearSerialWriteBuffer", "cdecl")
    QF_ClearSerialWriteBuffer.argtypes = []
    QF_ClearSerialWriteBuffer.restype = c_int

# QF_Serial.h: 38
if _libs["libQFM_SDK.so"].has("QF_CancelReadSerial", "cdecl"):
    QF_CancelReadSerial = _libs["libQFM_SDK.so"].get("QF_CancelReadSerial", "cdecl")
    QF_CancelReadSerial.argtypes = []
    QF_CancelReadSerial.restype = None

# QF_Serial.h: 39
if _libs["libQFM_SDK.so"].has("QF_CancelWriteSerial", "cdecl"):
    QF_CancelWriteSerial = _libs["libQFM_SDK.so"].get("QF_CancelWriteSerial", "cdecl")
    QF_CancelWriteSerial.argtypes = []
    QF_CancelWriteSerial.restype = None

# QF_Serial.h: 40
if _libs["libQFM_SDK.so"].has("QF_GetBaudrate", "cdecl"):
    QF_GetBaudrate = _libs["libQFM_SDK.so"].get("QF_GetBaudrate", "cdecl")
    QF_GetBaudrate.argtypes = []
    QF_GetBaudrate.restype = c_int

# QF_Serial.h: 42
if _libs["libQFM_SDK.so"].has("QF_SetSerialWriteCallback", "cdecl"):
    QF_SetSerialWriteCallback = _libs["libQFM_SDK.so"].get("QF_SetSerialWriteCallback", "cdecl")
    QF_SetSerialWriteCallback.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, c_int)]
    QF_SetSerialWriteCallback.restype = None

# QF_Serial.h: 43
if _libs["libQFM_SDK.so"].has("QF_SetSerialReadCallback", "cdecl"):
    QF_SetSerialReadCallback = _libs["libQFM_SDK.so"].get("QF_SetSerialReadCallback", "cdecl")
    QF_SetSerialReadCallback.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, c_int)]
    QF_SetSerialReadCallback.restype = None

# QF_Socket.h: 17
if _libs["libQFM_SDK.so"].has("QF_ReadSocket", "cdecl"):
    QF_ReadSocket = _libs["libQFM_SDK.so"].get("QF_ReadSocket", "cdecl")
    QF_ReadSocket.argtypes = [POINTER(c_ubyte), c_int, c_int]
    QF_ReadSocket.restype = c_int

# QF_Socket.h: 18
if _libs["libQFM_SDK.so"].has("QF_WriteSocket", "cdecl"):
    QF_WriteSocket = _libs["libQFM_SDK.so"].get("QF_WriteSocket", "cdecl")
    QF_WriteSocket.argtypes = [POINTER(c_ubyte), c_int, c_int]
    QF_WriteSocket.restype = c_int

# QF_Socket.h: 20
if _libs["libQFM_SDK.so"].has("QF_SetSocketWriteCallback", "cdecl"):
    QF_SetSocketWriteCallback = _libs["libQFM_SDK.so"].get("QF_SetSocketWriteCallback", "cdecl")
    QF_SetSocketWriteCallback.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, c_int)]
    QF_SetSocketWriteCallback.restype = None

# QF_Socket.h: 21
if _libs["libQFM_SDK.so"].has("QF_SetSocketReadCallback", "cdecl"):
    QF_SetSocketReadCallback = _libs["libQFM_SDK.so"].get("QF_SetSocketReadCallback", "cdecl")
    QF_SetSocketReadCallback.argtypes = [CFUNCTYPE(None, c_int, c_int)]
    QF_SetSocketReadCallback.restype = None

# QF_Socket.h: 23
if _libs["libQFM_SDK.so"].has("QF_ClearSocketReadBuffer", "cdecl"):
    QF_ClearSocketReadBuffer = _libs["libQFM_SDK.so"].get("QF_ClearSocketReadBuffer", "cdecl")
    QF_ClearSocketReadBuffer.argtypes = []
    QF_ClearSocketReadBuffer.restype = c_int

# QF_Socket.h: 24
if _libs["libQFM_SDK.so"].has("QF_ClearSocketWriteBuffer", "cdecl"):
    QF_ClearSocketWriteBuffer = _libs["libQFM_SDK.so"].get("QF_ClearSocketWriteBuffer", "cdecl")
    QF_ClearSocketWriteBuffer.argtypes = []
    QF_ClearSocketWriteBuffer.restype = c_int

enum_anon_37 = c_int# QF_UserFeedback.h: 28

QF_USER_FEEDBACK_FACE_DETECTED = 0x0# QF_UserFeedback.h: 28

QF_USER_FEEDBACK_LOOK_AT_THE_CAMERA_CORRECTLY = 0x1# QF_UserFeedback.h: 28

QF_USER_FEEDBACK_TURN_YOUR_HEAD_RIGHT = 0x2# QF_UserFeedback.h: 28

QF_USER_FEEDBACK_TURN_YOUR_HEAD_LEFT = 0x3# QF_UserFeedback.h: 28

QF_USER_FEEDBACK_TURN_YOUR_HEAD_UP = 0x4# QF_UserFeedback.h: 28

QF_USER_FEEDBACK_TURN_YOUR_HEAD_DOWN = 0x5# QF_UserFeedback.h: 28

QF_USER_FEEDBACK_MOVE_FORWARD = 0x6# QF_UserFeedback.h: 28

QF_USER_FEEDBACK_MOVE_BACKWARD = 0x7# QF_UserFeedback.h: 28

QF_USER_FEEDBACK_OUT_OF_ENROLLMENT_AREA = 0xA# QF_UserFeedback.h: 28

QF_USER_FEEDBACK_FACE_NOT_DETECTED = 0xFF# QF_UserFeedback.h: 28

QF_USER_FEEDBACK = enum_anon_37# QF_UserFeedback.h: 28

enum_anon_38 = c_int# QF_UserFeedback.h: 38

USER_FEEDBACK_TYPE_MESSAGE_CODE = (1 << 0)# QF_UserFeedback.h: 38

USER_FEEDBACK_TYPE_HEAD_POSITION = (1 << 1)# QF_UserFeedback.h: 38

UserFeedbackType = enum_anon_38# QF_UserFeedback.h: 38

# QF_UserFeedback.h: 47
class struct_anon_39(Structure):
    pass

struct_anon_39.__slots__ = [
    'topLeftX',
    'topLeftY',
    'bottomRightX',
    'bottomRightY',
]
struct_anon_39._fields_ = [
    ('topLeftX', c_int),
    ('topLeftY', c_int),
    ('bottomRightX', c_int),
    ('bottomRightY', c_int),
]

# QF_UserFeedback.h: 51
class struct_anon_40(Structure):
    pass

struct_anon_40.__slots__ = [
    'fields',
    'messageCode',
    'headPosition',
]
struct_anon_40._fields_ = [
    ('fields', c_int),
    ('messageCode', c_int),
    ('headPosition', struct_anon_39),
]

UserFeedbackData = struct_anon_40# QF_UserFeedback.h: 51

enum_anon_41 = c_int# QF_Key.h: 56

QF_KEY_OPTION_SET_ENCRYPTION_KEY = 0xC1# QF_Key.h: 56

QF_KEY_OPTION_SET_INITIALIZATION_VECTOR = 0xC2# QF_Key.h: 56

QF_KEY_OPTION_SET_SECURE_KEY = 0xC3# QF_Key.h: 56

QF_KEY_OPTION_SET_ENCRYPTION_KEY_WITH_VERIFICATION = 0xC4# QF_Key.h: 56

QF_KEY_OPTION_SET_INITIALIZATION_VECTOR_WITH_VERIFICATION = 0xC5# QF_Key.h: 56

QF_KEY_OPTION_SET_SECURE_KEY_WITH_VERIFICATION = 0xC6# QF_Key.h: 56

QF_KEY_OPTION_RESET_INITIALIZATION_VECTOR = 0xCA# QF_Key.h: 56

QF_KEY_OPTION_RESET_SECURE_KEY = 0xCB# QF_Key.h: 56

QF_KEY_OPTION_RESET_ENCRYPTION_KEY = 0xCC# QF_Key.h: 56

QF_KEY_OPTION = enum_anon_41# QF_Key.h: 56

enum_anon_42 = c_int# QF_Key.h: 62

QF_KEY_EXCHANGE_OPTION_SET_PUBLIC_KEY = 0xCD# QF_Key.h: 62

QF_KEY_EXCHANGE_OPTION_GET_PUBLIC_KEY = 0xCE# QF_Key.h: 62

QF_KEY_EXCHANGE_OPTION = enum_anon_42# QF_Key.h: 62

# QF_API.h: 40
if _libs["libQFM_SDK.so"].has("QF_GetSDKVersion", "cdecl"):
    QF_GetSDKVersion = _libs["libQFM_SDK.so"].get("QF_GetSDKVersion", "cdecl")
    QF_GetSDKVersion.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    QF_GetSDKVersion.restype = None

# QF_API.h: 41
if _libs["libQFM_SDK.so"].has("QF_GetSDKVersionString", "cdecl"):
    QF_GetSDKVersionString = _libs["libQFM_SDK.so"].get("QF_GetSDKVersionString", "cdecl")
    QF_GetSDKVersionString.argtypes = []
    QF_GetSDKVersionString.restype = c_char_p

# QF_API.h: 46
if _libs["libQFM_SDK.so"].has("QF_InitCommPort", "cdecl"):
    QF_InitCommPort = _libs["libQFM_SDK.so"].get("QF_InitCommPort", "cdecl")
    QF_InitCommPort.argtypes = [String, c_int, BOOL]
    QF_InitCommPort.restype = QF_RET_CODE

# QF_API.h: 47
if _libs["libQFM_SDK.so"].has("QF_CloseCommPort", "cdecl"):
    QF_CloseCommPort = _libs["libQFM_SDK.so"].get("QF_CloseCommPort", "cdecl")
    QF_CloseCommPort.argtypes = []
    QF_CloseCommPort.restype = QF_RET_CODE

# QF_API.h: 48
if _libs["libQFM_SDK.so"].has("QF_Reconnect", "cdecl"):
    QF_Reconnect = _libs["libQFM_SDK.so"].get("QF_Reconnect", "cdecl")
    QF_Reconnect.argtypes = []
    QF_Reconnect.restype = None

# QF_API.h: 49
if _libs["libQFM_SDK.so"].has("QF_SetBaudrate", "cdecl"):
    QF_SetBaudrate = _libs["libQFM_SDK.so"].get("QF_SetBaudrate", "cdecl")
    QF_SetBaudrate.argtypes = [c_int]
    QF_SetBaudrate.restype = QF_RET_CODE

# QF_API.h: 50
if _libs["libQFM_SDK.so"].has("QF_SetAsciiMode", "cdecl"):
    QF_SetAsciiMode = _libs["libQFM_SDK.so"].get("QF_SetAsciiMode", "cdecl")
    QF_SetAsciiMode.argtypes = [BOOL]
    QF_SetAsciiMode.restype = None

# QF_API.h: 51
if _libs["libQFM_SDK.so"].has("QF_InitSocket", "cdecl"):
    QF_InitSocket = _libs["libQFM_SDK.so"].get("QF_InitSocket", "cdecl")
    QF_InitSocket.argtypes = [String, c_int, BOOL]
    QF_InitSocket.restype = QF_RET_CODE

# QF_API.h: 52
if _libs["libQFM_SDK.so"].has("QF_CloseSocket", "cdecl"):
    QF_CloseSocket = _libs["libQFM_SDK.so"].get("QF_CloseSocket", "cdecl")
    QF_CloseSocket.argtypes = []
    QF_CloseSocket.restype = QF_RET_CODE

# QF_API.h: 53
if _libs["libQFM_SDK.so"].has("QF_SetInitSocketTimeout", "cdecl"):
    QF_SetInitSocketTimeout = _libs["libQFM_SDK.so"].get("QF_SetInitSocketTimeout", "cdecl")
    QF_SetInitSocketTimeout.argtypes = [c_int]
    QF_SetInitSocketTimeout.restype = QF_RET_CODE

# QF_API.h: 61
if _libs["libQFM_SDK.so"].has("QF_SetSetupSerialCallback", "cdecl"):
    QF_SetSetupSerialCallback = _libs["libQFM_SDK.so"].get("QF_SetSetupSerialCallback", "cdecl")
    QF_SetSetupSerialCallback.argtypes = [CFUNCTYPE(None, c_int)]
    QF_SetSetupSerialCallback.restype = None

# QF_API.h: 63
if _libs["libQFM_SDK.so"].has("QF_SetReadSerialCallback", "cdecl"):
    QF_SetReadSerialCallback = _libs["libQFM_SDK.so"].get("QF_SetReadSerialCallback", "cdecl")
    QF_SetReadSerialCallback.argtypes = [CFUNCTYPE(None, POINTER(BYTE), c_int, c_int)]
    QF_SetReadSerialCallback.restype = None

# QF_API.h: 65
if _libs["libQFM_SDK.so"].has("QF_SetWriteSerialCallback", "cdecl"):
    QF_SetWriteSerialCallback = _libs["libQFM_SDK.so"].get("QF_SetWriteSerialCallback", "cdecl")
    QF_SetWriteSerialCallback.argtypes = [CFUNCTYPE(None, POINTER(BYTE), c_int, c_int)]
    QF_SetWriteSerialCallback.restype = None

# QF_API.h: 70
if _libs["libQFM_SDK.so"].has("QF_SendPacket", "cdecl"):
    QF_SendPacket = _libs["libQFM_SDK.so"].get("QF_SendPacket", "cdecl")
    QF_SendPacket.argtypes = [BYTE, UINT32, UINT32, BYTE, c_int]
    QF_SendPacket.restype = QF_RET_CODE

# QF_API.h: 71
if _libs["libQFM_SDK.so"].has("QF_ReceivePacket", "cdecl"):
    QF_ReceivePacket = _libs["libQFM_SDK.so"].get("QF_ReceivePacket", "cdecl")
    QF_ReceivePacket.argtypes = [POINTER(BYTE), c_int]
    QF_ReceivePacket.restype = QF_RET_CODE

# QF_API.h: 72
if _libs["libQFM_SDK.so"].has("QF_SendRawData", "cdecl"):
    QF_SendRawData = _libs["libQFM_SDK.so"].get("QF_SendRawData", "cdecl")
    QF_SendRawData.argtypes = [POINTER(BYTE), UINT32, c_int]
    QF_SendRawData.restype = QF_RET_CODE

# QF_API.h: 73
if _libs["libQFM_SDK.so"].has("QF_ReceiveRawData", "cdecl"):
    QF_ReceiveRawData = _libs["libQFM_SDK.so"].get("QF_ReceiveRawData", "cdecl")
    QF_ReceiveRawData.argtypes = [POINTER(BYTE), UINT32, c_int, BOOL]
    QF_ReceiveRawData.restype = QF_RET_CODE

# QF_API.h: 74
if _libs["libQFM_SDK.so"].has("QF_SendDataPacket", "cdecl"):
    QF_SendDataPacket = _libs["libQFM_SDK.so"].get("QF_SendDataPacket", "cdecl")
    QF_SendDataPacket.argtypes = [BYTE, POINTER(BYTE), UINT32, UINT32]
    QF_SendDataPacket.restype = QF_RET_CODE

# QF_API.h: 75
if _libs["libQFM_SDK.so"].has("QF_ReceiveDataPacket", "cdecl"):
    QF_ReceiveDataPacket = _libs["libQFM_SDK.so"].get("QF_ReceiveDataPacket", "cdecl")
    QF_ReceiveDataPacket.argtypes = [BYTE, POINTER(BYTE), UINT32]
    QF_ReceiveDataPacket.restype = QF_RET_CODE

# QF_API.h: 76
if _libs["libQFM_SDK.so"].has("QF_SetSendPacketCallback", "cdecl"):
    QF_SetSendPacketCallback = _libs["libQFM_SDK.so"].get("QF_SetSendPacketCallback", "cdecl")
    QF_SetSendPacketCallback.argtypes = [CFUNCTYPE(None, POINTER(BYTE))]
    QF_SetSendPacketCallback.restype = None

# QF_API.h: 77
if _libs["libQFM_SDK.so"].has("QF_SetReceivePacketCallback", "cdecl"):
    QF_SetReceivePacketCallback = _libs["libQFM_SDK.so"].get("QF_SetReceivePacketCallback", "cdecl")
    QF_SetReceivePacketCallback.argtypes = [CFUNCTYPE(None, POINTER(BYTE))]
    QF_SetReceivePacketCallback.restype = None

# QF_API.h: 78
if _libs["libQFM_SDK.so"].has("QF_SetSendDataPacketCallback", "cdecl"):
    QF_SetSendDataPacketCallback = _libs["libQFM_SDK.so"].get("QF_SetSendDataPacketCallback", "cdecl")
    QF_SetSendDataPacketCallback.argtypes = [CFUNCTYPE(None, c_int, c_int)]
    QF_SetSendDataPacketCallback.restype = None

# QF_API.h: 79
if _libs["libQFM_SDK.so"].has("QF_SetReceiveDataPacketCallback", "cdecl"):
    QF_SetReceiveDataPacketCallback = _libs["libQFM_SDK.so"].get("QF_SetReceiveDataPacketCallback", "cdecl")
    QF_SetReceiveDataPacketCallback.argtypes = [CFUNCTYPE(None, c_int, c_int)]
    QF_SetReceiveDataPacketCallback.restype = None

# QF_API.h: 80
if _libs["libQFM_SDK.so"].has("QF_SetSendRawDataCallback", "cdecl"):
    QF_SetSendRawDataCallback = _libs["libQFM_SDK.so"].get("QF_SetSendRawDataCallback", "cdecl")
    QF_SetSendRawDataCallback.argtypes = [CFUNCTYPE(None, c_int, c_int)]
    QF_SetSendRawDataCallback.restype = None

# QF_API.h: 81
if _libs["libQFM_SDK.so"].has("QF_SetReceiveRawDataCallback", "cdecl"):
    QF_SetReceiveRawDataCallback = _libs["libQFM_SDK.so"].get("QF_SetReceiveRawDataCallback", "cdecl")
    QF_SetReceiveRawDataCallback.argtypes = [CFUNCTYPE(None, c_int, c_int)]
    QF_SetReceiveRawDataCallback.restype = None

# QF_API.h: 82
if _libs["libQFM_SDK.so"].has("QF_SetDefaultPacketSize", "cdecl"):
    QF_SetDefaultPacketSize = _libs["libQFM_SDK.so"].get("QF_SetDefaultPacketSize", "cdecl")
    QF_SetDefaultPacketSize.argtypes = [c_int]
    QF_SetDefaultPacketSize.restype = None

# QF_API.h: 83
if _libs["libQFM_SDK.so"].has("QF_GetDefaultPacketSize", "cdecl"):
    QF_GetDefaultPacketSize = _libs["libQFM_SDK.so"].get("QF_GetDefaultPacketSize", "cdecl")
    QF_GetDefaultPacketSize.argtypes = []
    QF_GetDefaultPacketSize.restype = c_int

# QF_API.h: 88
if _libs["libQFM_SDK.so"].has("QF_Command", "cdecl"):
    QF_Command = _libs["libQFM_SDK.so"].get("QF_Command", "cdecl")
    QF_Command.argtypes = [BYTE, POINTER(UINT32), POINTER(UINT32), POINTER(BYTE)]
    QF_Command.restype = QF_RET_CODE

# QF_API.h: 89
if _libs["libQFM_SDK.so"].has("QF_CommandEx", "cdecl"):
    QF_CommandEx = _libs["libQFM_SDK.so"].get("QF_CommandEx", "cdecl")
    QF_CommandEx.argtypes = [BYTE, POINTER(UINT32), POINTER(UINT32), POINTER(BYTE), CFUNCTYPE(BOOL, BYTE)]
    QF_CommandEx.restype = QF_RET_CODE

# QF_API.h: 90
if _libs["libQFM_SDK.so"].has("QF_CommandSendData", "cdecl"):
    QF_CommandSendData = _libs["libQFM_SDK.so"].get("QF_CommandSendData", "cdecl")
    QF_CommandSendData.argtypes = [BYTE, POINTER(UINT32), POINTER(UINT32), POINTER(BYTE), POINTER(BYTE), UINT32]
    QF_CommandSendData.restype = QF_RET_CODE

# QF_API.h: 91
if _libs["libQFM_SDK.so"].has("QF_CommandSendDataEx", "cdecl"):
    QF_CommandSendDataEx = _libs["libQFM_SDK.so"].get("QF_CommandSendDataEx", "cdecl")
    QF_CommandSendDataEx.argtypes = [BYTE, POINTER(UINT32), POINTER(UINT32), POINTER(BYTE), POINTER(BYTE), UINT32, CFUNCTYPE(BOOL, BYTE), BOOL]
    QF_CommandSendDataEx.restype = QF_RET_CODE

# QF_API.h: 92
if _libs["libQFM_SDK.so"].has("QF_Cancel", "cdecl"):
    QF_Cancel = _libs["libQFM_SDK.so"].get("QF_Cancel", "cdecl")
    QF_Cancel.argtypes = [BOOL]
    QF_Cancel.restype = QF_RET_CODE

# QF_API.h: 93
if _libs["libQFM_SDK.so"].has("QF_SetGenericCommandTimeout", "cdecl"):
    QF_SetGenericCommandTimeout = _libs["libQFM_SDK.so"].get("QF_SetGenericCommandTimeout", "cdecl")
    QF_SetGenericCommandTimeout.argtypes = [c_int]
    QF_SetGenericCommandTimeout.restype = None

# QF_API.h: 94
if _libs["libQFM_SDK.so"].has("QF_SetInputCommandTimeout", "cdecl"):
    QF_SetInputCommandTimeout = _libs["libQFM_SDK.so"].get("QF_SetInputCommandTimeout", "cdecl")
    QF_SetInputCommandTimeout.argtypes = [c_int]
    QF_SetInputCommandTimeout.restype = None

# QF_API.h: 95
if _libs["libQFM_SDK.so"].has("QF_GetGenericCommandTimeout", "cdecl"):
    QF_GetGenericCommandTimeout = _libs["libQFM_SDK.so"].get("QF_GetGenericCommandTimeout", "cdecl")
    QF_GetGenericCommandTimeout.argtypes = []
    QF_GetGenericCommandTimeout.restype = c_int

# QF_API.h: 96
if _libs["libQFM_SDK.so"].has("QF_GetInputCommandTimeout", "cdecl"):
    QF_GetInputCommandTimeout = _libs["libQFM_SDK.so"].get("QF_GetInputCommandTimeout", "cdecl")
    QF_GetInputCommandTimeout.argtypes = []
    QF_GetInputCommandTimeout.restype = c_int

# QF_API.h: 97
if _libs["libQFM_SDK.so"].has("QF_GetErrorCode", "cdecl"):
    QF_GetErrorCode = _libs["libQFM_SDK.so"].get("QF_GetErrorCode", "cdecl")
    QF_GetErrorCode.argtypes = [QF_PROTOCOL_RET_CODE]
    QF_GetErrorCode.restype = QF_RET_CODE

# QF_API.h: 102
if _libs["libQFM_SDK.so"].has("QF_GetModuleInfo", "cdecl"):
    QF_GetModuleInfo = _libs["libQFM_SDK.so"].get("QF_GetModuleInfo", "cdecl")
    QF_GetModuleInfo.argtypes = [POINTER(QF_MODULE_TYPE), POINTER(QF_MODULE_VERSION), POINTER(QF_HARDWARE_REVISION)]
    QF_GetModuleInfo.restype = QF_RET_CODE

# QF_API.h: 103
if _libs["libQFM_SDK.so"].has("QF_GetModuleString", "cdecl"):
    QF_GetModuleString = _libs["libQFM_SDK.so"].get("QF_GetModuleString", "cdecl")
    QF_GetModuleString.argtypes = [QF_MODULE_TYPE, QF_MODULE_VERSION, QF_HARDWARE_REVISION]
    QF_GetModuleString.restype = c_char_p

# QF_API.h: 104
if _libs["libQFM_SDK.so"].has("QF_GetModuleString2", "cdecl"):
    QF_GetModuleString2 = _libs["libQFM_SDK.so"].get("QF_GetModuleString2", "cdecl")
    QF_GetModuleString2.argtypes = []
    QF_GetModuleString2.restype = c_char_p

# QF_API.h: 105
if _libs["libQFM_SDK.so"].has("QF_SearchModule", "cdecl"):
    QF_SearchModule = _libs["libQFM_SDK.so"].get("QF_SearchModule", "cdecl")
    QF_SearchModule.argtypes = [String, POINTER(c_int), POINTER(BOOL), POINTER(QF_PROTOCOL), POINTER(UINT32), CFUNCTYPE(UNCHECKED(None), String, c_int)]
    QF_SearchModule.restype = QF_RET_CODE

# QF_API.h: 106
if _libs["libQFM_SDK.so"].has("QF_SearchModuleBySocket", "cdecl"):
    QF_SearchModuleBySocket = _libs["libQFM_SDK.so"].get("QF_SearchModuleBySocket", "cdecl")
    QF_SearchModuleBySocket.argtypes = [String, c_int, POINTER(BOOL), POINTER(QF_PROTOCOL), POINTER(UINT32)]
    QF_SearchModuleBySocket.restype = QF_RET_CODE

# QF_API.h: 107
if _libs["libQFM_SDK.so"].has("QF_Upgrade", "cdecl"):
    QF_Upgrade = _libs["libQFM_SDK.so"].get("QF_Upgrade", "cdecl")
    QF_Upgrade.argtypes = [String, c_int]
    QF_Upgrade.restype = QF_RET_CODE

# QF_API.h: 108
if _libs["libQFM_SDK.so"].has("QF_UpdatePatch", "cdecl"):
    QF_UpdatePatch = _libs["libQFM_SDK.so"].get("QF_UpdatePatch", "cdecl")
    QF_UpdatePatch.argtypes = [String, c_int]
    QF_UpdatePatch.restype = QF_RET_CODE

# QF_API.h: 109
if _libs["libQFM_SDK.so"].has("QF_Reset", "cdecl"):
    QF_Reset = _libs["libQFM_SDK.so"].get("QF_Reset", "cdecl")
    QF_Reset.argtypes = []
    QF_Reset.restype = QF_RET_CODE

# QF_API.h: 110
if _libs["libQFM_SDK.so"].has("QF_GetFirmwareVersion", "cdecl"):
    QF_GetFirmwareVersion = _libs["libQFM_SDK.so"].get("QF_GetFirmwareVersion", "cdecl")
    QF_GetFirmwareVersion.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    QF_GetFirmwareVersion.restype = QF_RET_CODE

# QF_API.h: 111
if _libs["libQFM_SDK.so"].has("QF_GetPatchVersion", "cdecl"):
    QF_GetPatchVersion = _libs["libQFM_SDK.so"].get("QF_GetPatchVersion", "cdecl")
    QF_GetPatchVersion.argtypes = [POINTER(c_int)]
    QF_GetPatchVersion.restype = QF_RET_CODE

# QF_API.h: 112
if _libs["libQFM_SDK.so"].has("QF_EnterDFUMode", "cdecl"):
    QF_EnterDFUMode = _libs["libQFM_SDK.so"].get("QF_EnterDFUMode", "cdecl")
    QF_EnterDFUMode.argtypes = []
    QF_EnterDFUMode.restype = QF_RET_CODE

# QF_API.h: 117
if _libs["libQFM_SDK.so"].has("QF_InitSysParameter", "cdecl"):
    QF_InitSysParameter = _libs["libQFM_SDK.so"].get("QF_InitSysParameter", "cdecl")
    QF_InitSysParameter.argtypes = []
    QF_InitSysParameter.restype = None

# QF_API.h: 118
if _libs["libQFM_SDK.so"].has("QF_GetSysParameter", "cdecl"):
    QF_GetSysParameter = _libs["libQFM_SDK.so"].get("QF_GetSysParameter", "cdecl")
    QF_GetSysParameter.argtypes = [QF_SYS_PARAM, POINTER(UINT32)]
    QF_GetSysParameter.restype = QF_RET_CODE

# QF_API.h: 119
if _libs["libQFM_SDK.so"].has("QF_SetSysParameter", "cdecl"):
    QF_SetSysParameter = _libs["libQFM_SDK.so"].get("QF_SetSysParameter", "cdecl")
    QF_SetSysParameter.argtypes = [QF_SYS_PARAM, UINT32]
    QF_SetSysParameter.restype = QF_RET_CODE

# QF_API.h: 120
if _libs["libQFM_SDK.so"].has("QF_GetMultiSysParameter", "cdecl"):
    QF_GetMultiSysParameter = _libs["libQFM_SDK.so"].get("QF_GetMultiSysParameter", "cdecl")
    QF_GetMultiSysParameter.argtypes = [c_int, POINTER(QF_SYS_PARAM), POINTER(UINT32)]
    QF_GetMultiSysParameter.restype = QF_RET_CODE

# QF_API.h: 121
if _libs["libQFM_SDK.so"].has("QF_SetMultiSysParameter", "cdecl"):
    QF_SetMultiSysParameter = _libs["libQFM_SDK.so"].get("QF_SetMultiSysParameter", "cdecl")
    QF_SetMultiSysParameter.argtypes = [c_int, POINTER(QF_SYS_PARAM), POINTER(UINT32)]
    QF_SetMultiSysParameter.restype = QF_RET_CODE

# QF_API.h: 122
if _libs["libQFM_SDK.so"].has("QF_Save", "cdecl"):
    QF_Save = _libs["libQFM_SDK.so"].get("QF_Save", "cdecl")
    QF_Save.argtypes = []
    QF_Save.restype = QF_RET_CODE

# QF_API.h: 123
if _libs["libQFM_SDK.so"].has("QF_ResetSysParameters", "cdecl"):
    QF_ResetSysParameters = _libs["libQFM_SDK.so"].get("QF_ResetSysParameters", "cdecl")
    QF_ResetSysParameters.argtypes = []
    QF_ResetSysParameters.restype = QF_RET_CODE

# QF_API.h: 128
if _libs["libQFM_SDK.so"].has("QF_GetNumOfTemplate", "cdecl"):
    QF_GetNumOfTemplate = _libs["libQFM_SDK.so"].get("QF_GetNumOfTemplate", "cdecl")
    QF_GetNumOfTemplate.argtypes = [POINTER(UINT32)]
    QF_GetNumOfTemplate.restype = QF_RET_CODE

# QF_API.h: 129
if _libs["libQFM_SDK.so"].has("QF_GetMaxNumOfTemplate", "cdecl"):
    QF_GetMaxNumOfTemplate = _libs["libQFM_SDK.so"].get("QF_GetMaxNumOfTemplate", "cdecl")
    QF_GetMaxNumOfTemplate.argtypes = [POINTER(UINT32)]
    QF_GetMaxNumOfTemplate.restype = QF_RET_CODE

# QF_API.h: 130
if _libs["libQFM_SDK.so"].has("QF_GetAllUserInfo", "cdecl"):
    QF_GetAllUserInfo = _libs["libQFM_SDK.so"].get("QF_GetAllUserInfo", "cdecl")
    QF_GetAllUserInfo.argtypes = [POINTER(QFUserInfo), POINTER(UINT32), POINTER(UINT32)]
    QF_GetAllUserInfo.restype = QF_RET_CODE

# QF_API.h: 131
if _libs["libQFM_SDK.so"].has("QF_GetAllUserInfoEx", "cdecl"):
    QF_GetAllUserInfoEx = _libs["libQFM_SDK.so"].get("QF_GetAllUserInfoEx", "cdecl")
    QF_GetAllUserInfoEx.argtypes = [POINTER(QFUserInfoEx), POINTER(UINT32), POINTER(UINT32)]
    QF_GetAllUserInfoEx.restype = QF_RET_CODE

# QF_API.h: 132
if _libs["libQFM_SDK.so"].has("QF_SortUserInfo", "cdecl"):
    QF_SortUserInfo = _libs["libQFM_SDK.so"].get("QF_SortUserInfo", "cdecl")
    QF_SortUserInfo.argtypes = [POINTER(QFUserInfo), c_int]
    QF_SortUserInfo.restype = None

# QF_API.h: 133
if _libs["libQFM_SDK.so"].has("QF_SetUserInfoCallback", "cdecl"):
    QF_SetUserInfoCallback = _libs["libQFM_SDK.so"].get("QF_SetUserInfoCallback", "cdecl")
    QF_SetUserInfoCallback.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, c_int)]
    QF_SetUserInfoCallback.restype = None

# QF_API.h: 134
if _libs["libQFM_SDK.so"].has("QF_CheckTemplate", "cdecl"):
    QF_CheckTemplate = _libs["libQFM_SDK.so"].get("QF_CheckTemplate", "cdecl")
    QF_CheckTemplate.argtypes = [UINT32, POINTER(UINT32)]
    QF_CheckTemplate.restype = QF_RET_CODE

# QF_API.h: 135
if _libs["libQFM_SDK.so"].has("QF_CheckTemplate2", "cdecl"):
    QF_CheckTemplate2 = _libs["libQFM_SDK.so"].get("QF_CheckTemplate2", "cdecl")
    QF_CheckTemplate2.argtypes = [POINTER(BYTE), POINTER(UINT32)]
    QF_CheckTemplate2.restype = QF_RET_CODE

# QF_API.h: 136
if _libs["libQFM_SDK.so"].has("QF_ReadTemplate", "cdecl"):
    QF_ReadTemplate = _libs["libQFM_SDK.so"].get("QF_ReadTemplate", "cdecl")
    QF_ReadTemplate.argtypes = [UINT32, POINTER(UINT32), POINTER(BYTE)]
    QF_ReadTemplate.restype = QF_RET_CODE

# QF_API.h: 137
if _libs["libQFM_SDK.so"].has("QF_ReadOneTemplate", "cdecl"):
    QF_ReadOneTemplate = _libs["libQFM_SDK.so"].get("QF_ReadOneTemplate", "cdecl")
    QF_ReadOneTemplate.argtypes = [UINT32, c_int, POINTER(BYTE)]
    QF_ReadOneTemplate.restype = QF_RET_CODE

# QF_API.h: 138
if _libs["libQFM_SDK.so"].has("QF_SetScanCallback", "cdecl"):
    QF_SetScanCallback = _libs["libQFM_SDK.so"].get("QF_SetScanCallback", "cdecl")
    QF_SetScanCallback.argtypes = [CFUNCTYPE(None, BYTE)]
    QF_SetScanCallback.restype = None

# QF_API.h: 139
if _libs["libQFM_SDK.so"].has("QF_ScanTemplate", "cdecl"):
    QF_ScanTemplate = _libs["libQFM_SDK.so"].get("QF_ScanTemplate", "cdecl")
    QF_ScanTemplate.argtypes = [POINTER(BYTE), POINTER(UINT32), POINTER(UINT32)]
    QF_ScanTemplate.restype = QF_RET_CODE

# QF_API.h: 140
if _libs["libQFM_SDK.so"].has("QF_SaveDB", "cdecl"):
    QF_SaveDB = _libs["libQFM_SDK.so"].get("QF_SaveDB", "cdecl")
    QF_SaveDB.argtypes = [String]
    QF_SaveDB.restype = QF_RET_CODE

# QF_API.h: 141
if _libs["libQFM_SDK.so"].has("QF_LoadDB", "cdecl"):
    QF_LoadDB = _libs["libQFM_SDK.so"].get("QF_LoadDB", "cdecl")
    QF_LoadDB.argtypes = [String]
    QF_LoadDB.restype = QF_RET_CODE

# QF_API.h: 142
if _libs["libQFM_SDK.so"].has("QF_ResetDB", "cdecl"):
    QF_ResetDB = _libs["libQFM_SDK.so"].get("QF_ResetDB", "cdecl")
    QF_ResetDB.argtypes = []
    QF_ResetDB.restype = QF_RET_CODE

# QF_API.h: 143
if _libs["libQFM_SDK.so"].has("QF_GetNumOfUser", "cdecl"):
    QF_GetNumOfUser = _libs["libQFM_SDK.so"].get("QF_GetNumOfUser", "cdecl")
    QF_GetNumOfUser.argtypes = [POINTER(UINT32)]
    QF_GetNumOfUser.restype = QF_RET_CODE

# QF_API.h: 148
if _libs["libQFM_SDK.so"].has("QF_ReadImage", "cdecl"):
    QF_ReadImage = _libs["libQFM_SDK.so"].get("QF_ReadImage", "cdecl")
    QF_ReadImage.argtypes = [POINTER(QFImage)]
    QF_ReadImage.restype = QF_RET_CODE

# QF_API.h: 149
if _libs["libQFM_SDK.so"].has("QF_ScanImage", "cdecl"):
    QF_ScanImage = _libs["libQFM_SDK.so"].get("QF_ScanImage", "cdecl")
    QF_ScanImage.argtypes = [POINTER(QFImage)]
    QF_ScanImage.restype = QF_RET_CODE

# QF_API.h: 150
if _libs["libQFM_SDK.so"].has("QF_SaveImage", "cdecl"):
    QF_SaveImage = _libs["libQFM_SDK.so"].get("QF_SaveImage", "cdecl")
    QF_SaveImage.argtypes = [String, POINTER(QFImage)]
    QF_SaveImage.restype = QF_RET_CODE

# QF_API.h: 151
if _libs["libQFM_SDK.so"].has("QF_ReleaseImage", "cdecl"):
    QF_ReleaseImage = _libs["libQFM_SDK.so"].get("QF_ReleaseImage", "cdecl")
    QF_ReleaseImage.argtypes = [POINTER(QFImage)]
    QF_ReleaseImage.restype = QF_RET_CODE

# QF_API.h: 160
if _libs["libQFM_SDK.so"].has("QF_SetUserFeedbackCallback", "cdecl"):
    QF_SetUserFeedbackCallback = _libs["libQFM_SDK.so"].get("QF_SetUserFeedbackCallback", "cdecl")
    QF_SetUserFeedbackCallback.argtypes = [CFUNCTYPE(None, UINT32)]
    QF_SetUserFeedbackCallback.restype = None

# QF_API.h: 161
if _libs["libQFM_SDK.so"].has("QF_SetUserFeedbackDataCallback", "cdecl"):
    QF_SetUserFeedbackDataCallback = _libs["libQFM_SDK.so"].get("QF_SetUserFeedbackDataCallback", "cdecl")
    QF_SetUserFeedbackDataCallback.argtypes = [CFUNCTYPE(None, UserFeedbackData, c_void_p), c_void_p]
    QF_SetUserFeedbackDataCallback.restype = None

# QF_API.h: 166
if _libs["libQFM_SDK.so"].has("QF_Identify", "cdecl"):
    QF_Identify = _libs["libQFM_SDK.so"].get("QF_Identify", "cdecl")
    QF_Identify.argtypes = [POINTER(UINT32), POINTER(BYTE)]
    QF_Identify.restype = QF_RET_CODE

# QF_API.h: 167
if _libs["libQFM_SDK.so"].has("QF_IdentifyTemplate", "cdecl"):
    QF_IdentifyTemplate = _libs["libQFM_SDK.so"].get("QF_IdentifyTemplate", "cdecl")
    QF_IdentifyTemplate.argtypes = [UINT32, POINTER(BYTE), POINTER(UINT32), POINTER(BYTE)]
    QF_IdentifyTemplate.restype = QF_RET_CODE

# QF_API.h: 168
if _libs["libQFM_SDK.so"].has("QF_IdentifyImage", "cdecl"):
    QF_IdentifyImage = _libs["libQFM_SDK.so"].get("QF_IdentifyImage", "cdecl")
    QF_IdentifyImage.argtypes = [UINT32, POINTER(BYTE), POINTER(UINT32), POINTER(BYTE)]
    QF_IdentifyImage.restype = QF_RET_CODE

# QF_API.h: 169
if _libs["libQFM_SDK.so"].has("QF_SetIdentifyCallback", "cdecl"):
    QF_SetIdentifyCallback = _libs["libQFM_SDK.so"].get("QF_SetIdentifyCallback", "cdecl")
    QF_SetIdentifyCallback.argtypes = [CFUNCTYPE(UNCHECKED(None), BYTE)]
    QF_SetIdentifyCallback.restype = None

# QF_API.h: 174
if _libs["libQFM_SDK.so"].has("QF_Verify", "cdecl"):
    QF_Verify = _libs["libQFM_SDK.so"].get("QF_Verify", "cdecl")
    QF_Verify.argtypes = [UINT32, POINTER(BYTE)]
    QF_Verify.restype = QF_RET_CODE

# QF_API.h: 175
if _libs["libQFM_SDK.so"].has("QF_VerifyTemplate", "cdecl"):
    QF_VerifyTemplate = _libs["libQFM_SDK.so"].get("QF_VerifyTemplate", "cdecl")
    QF_VerifyTemplate.argtypes = [UINT32, POINTER(BYTE), UINT32, POINTER(BYTE)]
    QF_VerifyTemplate.restype = QF_RET_CODE

# QF_API.h: 176
if _libs["libQFM_SDK.so"].has("QF_VerifyHostTemplate", "cdecl"):
    QF_VerifyHostTemplate = _libs["libQFM_SDK.so"].get("QF_VerifyHostTemplate", "cdecl")
    QF_VerifyHostTemplate.argtypes = [UINT32, UINT32, POINTER(BYTE)]
    QF_VerifyHostTemplate.restype = QF_RET_CODE

# QF_API.h: 177
if _libs["libQFM_SDK.so"].has("QF_VerifyImage", "cdecl"):
    QF_VerifyImage = _libs["libQFM_SDK.so"].get("QF_VerifyImage", "cdecl")
    QF_VerifyImage.argtypes = [UINT32, POINTER(BYTE), UINT32, POINTER(BYTE)]
    QF_VerifyImage.restype = QF_RET_CODE

# QF_API.h: 178
if _libs["libQFM_SDK.so"].has("QF_SetVerifyCallback", "cdecl"):
    QF_SetVerifyCallback = _libs["libQFM_SDK.so"].get("QF_SetVerifyCallback", "cdecl")
    QF_SetVerifyCallback.argtypes = [CFUNCTYPE(UNCHECKED(None), BYTE)]
    QF_SetVerifyCallback.restype = None

# QF_API.h: 183
if _libs["libQFM_SDK.so"].has("QF_Enroll", "cdecl"):
    QF_Enroll = _libs["libQFM_SDK.so"].get("QF_Enroll", "cdecl")
    QF_Enroll.argtypes = [UINT32, QF_ENROLL_OPTION, POINTER(UINT32), POINTER(UINT32)]
    QF_Enroll.restype = QF_RET_CODE

# QF_API.h: 184
if _libs["libQFM_SDK.so"].has("QF_EnrollTemplate", "cdecl"):
    QF_EnrollTemplate = _libs["libQFM_SDK.so"].get("QF_EnrollTemplate", "cdecl")
    QF_EnrollTemplate.argtypes = [UINT32, QF_ENROLL_OPTION, UINT32, POINTER(BYTE), POINTER(UINT32)]
    QF_EnrollTemplate.restype = QF_RET_CODE

# QF_API.h: 185
if _libs["libQFM_SDK.so"].has("QF_EnrollMultipleTemplates", "cdecl"):
    QF_EnrollMultipleTemplates = _libs["libQFM_SDK.so"].get("QF_EnrollMultipleTemplates", "cdecl")
    QF_EnrollMultipleTemplates.argtypes = [UINT32, QF_ENROLL_OPTION, c_int, UINT32, POINTER(BYTE), POINTER(UINT32)]
    QF_EnrollMultipleTemplates.restype = QF_RET_CODE

# QF_API.h: 186
if _libs["libQFM_SDK.so"].has("QF_EnrollImage", "cdecl"):
    QF_EnrollImage = _libs["libQFM_SDK.so"].get("QF_EnrollImage", "cdecl")
    QF_EnrollImage.argtypes = [UINT32, QF_ENROLL_OPTION, UINT32, POINTER(BYTE), POINTER(UINT32), POINTER(UINT32)]
    QF_EnrollImage.restype = QF_RET_CODE

# QF_API.h: 187
if _libs["libQFM_SDK.so"].has("QF_SetEnrollCallback", "cdecl"):
    QF_SetEnrollCallback = _libs["libQFM_SDK.so"].get("QF_SetEnrollCallback", "cdecl")
    QF_SetEnrollCallback.argtypes = [CFUNCTYPE(UNCHECKED(None), BYTE, QF_ENROLL_MODE, c_int)]
    QF_SetEnrollCallback.restype = None

# QF_API.h: 192
if _libs["libQFM_SDK.so"].has("QF_Delete", "cdecl"):
    QF_Delete = _libs["libQFM_SDK.so"].get("QF_Delete", "cdecl")
    QF_Delete.argtypes = [UINT32]
    QF_Delete.restype = QF_RET_CODE

# QF_API.h: 193
if _libs["libQFM_SDK.so"].has("QF_DeleteOneTemplate", "cdecl"):
    QF_DeleteOneTemplate = _libs["libQFM_SDK.so"].get("QF_DeleteOneTemplate", "cdecl")
    QF_DeleteOneTemplate.argtypes = [UINT32, c_int]
    QF_DeleteOneTemplate.restype = QF_RET_CODE

# QF_API.h: 194
if _libs["libQFM_SDK.so"].has("QF_DeleteMultipleTemplates", "cdecl"):
    QF_DeleteMultipleTemplates = _libs["libQFM_SDK.so"].get("QF_DeleteMultipleTemplates", "cdecl")
    QF_DeleteMultipleTemplates.argtypes = [UINT32, UINT32, POINTER(c_int)]
    QF_DeleteMultipleTemplates.restype = QF_RET_CODE

# QF_API.h: 195
if _libs["libQFM_SDK.so"].has("QF_DeleteAll", "cdecl"):
    QF_DeleteAll = _libs["libQFM_SDK.so"].get("QF_DeleteAll", "cdecl")
    QF_DeleteAll.argtypes = []
    QF_DeleteAll.restype = QF_RET_CODE

# QF_API.h: 196
if _libs["libQFM_SDK.so"].has("QF_SetDeleteCallback", "cdecl"):
    QF_SetDeleteCallback = _libs["libQFM_SDK.so"].get("QF_SetDeleteCallback", "cdecl")
    QF_SetDeleteCallback.argtypes = [CFUNCTYPE(UNCHECKED(None), BYTE)]
    QF_SetDeleteCallback.restype = None

# QF_API.h: 199
if _libs["libQFM_SDK.so"].has("QF_ReadQRCode", "cdecl"):
    QF_ReadQRCode = _libs["libQFM_SDK.so"].get("QF_ReadQRCode", "cdecl")
    QF_ReadQRCode.argtypes = [String, POINTER(c_int)]
    QF_ReadQRCode.restype = QF_RET_CODE

# QF_API.h: 204
if _libs["libQFM_SDK.so"].has("QF_ChangeKey", "cdecl"):
    QF_ChangeKey = _libs["libQFM_SDK.so"].get("QF_ChangeKey", "cdecl")
    QF_ChangeKey.argtypes = [QF_KEY_OPTION, POINTER(BYTE), POINTER(BYTE)]
    QF_ChangeKey.restype = QF_RET_CODE

# QF_API.h: 205
if _libs["libQFM_SDK.so"].has("QF_ResetKey", "cdecl"):
    QF_ResetKey = _libs["libQFM_SDK.so"].get("QF_ResetKey", "cdecl")
    QF_ResetKey.argtypes = [QF_KEY_OPTION]
    QF_ResetKey.restype = QF_RET_CODE

# QF_API.h: 210
if _libs["libQFM_SDK.so"].has("QF_GetSecurePacketProtocolMode", "cdecl"):
    QF_GetSecurePacketProtocolMode = _libs["libQFM_SDK.so"].get("QF_GetSecurePacketProtocolMode", "cdecl")
    QF_GetSecurePacketProtocolMode.argtypes = []
    QF_GetSecurePacketProtocolMode.restype = BOOL

# QF_API.h: 211
if _libs["libQFM_SDK.so"].has("QF_SetSecurePacketProtocolMode", "cdecl"):
    QF_SetSecurePacketProtocolMode = _libs["libQFM_SDK.so"].get("QF_SetSecurePacketProtocolMode", "cdecl")
    QF_SetSecurePacketProtocolMode.argtypes = [BOOL, POINTER(BYTE)]
    QF_SetSecurePacketProtocolMode.restype = BOOL

# QF_API.h: 212
if _libs["libQFM_SDK.so"].has("QF_SetSecureCode", "cdecl"):
    QF_SetSecureCode = _libs["libQFM_SDK.so"].get("QF_SetSecureCode", "cdecl")
    QF_SetSecureCode.argtypes = [POINTER(BYTE)]
    QF_SetSecureCode.restype = None

# QF_API.h: 213
if _libs["libQFM_SDK.so"].has("QF_CreateRandomSecureKey", "cdecl"):
    QF_CreateRandomSecureKey = _libs["libQFM_SDK.so"].get("QF_CreateRandomSecureKey", "cdecl")
    QF_CreateRandomSecureKey.argtypes = []
    QF_CreateRandomSecureKey.restype = QF_RET_CODE

# QF_API.h: 214
if _libs["libQFM_SDK.so"].has("QF_CreateKeyPair", "cdecl"):
    QF_CreateKeyPair = _libs["libQFM_SDK.so"].get("QF_CreateKeyPair", "cdecl")
    QF_CreateKeyPair.argtypes = [POINTER(BYTE), POINTER(BYTE)]
    QF_CreateKeyPair.restype = QF_RET_CODE

# QF_API.h: 215
if _libs["libQFM_SDK.so"].has("QF_GetSecureKey", "cdecl"):
    QF_GetSecureKey = _libs["libQFM_SDK.so"].get("QF_GetSecureKey", "cdecl")
    QF_GetSecureKey.argtypes = [POINTER(BYTE), POINTER(BYTE), POINTER(BYTE)]
    QF_GetSecureKey.restype = None

# QF_API.h: 216
if _libs["libQFM_SDK.so"].has("QF_PublicKeyExchange", "cdecl"):
    QF_PublicKeyExchange = _libs["libQFM_SDK.so"].get("QF_PublicKeyExchange", "cdecl")
    QF_PublicKeyExchange.argtypes = [POINTER(BYTE), POINTER(BYTE)]
    QF_PublicKeyExchange.restype = QF_RET_CODE

# QF_API.h: 222
if _libs["libQFM_SDK.so"].has("QF_ResetSystemConfiguration", "cdecl"):
    QF_ResetSystemConfiguration = _libs["libQFM_SDK.so"].get("QF_ResetSystemConfiguration", "cdecl")
    QF_ResetSystemConfiguration.argtypes = []
    QF_ResetSystemConfiguration.restype = QF_RET_CODE

# QF_API.h: 223
if _libs["libQFM_SDK.so"].has("QF_FormatUserDatabase", "cdecl"):
    QF_FormatUserDatabase = _libs["libQFM_SDK.so"].get("QF_FormatUserDatabase", "cdecl")
    QF_FormatUserDatabase.argtypes = []
    QF_FormatUserDatabase.restype = QF_RET_CODE

# QF_API.h: 228
if _libs["libQFM_SDK.so"].has("QF_ResetSystemParameter", "cdecl"):
    QF_ResetSystemParameter = _libs["libQFM_SDK.so"].get("QF_ResetSystemParameter", "cdecl")
    QF_ResetSystemParameter.argtypes = []
    QF_ResetSystemParameter.restype = QF_RET_CODE

# QF_Def.h: 51
try:
    TRUE = 1
except:
    pass

# QF_Def.h: 55
try:
    FALSE = 0
except:
    pass

# QF_Packet.h: 17
try:
    QF_PACKET_START_CODE = 0x40
except:
    pass

# QF_Packet.h: 18
try:
    QF_NETWORK_PACKET_START_CODE = 0x41
except:
    pass

# QF_Packet.h: 19
try:
    QF_SECURE_PACKET_START_CODE = 0x50
except:
    pass

# QF_Packet.h: 20
try:
    QF_SECURE_NETWORK_PACKET_START_CODE = 0x51
except:
    pass

# QF_Packet.h: 21
try:
    QF_PACKET_END_CODE = 0x0a
except:
    pass

# QF_Packet.h: 22
try:
    QF_PACKET_LEN = 13
except:
    pass

# QF_Packet.h: 23
try:
    QF_NETWORK_PACKET_LEN = 15
except:
    pass

# QF_Packet.h: 24
try:
    QF_SECURE_PACKET_LEN = 35
except:
    pass

# QF_Packet.h: 25
try:
    QF_SECURE_NETWORK_PACKET_LEN = 40
except:
    pass

# QF_Packet.h: 27
try:
    QF_PACKET_COMMAND = 0
except:
    pass

# QF_Packet.h: 28
try:
    QF_PACKET_TERMINAL_ID = 1
except:
    pass

# QF_Packet.h: 29
try:
    QF_PACKET_PARAM = 2
except:
    pass

# QF_Packet.h: 30
try:
    QF_PACKET_SIZE = 3
except:
    pass

# QF_Packet.h: 31
try:
    QF_PACKET_FLAG = 4
except:
    pass

# QF_Packet.h: 32
try:
    QF_PACKET_CHECKSUM = 5
except:
    pass

# QF_Packet.h: 37
try:
    QF_PACKET_START_CODE_POS = 0
except:
    pass

# QF_Packet.h: 38
try:
    QF_PACKET_COMMAND_POS = 1
except:
    pass

# QF_Packet.h: 39
try:
    QF_PACKET_PARAM_POS = 2
except:
    pass

# QF_Packet.h: 40
try:
    QF_PACKET_SIZE_POS = 6
except:
    pass

# QF_Packet.h: 41
try:
    QF_PACKET_FLAG_POS = 10
except:
    pass

# QF_Packet.h: 42
try:
    QF_PACKET_CHECKSUM_POS = 11
except:
    pass

# QF_Packet.h: 43
try:
    QF_PACKET_END_CODE_POS = 12
except:
    pass

# QF_Packet.h: 48
try:
    QF_DEFAULT_DATA_PACKET_SIZE = (4 * 1024)
except:
    pass

# QF_SysParameter.h: 13
try:
    QF_SYS_PARAMETER_NOT_FOUND = 0xffffffff
except:
    pass

# QF_SysParameter.h: 14
try:
    QF_SYS_PARAMETER_NOT_READ = 0x00
except:
    pass

# QF_SysParameter.h: 150
try:
    QF_VALID_CONFIG_FILE = 0xf1f2f3f4
except:
    pass

# QF_Template.h: 10
try:
    MAXIMUM_TEMPLATE_SIZE = 512
except:
    pass

# QF_Template.h: 13
try:
    QF_ADD_CHECKSUM = 0x70
except:
    pass

# QF_Template.h: 15
try:
    MAXIMUM_NUM_OF_TEMPLATE_PER_USER = 20
except:
    pass

# QF_Template.h: 52
try:
    QF_VALID_TEMPLATE_DB = 0x1f2f3f4f
except:
    pass

# QF_Delete.h: 11
try:
    QF_DELETE_ONLY_ONE = 0x70
except:
    pass

# QF_Delete.h: 12
try:
    QF_DELETE_MULTIPLE_ID = 0x71
except:
    pass

# QF_Misc.h: 7
try:
    QF_QRCODE_DECODED_TEXT_SIZE = 512
except:
    pass

# QF_Key.h: 16
try:
    MODULE_KEY_SIZE = 32
except:
    pass

# QF_Key.h: 17
try:
    IV_KEY_SIZE = 32
except:
    pass

# QF_Key.h: 18
try:
    SECURE_KEY_SIZE = 32
except:
    pass

# QF_Key.h: 19
try:
    PUBLIC_KEY_SIZE = 32
except:
    pass

# QF_Key.h: 20
try:
    PRIVATE_KEY_SIZE = 64
except:
    pass

# QF_Key.h: 22
try:
    SECURE_PACKET_DATA_SIZE = 32
except:
    pass

# QF_Key.h: 23
try:
    ENCRYPTION_KEY_SIZE = 32
except:
    pass

# QF_Key.h: 24
try:
    CHECKSUM_4_SIZE = 4
except:
    pass

# QF_Key.h: 25
try:
    SECURE_CODE_SIZE = 8
except:
    pass

# QF_Misc.h: 7
try:
    QF_QRCODE_DECODED_TEXT_SIZE = 512
except:
    pass

# QF_Version.h: 11
try:
    QFM_SDK_VERSION_MAJOR = 0
except:
    pass

# QF_Version.h: 12
try:
    QFM_SDK_VERSION_MINOR = 5
except:
    pass

# QF_Version.h: 13
try:
    QFM_SDK_VERSION_REVISION = 6
except:
    pass

# QF_Version.h: 16
try:
    QFM_SDK_FILE_VERSION_STR = '0.5.6'
except:
    pass

# No inserted files

# No prefix-stripping


# -*- coding: utf-8 -*-

"""

subprocess_mock.core

mock standard library subprocess module functionality

Copyright (C) 2024 Rainer Schwarzbach

This file is part of subprocess-mock.

subprocess-mock is free software: you can redistribute it and/or modify
it under the terms of the MIT License.

subprocess-mock is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the LICENSE file for more details.

"""


import logging
import subprocess
import sys
import time

from typing import Any, Dict, List, Optional, Tuple, Union


_PLATFORM_DEFAULT_CLOSE_FDS = object()

DEFAULT_ENCODING = "utf-8"

KW_RETURNCODE = "returncode"
KW_STDERR = "stderr"
KW_STDOUT = "stdout"

RETURNCODE_OK = 0
RETURNCODE_ERROR = 1


#
# Classes
#


# pylint: disable=too-many-instance-attributes,too-many-arguments,
# pylint: disable=too-many-locals,unused-argument


class Popen:

    """Rudimentary subprocess.Popen() mock object"""

    def __init__(
        self,
        args,
        bufsize=-1,
        executable=None,
        stdin=None,
        stdout=None,
        stderr=None,
        preexec_fn=None,
        close_fds=_PLATFORM_DEFAULT_CLOSE_FDS,
        shell=False,
        cwd=None,
        env=None,
        universal_newlines=False,
        startupinfo=None,
        creationflags=0,
        restore_signals=True,
        start_new_session=False,
        pass_fds=(),
        *,
        encoding=None,
        errors=None,
    ):
        """Create new Popen instance."""
        if bufsize is None:
            bufsize = -1  # Restore default
        #
        if not isinstance(bufsize, int):
            raise TypeError("bufsize must be an integer")
        #
        if sys.platform == "win32":
            if preexec_fn is not None:
                raise ValueError(
                    "preexec_fn is not supported on Windows platforms"
                )
            #
            any_stdio_set = any(
                stream is not None for stream in (stdin, stdout, stderr)
            )
            if close_fds is _PLATFORM_DEFAULT_CLOSE_FDS:
                close_fds = not any_stdio_set
            elif close_fds and any_stdio_set:
                raise ValueError(
                    "close_fds is not supported on Windows platforms"
                    " if you redirect stdin/stdout/stderr"
                )
            #
        else:
            # POSIX
            if close_fds is _PLATFORM_DEFAULT_CLOSE_FDS:
                close_fds = True
            #
            if pass_fds and not close_fds:
                logging.warning("pass_fds overriding close_fds.")
                close_fds = True
            #
            if startupinfo is not None:
                raise ValueError(
                    "startupinfo is only supported on Windows platforms"
                )
            #
            if creationflags != 0:
                raise ValueError(
                    "creationflags is only supported on Windows platforms"
                )
            #
        #
        self._stdout_target = stdout
        self._stderr_target = stderr
        self.args = args
        self.returncode = None
        self.universal_newlines = universal_newlines
        self.encoding = encoding
        self.errors = errors
        self._running = True

    def _bytes_lines(self, source: Union[bytes, str, None]) -> List[bytes]:
        """Return a list of bytes lines from bytes or str source"""
        if source is None:
            return []
        #
        if isinstance(source, str):
            source = source.encode(self.encoding or DEFAULT_ENCODING)
        #
        return source.splitlines()

    def _translate_newlines(
        self, data: Union[bytes, str], encoding: str, errors: str
    ):
        """from https://github.com/python/cpython/blob/
        v3.6.8/Lib/subprocess.py#L759
        """
        if isinstance(data, str):
            unicode_data = data
        else:
            unicode_data = data.decode(encoding, errors)
        #
        return unicode_data.replace("\r\n", "\n").replace("\r", "\n")

    def communicate(
        self,
        timeout: Optional[float] = None,
        stdout: Union[bytes, str, None] = None,
        stderr: Union[bytes, str, None] = None,
        returncode: int = RETURNCODE_OK,
    ) -> Tuple[Union[bytes, str, None], Union[bytes, str, None]]:
        """Communicate, set returncode..."""
        output_stdout: Union[bytes, str, None] = None
        output_stderr: Union[bytes, str, None] = None
        self._set_returncode(returncode)
        self.wait(timeout=timeout)
        if self._stdout_target is not None:
            stdout_lines: List[bytes] = self._bytes_lines(stdout)
            if self._stderr_target == subprocess.STDOUT:
                stdout_lines.extend(self._bytes_lines(stderr))
            #
            output_stdout = b"\n".join(stdout_lines)
        #
        if self._stderr_target == subprocess.PIPE:
            output_stderr = b"\n".join(self._bytes_lines(stderr))
        #
        if self.encoding or self.errors or self.universal_newlines:
            if output_stdout is not None:
                output_stdout = self._translate_newlines(
                    output_stdout, self.encoding, self.errors
                )
            #
            if output_stderr is not None:
                output_stderr = self._translate_newlines(
                    output_stderr, self.encoding, self.errors
                )
            #
        #
        return (output_stdout, output_stderr)

    def _remaining_time(self, endtime: Optional[float] = None) -> float:
        """Convenience for _communicate when computing timeouts."""
        if endtime is None:
            return 1.0
        #
        return endtime - time.monotonic()

    def _set_returncode(self, returncode: Optional[int] = None) -> None:
        """Set the returncode"""
        self.returncode = returncode

    def poll(self) -> Optional[int]:
        """Return the returncode"""
        returncode = self.returncode
        if returncode is None:
            return None
        #
        self._running = False
        return returncode

    def wait(self, timeout: Optional[float] = None) -> int:
        """Return the returncode after the process has ended"""
        if not self._running:
            raise ValueError("Process not running")
        #
        endtime: Optional[float] = None
        if timeout is not None:
            endtime = time.monotonic() + timeout
        #
        while self._remaining_time(endtime) > 0:
            if self.poll() is not None:
                break
            #
            time.sleep(0.01)
        #
        return self.returncode


class ModuleFunctions:

    """Mock a subprocess.call and store the results"""

    def __init__(self, returncode: int = RETURNCODE_OK) -> None:
        """Initialize the internal values"""
        self.__calls: List[
            Tuple[subprocess.CompletedProcess, Dict[str, Any]]
        ] = []
        self.__default_result: Dict[str, Any] = {KW_RETURNCODE: returncode}
        self.__next_result_override: Dict[str, Any] = {}

    @property
    def call_results(
        self,
    ) -> List[Tuple[subprocess.CompletedProcess, Dict[str, Any]]]:
        """Return all call results"""
        return self.__calls[:]

    @property
    def next_result_data(self) -> Dict[str, Any]:
        """get result data, applying and resetting temporary overrides"""
        current_result = dict(self.__default_result)
        current_result.update(self.__next_result_override)
        self.__next_result_override.clear()
        return current_result

    def inject_result_data(self, *, permanent=False, **kwargs):
        """inject result data,
        either permanently or just for the next call
        """
        if permanent:
            target_collection = self.__default_result
        else:
            target_collection = self.__next_result_override
        #
        for key, value in kwargs.items():
            if key in (KW_RETURNCODE, KW_STDERR, KW_STDOUT):
                target_collection[key] = value
            #
        #

    def reset(self) -> None:
        """Clear the calls list"""
        self.__calls.clear()

    # pylint: disable=redefined-builtin ; from mocked function
    def run(self, *popenargs, input=None, timeout=None, check=False, **kwargs):
        """mock subprocess.run()"""
        process = Popen(*popenargs, **kwargs)
        stdout, stderr = process.communicate(
            timeout=timeout, **self.next_result_data
        )
        run_result = subprocess.CompletedProcess(
            process.args,
            process.returncode,
            stdout=stdout,
            stderr=stderr,
        )
        self.__calls.append((run_result, kwargs))
        if check:
            run_result.check_returncode()
        #
        return run_result


# vim: fileencoding=utf-8 sw=4 ts=4 sts=4 expandtab autoindent syntax=python:

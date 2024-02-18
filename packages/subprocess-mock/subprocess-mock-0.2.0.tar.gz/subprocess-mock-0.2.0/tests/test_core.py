# -*- coding: utf-8 -*-

"""

tests.test_core

Unit test the core module


Copyright (C) 2024 Rainer Schwarzbach

This file is part of subprocess-mock.

subprocess-mock is free software: you can redistribute it and/or modify
it under the terms of the MIT License.

subprocess-mock is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the LICENSE file for more details.

"""


import pathlib
import subprocess
import tempfile

from unittest import TestCase

from unittest.mock import patch

from subprocess_mock import core

from .commons import RETURNCODE_OK, RETURNCODE_ERROR


SUBPROCESS_RUN = "subprocess.run"


class ModuleFunctions(TestCase):

    """Test the ModuleFunctions class"""

    def test_result_data(self) -> None:
        """.inject_result_data() method and .next_result_data property"""
        module_functions = core.ModuleFunctions()
        default_data = {core.KW_RETURNCODE: RETURNCODE_OK}
        base_data = {
            core.KW_RETURNCODE: RETURNCODE_ERROR,
            core.KW_STDERR: "error",
            core.KW_STDOUT: "normal output",
        }
        extended_data = dict(base_data)
        extended_data.update(surplus_member="not considered")
        module_functions.inject_result_data(**extended_data)
        with self.subTest("one-time override after inject, allowed data only"):
            self.assertDictEqual(module_functions.next_result_data, base_data)
        #
        with self.subTest("dafault data after result data access"):
            self.assertDictEqual(
                module_functions.next_result_data, default_data
            )
        #
        module_functions.inject_result_data(**extended_data, permanent=True)
        with self.subTest(
            "permanent override after inject, allowed data only"
        ):
            self.assertDictEqual(module_functions.next_result_data, base_data)
        #
        with self.subTest(
            "overridden data still available after result data access"
        ):
            self.assertDictEqual(module_functions.next_result_data, base_data)
        #

    def test_run(self) -> None:
        """.run() method"""
        module_functions = core.ModuleFunctions()
        with tempfile.TemporaryDirectory() as tempdir:
            new_file_path = pathlib.Path(tempdir) / "new_file.txt"
            with self.subTest("file does not pre-exist"):
                self.assertFalse(new_file_path.exists())
            #
            msg_prefix = "Non-mocked call:"
            with self.subTest(f"{msg_prefix} file does not pre-exist"):
                self.assertFalse(new_file_path.exists())
            #
            touch_command = ["touch", str(new_file_path)]
            result = subprocess.run(touch_command, check=False)
            with self.subTest(f"{msg_prefix} {core.KW_RETURNCODE}"):
                self.assertEqual(result.returncode, RETURNCODE_OK)
            #
            with self.subTest(
                f"{msg_prefix} mock call result was not registered"
            ):
                self.assertEqual(module_functions.call_results, [])
            #
            with self.subTest(f"{msg_prefix} file does post-exist"):
                self.assertTrue(new_file_path.exists())
            #
            new_file_path.unlink()
            with patch(SUBPROCESS_RUN, new=module_functions.run):
                touch_command = ["touch", str(new_file_path)]
                module_functions.inject_result_data(stderr="ignored data")
                result = subprocess.run(
                    touch_command,
                    stdout=subprocess.PIPE,
                    stderr=None,
                    check=False,
                )
                with self.subTest(core.KW_RETURNCODE):
                    self.assertEqual(result.returncode, RETURNCODE_OK)
                #
                with self.subTest(core.KW_STDOUT):
                    self.assertEqual(result.stdout, b"")
                #
                with self.subTest(core.KW_STDERR):
                    self.assertIsNone(result.stderr)
                #
                with self.subTest("mock call result was registered"):
                    last_result = module_functions.call_results[-1]
                    self.assertIs(result, last_result[0])
                #
                with self.subTest("file does not post-exist"):
                    self.assertFalse(new_file_path.exists())
                #
                with self.subTest("unsuccessful call"):
                    module_functions.inject_result_data(
                        returncode=RETURNCODE_ERROR
                    )
                    self.assertRaises(
                        subprocess.CalledProcessError,
                        subprocess.run,
                        touch_command,
                        check=True,
                    )
                #
            #
        #


# vim: fileencoding=utf-8 ts=4 sts=4 sw=4 autoindent expandtab syntax=python:

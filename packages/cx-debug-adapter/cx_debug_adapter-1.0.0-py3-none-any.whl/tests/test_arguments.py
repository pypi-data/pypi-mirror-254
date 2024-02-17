# MIT License
#
# Copyright (c) 2020 Espressif Systems (Shanghai) Co. Ltd.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# SPDX-License-Identifier: MIT

from tests.conftest import setup_teardown  # noqa: F401
import debug_adapter
import pytest


@pytest.mark.timeout(30)
def test_daargs_class(setup_teardown):  # noqa: F811
    da_args = debug_adapter.DaArgs()
    assert isinstance(da_args, debug_adapter.DaArgs)

    val = "test_args.log"
    da_args.port = val
    assert da_args.port == val

    val = "test_args.log"
    da_args = debug_adapter.DaArgs(log_file=val)
    assert da_args.log_file == val

    da_args_new_int = debug_adapter.DaArgs(new_arg_int=123)
    assert da_args_new_int.new_arg_int == 123

    val = 123
    da_args = debug_adapter.DaArgs(new_arg_int=val)
    assert da_args.new_arg_int == val

    val = "123"
    da_args = debug_adapter.DaArgs(new_arg2_str=val)
    assert da_args.new_arg2_str == val


if __name__ == "__main__":
    # run tests from this file; print all output
    pytest.main([__file__, "-s"])

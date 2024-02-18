import importlib
import os
import subprocess
import sys

from pygemstones.util import log


# -----------------------------------------------------------------------------
def run_external(
    path,
    module_name,
    command_name,
    command_params,
    show_log=False,
    show_error_log=False,
    throw_error=False,
):
    """
    Execute external command inside path and return the command result.

    Arguments:
        path : str

        module_name : str

        command_name: str

        command_params: dict

        show_log : bool

        show_error_log : bool

        throw_error : bool

    Returns:
        str
    """

    result = None

    sys_path = list(sys.path)
    original_cwd = os.getcwd()

    target_module = None
    command = None

    try:
        sys.path.insert(0, path)

        target_module = importlib.import_module(module_name)
        command = getattr(target_module, command_name)

        result = command(command_params)

        if show_log:
            log.colored(
                'Command "{0}" finished with success'.format(command_name), log.GREEN
            )
    except Exception as e:
        if show_error_log:
            log.e(
                'Error while call "{0}" on module "{1}": {2}'.format(
                    command_name, module_name, e
                ),
                fatal=(not throw_error),
            )

        if throw_error:
            raise

    finally:
        if module_name in sys.modules:
            del sys.modules[module_name]

        if target_module is not None:
            del target_module

        if command is not None:
            del command

        sys.path = sys_path
        os.chdir(original_cwd)

    return result


# -----------------------------------------------------------------------------
def run(args, shell=False, cwd=None, env=None, silent=False):
    """
    Run a command with optional settings inside an optional directory .

    Arguments:
        args : list[str]

        shell : False

        cwd : str

        env : dict

        silent : bool

    Returns:
        int
    """

    if silent:
        p = subprocess.Popen(
            args,
            cwd=cwd,
            shell=shell,
            env=env,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        out, err = p.communicate()

        if 0 != p.returncode:
            if out:
                print(out.decode("UTF-8"))

            if err:
                print(err.decode("UTF-8"))

            if not isinstance(args, str):
                args = " ".join(args)

            log.m(
                "{2}COMMAND:{3} {0}\n"
                "{4}WORKING DIR:{5} {1}".format(
                    args, cwd, log.YELLOW, log.RESET, log.YELLOW, log.RESET
                )
            )

            log.e("Command execution has failed")

        return p.returncode
    else:
        ret = subprocess.call(
            args,
            cwd=cwd,
            shell=shell,
            env=env,
        )

        if ret > 0:
            if not isinstance(args, str):
                args = " ".join(args)

            log.m(
                "{2}COMMAND:{3} {0}\n"
                "{4}WORKING DIR:{5} {1}".format(
                    args, cwd, log.YELLOW, log.RESET, log.YELLOW, log.RESET
                )
            )

            log.e("Command execution has failed")

        return ret

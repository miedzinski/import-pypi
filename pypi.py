import importlib.abc
import importlib.machinery
import subprocess
import sys


def install(pkgname, version=None):
    cmd = [sys.executable, '-m', 'pip', 'install']
    if version:
        cmd.append('{}=={}'.format(pkgname, version))
    else:
        cmd.append(pkgname)
    subprocess.check_call(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


class PipFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        try:
            install(fullname)
        except subprocess.CalledProcessError:
            return None
        else:
            return importlib.machinery.PathFinder().find_spec(
                fullname,
                path,
                target,
            )


sys.meta_path.append(PipFinder())

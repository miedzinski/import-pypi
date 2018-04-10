import importlib.abc
import importlib.machinery
import subprocess
import sys


def install(pkgname, version=None):
    cmd = [sys.executable, '-m', 'pip', 'install']
    version_specs = ('>=', '>', '<=', '<', '==')
    if version:
        version_spec = '=='
        if any([str.startswith(version, v) for v in version_specs]):
            version_spec, version = [
                (version[:len(v)], version[len(v):]) for v in version_specs
                if version.startswith(v)
            ][0]
        cmd.append('{}{}{}'.format(pkgname, version_spec, version))
    else:
        cmd.append(pkgname)
    subprocess.check_call(
        cmd,
        # stdout=subprocess.DEVNULL,
        # stderr=subprocess.DEVNULL,
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

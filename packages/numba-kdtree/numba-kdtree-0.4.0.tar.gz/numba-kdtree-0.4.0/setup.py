from setuptools import setup, find_packages, Extension
from distutils.command.build_ext import build_ext as build_ext_orig
from distutils.sysconfig import get_python_inc
from os.path import join, dirname
from distutils.sysconfig import customize_compiler
import platform

# standalone import of a module (https://stackoverflow.com/a/58423785)
def import_module_from_path(path):
    """Import a module from the given path without executing any code above it
    """
    import importlib
    import pathlib
    import sys

    module_path = pathlib.Path(path).resolve()
    module_name = module_path.stem  # 'path/x.py' -> 'x'
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)

    if module not in sys.modules:
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
    else:
        module = sys.modules
    return module

inc_dirs = [get_python_inc()]
inc_dirs.append(join(dirname(dirname(__file__)), 'src', 'ckdtree'))

ckdtree_src = ['init.cpp',
               'build.cpp',
               'query.cpp',
               'query_radius.cpp']

ckdtree_src = [join('src', 'ckdtree', x) for x in ckdtree_src]


class CTypesExtension(Extension): pass


class build_ext(build_ext_orig):
    def build_extension(self, ext):
        self._ctypes = isinstance(ext, CTypesExtension)
        if self._ctypes:
            customize_compiler(self.compiler)
            try:
                self.compiler.compiler_so.remove("-Wstrict-prototypes")
            except (AttributeError, ValueError):
                pass
        return super().build_extension(ext)

    def get_export_symbols(self, ext):
        if self._ctypes:
            return ext.export_symbols
        return super().get_export_symbols(ext)

    def get_ext_filename(self, ext_name):
        if self._ctypes:
            if platform.system() == "Windows":
                return ext_name + '.lib'
            else:
                return ext_name + '.so'
        return super().get_ext_filename(ext_name)


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

if platform.system() == "Windows":
    extra_compile_args = ['/O2', '/DKDTREE_COMPILING=1']
else:
    extra_compile_args = ['-fPIC', '-shared', '-O3', '-DKDTREE_COMPILING=1']
    if platform.system() == "Darwin":
        extra_compile_args.append('-std=c++11')

module = CTypesExtension('numba_kdtree._ckdtree',
                   sources=ckdtree_src,
                   include_dirs=inc_dirs,
                   extra_compile_args=extra_compile_args)

setup(
    name="numba-kdtree",
    author="Felix Igelbrink",
    author_email="felix.igelbrink@uni-osnabrueck.de",
    description="A kdtree implementation for numba.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mortacious/numba-kdtree",
    project_urls={
        "Bug Tracker": "https://github.com/mortacious/numba-kdtree/issues",
    },
    packages=find_packages(exclude=['examples', 'tests']),
    ext_modules=[module],
    install_requires=[
        'numba>=0.52',
    ],
    extras_require={
        'tests': ['pytest', 'scipy', 'requests', 'plyfile'],
    },
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
    ],
    python_requires=">=3.7",
    cmdclass={'build_ext': build_ext},
    zip_safe=True,
    setup_requires=['setuptools_scm'],
    use_scm_version = {
        "write_to": "numba_kdtree/_version.py",
        "version_scheme": "release-branch-semver"
    },
)

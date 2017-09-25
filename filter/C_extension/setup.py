from distutils.core import setup, Extension

module = Extension('exmod',
                    include_dirs = ['/usr/local/include'],
                    libraries = ['pthread'],
                    sources = ['extensionModule.c'])

setup(name = "extensionModule",
       version = "1.0",
       description = "This is an example package",
       author = "Viktor Studenyak",
       url = "",
       ext_modules = [module])
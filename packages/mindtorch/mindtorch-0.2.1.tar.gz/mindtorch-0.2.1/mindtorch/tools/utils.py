#!/usr/bin/env python
# -*- coding: utf-8 -*-
import importlib.util
import importlib

def try_import(module_name):
    """Try importing a module, with an informative error message on failure."""
    install_name = module_name

    if module_name.find('.') > -1:
        install_name = module_name.split('.')[0]

    try:
        mod = importlib.import_module(module_name)
        return mod
    except ImportError:
        err_msg = (
            "Failed importing {}. This likely means that some pytorch modules "
            "require additional dependencies that have to be "
            "manually installed (usually with `pip install {}`). ").format(
                module_name, install_name)
        raise ImportError(err_msg)

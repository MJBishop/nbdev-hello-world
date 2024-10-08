"""Fill in a module description here"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_core.ipynb.

# %% auto 0
__all__ = ['repo_string', 'filename_for_test_module', 'test_module', 'default_exp_string_for_test_module',
           'import_module_string_for_test_module', 'nbdev_export_to_string', 'format_test_module',
           'filename_for_module', 'default_exp_string_for_module', 'default_test_class_string_for_module',
           'format_module']

# %% ../nbs/01_core.ipynb 2
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell


# %% ../nbs/01_core.ipynb 3
from configparser import ConfigParser 

# %% ../nbs/01_core.ipynb 4
def repo_string():
    configure = ConfigParser() 
    configure.read('settings.ini') 
    lib_path = configure.get('DEFAULT','lib_path')
    return lib_path

# %% ../nbs/01_core.ipynb 5
def filename_for_test_module(module_name, index_str):
    return f"{index_str}_test_{module_name}.ipynb"

# %% ../nbs/01_core.ipynb 6
def test_module(module_name):
    return f'tests/test_{module_name}'

# %% ../nbs/01_core.ipynb 7
def default_exp_string_for_test_module(module_name):
    return f'#| default_exp {test_module(module_name)}'

# %% ../nbs/01_core.ipynb 8
def import_module_string_for_test_module(repo_name, module_name):
    return f'from {repo_name}.{module_name} import *'

# %% ../nbs/01_core.ipynb 9
def nbdev_export_to_string():
    return "#| hide \nimport nbdev; nbdev.nbdev_export()"

# %% ../nbs/01_core.ipynb 10
def format_test_module(module_name, index_str):
    fname = filename_for_test_module(module_name, index_str)
    repo_name = repo_string()

    # create a new empty notebook
    nb = new_notebook()  

    # add a code cells
    cell1 = new_code_cell(default_exp_string_for_test_module(module_name))
    nb['cells'].append(cell1)

    cell2_string = f"#| export \n{import_module_string_for_test_module(repo_name, module_name)}"
    cell2 = new_code_cell(cell2_string)
    nb['cells'].append(cell2)

    cell3 = new_code_cell(nbdev_export_to_string())
    nb['cells'].append(cell3)

    # save the notebook to a file

    with open(fname, 'w') as f:
        nbformat.write(nb, f)
        

# %% ../nbs/01_core.ipynb 12
def filename_for_module(module_name, index_str):
    return f"{index_str}_{module_name}.ipynb"

# %% ../nbs/01_core.ipynb 13
def default_exp_string_for_module(module_name):
    return f'#| default_exp {module_name}'

# %% ../nbs/01_core.ipynb 14
def default_test_class_string_for_module(module_name):
    return f'Test{module_name.title()}'

# %% ../nbs/01_core.ipynb 15
def format_module(module_name, index_str):
    fname = filename_for_module(module_name, index_str)

    # create a new empty notebook
    nb = new_notebook()  

    # add markdown

    # add a code cells
    cell1 = new_code_cell(default_exp_string_for_module(module_name))
    nb['cells'].append(cell1)

    cell2_string = "#| export \ndef foo(): pass"
    cell2 = new_code_cell(cell2_string)
    nb['cells'].append(cell2)

    cell3_string = (f"#| export {test_module(module_name)}\n"
                    "\n"
                    "import unittest\n"
                    "\n"
                    f"class {default_test_class_string_for_module(module_name)}(unittest.TestCase):\n"
                    f"   def test_foo(self): pass\n")

    cell3 = new_code_cell(cell3_string)
    nb['cells'].append(cell3)

    cell4_string = ("#| eval: false\n"
        "#| hide\n"
        "unittest.main(argv=[''], verbosity=2, exit=False)\n")
    cell4 = new_code_cell(cell4_string)
    nb['cells'].append(cell4)

    
    cell5 = new_code_cell(nbdev_export_to_string())
    nb['cells'].append(cell5)

    # save the notebook to a file

    with open(fname, 'w') as f:
        nbformat.write(nb, f)

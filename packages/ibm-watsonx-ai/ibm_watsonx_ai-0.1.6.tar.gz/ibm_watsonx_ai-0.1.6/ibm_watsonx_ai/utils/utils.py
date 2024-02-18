#  -----------------------------------------------------------------------------------------
#  (C) Copyright IBM Corp. 2023-2024.
#  https://opensource.org/licenses/BSD-3-Clause
#  -----------------------------------------------------------------------------------------
import sys
import inspect 

import ibm_watson_machine_learning.utils.utils as utils
from ibm_watson_machine_learning.utils.utils import NextResourceGenerator, DisableWarningsLogger

from ibm_watsonx_ai.utils.change_methods_docstring import copy_func, change_docstrings

@change_docstrings
class NextResourceGenerator(NextResourceGenerator):
    """Generator class to produce next list of resources from REST API."""
    pass

@change_docstrings
class DisableWarningsLogger(DisableWarningsLogger):
    """Class which disables logging warnings (for example for silent handling WMLClientErrors in try except).

    **Example**

    .. code-block:: python

        try:
            with DisableWarningsLogger():
                throw_wml_error()
        except WMLClientError:
            success = False

    """
    pass


attributes = dir(utils)

for attribute in attributes:
    attr = getattr(utils, attribute)
    if callable(attr) and not inspect.isclass(attr)\
          and hasattr(attr, '__globals__'):
        setattr(sys.modules[__name__], attribute, copy_func(getattr(utils, attribute)))


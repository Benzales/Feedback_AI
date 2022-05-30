#!/usr/bin/env python

import helper_functions as hf
import sys
import subprocess
import re

def test():
    import paths
    paths.check_directories()
    
    import error
    error.handle_errors()    

    import output
    output.check_output()

test()
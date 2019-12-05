#!/usr/bin/env python3                                            
#
# mriconvertpower9 fs ChRIS plugin app
#
# (c) 2016-2019 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#


import os
import sys
sys.path.append(os.path.dirname(__file__))

# import the Chris app superclass
from chrisapp.base import ChrisApp


Gstr_title = """

Generate a title from 
http://patorjk.com/software/taag/#p=display&f=Doom&t=mriconvertpower9

"""

Gstr_synopsis = """

(Edit this in-line help for app specifics. At a minimum, the 
flags below are supported -- in the case of DS apps, both
positional arguments <inputDir> and <outputDir>; for FS apps
only <outputDir> -- and similarly for <in> <out> directories
where necessary.)

    NAME

       mriconvertpower9.py 

    SYNOPSIS

        python mriconvertpower9.py                                         \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            <inputDir>                                                  \\
            <outputDir> 

    BRIEF EXAMPLE

        * Bare bones execution

            mkdir in out && chmod 777 out
            python mriconvertpower9.py   \\
                                in    out

    DESCRIPTION

        `mriconvertpower9.py` ...

    ARGS

        [-h] [--help]
        If specified, show help message and exit.
        
        [--json]
        If specified, show json representation of app and exit.
        
        [--man]
        If specified, print (this) man page and exit.

        [--meta]
        If specified, print plugin meta data and exit.
        
        [--savejson <DIR>] 
        If specified, save json representation file to DIR and exit. 
        
        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.
        
        [--version]
        If specified, print version number and exit. 

"""


class Mriconvertpower9(ChrisApp):
    """
    FreeSurfer's mriconvert on Power9.
    """
    AUTHORS                 = 'power9group (quinnyyy@bu.edu)'
    SELFPATH                = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC                = os.path.basename(__file__)
    EXECSHELL               = 'python3'
    TITLE                   = 'FreeSurfers mriconvert on Power9'
    CATEGORY                = ''
    TYPE                    = 'fs'
    DESCRIPTION             = 'FreeSurfers mriconvert on Power9'
    DOCUMENTATION           = 'http://wiki'
    VERSION                 = '0.1'
    ICON                    = '' # url of an icon image
    LICENSE                 = 'Opensource (MIT)'
    MAX_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MAX_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT           = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT           = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """
        self.add_argument('--exec', dest='exec', type=str, optional=True, help='the conversion program to use', default = '/usr/bin/convert')

        self.add_argument('--inputFile', dest='inputFile', type=str, optional=True, help='the input file to convert', default='')

        self.add_argument('--outputFile', dest='outputFile', type=str, optional=True, help='the output file', default = '')

        self.add_argument('--inputdir', dest='inputdir', type=str, optional=False, help='blah', default='')

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print("hello world from run")
        if not len(options.inputFile):
                print("ERROR: No input file has been specified!")
                print("You must specify an input file relative to the input directory.")
                sys.exit(1)

        if not len(options.outputFile):
                print("ERROR: No output file has been specified!")
                print("You must specicy an output file relative to the output directory.")
                sys.exit(1)

        str_cmd = '%s %s/%s %s/%s' % (options.exec, options.inputdir, options.inputFile, options.outputdir, options.outputFile)
        os.system(str_cmd)


    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)


# ENTRYPOINT
if __name__ == "__main__":
    print("The main is starting lets goooo")
    chris_app = Mriconvertpower9()
    chris_app.launch()


from unittest import TestCase
from unittest import mock
from mri_convert_ppc64.mri_convert_ppc64 import Mri_convert_ppc64


class Mri_convert_ppc64Tests(TestCase):
    """
    Test Mri_convert_ppc64.
    """
    def setUp(self):
        self.app = Mri_convert_ppc64()

    def test_run(self):
        """
        Test the run code.
        """
        args = []
        if self.app.TYPE == 'ds':
            args.append('inputdir') # you may want to change this inputdir mock
        args.append('outputdir')  # you may want to change this outputdir mock

        # you may want to add more of your custom defined optional arguments to test
        # your app with
        # eg.
        # args.append('--custom-int')
        # args.append(10)

        options = self.app.parse_args(args)
        self.app.run(options)

        # write your own assertions
        self.assertEqual(options.outputdir, 'outputdir')

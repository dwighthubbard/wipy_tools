import unittest


class TestModuleImports(unittest.TestCase):
    def test_import_telnet(self):
        import wipy_cli.telnet


if __name__ == '__main__':
    unittest.main()
import unittest
import asyncio
import socket

from async_scanner import COMMON_SERVICE_MAP, create_arg_parser, run_scan


class TestScanner(unittest.TestCase):

    def test_service_known(self):
        self.assertEqual(COMMON_SERVICE_MAP[22], "SSH")

    def test_service_unknown(self):
        self.assertNotIn(9999, COMMON_SERVICE_MAP)

    def test_localhost(self):
        ip = socket.gethostbyname("localhost")
        self.assertTrue(ip.startswith("127."))

    def test_parser_defaults(self):
        parser = create_arg_parser()
        args = parser.parse_args([])
        self.assertEqual(args.target, "localhost")

    def test_parser_custom(self):
        parser = create_arg_parser()
        args = parser.parse_args(["example.com", "-s", "10", "-e", "20"])
        self.assertEqual(args.start, 10)
        self.assertEqual(args.end, 20)

    def test_small_scan(self):
        results = asyncio.run(run_scan("localhost", 1, 5, quiet=True))
        self.assertIsInstance(results, list)


if __name__ == "__main__":
    unittest.main()

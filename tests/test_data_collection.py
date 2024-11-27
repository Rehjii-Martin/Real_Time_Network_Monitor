import unittest

from utils.data_collection import get_active_connections


class TestDataCollection(unittest.TestCase):
    def test_get_active_connections(self):
        connections = get_active_connections()
        self.assertIsInstance(connections, list)
        for conn in connections:
            self.assertIsInstance(conn, dict)
            self.assertIn("local_ip", conn)
            self.assertIn("remote_ip", conn)
            self.assertIn("hostname", conn)


if __name__ == "__main__":
    unittest.main()

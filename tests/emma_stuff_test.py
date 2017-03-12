import unittest
from emma_stuff import check_urls


class TestEmmaStuff(unittest.TestCase):

    def test_check_urls(self):
        urls_to_check = [
            "http://google.com", "http://httpbin.org/status/404", "http://www.yahoo.com",
            "http://httpbin.org/status/500", "http://httpbin.org/status/202",
            "http://httpbin.org/status/201", "http://httpbin.org/status/403",
            "http://httpbin.org/status/503"]
        responses = check_urls(urls_to_check)
        self.assertEqual(
            "Unable to reach: http://httpbin.org/status/404 an HTTP status code of 404 was returned",
            responses[0])
        self.assertEqual(
            "Unable to reach: http://httpbin.org/status/500 an HTTP status code of 500 was returned",
            responses[1])
        self.assertEqual(
            "Unable to reach: http://httpbin.org/status/403 an HTTP status code of 403 was returned",
            responses[2])
        self.assertEqual(
            "Unable to reach: http://httpbin.org/status/503 an HTTP status code of 503 was returned",
            responses[3])


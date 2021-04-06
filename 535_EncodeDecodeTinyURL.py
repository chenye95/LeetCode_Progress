"""
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it
 returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode
algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
"""
from random import choice
from string import ascii_letters


class Codec:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.short_url_len = 6
        self.letter_number_set = ascii_letters + "0123456789"
        self.short_url_prefix = "http://tinyurl.com/"

    def encode(self, long_url: str) -> str:
        """
        Encode a URL, long_url, to a shortened one

        :param long_url: original url to encode
        :return: shortened url of length self.short_url_len
        """
        while long_url not in self.url_to_code:
            code = "".join(choice(self.letter_number_set) for _ in range(self.short_url_len))
            if code not in self.code_to_url:
                self.code_to_url[code] = long_url
                self.url_to_code[long_url] = code

        return self.short_url_prefix + self.url_to_code[long_url]

    def decode(self, short_url: str) -> str:
        """
        Decodes a shortened URL, short_url, to its original URL.

        :param short_url: shortened url of length self.short_url_len
        :return: original url
        """
        return self.code_to_url[short_url[-self.short_url_len:]]


test_codec = Codec()
url_lists = ["www.google.com",
             "www.microsoft.com",
             "www.azure.com",
             "www.hotmail.com", ]
url_map = {}
for test_long_url in url_lists:
    url_map[test_long_url] = test_codec.encode(test_long_url)
for test_long_url, shortened_url in url_map.items():
    assert test_codec.encode(test_long_url) == shortened_url
    assert test_codec.decode(shortened_url) == test_long_url

import json
import re

with open('services/url_to_image_mapping.json') as f:
    _url_to_image_mapping = json.load(f)


class ComparisonService:
    url_id_pattern = re.compile("(?<=\/)[\w\-]+$")

    def __init__(self):
        self._url_comparisons = 0
        self._image_comparisons = 0
        self._string_comparisons = 0

    def strings_are_equal(self, url1, url2):
        self._string_comparisons += 1
        return url1 == url2

    def urls_are_equal(self, url1, url2):
        self._url_comparisons += 1
        try:
            url_id_1 = self.url_id_pattern.search(url1).group()
            url_id_2 = self.url_id_pattern.search(url2).group()
        except AttributeError:
            raise TypeError("Not a url!")

        return url_id_1 == url_id_2

    def images_are_equal(self, url1, url2):
        self._image_comparisons += 1
        return _url_to_image_mapping[url1] == _url_to_image_mapping[url2]

    def __del__(self):
        print('*******************')
        print('COMPARISONS SUMMARY')
        print('*******************')
        print('total STRING comparisons:', self._string_comparisons)
        print('total URL comparisons:', self._url_comparisons)
        print('total IMAGE comparisons:', self._image_comparisons)

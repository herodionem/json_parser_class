import json

from jsonpath_ng import parse


class walmartJSONParser:
    def __init__(self, json_str, url=None):
        self._base = json_str
        self.base = json.loads(self._base)
        if url:
            self.url = url.split('?')[0]
        else:
            self.url = self.get_base_url()

    @property
    def current_page_url(self):
         return self.url \
            + '?' \
            +  [i['url'] for i in self.base['searchContent']['preso']['pagination']['pages'] if i.get('selected')][0] \
            + '&' \
            + self.base['searchContent']['preso']['pagination']['additionalparams']

    def get_base_url(self):
        page_url = parse('searchContent..pageMetadata.canonical')
        return [i.value for i in page_url.find(self.base)][0]

    @property
    def next_page_url(self):
        return self.url + '?' +  self.base['searchContent']['preso']['pagination']['next']['url']

    @property
    def department_links(self):
        return [i for i in self.base['searchContent']['preso']['facets'] if i.get('name') == 'Departments'][0]['values']

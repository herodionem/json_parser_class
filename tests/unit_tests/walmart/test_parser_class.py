import json

import pytest
from pytest_mock import mocker
from parsers.walmart.parser_class import walmartJSONParser


_sample = open('search_content_html.json', 'r').read()


# Has methods:
def test_has_method_current_page_url():
    assert hasattr(walmartJSONParser, 'current_page_url')

def test_has_method_next_page_url():
    assert hasattr(walmartJSONParser, 'next_page_url')

def test_has_method_department_links():
    assert hasattr(walmartJSONParser, 'department_links')

def test_base_url_location():
    w = walmartJSONParser(_sample)
    assert w.base['searchContent']['preso']['pageMetadata']['canonical'].startswith("https://www.walmart.com")

# Ensure data comes from the right part of the json object
#   current_page_url - /searchContent/preso/pagination
def test_current_page_url_node():
    w = walmartJSONParser(_sample)
    assert w.current_page_url == 'https://www.walmart.com/browse/home/kitchen-dining/4044_623679?cat_id=4044_623679&%7B%22polaris%22%3A%7B%22rerankOffset%22%3A%221%22%7D%7D'

#   next_page_url - /searchContent/preso/pagination
def test_next_page_url_node():
    w = walmartJSONParser(_sample)
    assert w.next_page_url == 'https://www.walmart.com/browse/home/kitchen-dining/4044_623679?page=2&cat_id=4044_623679'

#   department_links - /searchContent/preso/facets -> Departments
def test_department_links():
    w = walmartJSONParser(_sample)
    assert len(w.department_links) == 14
    # department object should have the following properties:
        # id (e.g., "4044_623679")
        # name (e.g., "Kitchen & Dining")
        # url (typically a query string)
        # baseSeoURL (e.g., /browse/home/kitchen-dining/4044_623679)
    assert not any([{'id','name','url','baseSeoURL'} - set(i.keys()) for i in w.department_links])

# Just to prove I can mock my code...
# Most of my time testing has been spent with the `unittest` module but pytest
# is so much nicer to set up and work with generally... Although working with mocks
# in unittest you'll definitely learn the importance of minding the namespace
# you're mocking in, as well as fact that magic mock can return some very un-
# expected results (like creating a new mock object instead of returning the
# one you were working with from a function...)
def test_mock_method(mocker):
    mocker.patch.object(walmartJSONParser, 'get_base_url')
    walmartJSONParser.get_base_url.return_value = "testy testy - it's the besty"
    w = walmartJSONParser(_sample)
    assert w.url == "testy testy - it's the besty"

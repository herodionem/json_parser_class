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

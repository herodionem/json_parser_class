# Walmart JSON Parser Class

This demo class provides several methods / properties that give some introspection into a json object that might appear on a given Walmart web page.

I chose to use properties instead of functions to surface a lot of this data because I tend to prefer to leave calling actual functions to things that will actually change the state of something; like the "current_page_url". I could have the `next_page_url` both as a property and function - the property surfaces the text value of the next webpage in the pagination list, and the function could actually reassign the current page url attribute to be the next page url (thus allowing the next page url property to reflect that same stateful change to the current page) Obviously that's not fully implemented in this rudimentary demonstration.

Due to the ever-changing nature of retailer websites, I would allow these "stateful" sorts of classes to retrieve much of their configurations from a database. For example, the string that determines the JSONpath search location for the url. The position in the JSON could easily change, depending on the day, location, or even the browser you are using. Each of these scenarios could have a specific solution that would be handled by simply loading the relevant configuration at the time the class object gets instantiated.

## Run the Tests

1. Navigate to the root directory of the repo
1.5 run `python -m venv py_env && source py_env/bin/activate`
2. run `pip install -r requirements.txt`
3. run `python -m pytest` -- pytest will auto-discover any tests it could run


### extra methods I might include off the top of my head:
    - department_list: attribute - return formatted list of department names and/or urls
    - get_department_list: generator - yields the list one at a time in a specified format
    - next_page: method - sets next page url to the current page

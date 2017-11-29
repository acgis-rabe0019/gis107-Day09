# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        exercise_template_tests.py
#
# Purpose:     Test functions for functions in exercise_template.py
#
# Author:      David Viljoen
#
# Created:     24/11/2017
#-------------------------------------------------------------------------------

import sys
import inspect
import world_pop_explorer as wpe
reload(wpe)

# Add import statement for the module under test as follows:
# import module_under_test as alias

# For example:
# import world_pop_explorer as wpe
# reload(wpe)

def main():
    # Find and call all functions that begin with "test"
    test_funcs = get_test_functions()
    for test_func in test_funcs:
        test_func()

# Copy/paste/change the test template below to create new test functions, where:
#    - the test function name must begin with the word "test"
#    - desc = Description of the test being made
#    - expected = Expected result from calling the function
#    - actual = Actual result from calling the function
#    - func = Function being tested (the actual function, not the name)"""
#
def template_for_test_functions():
    desc = ""
    expected = ""
    actual = ""
    print_test_results(func, desc, expected, actual)

# ------------------------------------------------------------------------------

def test_get_country_count():
    desc = "Get count of countries in list"
    expected = 233
    actual = wpe.get_country_count()
    print_test_results(wpe.get_country_count, desc, expected, actual)

def test_conv_num_with_commas():
    desc = "convert a number with commas (str) to a number."
    expected = 1244787
    actual = wpe.conv_num_with_commas('1,244,787')
    print_test_results(wpe.conv_num_with_commas, desc, expected, actual)

def test_get_top_five_countries():
    desc = "Get top five most populated countries in list"
    expected = ['China', 'India', 'United States', 'Indonesia', 'Brazil']
    actual = wpe.get_top_five_countries()
    print_test_results(wpe.get_top_five_countries, desc, expected, actual)

def test_set_country_populations_dict():
    desc = "country population dict where key is country name and value is a tuple with 2 values"
    expected = {'China':('1,409,517,397','+0.4%')}
    actual = wpe.set_country_populations_dict()
    print_test_results(wpe.set_country_populations_dict, desc, expected, actual)

def test_get_population():
    desc = "Get population for specified country"
    expected = '1,409,517,397'
    actual = wpe.get_population('China')
    print_test_results(wpe.get_population, desc, expected, actual)

def test_get_continents():
    desc = "Get list of continents"
    expected = ''
    actual = wpe.get_continents()
    print_test_results(wpe.get_population, desc, expected, actual)

def test_get_continent_population():
    desc = "Return dictionary with key is cont name and value is the total for the population"
    expected = ''
    ##actual = wpe.get_continent_populations('North America')
    ##print_test_results(wpe.get_population, desc, expected, actual)
# ------------------------------------------------------------------------------
# Test template helper functions.  Code in this section should not need to
# modified.
#
def get_test_functions():
    """Returns a list of functions that begin with the word test in the order
       they appear in this file."""

    test_funcs = [obj for name,obj in inspect.getmembers(sys.modules[__name__])
                     if (inspect.isfunction(obj) and name.startswith('test'))]
    src = inspect.getsource(sys.modules[__name__])
    lines = src.split('\n')

    # Create a dictionary with key=function name and value is 0-based order
    # in the module
    ordered_func_names = dict()
    ordered_funcs = list()
    func_index = 0
    for line in lines:
        if line.find("def test") > -1 and not line.find('line.find') > -1:
            func_name = line.split("(")[0].split()[1]
            ordered_func_names[func_name] = func_index
            # Create an empty list with sampe number of elements as test
            # functions
            ordered_funcs.append('')
            func_index += 1
    for test_func in test_funcs:
        index = ordered_func_names[test_func.__name__]
        ordered_funcs[index] = test_func
    return ordered_funcs

def print_test_results(func_tested, desc, expected, actual):
    """func_tested is the function being tested
       desc = Test description
       expected = Expected result of test
       actual = Actual result of test """

    if not callable(func_tested):
        raise Exception("{} is not a function".format(func_tested))

    func_name = func_tested.__name__
    if expected == actual:
        print "PASSED: {}".format(func_name)
        print "Detail: {}".format(desc)
    else:
        print "FAILED: {}".format(func_name)
        print "Desc:   {}".format(desc)
        print "Expect: {}".format(expected)
        print "Actual: {}".format(actual)
    print ""

if __name__ == '__main__':
    main()

# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        world_pop_explorer.py
#
# Purpose:     Provide some functions to analyze the data in
#              world_pop_by_country.py
#
# Author:      David Viljoen
#
# Created:     24/11/2017
#-------------------------------------------------------------------------------

from world_pop_by_country import data as country_populations

# Key = country and value is number (i.e. not text containing commas)
#
country_populations_dict = dict()

def main():
    lines = country_populations.split('\n')
    print "country_populations has the following columns:"
    print lines[0]
    print repr(lines[0])
    ci = lines[162]
    print "\nData is UTF-8 encoded.  That is, printed as is:"
    print ci
    print "\nData prined with .decode('utf-8'):"
    print ci.decode('utf-8')

def get_country_count():
    """Return the number of countries in country_populations.  Create a list
	   where each element of the list contains a line of data from
	   country_populations and return the length of this list"""
    numbers=country_populations.split('\n')
    count_numbers= len(numbers)-1
    return count_numbers


def conv_num_with_commas(number_text):
    """Convert a number with commas (str) to a number.
       e.g. '1,000' would be converted to 1000"""
    number=number_text.split(',')
    item=''
    for numero in number:
        item+=numero
    final_number=float(item)
    return final_number

def get_top_five_countries():
    """Return a list of names of the top five countries in terms of population"""
    countries=country_populations.split('\n')
    top_5=[]
    count=0
    for country in countries:
        if count<6:
            data= country.split('\t')
            top_5.append(data[1])
            count+=1
    top_5.remove('Country')
    return top_5


def set_country_populations_dict():
    """Sets the country_populations_dict dictionary where key is country name
         and value is a tuple containing two elements:
            1. A numeric version of the comma separated number in the
               Pop 01Jul2017 column
            2. The % decrease as a number
    """
    countries=country_populations.split('\n')
    for country in countries:
        country_data= country.split('\t')
        name= country_data[1]
        pop_2017= country_data[5]
        percentage= country_data[6]
        country_populations_dict.update({name:(pop_2017,percentage)})
    return country_populations_dict


def get_population(country_name):
    """Given the name of the country, return the population as of 01Jul2017
       from country_populations_dict.  If the country_populations_dict is
       empty (i.e. no keys or values), then run set_country_populations_dict
       to initialize it."""
    country_population=set_country_populations_dict()
    country_data=country_population[country_name]
    population_data=country_data[0]
    return population_data


def get_continents():
    """Return the list of continents"""
    data=country_populations.split('\n')
    continents=[]
    unique_cont=[]

    for country in data:
        split_data= country.split('\t')
        continents.append(split_data[2])
    for cont in continents:
        if cont != "Continent":
            if continents.count(cont)>1:
                while continents.count(cont)>1:
                    continents.remove(cont)
                unique_cont.append(cont)
    return unique_cont

def get_continent_populations():
    """Returns a dict where the key is the name of the continent and
       the value is the total of all countries on that continent"""
    continents=["Asia","Europe","Americas","Africa","Oceania"]
    Asia=0
    Europe=0
    Americas=0
    Africa=0
    Oceania=0
    continent_population_dict=dict()
    data=country_populations.split('\n')

    for country in data:
        country_data= country.split('\t')

        if country_data[2]==continents[0]:
            Asia+=conv_num_with_commas(country_data[5])
        if country_data[2]==continents[1]:
            Europe+=conv_num_with_commas(country_data[5])
        if country_data[2]==continents[2]:
            Americas+=conv_num_with_commas(country_data[5])
        if country_data[2]==continents[3]:
            Africa+=conv_num_with_commas(country_data[5])
        if country_data[2]==continents[4]:
            Oceania+=conv_num_with_commas(country_data[5])
    continent_population_dict[continents[0]]=Asia
    continent_population_dict[continents[1]]=Europe
    continent_population_dict[continents[2]]=Americas
    continent_population_dict[continents[3]]=Africa
    continent_population_dict[continents[4]]=Oceania
    return continent_population_dict
if __name__ == '__main__':
    main()


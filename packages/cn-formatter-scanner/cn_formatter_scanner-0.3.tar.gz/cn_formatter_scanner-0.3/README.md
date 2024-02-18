#Title Formatter Python Package
##Overview
The Title Formatter Python package is a lightweight utility designed to assist with the formatting of titles, specifically handling special characters, diacritics, and articles. Additionally, the package includes a function to generate a unique property key, which is derived using MD5 hashing based on the formatted title. This ensures that properties with similar attributes will have the same unique key.

### Installation
To install the Title Formatter package, use the following pip command:


Usage
Formatting Titles
To format a title, use the format_title function provided by the package. The function takes four parameters: title, city, state, and country. It returns the formatted title as a string.

`from formatter.formatter import CNFormatter`

### Input data
title = "The 100 Sůnşệţ Hòtệl - ĊĦŜẸ Ċệrťíƒíệd"
city = "London"
state = "England"
country = "United Kingdom"

### Format the title
formatted_title = format_title(title, city, state, country)
print("Formatted Title:", formatted_title)

### Generate property key
property_key = ft.get_property_key(title, city, state, country) == '208379f3bac1b0ac8548e12cf1097bbe'
print("Property Key:", property_key)

### Output: 
Formatted Title: 100sunset
Property Key: 5d41402abc4b2a76b9719d911017c592

```bash
Copy code
pip install title-formatter
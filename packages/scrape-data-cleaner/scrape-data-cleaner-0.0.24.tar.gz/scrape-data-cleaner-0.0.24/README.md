# Scrape Data Cleaner

Clean scraped data fields to recieve your disired text without unicodes,spaces and other unessesary quirks.

# Installation

`pip install scrape-data-cleaner`

# Basic Usage
```python
from cleaner import string_cleaner,price_cleaner,remove_char
print(string_cleaner('Iphone 8   plus \  '))
print(price_cleaner(remove_char('USD 100')))
```

# Modules

### **string_cleaner** :

Cleans strings strings encode and re-encode them in ASCII

### **string_cleaner_array :**

Takes an array of strings encode and re-encode them in ASCII then return an array.

### **string_cleaner_array_wine:**

Takes an array of strings encode and re-encode them in ASCII then return an array however during cleaning does not force removing of spaces and tabs.

### **price_cleaner:**

Performs string cleaning from `string_cleaner` then converts the response to `Integer`.

### **get_price:**

Extracts price from a rouge string then converts the response to `Integer`.

i.e **string="\a \t rr$12.5"** outputs `12`

### **remove_special_char :**

Removes special characters from string i.e.` * - &` e.t.c.

### **remove_char:**

Removes all characters and leaves out only integers.

### **remove_char_special:**

Removes all characters and leaves out only integers but first checks for `.00 `and replaces that with nothing to avoid getting price with extra 00.

### **cleanhtml:**

Extracts text from HTML and returns a string.

### **cleanhtml_array:**

Extracts text from an array of HTML and returns an array of strings.

### **cleanhtml_array2:**

Extracts text from an array of HTML and returns an array of strings however does `string_cleaner` for each string.

### **nbsp_replacer:**

Replaces unicode `\u00a0` with a space.

### **ratings_extractor:**

Extracts ratings from style for stars. Takes style of this format `width:80% `and converts that to a rating of 1 to 5.

### **specs_table_gen:**

Takes two arrays and combine them with **:** return one array.

### **space_tabs_remover:**

Removes spaces and tabs i.e if there is `\u,\r ,\n .` This is more aggressive.

### **extract_list:**

Extracts text in HTML list`li`from a HTML block. Takes raw HTML and returns an array of strings.

### **gen_link2:**

Receives two strings name of store and the link then creates a custom url 

i.e 

`gen_link2('amazon','https://amazon/product/iphone-7.html')`

**Results:**` /amazon/iphone-7`

### **simple_split:**

Receives two strings name of store and the link then creates a custom url 

i.e 

`simple_split('amazon','/iphone-7/product')`

**Results:**` /amazon/iphone-7__product`

### **extract_from_ldjson:**

Extract a value from ld/json. i.e` extract_from_ldjson(ld_json,'name')` will extract the name value in the ld/json.

### **table_shaker:**

Only works if your using scrapy. Takes the HTML block with the table and an array of the types of data in table. i.e` table_shaker(response.css('table'),['td','td'])`.

 **Note:** Array can be `['th','td']`,`['th','th'] `depending on the table.

### **get_description :**

Extracts description from HTML and returns an array with dictionaries with keys of either text or title. Takes Raw HTML.

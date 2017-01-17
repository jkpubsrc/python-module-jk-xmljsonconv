jk_xmljsonconv
==============

Introduction
------------

This python module provides possibilities to convert XML to JSON vice versa through a conversion manager.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/python-module-jk-xmljsonconv)
* [pypi.python.org](https://pypi.python.org/pypi/jk_xmljsonconv)

How to use this module
----------------------

### Requirements

This module will require the following python modules to operate:

* [jk_temporary](https://github.com/jkpubsrc/python-module-jk-temporary) - License: Apache 2.0
* [dicttoxml](https://pypi.python.org/pypi/dicttoxml) - License: GPL2
* [xmltodict](https://pypi.python.org/pypi/xmltodict) - License: MIT

### Import

To import this module use the following statement:

```python
import jk_xmljsonconv
```

### Initializing the format converter main object

It is very simple to prepare the main converter object for use:

```python
c = jk_xmljsonconv.FormatConverter(tempDirPath)
```

The variable `tempDirPath` must provide an exsting and empty directory. Here temporary files required during conversion will be stored.

Files created in this temporary directory will be provided to the caller. If you request a file from the converter it will create
one for you. It is your resposibility to move the file to whichever place you want it to be after the conversion process. (Or delete
the file if you decide to not use the file any more.)

### List the formats and conversions supported

To get an overview about what kind of conversions are supported, run the following code:

```python
print("The following formats are supported: " + str(c.listFormats()) + "\n")
print("The following format conversions are supported: " + str(c.listConversions()) + "\n")
```

This will output something like this:

    The following formats are supported: ['json', 'jsonfile', 'jsonstr', 'xml', 'xmlfile', 'xmlstr']

    The following format conversions are supported: ['json->jsonfile', 'json->jsonstr', 'json->xml',
    'json->xmlfile', 'json->xmlstr', 'jsonfile->json', 'jsonfile->jsonstr', 'jsonfile->xml', 'jsonfile->xmlfile',
    'jsonfile->xmlstr', 'jsonstr->json', 'jsonstr->jsonfile', 'jsonstr->xml', 'jsonstr->xmlfile',
    'jsonstr->xmlstr', 'xml->json', 'xml->jsonfile', 'xml->jsonstr', 'xml->xmlfile', 'xml->xmlstr',
    'xmlfile->json', 'xmlfile->jsonfile', 'xmlfile->jsonstr', 'xmlfile->xml', 'xmlfile->xmlstr',
    'xmlstr->json', 'xmlstr->jsonfile', 'xmlstr->jsonstr', 'xmlstr->xml', 'xmlstr->xmlfile']

The file formats supported are:

| File Format ID | Data Type     | Description                                                      |
| -------------- | ------------- | ---------------------------------------------------------------- |
| json           | json-object   | An object that can be a used as a JSON data structure in memory. |
| jsonfile       | string        | The file path of a JSON file.                                    |
| jsonstr        | string        | The JSON data provided as a string.                              |
| xml            | xml-object    | An object that can be a used as an XML data structure in memory. |
| xmlfile        | string        | The file path of an XML file.                                    |
| xmlstr         | string        | The XML data provided as a string.                               |

The file conversion IDs are built from these IDs.

### Perform a conversion

It is very easy to perform a conversion:

```python
resultData = str(c.convert1(convID, inputData))
```

F.e. if you provide an XML string this could look like this:

```python
SOME_XML_INPUT = "<?xml version=\"1.0\"?><html><body><h1>Some heading</h1><div><p>Some text.</p></div></body></html>"

resultData = str(c.convert1("xmlstr->jsonstr", SOME_XML_INPUT))
```

With `resultData` containing the following string after conversion:

```
{"html":{"body":{"h1":"Some heading","div":{"p":"Some text."}}}}
```

Methods of class FormatConverter
--------------------------------

The next lines declare the methods the `FormatConverter` class will provide:

```python
#
# Constructor method.
#
# @param		object tempDir			Either provide a directory path here for temporary files or a <c>TempDir</c> object.
#
def __init__(self, tempDir)
```

```python
#
# Get a list of formats supported.
#
# @return		string[]		Returns a list of IDs.
#
def listFormats()
```

```python
#
# Get a list of all conversions supported.
#
# @return		string[]		Returns a list of IDs.
#
def listConversions()
```

```python
#
# Convert the input data.
#
# @param		string convID			A conversion ID such as f.e. "xmlstr->jsonstr".
# @param		object inputData		The input data. The type of this data must correlate with the source format type specified.
# @return		object					The result data. The type of this data will depend on the conversion specified.
#
def convert1(convID, inputData)
```

```python
#
# Convert the input data.
#
# @param		string fromFormat		The source format of the conversion.
# @param		string toFormat			The target format desired.
# @param		object inputData		The input data. The type of this data must correlate with the source format type specified.
# @return		object					The result data. The type of this data will depend on the conversion specified.
#
def convert2(fromFormat, toFormat, inputData)
```

```python
#
# Get a converter by conversion ID.
#
# @param		string convID			A conversion ID such as f.e. "xmlstr->jsonstr".
# @return		AbstractConverter		Eiter returns <c>None</c> if no converter is available or the converter object that performs the conversion.
#
def getConverter1(convID)
```

```python
#
# Get a converter by conversion ID.
#
# @param		string fromFormat		The source format of the conversion.
# @param		string toFormat			The target format desired.
# @return		AbstractConverter		Eiter returns <c>None</c> if no converter is available or the converter object that performs the conversion.
#
def getConverter2(fromFormat, toFormat)
```

Contact Information
-------------------

This is Open Source code. That not only gives you the possibility of freely using this code it also
allows you to contribute. Feel free to contact the author(s) of this software listed below, either
for comments, collaboration requests, suggestions for improvement or reporting bugs:

* Jürgen Knauth: jknauth@uni-goettingen.de, pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0




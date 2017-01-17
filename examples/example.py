#!/usr/bin/env python3
# -*- coding: utf-8 -*-





import os
import sys
import sh

import jk_xmljsonconv




SOME_XML_INPUT = "<?xml version=\"1.0\"?><html><body><h1>Some heading</h1><div><p>Some text.</p></div></body></html>"

TEMP_DIR_PATH = "/tmp/jk_xmljsonconv"

if not os.path.isdir(TEMP_DIR_PATH):
	os.mkdir(TEMP_DIR_PATH)




c = jk_xmljsonconv.FormatConverter(TEMP_DIR_PATH)

print("The following formats are supported: " + str(c.listFormats()) + "\n")
print("The following format conversions are supported: " + str(c.listConversions()) + "\n")


print("Demonstrating the conversion capabilities ...")

for convID in ["xmlstr->jsonstr", "xmlstr->json", "xmlstr->jsonfile"]:
	print("\t" + convID + " : " + str(c.convert1(convID, SOME_XML_INPUT)))

print()















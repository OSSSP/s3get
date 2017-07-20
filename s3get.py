#!/usr/bin/env python

import subprocess
import os.path
import sys
import urllib2
from xml.etree.ElementTree import parse

def main():
    xml = getXML()
    parseXML(xml)

def getXML():
    response = urllib2.urlopen(sys.argv[1])
    xml = response.read()
    if os.path.isfile('data.xml'):
        os.remove('data.xml')
    with open('data.xml', 'a') as f:
        f.write(xml)
    doc = parse('data.xml').getroot()
    return doc

def parseXML(xml):
    for child in xml:
        for contents in child[:1]:
            key = contents.text
            downloadFile(key)

def downloadFile(key):
    cmd = 'wget '+sys.argv[1]+key
    subprocess.call(cmd, shell=True)

if __name__=='__main__':
    main()

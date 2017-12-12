#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


# Lädt alle Eigenschaften der aaindex1.txt in eine Liste
# Out: Liste mit aaIndex-Eigenschaften
def parseAaIndex():
    source = "data/aaindex1.txt"
    if not os.path.isfile(source):
        source = "../data/aaindex1.txt"
    input_file = open(source, "r")
    lines = input_file.read().splitlines()
    totalaaIndex = []
    counter = 0
    for i in range(len(lines)):
        if lines[i][0] == "I":
            bothLines = lines[i + 1] + lines[i + 2]
            partielaaIndex = bothLines.split()
            totalaaIndex.append(partielaaIndex)
            counter += 1
    input_file.close()
    return totalaaIndex


# Entfernt Eigenschaften in denen NA vorkommt und Floatet die Liste
# Out: neue Liste der aaIndex-Eigenschaftens
def getFeaturesforAAX():
    a = parseAaIndex()
    rmv = []
    for feature in a:
        if 'NA' in feature:
            rmv.append(feature)
    for feature in rmv:
        a.remove(feature)
    lst = []
    for feature in a:
        b = map(float, feature)
        lst.append(b)
    return lst

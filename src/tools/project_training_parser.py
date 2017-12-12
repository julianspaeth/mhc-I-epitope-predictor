#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


# Lädt Trainingsdatensatz in einen Array
# Out: Trainingsdaten, Liganden und Labels
def parseProjectTraining():
    training_data = []
    source = "data/project_training.txt"
    if not os.path.isfile(source):
        source = "../data/project_training.txt"
    input_file = open(source, "r")
    ligands = []
    labels_str = []
    input_file.next()
    for line in input_file:
        ligands.append(line.split(None, 1)[0])
        labels_str.append(line[-2])
    input_file.close()
    labels = []
    for i in range(len(labels_str)):
        labels.append(int(labels_str[i]))
    for x in range(0, len(ligands)):
        training_data.append([ligands[x], labels[x]])

    return training_data, ligands, labels

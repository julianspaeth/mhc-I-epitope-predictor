#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hier befinden sich die Methoden zur Vorverarbeitung der Trainingsdaten und Inputdaten
import tools.project_training_parser as project_training_parser
import tools.total_aaindex_parser as total_aaindex_parser
import numpy as np
from sklearn.externals import joblib
from sklearn import preprocessing
from sklearn.feature_selection import SelectPercentile, f_classif

# Lädt Trainingsdaten von training_data.txt
trainingData, ligands, labels = project_training_parser.parseProjectTraining()


# Gibt Trainingsdaten aus
# Out: Trainingsdaten
def getTrainingData():
    return trainingData


# Gibt Liganden der Trainingsdaten aus
# Out: Liganden des Trainingsdatensatzes
def getLigands():
    return ligands


# Gibt Labels der Trainingsdaten aus
# Out: Labels des Trainingsdatensatzes
def getLabels():
    return labels


# Gibt Liste mit Features für die Trainingsdaten aus
# Out: Features für Aminosäuren
def getFeaturesForAS(x):
    features_for_as = []
    for feature in total_aaindex_parser.getFeaturesforAAX():
        features_for_as.append(feature[x])
    return features_for_as


# Weist jeder Aminosäure seine Features zu
# Out: Dictionary das jeder Aminosäure seine Eigenschaften zuweist
def setAllFeatures():
    aas = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]
    feature_dic = {}
    for x in range(0, len(aas)):
        feature_dic.update({aas[x]: getFeaturesForAS(x)})
    return feature_dic


# Stellt Peptide als Feature-Vektor dar
# In: Liganden und Features
# Out: Liganden als Feature-Vektor
def featureLigands(ligands, features):
    a = setAllFeatures()
    number_of_features = len(a["A"])
    ligands_featured = []
    for x in range(0, len(ligands)):
        peptide = []
        for y in range(0, number_of_features):
            for char in ligands[x]:
                peptide.append(features[char][y])
        ligands_featured.append(peptide)
    return ligands_featured


# Bereitet Trainingsdaten für SVM auf
# Out: Skalierte und Selektierte Features und Labels der Trainingsdaten
def prepareTrainingData():
    # Einlesen der Trainingsdaten und casten in Numpy Array
    labels = np.array(getLabels())
    features = np.array(featureLigands(getLigands(), setAllFeatures()))
    # Skalierung der Trainingsdaten mit MinMaxScaler
    scaler = preprocessing.MinMaxScaler()
    scaled_features = scaler.fit_transform(features)
    # Feature Selection mit 10 Percentil
    selector = SelectPercentile(f_classif, percentile=10)
    selector.fit(scaled_features, labels)
    # Speichere Selektor um ihn bei INPUT später auch zu verwenden
    joblib.dump(selector, '../selector/selector.pkl')
    selected_features = selector.transform(scaled_features)
    return selected_features, labels


# Bereitet Input-Daten fuer SVM auf
# In: Liganden aus Input
# Out: Skalierte und Selektierte Feature-Vektoren des Inputs
def prepareData(ligands):
    # Skalierung mit MinMaxScaler
    scaler = preprocessing.MinMaxScaler()
    scaled_features = scaler.fit_transform(np.array(featureLigands(ligands, setAllFeatures())))
    # Feature Selection mit Selektor aus Trainingsvorgängen
    selector = joblib.load('selector/selector.pkl')
    selected_features = selector.transform(scaled_features)
    return selected_features

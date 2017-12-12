#!/usr/bin/python
# -*- coding: utf-8 -*-

# Führt eine Stratified 10-Fold Kreuzvalidierung auf den Trainingsdaten aus, um die Qualität zu beurteilen
import tools.svm_methods as svm_methods

meanAUC = 0
meanFPR = 0
meanTPR = 0
counter = 0
#Führe Kreuzvalidierung durch (10 Stratified-KFold)
for ligands_train, ligands_test, labels_train, labels_test in svm_methods.skfCV():
    #Grid-Search jeweils für die 10 Datensätze
    svm = svm_methods.svmGridFit(ligands_train, labels_train)
    #Vorhersage der Labels für die jeweils 10 Datensätze
    predicted_labels = svm_methods.svmPredict(svm, ligands_test)
    #Zeige AUC für die jeweils 10 Datensätze
    print(svm_methods.getAUC(predicted_labels, labels_test))
    #Berechne mittleren AUC
    meanAUC = meanAUC+svm_methods.getAUC(predicted_labels, labels_test)
    fpr, tpr = svm_methods.getFprTpr(predicted_labels, labels_test)
    meanFPR = meanFPR+fpr
    meanTPR = meanTPR+tpr
    counter = counter + 1
#Zeige Mittleren AUC Wert der 10 Durchgänge
meanAUC = meanAUC/counter
meanFPR = meanFPR/counter
meanTPR = meanTPR/counter
print("MEAN AUC: %s" % (meanAUC))
svm_methods.plotMeanROC(meanFPR, meanTPR)
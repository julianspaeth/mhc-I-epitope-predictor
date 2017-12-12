#!/usr/bin/python
# -*- coding: utf-8 -*-

# Eine neue SVM wird erstellt und in das SVM-Verzeichnis gespeichert
# Die SVM wird auf dem kompletten Datensatz trainiert

import prep
import svm_methods
from sklearn.externals import joblib

# Bereite Daten für SVM auf
features, labels = prep.prepareTrainingData()
# Grid-Search für kompletten Trainingsdatensatz
svm = svm_methods.svmGridFit(features, labels)
# Sage Labels für Trainingsdatensatz vorraus
# predicted_labels = svm_methods.svmPredict(svm, features)
# Zeige Ergebnisse der Vorhersage an
# svm_methods.showResults(predicted_labels, labels)
# svm_methods.plotROC(predicted_labels, labels)
# Speichere SVM
joblib.dump(svm, '../svm/svm.pkl')

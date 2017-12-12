#!/usr/bin/python
# -*- coding: utf-8 -*-

import tools.prep as prep
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt


# Hier befinden sich die Methoden zum erstellen und trainieren einer SVM

# 10-Stratified-KFold Kreuzvalidierung der Daten
# Out: Jeweils Folds des Datensatzes
def skfCV():
    # Liest aufbereitete Trainingsdaten ein
    features, labels = prep.prepareTrainingData()
    # Initialisiere SKF mit 10 Folds
    skf = StratifiedKFold(labels, n_folds=10)
    # Teile Datensatz in Folds auf
    for train, test in skf:
        features_train, features_test, labels_train, labels_test = features[train], features[test], labels[train], \
                                                                   labels[test]
        yield features_train, features_test, labels_train, labels_test


# SVM mit Grid-Search
# In: Features und Labels
# Out: SVM mit bestem Parameter
def svmGridFit(features, labels):
    param_grid = [{'C': [1, 10, 20, 30, 40, 50, 100, 500, 750, 1000], 'gamma': [0.1, 0.01, 0.001, 0.002, 0.003, 0.005]}]
    svm = SVC(kernel='rbf', cache_size=1000, class_weight='balanced')
    clf = GridSearchCV(svm, param_grid=param_grid, cv=10, scoring='roc_auc')
    clf.fit(features, labels)
    # print "Best parameters: %s" % clf.best_params_
    return clf


# Vorhersage der Labels für Input
# In: Input-Features
# Out: Vorhergesagte Labels
def svmPredict(clf, input):
    pred_labels = clf.predict(input)
    return pred_labels


# Zeigt Anzahl der Binder und Nicht-Binder an
# In: Labels
# Out: Binder, nicht-Binder
def showBinder(labels):
    binder = 0
    nonBinder = 0
    for p in labels:
        if p == 1:
            binder = binder + 1
        else:
            nonBinder = nonBinder + 1
    return binder, nonBinder


# Gibt FPR und TPR einer Vorhersage heraus
# In: Vorhergesagt Labels, Test Labels
# Out: FPR, TPR
def getFprTpr(pred_labels, test_labels):
    fpr, tpr, thresholds = roc_curve(test_labels, pred_labels)
    return fpr, tpr


# Plottet ROC Kurve aus FPR und TPR
# In: False Positive Rate, True Positiv Rate
# Out: ROC-Plot
def plotMeanROC(fpr, tpr):
    roc_auc = auc(fpr, tpr)
    plt.title('Receiver Operating Characteristic')
    plt.plot(fpr, tpr, 'b', label='AUC = %0.2f' % roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([-0.1, 1.2])
    plt.ylim([-0.1, 1.2])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    print("ROC-Curve plotted")
    plt.show()


# Plottet ROC Kurve von der Vorhersage
# In: Vorhergesagte Labels, Test Labels
# Out: ROC-Plot
def plotROC(pred_labels, test_labels):
    false_positive_rate, true_positive_rate, thresholds = roc_curve(test_labels, pred_labels)
    roc_auc = auc(false_positive_rate, true_positive_rate)
    plt.title('Receiver Operating Characteristic')
    plt.plot(false_positive_rate, true_positive_rate, 'b', label='AUC = %0.2f' % roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([-0.1, 1.2])
    plt.ylim([-0.1, 1.2])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    print("ROC-Curve plotted")
    plt.show()


# Gibt Ergebnisse der Vorhersage aus
# In: Vorhergesagte Labels, Testlabels
# Out: Zeigt Anzahl der Binder, nicht-Binder und AUC an
def showResults(pred_labels, test_labels):
    binder, nonBinder = showBinder(pred_labels)
    false_positive_rate, true_positive_rate, thresholds = roc_curve(test_labels, pred_labels)
    roc_auc = auc(false_positive_rate, true_positive_rate)
    print("SVM predicted %s binder and %s nonBinder. AUC = %s" % (binder, nonBinder, roc_auc))


# Ermittelt AUC der Vorhersage
# In: Vorhergesagte Labels, Testlabels
# Out: AUC der Vorhersage
def getAUC(pred_labels, test_labels):
    false_positive_rate, true_positive_rate, thresholds = roc_curve(test_labels, pred_labels)
    roc_auc = auc(false_positive_rate, true_positive_rate)
    return roc_auc

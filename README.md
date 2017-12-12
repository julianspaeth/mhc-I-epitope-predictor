# mhc-I-epitope-predictor
MHC-class-I epitope binding predictor based on a SVM. 

MHC-Klasse-I Moleküle spielen seit einigen Jahren eine wichtige Rolle in der Entwicklung von Impfstoffen. Mit ihnen ist es möglich, die derzeit immer häuﬁger verwendeten Epitop-basierten Impfstoffe einerseits sehr efﬁzient zu machen und andererseits die Nebenwirkungen von klassischen Impfstoffen zu umgehen. Mit Hilfe von maschinellen Lernverfahren, hier einer Support Vektor Maschine (SVM), lassen sich efﬁziente und genaue Vorhersagen für mögliche MHC-I-Epitope machen. Die hier vorgestellte Methode sagt für 9-mer Peptide voraus, ob sie an einem MHC-I-Molekül binden oder nicht. Das Programm wurde in Python mit scikit-learn umgesetzt und generiert aus einer Input-Datei mit Peptiden der Länge 9 eine Output-Datei, in der jedem der eingegebenen Peptiden die Eigenschaft "Binder" (1) oder "Nicht-Binder" (0) zugeordnet wird. Die SVM wurde auf einem Trainingsdatensatz für ein unbekanntes HLA-Klasse-1 Allel mit 727 9-mer Peptiden trainiert und hat mit einem mittleren AUC-Wert von 0.85 eine relativ hohe Vorhersagegenauigkeit.

## Programme und Frameworks
Die folgenden Programme werden benötigt:

Python 		2.7.11
Numpy		1.11.0
SciPy 		0.16.1
Scikit-learn	0.17.0
(Matplotlib	1.5.1)

## Programm ausführen
Alle Befehle müssen in der Python-Umgebung ausgeführt werden.

Ausführen des Programms:
	> main.py --input <Pfad/zum/Input> --output <Name_des_Output>
	(beim Output muss eine Dateiendung angegeben werden, z.B. .txt)

Hilfe anzeigen lassen:
	> main.py -h

Debugmodus aktivieren:
	> main.py -d

neue SVM trainieren und speichern (falls svm.pkl nicht vorhanden):
	> tools/svm.py 

## Input/Output

Es werden ausschließlich Input-Files mit dem folgenden Aufbau akzeptiert:
	<sequence1>
	<sequence2>
	<sequence3>
	<sequence4>
	...

Der Output wird mit folgendem Aufbau generiert:
	<sequence1><tab><classification>
	<sequence2><tab><classification>
	<sequence3><tab><classification>
	<sequence4><tab><classification>
	...
		
## Authors: Julian Späth, Rehan App & Kevin Krumm




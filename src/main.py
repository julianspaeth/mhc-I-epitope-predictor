#!/usr/bin/python

from optparse import OptionParser, OptionGroup
import tools
from sklearn.externals import joblib


DEBUG = False

# print debug messages and errors
def debug(s):
    if DEBUG:
        print("DEBUG: " + s)


def error(s):
    print("ERROR: " + s)


# read the input file and parse the lines
def parseAndReadInput(s):
    try:
        source = s
        datei = open(source, "r")
        lines = datei.read().splitlines()
        new_lines = []
        for line in lines:
            # remove whitespace and tab
            new_line = line.replace(' ','')
            new_line = new_line.replace('\t','')
            if(len(new_line) == 9):
                new_lines.append(new_line)
        debug("Got input: %s" % new_lines)
        return new_lines
    except Exception as e:
        error("Couldn't read input file: %s" % str(e))
        return None


# main method with menu
if __name__ == '__main__':
    # build menu structure
    usage = "\nCopyright (C) 2016 App, Krumm, Spaeth - Use at your own risk!\n" + \
            "description: this is an SVM based MHC-I predictor \n\n" + \
            "Input file required."

    parser = OptionParser(usage)
    parser.add_option("-d", "--debug",
                      action="store_true", dest="debug", default=False)

    option_group = OptionGroup(parser, "Open input file")
    option_group.add_option("--input", dest="input",
                            help="path to the input file")
    option_group.add_option("--output", dest="output",
                            help="name of the generated output file")
    parser.add_option_group(option_group)

    (options, args) = parser.parse_args()

    DEBUG = options.debug

    # if input is given:
    # set input path, read and parse input, execute svm
    if options.input and options.output:
        debug("Reading input file: " + options.input)
        input_list = parseAndReadInput(options.input)
        features = tools.prep.prepareData(input_list)
        try:
            debug("Loading existing svm...")
            svm = joblib.load('svm/svm.pkl')
        except Exception as e:
            error("Couldn't load svm file: %s \n +"
                  "-> First execute tools/svm.py to generate a svm." % str(e))
        # save prediction in file
        predicted_labels = tools.svm_methods.svmPredict(svm, features)
        try:
            out_file = open("%s" % options.output, "w+")
            for x in range(0, len(input_list)):
                out_file.write("%s\t%s\n" % (input_list[x], predicted_labels[x]))
            debug("Generated output file %s" %options.output)
        except Exception as e:
            error("Could't create output file: %s" % str(e))
    else:
        error("No input and output given!")

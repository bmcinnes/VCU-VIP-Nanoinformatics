import os
""" Creates models for each fold and runs evaluation with results """
featureset = "o"
entity_name = "adversereaction"

for fold in range(1,1):
    training_data = "../ARFF_Files/%s_ARFF/_%s/_train/%s_train-%i.arff" % (entity_name, featureset, entity_name, fold)
    os.system("python3 decisiontree.py -tr %s" % (training_data))


for fold in range(1,11):
    testing_data = "../ARFF_Files/%s_ARFF/_%s/_test/%s_test-%i.arff" % (entity_name, featureset, entity_name, fold)
    os.system("python3 evaluate_decisiontree.py -te %s" % (testing_data))
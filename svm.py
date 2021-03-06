# used for csv data manipulation
import pandas as pd 

# used in obtaining arguments
import sys

# used for svm and the metrics 
from sklearn import svm, metrics

# used for getting project constants
import constants as c

# used for exporting model
from joblib import dump, load

# for stats
import numpy as np

# accepts arguments
# sys.argv[1] = filepath to the output.csv
# sys.argv[2] = percentage for training (optional)

if len(sys.argv) > 1:
    csv_file = sys.argv[1]
    try:
        try:
            TRAIN_PERCENT_IN_DECIMAL = float(sys.argv[2])
        except Exception as iden:
            TRAIN_PERCENT_IN_DECIMAL = c.TRAIN_PERCENT
        data = pd.read_csv(csv_file)
    except Exception as e:
        print("Please input the correct .CSV file.")
        exit()
else:
    print("Please include the path to the csv file (output.csv) in the arguments")
    exit()

# informative print statements
print(str(data.shape[0]) + " rows obtained.")

# number of rows to obtain for training
train = int(TRAIN_PERCENT_IN_DECIMAL * data.shape[0])

args = list(sys.argv)
try:
    args.index('trainonly')
    train_data = data
    print("100% of " + str(csv_file) + " used for training." )
except Exception as identifier:
    print(str(TRAIN_PERCENT_IN_DECIMAL * 100) + "%" + " used for training. Remaining will be used for testing." )
    # splitting to train and testing
    train_data = data[['name','perceptual_spread','bark_length','interbark_interval','roughness', 'pitch','aggressive']][:train]
    testing_data = data[['name','perceptual_spread','bark_length','interbark_interval','roughness', 'pitch']][train:]

    # exporting csv for testing
    testing_data.to_csv('output_experiment.csv')

# training the model
svc = svm.SVC(kernel='rbf', C=55.0 ,gamma='scale')
# C is the penalty value 

val_split =  int(TRAIN_PERCENT_IN_DECIMAL * train_data.shape[0])
# making datasets for features and test
_features = train_data[['perceptual_spread','bark_length','interbark_interval','roughness', 'pitch']][:val_split]
_test = train_data[['aggressive']][:val_split]

# for validation
test_features = train_data[['perceptual_spread','bark_length','interbark_interval','roughness', 'pitch']][val_split:]
test_classes = train_data[['aggressive']][val_split:]

print(_features.shape[0], "for training")
print(test_features.shape[0], "for validation")

# training the SVM
svc.fit(_features,_test.values.ravel())

# predicting results
pred = svc.predict(test_features)

print("Confusion Matrix:\n" + str(metrics.confusion_matrix(test_classes,pred)))

print("Accuracy: " + str(metrics.accuracy_score(test_classes,pred)))

print("Is this ok? (y/n)")
choice = str(input()).lower()
if choice == 'y':
    print("Exporting model...")

    dump(svc,'model.joblib')

    print("Model Exported into model.joblib")
    
    # model testing (to test if the same model has been saved)
    print("Checking exported model...")
    svm2 = load('model.joblib')
    pred2 = svm2.predict(test_features)

    print("Confusion Matrix:\n" + str(metrics.confusion_matrix(test_classes,pred2)))

    print("Accuracy: " + str(metrics.accuracy_score(test_classes,pred2)))

else:
    new_data = data[['name','perceptual_spread','bark_length','interbark_interval','roughness', 'pitch','aggressive']]
    new_data = data.sample(frac=1).reset_index(drop=True)
    new_data.to_csv(csv_file)
    print("model not saved.")
    print("dataset", str(csv_file) ,"reshuffled")
#!/usr/bin/python

# This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

# Use a Naive Bayes Classifier to identify emails by their authors

# authors and labels:
# Sara has label 0
# Chris has label 1

import sys

sys.path.append("../tools/")

from sklearn.naive_bayes import GaussianNB as gnb
from email_preprocess import preprocess
from time import time


# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

# create classifier
clf = gnb()

t0 = time()

# fit the classifier on the training features and labels
clf.fit(features_train, labels_train)

print "training time:", round(time() - t0, 3), "s"

accuracy = clf.score(features_test, labels_test)

print(accuracy)


#########################################################

#!/usr/bin/python

import matplotlib as mpl

# mpl.use("TkAgg")

from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture


features_train, labels_train, features_test, labels_test = makeTerrainData()


# the training data (features_train, labels_train) have both "fast" and "slow"
# points mixed together--separate them so we can give them different colors
# in the scatterplot and identify them visually
grade_fast = [features_train[ii][0]
              for ii in range(0, len(features_train)) if labels_train[ii] == 0]
bumpy_fast = [features_train[ii][1]
              for ii in range(0, len(features_train)) if labels_train[ii] == 0]
grade_slow = [features_train[ii][0]
              for ii in range(0, len(features_train)) if labels_train[ii] == 1]
bumpy_slow = [features_train[ii][1]
              for ii in range(0, len(features_train)) if labels_train[ii] == 1]


# initial visualization
# mpl.pyplot.xlim(0.0, 1.0)
# mpl.pyplot.ylim(0.0, 1.0)
# mpl.pyplot.scatter(bumpy_fast, grade_fast, color="b", label="fast")
# mpl.pyplot.scatter(grade_slow, bumpy_slow, color="r", label="slow")
# mpl.pyplot.legend()
# mpl.pyplot.xlabel("bumpiness")
# mpl.pyplot.ylabel("grade")
# mpl.pyplot.show()
################################################################################


# your code here!  name your classifier object clf if you want the
# visualization code (prettyPicture) to show you the decision boundary

# 1. K nearest neighbours

# from sklearn import neighbors
# clf = neighbors.KNeighborsClassifier()
# clf = clf.fit(features_train, labels_train)
# print clf.score(features_test, labels_test)

# 2. adaboost

# from sklearn.ensemble import AdaBoostClassifier
# clf = AdaBoostClassifier()
# clf = clf.fit(features_train, labels_train)
# print clf.score(features_test, labels_test)

# 3. random forest

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf = clf.fit(features_train, labels_train)
print clf.score(features_test, labels_test)


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass

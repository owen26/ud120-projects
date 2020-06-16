#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(
    open("../final_project/final_project_dataset.pkl", "rb"))

print(len(enron_data))

print('example', enron_data["SKILLING JEFFREY K"])

print(len(enron_data["SKILLING JEFFREY K"].keys()))

pois = {name: features for (name, features)
        in enron_data.items() if features['poi'] == 1}

print('poi', len(pois))

names_list = open("../final_project/poi_names.txt",
                  "r").read().splitlines()[2:]

names_trimmed_list = [x[4:] for x in names_list]

poi_names = [k for k, v in enron_data.items() if v['poi'] ==
             1]

# print('names', names_trimmed_list)

# print('poi names', poi_names)

poi_names_filtered = [k for k in poi_names if any(
    k.split()[0].capitalize() in n for n in names_trimmed_list)]

print('poi_names_filtered', len(poi_names_filtered))

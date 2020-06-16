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

data_length = len(enron_data)

print('data length', data_length)

print('example', enron_data["SKILLING JEFFREY K"])

# print(len(enron_data["SKILLING JEFFREY K"].keys()))

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

print('james stock value', enron_data['PRENTICE JAMES']['total_stock_value'])

print('wesley emails from poi',
      enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

print('stock exerised by jeffrey',
      enron_data["SKILLING JEFFREY K"]['exercised_stock_options'])

print('how many folks have qualified salary', len(
    [k for k, v in enron_data.items() if v['salary'] != 'NaN']))

print('how many folks have email addresses', len(
    [k for k, v in enron_data.items() if v['email_address'] != 'NaN']))

people_without_total_payments = len(
    [k for k, v in enron_data.items() if v['total_payments'] == 'NaN'])

print('how many folks do not have total payments', people_without_total_payments)

print('percentage of that', float(
    people_without_total_payments) / float(data_length))

poi_without_payments = [k for k, v in enron_data.items(
) if v['total_payments'] == 'NaN' and v['poi'] == 1]

print('debug', poi_without_payments)

# print('percentage of poi without total payments',
#       float(len(poi_without_payments)) / float(data_length))

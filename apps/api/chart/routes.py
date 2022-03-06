import numpy
from flask import render_template, request

import pandas as pd
from flask_login import login_required
from apps.api.chart import blueprint


@blueprint.route('/chart', methods=['GET'])
@login_required
def student_chart():
    df = pd.read_csv('advanced_python.csv', sep=';')

    birthday = df['DOB'].values

    list_dob = []
    for data in birthday:
        list_dob.append(data[-4:])

    data = numpy.array(list_dob)
    unique, counts = numpy.unique(data, return_counts=True)

    data_return = dict(zip(unique, counts))
    key_data = data_return.keys()

    return render_template('home/charts-morris.html', keys=key_data, data=data_return)

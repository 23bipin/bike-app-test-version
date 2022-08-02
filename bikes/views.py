from re import search
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

import pandas as pd
import numpy as np

import json


class HomePageView(TemplateView):
    template_name = "home.html"


class SearchPageView(TemplateView):
    template_name = "search.html"


def datatable(request):
    df = pd.read_csv("static/database/2021-05.csv", nrows=1000)
    df.columns = [
        "time_depart",
        "time_return",
        "depart_stn_id",
        "depart_stn_name",
        "return_stn_id",
        "return_stn_name",
        "distance",
        "duration",
    ]

    # filter for duration
    df = df.drop(df[df.duration < 10].index)
    df["duration"] = df["duration"].div(60)
    df = df.round(decimals=2)

    # filter for distance
    df = df.drop(df[df.distance < 10].index)
    df["distance"] = df["distance"].div(1000)
    df = df.round(decimals=2)

    # parsing to json
    json_records = df.reset_index().to_json(orient="records")
    arr = []
    arr = json.loads(json_records)
    contextt = {"d": arr}  # dictionary, "d" is the key, json record value

    return render(request, "datatable.html", contextt)

from django.http import HttpResponse
from django.shortcuts import render
from .form import UserForm
import Main
import glob
import json


def index(request):
    if request.method == "POST":
        doc_num = request.POST.get("doc_num")

        version  = request.POST.get("version")

        mm = Main.main()


        mm.run(doc_num,version)
        file_names = glob.glob('C:/Users/izinovyev/Downloads/edijson*')

        for name in file_names:
            name
        # file = open("C:/Users/izinovyev/Downloads/" + name[29:], "r")

        dicts_from_file = {}

        print(name[29:])
        text=''
        with open("C:/Users/izinovyev/Downloads/" + name[29:], 'r') as inf:
            for line in inf:
                dicts_from_file = json.loads(line)
                text+='\n'+dicts_from_file["segmentWithError"] + ': ' + dicts_from_file["message"] + " Value: " + dicts_from_file["value"] + " Path: " + dicts_from_file["errorHashCode"]

        return HttpResponse("<h2>Errors for doc num:  {0}</h2>".format(doc_num)+"<h2>Json file name:  {0}</h1>".format(name[29:])+text)

    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})


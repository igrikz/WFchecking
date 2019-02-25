from django.http import HttpResponse
from django.shortcuts import render
from .form import UserForm
import Main



def index(request):
    if request.method == "POST":
        doc_num = request.POST.get("doc_num")

        version  = request.POST.get("version")

        mm = Main.main()


        mm.run(doc_num,version)

        return HttpResponse("<h2>Errors for doc num:  {0}</h2>".format(doc_num))

    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})


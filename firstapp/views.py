from django.http import HttpResponse
from django.shortcuts import render
from .form import UserForm
import Main



def index(request):
    if request.method == "POST":
        doc_num = request.POST.get("doc_num")

        version  = request.POST.get("version")

        mm = Main.main()
        #conv = File_x12.creats_x12()

        mm.run(doc_num,version)
        #conv.spFeds("4010")
        #wc.puschInweb()
        return HttpResponse("<h2>Hello, {0}</h2>".format(version))

    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})


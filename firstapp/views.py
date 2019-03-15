from django.http import HttpResponse
from django.shortcuts import render
from .form import UserForm
import Main
import glob
from bs4 import BeautifulSoup

def index(request):
    if request.method == "POST":
        doc_num = request.POST.get("doc_num")

        version  = request.POST.get("version")

        mm = Main.main()


        mm.run(doc_num,version)
        file_names = glob.glob('C:/Users/izinovyev/Downloads/edijson*')

        for name in file_names:
            name





        file = open("testHTML.html", "r")


        soup = BeautifulSoup(file.read(), features="lxml")
        tbody = soup.find_all('tbody')
        tt=''
        errors=''
        for i in tbody:

            if i.find_all('tr')[0].find_all('td')[2].text != 'EF - Element functional rule failed':
                tr = i.find_all('tr')[2:]
                err = dict(segmentWithError=i.find_all('tr')[0].find_all('td')[1].text,
                           message=i.find_all('tr')[2].find_all('td')[0].text,
                           value=i.find_all('tr')[2].find_all('td')[1].text,
                           data=i.find_all('tr')[4].find_all('td')[0].find_all('p')[-1].text)
                tt=i.find_all('tr')[4].find_all('td')[0]
                errors+=("<p>Error in: "+err['segmentWithError']+",  "
                         +err['message']+'  '+ err['value']
                            + "<p><font color=red> "+err['data']+"</font>")



        file.close()
        if errors !='':
            return HttpResponse("<h4>Errors OBSOSA SE for doc num:  {0}</h2>".format(
                doc_num) + errors)
        else:
            outfeds = ''
            file = open('test.feds', 'r')
            for i in file:
                outfeds += i + '<br>'
            return HttpResponse(
                "<h2>Errors Y OBSOSA SE .NET for doc num:  {0}</h5>".format(doc_num) + "<p>FEDS: {0}".format(
                    outfeds) )







    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})


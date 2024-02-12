import datetime
import random

from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "name": "Jakhongir",
        "age": random.randint(1, 23),
        "time": datetime.datetime.now().strftime("%Y.%m.%d")

    }
    return HttpResponse(f"""<h1 style="color: red;">{context['name']} ning yoshi {context['age']} da.</h1>
    <p>Bugun: <code> {context['time']}</code> </p>""")
from django.shortcuts import render
import pandas as pd

def base_view(request):
    df=pd.read_csv('http://127.0.0.1:8000/app/static/media/Facebook_Insights_Data_Export_-_UniCredit_Bank_Ceska_republika_-_2017-03-03_ChWJpXG.csv')
    dfd=df.head()
    user=request.user  # can be anonymous user
    session=request.session.session_key
    ctx={'mydesc':dfd.to_html(), 'user': user, 'session' : session}
    return render(request, 'index.html', ctx)
# Create your views here.

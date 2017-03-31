from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from .models import CSV
import pandas as pd
import numpy as np
from .forms import CSVForm
import uuid
from ipware.ip import get_ip


from datetime import datetime
def convert_date(date):
    new_date = datetime.strptime(date, '%Y-%m-%d')
    return new_date

def convert_date2(date):
    new_date2 = datetime.strptime(date, '%m/%d/%Y %I:%M:%S %p')
    return new_date2

def create_report(csv1, csv2):
    file1 = csv1
    file2 = csv2

    data=pd.read_csv(file1,encoding='utf-8', skiprows=[1])
    uniporn=pd.DataFrame(data)

    datax=pd.read_csv(file2,encoding='utf-8', skiprows=[1])
    uniporn_Posts=pd.DataFrame(datax)
    df = pd.DataFrame(uniporn, columns=['Dlouhodobý Celkový počet To se mi líbí', '28 dní Aktivní uživatelé stránky', '28 dní Celkový dosah',])
    df = df[df.columns.difference(['Datum'])].astype(np.float64)
    df = uniporn.iloc[:len(uniporn), [0,1,9,12,15,18,21,24,31,34,37,40,43,46,71,74,77,80,86,98]]
    uniporn["Datum"] = uniporn["Datum"].apply(convert_date)
    df2 = uniporn.iloc[:len(uniporn),[1]]
    last_value = df2.iloc[len(df2)-1, [0]]
    fans_celkem = last_value["Dlouhodobý Celkový počet To se mi líbí"]
    first_value = df2.iloc[1, [0]]
    fans_start = first_value["Dlouhodobý Celkový počet To se mi líbí"]
    narust_fans = fans_celkem - fans_start
    df['Datum'].values[::1]
    array_date = df['Datum'].values
    array_values = df['Dlouhodobý Celkový počet To se mi líbí'].values
    array_fans_online = df["Denně Denní počet fanoušku online"].values
    array_celkovy_dosah = df["28 dní Celkový dosah"].values
    array_celkovy_zobrazeni = df["28 dní Celkový počet zobrazení"].values
    df4 = pd.DataFrame(uniporn_Posts)
    df4.fillna(0, inplace=True)
    #výpočet stories
    komenty_prispevek = df4['Dlouhodobý Příběhy na příspěvky podle typu akce - comment'].astype(np.float64)
    like_prispevek = df4['Dlouhodobý Příběhy na příspěvky podle typu akce - like'].astype(np.float64)
    share_prispevek = df4['Dlouhodobý Příběhy na příspěvky podle typu akce - share'].astype(np.float64)

    #výpočet consumptions
    play_clicks_prispevek = df4['Dlouhodobý Využití příspěvků podle typu - clicks to play'].astype(np.float64)
    link_clicks_prispevek = df4['Dlouhodobý Využití příspěvků podle typu - link clicks'].astype(np.float64)
    other_clicks_prispevek = df4['Dlouhodobý Využití příspěvků podle typu - other clicks'].astype(np.float64)
    photo_view_clicks_prispevek = df4['Dlouhodobý Využití příspěvků podle typu - photo view'].astype(np.float64)

    #výpočet stories pro příspěvek s jedním ID
    stories_engagement_post = (komenty_prispevek [0] + like_prispevek [0] + share_prispevek [0])

    #výpočet consumptions pro příspěvek s jedním ID
    consumption_engagement_post = (play_clicks_prispevek [0] + link_clicks_prispevek [0] + other_clicks_prispevek [0] + photo_view_clicks_prispevek [0])

    #výpočet engagementu celkem (stories+consumptions) pro příspěvek s jedním ID
    engagement_post = stories_engagement_post + consumption_engagement_post

    dosah_prispevek = df4['Dlouhodobý Celkový dosah příspěvku'].astype(np.float64)
    engagement_rate_post = ((engagement_post / dosah_prispevek [0])*100)
    stories_rate_post = ((stories_engagement_post / dosah_prispevek [0])*100)
    consumption_rate_post = ((consumption_engagement_post / dosah_prispevek [0])*100)
    uniporn_Posts["Příspěvky uživatele"]
    df4["Příspěvky uživatele"]
    uniporn_Posts["Příspěvky uživatele"] = uniporn_Posts["Příspěvky uživatele"].apply(convert_date2)
    datum_prispevek = df4['Příspěvky uživatele']
    datum_prispevek = datum_prispevek[0]
    delkaznaku_prispevek = df4['Zpráva příspěvku'].str.len()
    delkaznaku_prispevek = delkaznaku_prispevek[0]
    komentovatelnost_prispevek = ((komenty_prispevek / dosah_prispevek)*100)
    komentovatelnost_prispevek=komentovatelnost_prispevek[0]
    oblibenost_prispevek = ((like_prispevek / dosah_prispevek)*100)
    oblibenost_prispevek=oblibenost_prispevek [0]
    sdilitelnost_prispevek = ((share_prispevek / dosah_prispevek)*100)
    sdilitelnost_prispevek = sdilitelnost_prispevek[0]
    share_prispevek=share_prispevek [0]
    klikatelnost_prispevek = consumption_rate_post
    dosahorganicky_prispevek = df4['Dlouhodobý Organický dosah příspěvku'].astype(np.float64)
    dosahorganicky_prispevek=dosahorganicky_prispevek [0]
    dosahplaceny_prispevek = df4['Dlouhodobý Placený dosah příspěvku'].astype(np.float64)
    dosahplaceny_prispevek=dosahplaceny_prispevek [0]
    zobrazeni_prispevek = df4['Dlouhodobý Celkový počet zobrazení příspěvku'].astype(np.float64)
    zobrazeni_prispevek=zobrazeni_prispevek [0]
    zobrazeniorganicky_prispevek = df4['Dlouhodobý Počet zobrazení organického příspěvku'].astype(np.float64)[0]
    zobrazeniorganicky_prispevek2 = df4['Dlouhodobý Počet placených zobrazení příspěvku'].astype(np.float64)[0]
    typ_prispevek = df4['Typ']
    typ_prispevek=typ_prispevek[0]
    zasah_vs_fans_prispevek = ((fans_celkem / dosah_prispevek [0])*100)
    frekvence_prispevek = zobrazeni_prispevek / dosah_prispevek
    frekvence_prispevek=frekvence_prispevek [0]
    image = df4['Přímý odkaz']
    image = image [0]
    return {'fans_sum' : fans_celkem, 'dates' : array_date, 'fans_progres' : narust_fans,
    'fans_start' : fans_start, 'fans_end' : fans_celkem, 'fans_online' : array_fans_online, 'full_reach' : array_celkovy_dosah,
    'full_seen' : array_celkovy_zobrazeni, 'comments' : komenty_prispevek, 'play_clicks' : play_clicks_prispevek,
    'other_clicks' : other_clicks_prispevek, 'stories_eng' : stories_engagement_post, 'consuption' : consumption_engagement_post,
    'eng_post' : engagement_post, 'reach_post' : dosah_prispevek, 'eng_rate_post' : engagement_rate_post,
    'stories_rate_post' : stories_rate_post, 'cons_rate_post' : consumption_rate_post, 'story_date' : datum_prispevek,
    'story_len' : delkaznaku_prispevek, 'story_comment' : komentovatelnost_prispevek, 'story_fav' : oblibenost_prispevek,
    'story_share' : sdilitelnost_prispevek, 'story_click' : klikatelnost_prispevek, 'organic_reach' : dosahorganicky_prispevek,
    'pay_reach' : dosahplaceny_prispevek, 'type' : typ_prispevek, 'unique_vs_fans' : zasah_vs_fans_prispevek,
    'freq' : frekvence_prispevek, 'fans_all' : array_values, 'post_image' : image, 'zobrazeni_prispevek' : zobrazeni_prispevek,
    'zobrazeniorganicky_prispevek2' : zobrazeniorganicky_prispevek2, 'zobrazeniorganicky_prispevek' : zobrazeniorganicky_prispevek}

def base_view(request):
    ip = get_ip(request)
    user=request.user  # can be anonymous user
    csvs = CSV.objects.filter(ip_address = ip, user = user.id).order_by('-created')[0]
    session=request.session.session_key

    base_url = 'http://127.0.0.1:8000/app/static/media/'


    csv1 = base_url + str(csvs.uploaded_csv1)
    csv2 = base_url + str(csvs.uploaded_csv2)

    dates = ""
    fans_online = ""
    full_reach = ""
    full_seen = ""
    fans_all = ""
    seen = ""
    paid_seen = ""
    metrics = create_report(csv1, csv2)
    ctx={'user': user, 'session' : session}
    for key, value in metrics.items():
        ctx[key] = value
        if key == 'dates':
            for j in value:
                dates = dates + "," + j
            ctx["dates2"] = dates
        elif key == 'fans_online':
            for k in value:
                fans_online = fans_online + "," + str(k)
            ctx["fans_online2"] = fans_online
        elif key == 'fans_all':
            for k in value:
                fans_all = fans_all + "," + str(k)
            ctx["fans_all2"] = fans_all
        elif key == 'full_reach':
            for k in value:
                full_reach = full_reach + "," + str(k)
            ctx["full_reach2"] = full_reach
        elif key == 'full_seen':
            for k in value:
                full_seen = full_seen + "," + str(k)
            ctx["full_seen2"] = full_seen
        else:
            pass




    return render(request, 'reports/graf.html', ctx)


def add_csv(request):
    ip = get_ip(request)
    user = request.user
    if request.method == 'POST':

        form = CSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv = CSV.objects.filter(ip_address = ip, user = user.id)
            csv.delete()
            print (csv)
            csv1 = form.cleaned_data['uploaded_csv1']
            csv2 = form.cleaned_data['uploaded_csv2']
            csv = CSV.objects.create(
                uuid = uuid.uuid4(),
                uploaded_csv1 = csv1,
                uploaded_csv2 = csv2,
                ip_address = get_ip(request)
            )
            csv.save()

            return HttpResponseRedirect(reverse('results'))
        else:
            csv = CSV.objects.filter(ip_address = ip, user = user.id)
            csv.delete()
            print (csv)
            return HttpResponseRedirect(reverse('results'))
    else:
        form = CSVForm
    context = {'form' : form}
    template_name = 'reports/import.html'
    return render(request, template_name, context)

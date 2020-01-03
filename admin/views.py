from django.conf import settings
from django.shortcuts import render
from guests.save_the_date import SAVE_THE_DATE_CONTEXT_MAP


def home(request):
    return render(request, 'home.html', context={
        'save_the_dates': SAVE_THE_DATE_CONTEXT_MAP,
        'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
    })

def products(request):
	return render(request, 'home.html')

def csv(request):
	csvfile = request.FILES['csv_file']
	data = pd.read_csv(csvfile.name)
	data_html = data.to_html()
	context = {'loaded_data': data_html}
	return render(request, "demo1.html", context)

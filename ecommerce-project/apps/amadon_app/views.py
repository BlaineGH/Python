from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string

def index(request):
	return render(request, 'amadon_app/index.html')

def checkout(request):
	if 'price' not in request.session:
		request.session['price'] = 0
	if 'items' not in request.session:
		request.session['items'] = 0
	if 'totalprice' not in request.session:
		request.session['totalprice'] = 0

	context = {
		'price': request.session['price'],
		'amount': request.session['items'],
	}

	return render(request, 'amadon_app/checkout.html', context)

def buy(request):
	if request.method == 'POST':
		if request.POST['product_id'] =='1015':
			request.session['price'] = int(request.POST['quantity'])* 19.99
			request.session['items'] = int(request.POST['quantity'])
		if request.POST['product_id'] == '1016':
			request.session['price'] = int(request.POST['quantity'])* 29.99
			request.session['items'] = int(request.POST['quantity'])
	return redirect('/checkout')
				
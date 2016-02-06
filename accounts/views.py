from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from accounts.command_factory import CommandFactory
from accounts.commands import CommandError
from accounts.forms import TransactionForm
from accounts.models import Account
import logging

logging.basicConfig()

def transactions(request):
    accounts = Account.objects.all()
    context = {'accounts':accounts}
    return HttpResponse(render(request, 'accounts/transactions.html', context))

def payment(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TransactionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            try:
                transaction = form.save(commit=False)
                factory = CommandFactory()
                cmd = factory.create_command("TRANS", transaction)
                cmd.execute()
                messages.success(request, "Transfer succesful")
                cmd = factory.create_command("NOTIFY", transaction)
                cmd.execute()
                
            except CommandError as ce:
                messages.error(request, ("Transfer unsuccesful: %s" % ce))
            except Exception as e:
                logging.error(e)
                messages.error(request, "Something went wrong, please try again")
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('payments'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TransactionForm()

    return render(request, 'accounts/payment.html', {'form': form})
#     return HttpResponse(render(request, 'accounts/payment.html', {}))

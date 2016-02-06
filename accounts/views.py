from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from accounts.commands.command_factory import CommandFactory
from accounts.commands.commands import CommandError
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
                #Retrieve transaction from form
                transaction = form.save(commit=False)
                #create factory
                factory = CommandFactory()
                #Try the transaction, if something goes wrong, an exception will be raised
                _make_transaction(request, transaction, factory)
                #Notify the transaction
                _notify_transaction(transaction, factory)
                
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


def _make_transaction(request, transaction, factory):
    cmd = factory.create_command("TRANS", transaction)
    cmd.execute()
    messages.success(request, "Transfer succesful")


def _notify_transaction(transaction, factory):
    cmd = factory.create_command("NOTIFY", transaction)
    cmd.execute()
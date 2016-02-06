# test-payments-app
This is my solution to the proposed programming test. Please, follow this instruction in order to install and run the application.
## Prerequisites
In order to run and use this app, you will need:
* [pip](https://pip.pypa.io/en/stable/installing/)
* [FakeSMTP](https://nilhcem.github.io/FakeSMTP/) or similar SMTP server that will need to listen port **2525**
* It is also recommended to use a virtual environment using [virtualenv](https://virtualenv.readthedocs.org/en/latest/index.html)
    *   Download virtualenv with `pip install virtualenv`
    *   Create a new virtualenv with `virtualenv venv`. This will create a new folder `venv`
    *   To activate the virtual environment `source venv/bin/activate`
    
## Installation
* Clone the repository in a folder of your election
* Enter into the folder `test-payments-app` and run `pip install -r requirements.txt` to install all the dependencies
* Run `./manage.py migrate` in order to create the db schema (Note: For simplicity, it will create a sqlite3 file as database)
* Now, we need to create an admin user in the system, so run `./manage.py createsuperuser` and enter a username, email(optional) and password 

## Running the tests
* from the folder `test-payments-app` run `./manage.py test`

## Running the server
* Now we are ready to launch the app. Just run `./manage.py runserver` and it will launch a web server in `localhost:8000`
* If we point the browser to that address, we will see the app home page. Going to the transactions page will show nothing as there are no accounts yet.
* In order to create some accounts, we have to go to the admin site, which is on `localhost:8000/admin`. Then we will be able to log with the user created previously.
* Click on "add account" and create some accounts.
* Now we are ready to make some transactions between accounts.

## Making transactions
We can make transactions from the payment page. On the "From" select, we will only see
those accounts with balance greater than 0.

If we try an invalid transaction (same account or insufficient funds) we will see an error message. If the transaction is successful, we will see a success message and both accounts will be notified by email. At this point, make sure that the SMTP server is running and listening at port 2525.

## Implementation decisions
### Used Patterns
The main part of the app is the payment functionality. To make it the most extensible possible I've implemented the [Command Pattern](https://en.wikipedia.org/wiki/Command_pattern). This will allow us to decouple the execution of the tasks from the executer.

I've also used the [Factory Pattern](https://en.wikipedia.org/wiki/Factory_%28object-oriented_programming%29) to keep decoupled the executer from the implementation details of the task.

On this particular case, there are two different tasks (commands) to perform: make a transaction and notify a transaction. The executer of this tasks will be the same on both cases, the view that renders the payment form. You can see that from `accounts/views.py` we don't import neither of the commands implementations (`TransferCommand` and `NotifyCommand`), so the view is completely decoupled from the commands implementation details.

Add a new command in the future will only involve the creation of the command implementation, and the modification of the factory to add it. Then we just have to ask the factory for the command from the client code and execute it.

### About the test coverage
Due to time shortage, I haven't implemented tests for all the classes. I've focused in the `TransferCommand` as it is the class that encapsulated most bussiness logic. 


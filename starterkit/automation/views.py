from django.views.generic import TemplateView
from _keenthemes.__init__ import KTLayout
import pymongo
from django.shortcuts import render
from pprint import pprint


connect_string = 'mongodb+srv://gonn-user:Sharma%4011@ihrms-free.ysswmv8.mongodb.net/msv4'
my_client = pymongo.MongoClient(connect_string)

#Define the database name
dbname = my_client['msv4']

#Get/create collection name remember that you will see the database in your mongodb cluster only after you create a collection
collection_name = dbname["Users"]

class AutomationView(TemplateView):
    # Default template file
    # Refer to dashboards/urls.py file for more pages and template files
    template_name = 'dashboards/dashboard-1.html'

    # Custom Methods
    def action(request): 
        if request.method == "POST": 
            pprint('Called')
            # data = function_call() #the function you want to call 
            print('Called')
            # return render(request,'index.html',{'data': 'OK'}) 

    # Predefined function
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # A function to init the global layout. It is defined in _keenthemes/__init__.py file
        context = KTLayout.init(context)

        return context
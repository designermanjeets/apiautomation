from django.shortcuts import render
from django.views.generic import TemplateView
from pprint import pprint
from _keenthemes.__init__ import KTLayout
from _keenthemes.libs.theme import KTTheme
import logging
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import pandas as pd
from django.contrib import admin

import pymongo

connect_string = 'mongodb+srv://gonn-user:Sharma%4011@ihrms-free.ysswmv8.mongodb.net/msv4'
my_client = pymongo.MongoClient(connect_string)

#Define the database name
dbname = my_client['msv4']

#Get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
collection_name = dbname["Users"]

class SystemView(TemplateView):
    template_name = 'pages/system/not-found.html'
    status = ''

    def simple_upload(request):
        pprint(pd)
        if request.method == 'POST':
            # myfile = request.FILES['myfile']
            # fs = FileSystemStorage()
            # filename = fs.save(myfile.name, myfile)
            # uploaded_file_url = fs.url(filename)
            # return render(request, 'core/simple_upload.html', {
            #     'uploaded_file_url': uploaded_file_url
            # })
            return render(request, 'pages/system/error.html')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # A function to init the global layout. It is defined in _keenthemes/__init__.py file
        context = KTLayout.init(context)

        # Define the layout for this module
        # _templates/layout/system.html
        context.update({
            'layout': KTTheme.setLayout('system.html', context),
            'status': self.status,
        })

        return context

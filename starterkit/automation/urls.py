from django.urls import path
from automation.views import AutomationView

app_name = 'automation'

urlpatterns = [
    # ...

    path('automation', AutomationView.as_view(template_name = 'pages/automation/list.html'), name='automation'),

    # ...
]
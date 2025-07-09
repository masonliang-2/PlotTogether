# Django Backend architecture

[manage.py]  
     |
     v
[plottogether/settings.py] --> [api/apps.py]
     |
     v
[plottogether/urls.py] --> [api/urls.py] -> [api/views.py]
                                                  |
                                                  v
[services/config.py] <- [services/database.py]  <- [services/analysis.py]
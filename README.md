![alt text](https://raw.githubusercontent.com/WADPlaceholdr/Placeholdr/master/static/images/logonobg.png)


## Description
placeholdr is a Django web application with the objective of allowing people to browse through places of interest and create trips based on those places, with a user community that provides ratings, comments, pictures.

## Demo
a live demo is available at https://max.ardeer.co.uk/placeholdr

## External sources
* django
* Google Maps API
* Bootstrap
* django-bootstrap4
* animate.css
* wow.js
* Search code snippet by julienphalip.com
* django-csp
* django-mathfilters
* django-referrer-policy
* django-geoposition
* Pillow
* pytz
* selenium

## Requirements
(see [requirements.txt](https://github.com/WADPlaceholdr/Placeholdr/blob/master/requirements.txt))
* Python 3.6.x
* pip3
* Django==1.11.7
* django-bootstrap4==0.0.6
* django-csp==3.3
* django-mathfilters==0.4.0
* django-referrer-policy==1.0
* django-geoposition==0.3.1
* Pillow==5.0.0
* pytz==2018.3
* selenium==3.11.0

## Installation

# Ubuntu Deployment

install all prerequisites
```
sudo apt-get update
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
```

open port 8000
```
sudo ufw allow 8000/tcp
sudo ufw enable
sudo ufw status
```

set up a virtualenv
```
sudo pip3 install virtualenv
virtualenv placeholdr
```

clone this repository
```
git clone https://github.com/maxburton/placeholdr.git
```

activate the virtualenv
```
source myprojectenv/bin/activate
```

edit the settings file and add your IP/domain name to ALLOWED_HOSTS
```
sudo nano placeholdr_project/settings.py
ALLOWED_HOSTS=['EC2_DNS_NAME', 'www.url.com']
```

install requirements
```
cd Placeholdr
pip install –r requirements.txt --yes
```

**optional** create deployment_variables.py
(don't use for development/test environment, deployment only)
(default conf file uses HTTPS with HTST and all security headers strictly configured
```
mv placeholdr_project/deployment_variables.py.conf placeholdr_project/deployment_variables.py
```


create database
```
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

test that the server runs:
```
python manage.py runserver 0.0.0.0:8000
```
and go to www.url.com:8000 to see if it is running

create a new virtualhost file in /etc/apache2/sites-available/
populate it with:
```
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    ServerName www.placeholdr.ardeer.co.uk
    ServerAlias placeholdr.ardeer.co.uk
    DocumentRoot /var/www/placeholdr
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
    Alias /robots.txt /var/www/placeholdr/static/robots.txt
    Alias /favicon.ico /var/www/placeholdr/static/favicon.ico
    Alias /static /var/www/placeholdr/static
    Alias /media /var/www/placeholdr/media
    <Directory /var/www/placeholdr/static>
        Require all granted
    </Directory>
    <Directory /var/www/placeholdr/media>
        Require all granted
    </Directory>
    <Directory /var/www/placeholdr>
        Require all granted
    </Directory>
    <Directory /var/www/placeholdr/placeholdr_project>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
    WSGIDaemonProcess placeholdr_project python-path=/var/www/placeholdr python-home=/var/www/placeholdr/placeholdrenv
    WSGIProcessGroup placeholdr_project
    WSGIScriptAlias / /var/www/placeholdr/placeholdr_project/wsgi.py
</VirtualHost>
```

Set permissions
```
chmod 775 db.sqlite3
sudo chown :www-data db.sqlite3
sudo chown -R :www-data /var/www/placeholdr
chmod 775 /var/www/placeholdr
chmod 775 /var/www/placeholdr/placeholdrenv
sudo service apache2 restart
```


**optional** populate placeholdr with sample data
```
python population_script.py
```

SUMMARY

```
git clone https://github.com/maxburton/placeholdr.git
cd Placeholdr
pip install –r requirements.txt --yes
$ mv placeholdr/deployment_variables.py.conf placeholdr/deployment_variables.py
python manage.py migrate
python population_script.py
```


## Support
for support please submit an issue on [GitHub](https://github.com/WADPlaceholdr/Placeholdr/issues)

## Contact
wadplaceholdr@gmail.com

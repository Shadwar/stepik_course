sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/hello
sudo ln -s /home/box/web/etc/gunicorn_django.conf /etc/gunicorn.d/django
sudo /etc/init.d/gunicorn restart

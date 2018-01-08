sudo ln -fs /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

source web/myvenv/bin/activate
gunicorn -b 0.0.0.0:8080 --pythonpath /home/box/web hello:hello &
gunicorn -b 0.0.0.0:8080 --pythonpath /home/box/web/ask ask.wsgi:application &

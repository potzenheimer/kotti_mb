Introduction
============

A first attempt on replacing our beloved CMS with something more lightweight
when serving less ambigious and less content heavy sites.

Installation
------------

Install the necessary requirements into a dedicated **virtualenv**


```bash
virtualenv mysite
cd mysite
bin/pip install -r https://raw.github.com/Kotti/Kotti/master/requirements.txt
```

In order to start local development, please download an example ini-file.
Example using *curl* (could also be wget)

```bash
curl -O https://github.com/Kotti/Kotti/raw/master/app.ini
```

To run Kotti using the app.ini example configuration file:

```bash
bin/pserve app.ini
```

The pserve command above uses SQLite as the default database. On first run,
Kotti will create a SQLite database called Kotti.db in your mysite directory.

Kotti includes support for PostgreSQL, MySQL and SQLite (tested regularly),
and other SQL databases. The default use of SQLite makes initial development
easy. SQLite may prove to be adequate for some deployments.

The necessary system dependencies for sqlite on debian linux would be:

```bash
apt-get install libsqlite3-dev
bin/pip install pysqlite
```

**Note:*** on osx with working xCode installation you should normally not
need to install anything.

Deployment
----------

The package includes an example deployment.ini file that you can use to run
the blogging application via supervisord and Nginx.

In order to run it with Nginx native uWSGI support for example append
the following to the deployment configuration:

```ini
[uwsgi]
socket = 127.0.0.1:5001
#socket = /opt/sites/mysite/<your_domain>.sock
master = true
processes = 4
home = /opt/sites/brem/
chmod-socket = 666
processes = 1
```


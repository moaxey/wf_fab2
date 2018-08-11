Webfaction fabric2 helper scripts
=========================

These scripts utilise the [Webfaction API](https://docs.webfaction.com/xmlrpc-api/) via python and [Fabric 2](http://www.fabfile.org/) to conveniently run some common tasks.

Presently there are just a small selection, mostly related to managing letsencrypt certificates.

Installation
------------

You could install this in your system python3, into your virtualnv or into your pipenv as a dev dependency

> $ pip install --dev webfaction_fab2

Usage
-----

Generate a fabfile.py in the root of your project, something like this:

> $ pipen run python -m wf_fab2.makefab

And then start using the commands

> $ pipenv run fab -l
```
 Loading .env environment variables...
Available tasks:

  acme-install     Install acme.sh for Letsencrypt certificates on a webfaction host.
  acme-uninstall   Uninstall acme.sh from a webfaction host.
  check-websites   Check http response mode of all configured websites.
  secure-domains   Validate, generate and install Letsencrypt certificates.
```

Development
-----------

I had a pretty comprehensive and well tested set of scripts for fabric 1.x enabling provisioning and deploying django projects onto webfaciton hosts. As I slowly move them to fabric2 I'm intending to share them here.

https://github.com/moaxey/wf_fab2

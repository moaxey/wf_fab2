Webfaction helper scripts
=========================

These scripts utilise the [Webfaction API] (https://docs.webfaction.com/xmlrpc-api/) via python and [Fabric 2](http://www.fabfile.org/) to conveniently run some common tasks.

Presently there are just a small selection.

- acme-install: Install [acme.sh](https://github.com/Neilpang/acme.sh) for Letsencrypt certificates on a webfaction host.
- acme-uninstall: Uninstall acme.sh from a webfaction host.
- check-websites:  Check http response mode of all configured websites.
- secure-domains:   Validate domains with [dns manual method](https://github.com/Neilpang/acme.sh/wiki/dns-manual-mode), generate and install (or renew) Letsencrypt certificates.


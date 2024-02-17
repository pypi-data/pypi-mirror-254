
=============================================
Open Forms extension Haal centraal HR prefill
=============================================

:Version: 0.3.0
:Source: https://github.com/open-formulieren/open-forms-ext-haalcentraal-hr
:Keywords: Open Forms Extension, Haal Centraal HR
:PythonVersion: 3.10

|build-status| |code-quality| |black| |coverage| |docs|

|python-versions| |django-versions| |pypi-version|

Open Forms extension to prefill form fields with data coming from the `Haal Centraal HR API`_.

.. _Haal Centraal HR API: https://app.swaggerhub.com/apis/DH-Sandbox/handelsregister/1.3.0

.. contents::

.. section-numbering::

Features
========

* Configuration in the admin for the Haal Centraal service
* The Haal Centraal client performs the token exchange with Keycloak
* Retrieve prefill data from the ``MaatschappelijkeActiviteitRaadplegen`` API endpoint based on KvK number.

.. note::

   The Haal Centraal HR API is a Den Haag specific API and not a national Dutch standard.

Installation
============

Requirements
------------

* Python 3.8 or above
* setuptools 30.3.0 or above
* Django 3.2 or newer


Usage
=====

For an explanation of this how this extension works, look at the Open Forms `developer documentation`_.

To see how to build and distribute an image with this extension, look at the Open Forms documentation about
`building and distributing extensions`_.

.. _developer documentation: https://open-forms.readthedocs.io/en/latest/developers/extensions.html#keycloak-token-exchange-extension
.. _building and distributing extensions: https://open-forms.readthedocs.io/en/latest/developers/extensions.html#keycloak-token-exchange-extension


Configuration
=============

In the Open Forms Admin:

* Go to **Configuration** > **Services** and create a service for Haal Centraal HR.
* Go to **Miscellaneous** > **Token exchange plugin configurations**.
  Click on **Add Token exchange plugin configuration** and fill in the details:

  * Select the service for which you want the token authorisation to be performed.
  * Add the Keycloak audience.

  Save the configuration.
* The prefill will be available in the form designer in the same way as other prefill plugins.


.. |build-status| image:: https://github.com/open-formulieren/open-forms-ext-haalcentraal-hr/workflows/Run%20CI/badge.svg
    :alt: Build status
    :target: https://github.com/open-formulieren/open-forms-ext-haalcentraal-hr/actions?query=workflow%3A%22Run+CI%22

.. |code-quality| image:: https://github.com/open-formulieren/open-forms-ext-haalcentraal-hr/workflows/Code%20quality%20checks/badge.svg
     :alt: Code quality checks
     :target: https://github.com/open-formulieren/open-forms-ext-haalcentraal-hr/actions?query=workflow%3A%22Code+quality+checks%22

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. |coverage| image:: https://codecov.io/github/open-formulieren/open-forms-ext-haalcentraal-hr/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/open-formulieren/open-forms-ext-haalcentraal-hr
    :alt: Coverage status

.. |docs| image:: https://readthedocs.org/projects/prefill_haalcentraalhr/badge/?version=latest
    :target: https://prefill_haalcentraalhr.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/open-forms-ext-haalcentraal-hr.svg

.. |django-versions| image:: https://img.shields.io/pypi/djversions/open-forms-ext-haalcentraal-hr.svg

.. |pypi-version| image:: https://img.shields.io/pypi/v/open-forms-ext-haalcentraal-hr.svg
    :target: https://pypi.org/project/open-forms-ext-haalcentraal-hr/

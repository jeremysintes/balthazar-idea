{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
========

* TODO



Quickstart
==========

1. Clone the git

.. code-block:: console

    git clone gh://{{ cookiecutter.git_username }}/{{ cookiecutter.project_slug }}

2. It is recommended to create a developpement environment (exemple below with Anaconda):

.. code-block:: console

	conda create –n {{ cookiecutter.project_slug }}

3. Activate the developpement environment :

.. code-block:: console

   activate {{ cookiecutter.project_slug }}

4. Install the required librairies :

.. code-block:: console

    pip install -r requirements




License
=======

{% if cookiecutter.open_source_license == 'Not open source' %}
{{ cookiecutter.project_name }} is not open source.
{% endif %}

{% if is_open_source %}
{{ cookiecutter.project_name }} is licensed under the {{ cookiecutter.open_source_license }} - see the LICENSE.rst file for details
{% endif %}

Changes
=======

**unreleased**



Credits
=======

This package was created with Cookiecutter_ and the `jeremysintes/cookiecutter-python_boilerplate`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`jeremysintes/cookiecutter-python_boilerplate`: https://github.com/jeremysintes/cookiecutter-python_boilerplate


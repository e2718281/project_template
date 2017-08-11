Install
=========

This is where you write how to get a new laptop to run this project.

Install
=========

To run this project on a new laptop:
----------------------------------------

1. On the local computer, navigate to directory where you keep you django projects.  Use cookiecutter to generate project template:


``cookiecutter https://github.com/e2718281/project_template``

------------

2. Go to github.com and create the intended repo.  Create ``.gitignore`` (Python template) and a README file.

------------

3. Add ``.idea`` and ``db.sqlite3`` to the ``.gitignore`` file.  ``.env`` should be ignored in the Python template.

------------

4. On the local computer navigate into the top-level directory of the newly-generated project (ie. the one with ``manage.py``)
::

``git init``
``git pull https://github.com/<newly_created_github_repo>``

------------

5. Open project in PyCharm.

------------

6. Use PyCharm to make commit into git repo.

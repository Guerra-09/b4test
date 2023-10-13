# b4test

## Installation steps
<ul>
  <li> (optional) pip install pipenv </li>
  <li> python --version</li>
  <li> (inside folder) pipenv --python 3.10  </li>
  <li> pipenv --venv </li>
  <li> pipenv graph </li>
  <li> pipenv install django pylint pylint-django pylint-celery </li>
  <li> pipenv run django-admin startproject {proyectName} </li>
  <li> pipenv shell </li>
  <li> python manage.py startapp {appName} </li>
</ul>

## Do not forget 
<ul>
  <li> in project settings, add app to installed apps  </li>
  <li> csrf_token </li>
  <li> *input type=text name="nombre a buscar desde la view" value={{algo.name}}  hidden* </li>
  <li> form action="{% url 'namedInURL' %}", method="POST" </li>
</ul>

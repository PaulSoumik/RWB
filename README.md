# Research-Web-Portal

<p align="center">
  <img  src=/static/research_portal_cropped.png>
</p>

<p align="center">
  <img  src=http://ForTheBadge.com/images/badges/made-with-python.svg>
  <br>
  <a href="#about">About</a> •
  <a href="#objectives">Objectives</a> •
  <a href="#screenshots">Screenshots</a> •
  <a href="#communication-channels">Communication</a> •
  <a href="#contribution">Contribution</a> •
  <a href="#license">License</a> •
</p>

## About

Research web-portal for the students and professors of NIT Durgapur where information of the ongoing research projects from each department is available, with a short description of goals and required skills. It aims to fill the gap between students and professors of NIT Durgapur by maintaining a hub for all research projects.

## Objectives

- Meet the demand for open access institutional repository and offer a central data hub for more comprehensive research informations.
- Sychronize and showcase NITDGP's research activities.
- Provide students with an easy ,intuitive and personalised web-interface for facilitating access to the information of their primary relevance and interests.
- Smoothen the administrative workflow and enhance the impact of NITDGP's research outputs.

## Screenshots
![Screenshot 1](/static/s1.JPG)
![Screenshot 2](/static/s2.JPG)

## Steps to Reproduce
* Start off by forking this repository and cloning it to get your local copy. Make sure you run this in git bash.

  ```bash
  > git clone https://github.com/ieeesb-nitdgp/Research-Web-Portal.git
  ```
* If you prefer a virtual-environment ([pipenv](https://pipenv.readthedocs.io/) suggested) you should have pip and pipenv installed.

  ```bash
  > sudo apt install python3-pip python3-dev
    pip3 install --user pipenv 
  ```
  Add pipenv to PATH
  
  ```bash
  echo "PATH=$HOME/.local/bin:$PATH" >> ~/.bashrc
  source ~/.bashrc
  ```
 
* Navigate to the cloned repository directory and initiate a python 3 environment.
  
  ```bash
  > pipenv --three 
  ```
* Activate your virtual environment.
  
  ```bash
  > pipenv shell
  ```
  After successful activation, the code within parentheses will appear before the prompt in the bash similar to this:
  ```bash
  (Research-Web-Portal-d4334452)D:\Repository\Research-Web-Portal>
  ``` 
  Now install all requisites in requirements.txt .

  ```bash
  cd Research-Web-Portal
  pip install -r requirements.txt
  ```
  where x is everything inside requirements.txt

  Here is what your Pipfile will appear when you're ready to go ( you can view it by running > pip freeze )

  ```bash
  certifi==2019.9.11
  chardet==3.0.4
  defusedxml==0.6.0
  Django==2.1.7
  djangorestframework==3.10.3
  gunicorn==19.9.0
  idna==2.8
  oauthlib==3.1.0
  psycopg2==2.8.4
  PyJWT==1.7.1
  python3-openid==3.1.0
  pytz==2018.9
  requests==2.22.0
  requests-oauthlib==1.2.0
  six==1.12.0
  social-auth-app-django==3.1.0
  social-auth-core==3.2.0
  urllib3==1.25.6
  whitenoise==4.1.2
  ```
  
* Run the following command in your terminal.

  ```bash
  > python manage.py runserver
  ```
  
* Navigate to http://localhost:8000 in any web browser to see it in action.Have fun!

## Contribution

* *Head to [contribution guidelines](https://github.com/ieeesb-nitdgp/Research-Web-Portal/wiki/Contribution-Guidelines) to know more about how you can help us to improve.*

* *Exactly putting we want it to be simple are permissive. Interested contributors are heartedly welcomed. :blush:* 

## Communication Channels

* All related communications take place via Slack. Join [here](https://join.slack.com/t/ieee-sbnitdgp/shared_invite/enQtODM4OTgwODg5NzM0LTM1NjhkMWU5NzYxMTQwODEwM2JmMDk0ZWYwOTgzYzQzZTUyOWY1YTY1NDY5NDFiYjU3MmFhMTA3NjE3YzdmZWM)

## License

Copyright © IEEE SB NIT Durgapur.

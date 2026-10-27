# Back-end-Development-Capstone

Django band website, completed from the official [IBM starter](https://github.com/ibm-developer-skills-network/sfvih-Back-end-Development-Capstone).
Original starter attribution and license are retained. Changes were prepared with AI assistance and should be reviewed by the learner before submission.

## Environment Setup

Tested locally with Python 3.14. Flask/Django dependency versions are pinned in requirements.txt. Run from this repository:

```sh
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

The original course bin/setup.sh is preserved as supplied by IBM; it targets the course Cloud IDE. Local verification used the Python setup described above, rather than claiming that the Cloud IDE setup script ran.

## Implemented work

Concert, ConcertAttending, Photo and Song models; URL routing; signup/login/logout; concert list and RSVP; songs and photos obtained from the corresponding Flask microservices; lyrics modal; admin model registration; service timeout/error handling.

```sh
python manage.py migrate
python manage.py test concert
python manage.py runserver 127.0.0.1:8000
```

Defaults connect to Songs at http://127.0.0.1:5001 and Pictures at http://127.0.0.1:5002. Set SONGS_SERVICE_URL and PICTURES_SERVICE_URL for deployed microservices. For deployment also set DJANGO_SECRET_KEY, DJANGO_ALLOWED_HOSTS and DJANGO_DEBUG=0. DJANGO_DB_PATH can configure the SQLite path. Create an admin account with python manage.py createsuperuser; no fixed administrator credentials are embedded.

Dockerfile and deployment.yml are completed. Set the actual registry image in deployment.yml and create its referenced ConfigMap/Secret before applying. The deployment was executed in the Skills Network IBM Cloud lab. Set DJANGO_CSRF_TRUSTED_ORIGINS to the exact HTTPS application origin when running behind the OpenShift router.

## Verification

Migrations succeeded, Django check found no issues, and 4 application tests passed. Songs, photos and the lyrics modal were verified in a real browser.

## Submission status

Prepared and tested locally. Published to https://github.com/aruzhanrysbayeva/Back-end-Development-Capstone. IBM Cloud deployment was verified; local and cloud evidence are identified separately.


## Verified cloud deployment

Kubernetes Deployment on the course OpenShift cluster; image djangoserver:4. Migrations and collectstatic succeeded. Browser verification covered home, songs, photos, HTTPS signup/login, admin login page and two demonstration concerts.

Application: https://djangoserver-sn-labs-chalkyretro2.labs-prod-openshift-san-a45631dc5778dc6371c67d206ba9ae5c-0000.us-east.containers.appdomain.cloud

The course lab is temporary. MongoDB and SQLite use demonstration storage; do not treat this environment as a persistent production deployment. No administrator password or service secret is committed.

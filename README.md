# Installation step
1. Technical requirement
Python version 3.12.2
2. Clone the project
```console
git clone <repo-url>
```
3. Navigate to the cloned folder
```console
cd  <folder-name>
```
4. Create a virtual environment.
```console
python -m venv <your-virtual-env-name>
<your-virtual-env-name>\Scripts\activate
```
5. Install modules.
```console
pip3 install --upgrade pip
pip install -r requirements.txt
```
6. Create environment variable for local database
Manually create a file with name '.env' and add the configuration of local database such as:
- DEBUG.
- SECRET_KEY.
- DB_NAME.
- DB_USER.
- DB_PASSWORD.
- DB_HOST.
- DB_PORT.

**Do not push the env file to the github** 
7. Run the program
```console
python manage.py runserver
```
# Workflow
1. Pull the changes to local machine
```console
git pull <repo-name>
```
2. Create a branch for version or fix an issue
```console
git branch <branch-name>
```
3. Switch to the version branch
```console
git checkout <branch-name>
```
4. Commit the change to the version branch and open pull request to propose changes to the main branch
```console
git commit -m "#issue number - Text"
```
Example:
```console
git commit -m "#1 - Lorem ipsum"
or
git commit -m "#1 - Fixed"
```
5. Merge child branch to the main branch.
6. **Do not push directly to the main branch.**


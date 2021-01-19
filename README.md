# Flask Application 3.3 for Python Basic Course

# Usage
### 1. Create virtual environment to local environment
```
# Create virtual environment
pyenv virtualenv 3.7.0 pytweet_mysql

# Apply on local environment 
pyenv local pytweet_mysql

# rehash
pyenv rehash 
```

### 2. Install packages we need
```bash
pip install -r requirements.txt
```

### 3. The setting of environment variable
```bash
export FLASK_APP=run.py
```

### 4. Set up DB(Flask-Migrate)
```
# We need to create DB anyway
mysql -u [User Name] -p

>>> CREATE DATABASE pytweet_mysql_development;
```

```bash
# Initialization
flask db init

# Create a migration file
flask db migrate

# Run a migration
flask db upgrade

# (Rollback of migration) <= Downgrade migration o the one version before
flask db downgrade
```

### 5. Start up the server
```bash
flask run
```

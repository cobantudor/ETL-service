#!/bin/bash

# Start cron service
service cron start

export FLASK_APP="run.py"

# Register crontab jobs
flask crontab add

# Start application
python run.py
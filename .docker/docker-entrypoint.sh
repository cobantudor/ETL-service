#!/bin/bash

# Start cron service
service cron start

# Start application
python app.py
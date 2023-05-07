#!/bin/bash
#
# Runs an application with given environment variables.
#
# Accepts only one (optional) argument - an .env file that will be for application.
# If none is provided, application will user a default configuration.

exec python src/main.py

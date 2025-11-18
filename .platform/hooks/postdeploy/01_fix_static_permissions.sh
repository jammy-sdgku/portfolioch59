#!/bin/bash
echo "Fixing static files permissions..."
chmod -R 755 /var/app/current/staticfiles/
chown -R webapp:webapp /var/app/current/staticfiles/
echo "Static files permissions fixed!"


#!/bin/bash
echo "Fixing static files permissions..."

STATIC_DIR="/var/app/current/staticfiles"

if [ -d "$STATIC_DIR" ]; then
    find "$STATIC_DIR" -type d -exec chmod 755 {} \;
    find "$STATIC_DIR" -type f -exec chmod 644 {} \;
    chown -R webapp:webapp "$STATIC_DIR"
    echo "Static files permissions fixed!"
else
    echo "Directory $STATIC_DIR does not exist. Skipping permission fix."
fi



# My Identity Website

Render settings:
- Root Directory: `website` (when deploying from the combined repository)
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

Public page: `/`
Admin page: `/admin`

Important: secure Firebase with Firebase Authentication and restrictive Realtime Database Rules before publishing.

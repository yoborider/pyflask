#!/usr/bin/env python
# coding: utf8

from app import app

# Dev
app.run(debug=True, host='0.0.0.0', port=5000)
# Production
# app.run( host='0.0.0.0' )

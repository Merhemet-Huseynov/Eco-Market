#!/bin/bash

cd promart || exit 1
celery -A promart worker --loglevel=info --pool=solo
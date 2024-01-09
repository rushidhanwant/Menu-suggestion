#!/bin/bash

python3 -m uvicorn app.main:app --host 127.0.0.1 --port 8081 --reload

# Wait for all background processes to finish
wait
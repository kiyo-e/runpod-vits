#!/bin/bash

echo "Worker Initiated"

echo "Starting SD API Server For PROD 🚀"
python server_fastapi.py &

echo "Starting RunPod Handler 🏃‍♂💨"

# localでテストするときはこちらにする
# python -u ./runpod_handler.py --rp_serve_api --rp_api_host='0.0.0.0'
python -u ./runpod_handler.py
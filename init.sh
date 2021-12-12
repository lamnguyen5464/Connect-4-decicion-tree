rm -rf local_env &&
python3 -m venv local_env &&
source local_env/bin/activate &&
pip install -r requirements.txt &&
deactivate
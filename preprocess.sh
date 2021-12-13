source local_env/bin/activate &&
mkdir output ;
cd dataset &&
mkdir parsingdata ;
cd .. ;
python3 src/preprocess.py ;
deactivate


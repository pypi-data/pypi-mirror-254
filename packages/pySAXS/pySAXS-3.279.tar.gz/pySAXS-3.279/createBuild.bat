python createChanges.py
cd build
del /q *.*
cd..
cd dist
del /q *.*
cd..
rem python setup.py bdist --format=wininst
rem python setup.py bdist_wheel --universal
rem distribution tar
rem python setup.py  bdist --format=gztar
python -m build
rem twine upload dist/*

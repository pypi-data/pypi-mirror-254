This is the project description

hatch build -t wheel

twine upload --repository testpypi dist/*

To run the tests

cd src
python -m unittest test/test_route53.py
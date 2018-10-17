.PHONY: deploy
deploy: build
	twine upload dist/*

.PHONY: test-deploy
test-deploy: build
	twine upload -r pypitest dist/*

.PHONY: build
build:
	python setup.py bdist_wheel

.PHONY: clean
clean:
	rm -rf build dist peewee_seed.egg-info
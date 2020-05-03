# whitelist files for formatting and linting
WHITELIST_FILES = CtCI-6th-Edition/

# formats the project
format:
	isort ${WHITELIST_FILES} -rc --atomic -y $(ISORT_ARGS)
	black $(WHITELIST_FILES) --line-length=79 $(BLACK_ARGS)

# lints the project
lint:
	pylint $(WHITELIST_FILES)

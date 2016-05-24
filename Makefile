.PHONY: build
build:
	./template.py


.PHONY: clean
clean:
	find . -mindepth 1 -maxdepth 1 -type d ! -name '.git*' -print0 | \
		xargs -0 rm -r

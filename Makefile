FILE ?= the_future_king.txt

.PHONY: run
run:
	@python3 src/main.py ${FILE}
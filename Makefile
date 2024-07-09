.PHONY: run
run:
	uvicorn app.main:app --reload --port 8000


.PHONY: webdocs
webdocs:
	mkdocs serve -a 127.0.0.1:5000

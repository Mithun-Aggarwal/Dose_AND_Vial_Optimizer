.PHONY: run freeze clean

run:
	streamlit run streamlit_app.py

freeze:
	pip freeze | sort > requirements.lock

clean:
	rm -f requirements.lock

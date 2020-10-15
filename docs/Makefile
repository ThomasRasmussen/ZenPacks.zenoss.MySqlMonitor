OUTPUT_HTML = README.html

docs:
	cat top.css > $(OUTPUT_HTML)
	pandoc -f markdown -t html header.md --template=template.html >> $(OUTPUT_HTML)
	pandoc -f markdown -t html releases.md --template=template.html >> $(OUTPUT_HTML)
	pandoc -f markdown -t html body.md --template=template.html --table-of-contents >> $(OUTPUT_HTML)
	python docs.py

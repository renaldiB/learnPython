import pdfplumber as plb

with plb.open("lyric.pdf") as text:
    for page_no, page in enumerate(text.pages, start=1):
        print(f"Halaman: {page_no} \n")
        data = page.extract_text()
        print(data.strip())
        print("\n")
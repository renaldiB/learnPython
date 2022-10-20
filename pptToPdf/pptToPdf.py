import aspose.slides as slides

pres = slides.Presentation("pptMKB.pptx")
pres.save("converted.pdf", slides.export.SaveFormat.PDF)

"""

@kylel

"""

import json
import os
import pathlib

from papermage.magelib import Document
from papermage.recipes import CoreRecipe
from papermage.visualizers.visualizer import plot_entities_on_page

# load doc
recipe = CoreRecipe()
pdfpath = pathlib.Path(__file__).parent.parent / "tests/fixtures/1903.10676.pdf"
# pdfpath = pathlib.Path(__file__).parent.parent / "tests/fixtures/2304.02623v1.pdf"
doc = recipe.from_pdf(pdf=pdfpath)

# visualize tokens on the 1st page
plot_entities_on_page(page_image=doc.images[0], entities=doc.tokens)

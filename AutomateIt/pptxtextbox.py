#!/usr/bin/env python

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : pptxtextbox
# @created     : Monday Jan 09, 2023 14:05:28 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
import collections
import collections.abc
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation()
blank_slide_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(blank_slide_layout)
txBox = slide.shapes.add_textbox(Inches(2), Inches(2), Inches(5), Inches(1))
tf = txBox.text_frame
tf.text = "Wow! I'm inside a textbox"
p = tf.add_paragraph()
p.text = "Adding a new text"
p.font.bold = True
p.font.italic = True
p.font.size = Pt(30)
prs.save("textBox.pptx")

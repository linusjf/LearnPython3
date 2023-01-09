#!/usr/bin/env python

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : helloworld
# @created     : Monday Jan 09, 2023 15:52:17 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
import collections
import collections.abc
from pptx import Presentation

prs = Presentation()
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]

title.text = "Hello, World!"
subtitle.text = "python-pptx was here!"

prs.save('helloworld.pptx')

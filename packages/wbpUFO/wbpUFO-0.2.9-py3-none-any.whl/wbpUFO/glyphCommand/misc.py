"""
misc
===============================================================================

Misc Glyph Commands 
"""
from __future__ import annotations

from typing import TYPE_CHECKING
import logging

import wx

from wbDefcon import Color
from ufo2ft.constants import OPENTYPE_CATEGORIES_KEY

from .base import GlyphCommand
from .parameter import (
    ParamBoolRequired,
    ParamColour,
    ParamEnumeration,
    ParamStrRequired,
)

if TYPE_CHECKING:
    from wbDefcon.objects.glyph import Glyph

log = logging.getLogger(__name__)
# ALPHABET_OTC_KEY = "com.Alphabet-Type.openTypeCategory"


class NoteCommand(GlyphCommand):
    name = "Note"
    ADD = 0
    REPLACE = 1
    parameters = [
        ParamStrRequired("t", "Text"),
        ParamEnumeration("m", "Mode", ["Add to note", "Replace note"], ADD),
    ]

    def _execute(self, glyph: Glyph):
        if glyph.note and self.m == self.ADD:
            glyph.note = glyph.note.strip() + "\n" + self.t
            print("text added")
        else:
            glyph.note = self.t
            print("text set")


class SkipExportCommand(GlyphCommand):
    name = "Skip export"
    parameters = [ParamBoolRequired("s", "Skip", True)]

    def _execute(self, glyph: Glyph):
        skipExportGlyphs = glyph.font.lib.get("public.skipExportGlyphs", [])
        if self.s:
            if glyph.name in skipExportGlyphs:
                return
            skipExportGlyphs.append(glyph.name)
        else:
            if glyph.name in skipExportGlyphs:
                skipExportGlyphs.remove(glyph.name)
            else:
                return
        glyph.font.lib["public.skipExportGlyphs"] = skipExportGlyphs


class MarkCommand(GlyphCommand):
    name = "Mark glyph"
    parameters = [ParamColour("c", "Colour", wx.WHITE)]

    def _execute(self, glyph: Glyph):
        if self.c == wx.WHITE:
            glyph.markColor = None
        else:
            glyph.markColor = Color.from_wx(self.c)


class SetOpentypeCategoryCommand(GlyphCommand):
    name = "Set OpenType category"
    OpentypeCategory = ["unassigned", "base", "ligature", "mark", "component"]
    parameters = [
        ParamEnumeration(
            "c",
            "OpenType Category",
            OpentypeCategory,
            0,
        ),
    ]

    def _execute(self, glyph: Glyph):
        font = glyph.font
        if OPENTYPE_CATEGORIES_KEY not in font.lib:
            font.lib[OPENTYPE_CATEGORIES_KEY] = {}
        if not self.c and glyph.name in font.lib[OPENTYPE_CATEGORIES_KEY]:
            del font.lib[OPENTYPE_CATEGORIES_KEY][glyph.name]
            return
        font.lib[OPENTYPE_CATEGORIES_KEY][glyph.name] = self.OpentypeCategory[self.c]


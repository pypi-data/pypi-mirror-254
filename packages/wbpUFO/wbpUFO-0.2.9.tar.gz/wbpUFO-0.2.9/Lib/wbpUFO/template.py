"""
template
===============================================================================

Document Templates for UFOs and imports to UFO WorkBench
"""
import os

import wx
from fontTools.ufoLib import UFOFileStructure
from glyphsLib.builder import to_ufos
from glyphsLib.parser import load

import wbDefcon
from wbBase.document import dbg
from wbBase.document.template import (
    DEFAULT_TEMPLATE_FLAGS,
    TEMPLATE_NO_CREATE,
    DocumentTemplate,
)

from .document import UfoDocument
from .view.font import UfoFontView


class UfoTemplate(DocumentTemplate):
    """
    Main Template for Unified Font Objects
    """
    def __init__(self, manager):
        DocumentTemplate.__init__(
            self,
            manager=manager,
            description="UFO (Unified Font Object)",
            filter="*.ufo;*.ufoz",
            dir="",
            ext=".ufo",
            docTypeName="UFO document",
            viewTypeName="UFO Font View",
            docType=UfoDocument,
            viewType=UfoFontView,
            flags=DEFAULT_TEMPLATE_FLAGS,
            icon=wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_FRAME_ICON),
        )


class VFBTemplate(DocumentTemplate):
    """Template for FontLab VFB files - import only"""

    def __init__(self, manager):
        DocumentTemplate.__init__(
            self,
            manager=manager,
            description="FontLab file (import only)",
            filter="*.vfb",
            dir="",
            ext=".ufo",
            docTypeName="UFO document",
            viewTypeName="UFO Font View",
            docType=UfoDocument,
            viewType=UfoFontView,
            flags=DEFAULT_TEMPLATE_FLAGS | TEMPLATE_NO_CREATE,
            icon=wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_FRAME_ICON),
        )


class GlyphsTemplate(DocumentTemplate):
    """Template for Glyphs App files - import only"""

    def __init__(self, manager):
        DocumentTemplate.__init__(
            self,
            manager=manager,
            description="Glyphs App file (import only)",
            filter="*.glyphs",
            dir="",
            ext=".ufo",
            docTypeName="UFO document",
            viewTypeName="UFO Font View",
            docType=UfoDocument,
            viewType=UfoFontView,
            flags=DEFAULT_TEMPLATE_FLAGS | TEMPLATE_NO_CREATE,
            icon=wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_FRAME_ICON),
        )

    def CreateDocument(self, path, flags):
        """
        Creates a new instance of the associated document class (UfoDocument)
        for each master in the Glyphs file
        """
        dbg(f'GlyphsTemplate.CreateDocument(path="{path}", flags={flags})', indent=1)
        result = None
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as glyphsFile:
                with wx.BusyInfo("Loading Glyphs File please wait"):
                    glyphsFont = load(glyphsFile)
                    ufos = to_ufos(glyphsFont, ufo_module=wbDefcon)
            result = []
            for font in ufos:
                font._ufoFormatVersion = 3
                font._ufoFileStructure = UFOFileStructure.ZIP
                doc = self._docType()
                doc.template = self.documentManager.FindTemplateByType(UfoTemplate)
                self.documentManager.AddDocument(doc)
                doc.font = font
                if doc.OnCreate(path, flags):
                    doc.set_modificationDate()
                    doc.saved = False
                    doc.modified = False
                    doc.UpdateAllViews(self, ("font loaded", True))
                    result.append(doc)
                else:
                    if doc in self.documentManager.documents:
                        doc.DeleteAllViews()
        dbg(f"GlyphsTemplate.CreateDocument() returns {result}", indent=0)
        return result

from typing import List, Optional, Dict, Iterable
import aspose.pycore
import aspose.pydrawing
import aspose.cells
import aspose.cells.charts
import aspose.cells.digitalsignatures
import aspose.cells.drawing
import aspose.cells.drawing.activexcontrols
import aspose.cells.drawing.equations
import aspose.cells.drawing.texts
import aspose.cells.externalconnections
import aspose.cells.json
import aspose.cells.markup
import aspose.cells.metadata
import aspose.cells.numbers
import aspose.cells.ods
import aspose.cells.pivot
import aspose.cells.properties
import aspose.cells.querytables
import aspose.cells.rendering
import aspose.cells.rendering.pdfsecurity
import aspose.cells.revisions
import aspose.cells.saving
import aspose.cells.settings
import aspose.cells.slicers
import aspose.cells.slides
import aspose.cells.tables
import aspose.cells.timelines
import aspose.cells.utility
import aspose.cells.vba
import aspose.cells.webextensions

class AdjustFontSizeForRowType:
    '''Represents which kind of rows should be ajusted.'''
    
    @classmethod
    @property
    def NONE(cls) -> AdjustFontSizeForRowType:
        '''No adjsut.'''
        ...
    
    @classmethod
    @property
    def EMPTY_ROWS(cls) -> AdjustFontSizeForRowType:
        '''If the row is empty, change font size to fit row height.'''
        ...
    
    ...

class SlideViewType:
    '''Represents the type when exporting to slides.'''
    
    @classmethod
    @property
    def VIEW(cls) -> SlideViewType:
        '''Exporting as view in MS Excel.'''
        ...
    
    @classmethod
    @property
    def PRINT(cls) -> SlideViewType:
        '''Exporting as printing.'''
        ...
    
    ...


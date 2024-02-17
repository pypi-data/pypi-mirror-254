from dataclasses import dataclass
from typing import Optional

@dataclass
class PatentTextLine:
    page_num: int  # 0-based index returned from PDFPageDetailedAggregator. TODO: rename to index
    text: str
    line_index: int  # line index counting TextLine instances from top to bottom of page
    column_index: Optional[int]  # 0 or 1 or None if noncolumnar
    line_num: Optional[int] = None  # human labeled line number, multiple of 5
    column_num: Optional[int] = None  # human labeled column number
    paragraph_num: Optional[int] = None  # alternative human labeling method often in form [XXXX] at beginning of paragraph

@dataclass
class GeneratedPassage:
    prior_art_source_id: int
    text: str
    claim_element_id: int
    model_id: str
    start_line: Optional[PatentTextLine] = None
    end_line: Optional[PatentTextLine] = None
    ranking: int = 0
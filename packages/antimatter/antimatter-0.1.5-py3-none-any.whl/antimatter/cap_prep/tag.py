from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

import antimatter_engine as am

from antimatter.fieldtype import converters
from antimatter.fieldtype.fieldtypes import FieldType

TAG_SOURCE = "manual"
TAG_VERSION = (0, 0, 0)


class TagType(Enum):
    """
    The span tag types
    """
    Unary = 0
    String = 1
    Number = 2
    Boolean = 3
    Date = 4


@dataclass
class SpanTag:
    """
    Defines a span tag manually to the data contained in the cell path. The tag
    is applied to the subset of data contained between start (inclusive) and end
    (exclusive).

    The cell path describes which cell to apply this tag to. Cell paths can be
    created using the antimatter.cell_path.cell_path(cname, rnum) helper function,
    which takes the name of the column and the row number. As an example, if the
    cell to apply this span tag to was in a column named "name" and was in row 10
    of the data, the cell path would be "name[10]".
    """
    name: str
    cell_path: str
    start: int
    end: int
    tag_type: TagType = TagType.Unary
    tag_value: str = ""


@dataclass
class ColumnTag:
    """
    Defines a column tag manually set to apply a rule to a particular column of data.
    """
    column_name: str
    tag_names: List[str]
    tag_type: TagType = TagType.Unary
    tag_value: str = ""


@dataclass
class CapsuleTag:
    """
    Defines a capsule tag manually set to apply a rule to a capsule.
    """
    name: str
    tag_type: TagType = TagType.Unary
    tag_value: str = ""


class SpanTagApplicator:
    """
    SpanTagApplicator wraps user-provided span tags into intermediary form span
    tags when the tag applies to cell data.
    """

    _tags: Dict[str, List[SpanTag]]

    def __init__(self, span_tags: List[SpanTag]):
        """
        Initialize a SpanTagApplicator with a list of use-provided span tags.

        :param span_tags: User-provided span tags
        """
        tags = {}
        for tag in span_tags or []:
            if tag.cell_path not in tags:
                tags[tag.cell_path] = []
            tags[tag.cell_path].append(tag)
        self._tags = tags

    def span_tags_for_cell(self, cell_path: str, cell_val: bytes, field_type: FieldType) -> List[am.PySpanTag]:
        """
        Given the path to a cell, provide a list of intermediary form span tags
        that apply to the cell. The cell's value and field type are used to ensure
        span tags are applied properly across various types of data. For example,
        when a user specifies start and end indices for a string, they likely intend
        to index it based on rune, not on byte.

        :param cell_path: The name of the path to a cell
        :param cell_val: The value in generic form of the cell pointed to in the cell path
        :param field_type: The original type of data in the cell
        :return: A list of span tags that apply to the cell pointed to in the cell path
        """
        tags = []
        if span_tags := self._tags.get(cell_path):
            for st in span_tags:
                start = st.start
                end = st.end

                if field_type is FieldType.String:
                    # Caller shouldn't have to know that the underlying type is
                    # bytes. Convert back to string, so we can index by rune and
                    # find the byte positioning
                    data = converters.Standard.field_converter_from_generic(FieldType.String)(cell_val)
                    converter = converters.Standard.field_converter_to_generic(FieldType.String)
                    b_idx = 0
                    for i, rune in enumerate(data):
                        if i == st.start:
                            start = b_idx
                        b = converter(rune)
                        b_idx += len(b)
                        if i+1 == st.end:
                            end = b_idx

                tags.append(am.PySpanTag(am.PyTag(
                    st.name, st.tag_type.value, st.tag_value, TAG_SOURCE, TAG_VERSION
                ), start, end))
        return tags

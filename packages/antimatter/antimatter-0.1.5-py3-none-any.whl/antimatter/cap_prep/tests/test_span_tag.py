import re

from antimatter.cap_prep.tag import SpanTag, SpanTagApplicator
from antimatter.fieldtype.fieldtypes import FieldType


class TestSpanTagApplicator:
    def test_span_tags_for_cell_accented_characters(self):
        matching_cell_path = "col[0]"
        cell_value = "à, è, ì, ò, ù,; À, È, Ì, Ò, Ù"
        cell_value_generic = cell_value.encode("utf-8")

        span_tags = [SpanTag("tag", matching_cell_path, 3, 9)]
        applicator = SpanTagApplicator(span_tags)

        tags = applicator.span_tags_for_cell(matching_cell_path, cell_value_generic, FieldType.String)
        assert len(tags) == len(span_tags)

        st = span_tags[0]
        pyst = tags[0]

        # The start and end indices must be different because we're using multibyte unicode
        # characters and want to let callers index strings by rune (while behind the scenes
        # we index by bytes)
        assert tags[0].start != span_tags[0].start
        assert tags[0].end != span_tags[0].end

        # Sub out the substring contained in the span tag for the provided indices and
        # for the applied span tag's indices against the generic data
        redacted_str = re.sub(cell_value[st.start:st.end], "{redacted}", cell_value)
        redacted_bytes = re.sub(cell_value_generic[pyst.start:pyst.end], b"{redacted}", cell_value_generic)

        # The results should be the same
        assert redacted_str.encode("utf-8") == redacted_bytes

    def test_span_tags_repeating_substring_regression(self):
        """
        sc-3782
        Regression test for an issue with how string value span tag indexes were
        not properly converted to byte value indexes.
        """
        matching_cell_path = "col[0]"
        cell_value = "hello hello hello"
        cell_value_generic = cell_value.encode("utf-8")

        span_tags = [SpanTag("tag", matching_cell_path, 6, 11)]
        applicator = SpanTagApplicator(span_tags)

        tags = applicator.span_tags_for_cell(matching_cell_path, cell_value_generic, FieldType.String)
        assert len(tags) == len(span_tags)

        st = span_tags[0]
        pyst = tags[0]

        # The start and end indices must be the same because we're using
        # standard ASCII characters
        assert tags[0].start == span_tags[0].start
        assert tags[0].end == span_tags[0].end

        # Sub out the substring contained in the span tag for the provided indices and
        # for the applied span tag's indices against the generic data
        redacted_str = re.sub(cell_value[st.start:st.end], "{redacted}", cell_value)
        redacted_bytes = re.sub(cell_value_generic[pyst.start:pyst.end], b"{redacted}", cell_value_generic)

        # The results should be the same
        assert redacted_str.encode("utf-8") == redacted_bytes

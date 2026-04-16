# tests/test_stubs.py

import textwrap
import pytest
from uncoded.stubs import StubClass, StubFunction, StubModule, StubParam, extract_stub, render_stub

class TestExtractStub:  # L15-181

    def test_simple_function(self):  # L16-30
        ...

    def test_function_no_annotations(self):  # L32-40
        ...

    def test_async_function(self):  # L42-50
        ...

    def test_private_function_included(self):  # L52-60
        ...

    def test_class_with_attributes_and_methods(self):  # L62-89
        ...

    def test_class_line_range(self):  # L91-107
        ...

    def test_class_with_bases(self):  # L109-115
        ...

    def test_class_no_bases(self):  # L117-123
        ...

    def test_docstring_first_sentence_only(self):  # L125-132
        ...

    def test_no_docstring(self):  # L134-140
        ...

    def test_kwargs_and_varargs(self):  # L142-150
        ...

    def test_imports_collected(self):  # L152-166
        ...

    def test_syntax_error_raises(self):  # L168-170
        ...

    def test_source_order_preserved(self):  # L172-181
        ...

class TestRenderStub:  # L184-297

    def test_header_contains_path(self):  # L185-187
        ...

    def test_imports_rendered(self):  # L189-195
        ...

    def test_function_line_range(self):  # L197-203
        ...

    def test_async_function_prefix(self):  # L205-212
        ...

    def test_function_with_annotations(self):  # L214-227
        ...

    def test_docstring_excerpt_rendered(self):  # L229-243
        ...

    def test_class_with_bases(self):  # L245-250
        ...

    def test_class_no_bases(self):  # L252-257
        ...

    def test_attribute_with_annotation(self):  # L259-271
        ...

    def test_method_indented(self):  # L273-293
        ...

    def test_ends_with_newline(self):  # L295-297
        ...

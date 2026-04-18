# tests/test_extract.py

import textwrap
from uncoded.extract import extract_module, walk_source

class TestExtractModule:  # L6-243

    def test_classes_and_functions(self):  # L7-35
        ...

    def test_async_functions_and_methods(self):  # L37-54
        ...

    def test_empty_module(self):  # L56-60
        ...

    def test_all_private_symbols_included(self):  # L62-78
        ...

    def test_module_level_constants(self):  # L80-90
        ...

    def test_type_alias_classic(self):  # L92-100
        ...

    def test_type_alias_pep695(self):  # L102-110
        ...

    def test_tuple_unpacking_skipped(self):  # L112-119
        ...

    def test_unannotated_class_variable(self):  # L121-132
        ...

    def test_module_with_only_constants_is_kept(self, tmp_path):  # L134-143
        ...

    def test_annotated_attributes(self):  # L145-164
        ...

    def test_class_with_all_private_members(self):  # L166-183
        ...

    def test_property_classified_as_attribute(self):  # L185-200
        ...

    def test_property_setter_and_deleter_suppressed(self):  # L202-222
        ...

    def test_preserves_source_order(self):  # L224-243
        ...

class TestWalkSource:  # L246-339

    def test_basic_walk(self, tmp_path):  # L247-272
        ...

    def test_nested_subpackage(self, tmp_path):  # L274-286
        ...

    def test_includes_private_subdirectory(self, tmp_path):  # L288-300
        ...

    def test_includes_init_with_symbols(self, tmp_path):  # L302-313
        ...

    def test_skips_empty_init(self, tmp_path):  # L315-325
        ...

    def test_skips_syntax_errors(self, tmp_path):  # L327-339
        ...

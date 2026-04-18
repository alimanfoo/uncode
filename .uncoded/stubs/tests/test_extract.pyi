# tests/test_extract.py

import textwrap
from uncoded.extract import extract_module, walk_source

class TestExtractModule:  # L6-205

    def test_classes_and_functions(self):  # L7-35
        ...

    def test_async_functions_and_methods(self):  # L37-54
        ...

    def test_empty_module(self):  # L56-60
        ...

    def test_module_level_constants(self):  # L62-71
        ...

    def test_type_alias_classic(self):  # L73-81
        ...

    def test_type_alias_pep695(self):  # L83-91
        ...

    def test_tuple_unpacking_skipped(self):  # L93-100
        ...

    def test_unannotated_class_variable(self):  # L102-113
        ...

    def test_module_with_only_constants_is_kept(self, tmp_path):  # L115-124
        ...

    def test_annotated_attributes(self):  # L126-145
        ...

    def test_property_classified_as_attribute(self):  # L147-162
        ...

    def test_property_setter_and_deleter_suppressed(self):  # L164-184
        ...

    def test_preserves_source_order(self):  # L186-205
        ...

class TestWalkSource:  # L208-287

    def test_basic_walk(self, tmp_path):  # L209-234
        ...

    def test_nested_subpackage(self, tmp_path):  # L236-248
        ...

    def test_includes_init_with_symbols(self, tmp_path):  # L250-261
        ...

    def test_skips_empty_init(self, tmp_path):  # L263-273
        ...

    def test_skips_syntax_errors(self, tmp_path):  # L275-287
        ...

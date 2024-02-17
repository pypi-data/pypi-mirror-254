import pytest
from ssb_altinn3_util.models.basic_file import BasicFile
from altinn3_test_lib.utils.fileutils import read_file_lines_into_object

import base64

@pytest.fixture(scope="function")
def basic_file_factory():
    def create_basic_file(
            filename: str,
            content_type: str = "test_content",
            b64content: str = "abcd1234test",
            string_content: str = "",
    ) -> BasicFile:
        if len(string_content) > 0:
            encoded_bytes = base64.b64encode(bytes(string_content, "utf-8"))
            b64content = encoded_bytes.decode("utf-8")

        return BasicFile(
            filename=filename,
            content_type=content_type,
            base64_content=b64content
        )

    return create_basic_file


@pytest.fixture(scope="function")
def create_simple_prefill():
    return read_file_lines_into_object("simple_prefill.txt")
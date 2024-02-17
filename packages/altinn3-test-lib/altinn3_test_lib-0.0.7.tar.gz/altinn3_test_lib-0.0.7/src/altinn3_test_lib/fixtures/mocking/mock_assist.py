from typing import Dict, Optional, Tuple

import pytest
from pytest_mock.plugin import MockerFixture

from unittest.mock import MagicMock

from altinn3_test_lib.resources.mocking import MockBehavior


@pytest.fixture(scope="function")
def mocker_factory(mocker: MockerFixture):
    """
    Mocks either a single object/method or a collection.  Behavior is specified via the MockBehavior-object
    (from altinn3_test_lib.resources.mocking import MockBehavior).

    :param mocker: default pytest mocker fixture.  Used for mock building.  Injected automatically
    :return: EITHER a MagicMock object, if called with a single mock-request OR a collection of mocks, in order of
    creation, if a collection is supplied as input.

    """
    def mock_selector(*args, **kwargs):
        if isinstance(args[0], Dict):
            return add_mocks(args[0])
        if isinstance(args[0], str):
            return add_mock(args[0], **kwargs)

    def add_mocks(mock_refs: Dict[str, Optional[MockBehavior]]) -> Tuple[MagicMock]:
        """
        Adds a collection of mocks to the current test function.
        :param mock_refs: A dictionary of mock identifiers and behaviors
        :return: tuple of mocks created in order of creation
        """
        mocks = []
        for key in mock_refs.keys():
            mocks.append(add_mock(key, mock_refs[key]))
        return tuple(mocks)

    def add_mock(object_ref: str, behavior: Optional[MockBehavior] = None) -> MagicMock:
        """
        Adds a single mock to the test.
        :param object_ref: mock identifier (package-path)
        :param behavior: desired behavior for the mock
        :return: the mock
        """
        params = {}
        if behavior is not None:
            if behavior.return_value is not None:
                params["return_value"] = behavior.return_value
            if behavior.side_effect is not None:
                params["side_effect"] = behavior.side_effect

        mock = mocker.patch(object_ref, **params)

        return mock

    return mock_selector

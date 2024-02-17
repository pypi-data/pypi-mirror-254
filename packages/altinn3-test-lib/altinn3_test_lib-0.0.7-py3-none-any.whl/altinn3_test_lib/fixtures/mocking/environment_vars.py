import os

from typing import Dict, Optional

import pytest
from pytest_mock.plugin import MockerFixture

from altinn3_test_lib.resources.mocking import MockBehavior

# This list will be mocked in every test the mock_env_wireup fixture is used.
shared_mocks = {
    "google.auth.default": MockBehavior(return_value=("creds", "project"), side_effect=None)
}


# This is a placeholder fixture.  Override in the using applications conftest.py after importing plugins
# to sepecify what should be mocked in every test using the mock_env_wireup fixture.
# NOTE:  Mocks listed here can be overridden locally in tests by using the mocker_factory fixture.
@pytest.fixture(scope="function")
def global_mocks() -> Dict[str, Optional[MockBehavior]]:
    return {}


@pytest.fixture(scope="function")
def mock_env_wireup(mocker: MockerFixture, mocker_factory, global_mocks):
    """
    Mocks environment variables for tests and handles mocks defined in the global_mocks and shared_mocks collections.
    :param mocker: pytest mocker fixture
    :param mocker_factory: factory function for creating mock objects en masse
    :param global_mocks: fixture holding mocks used by all tests referencing this fixture
    :return: the wire-up-function.  Call it to activate.
    """
    def wireup(expected_source: str = "test_app"):
        mocker.patch.dict(
            os.environ,
            {
                "APPROVED_EVENT_SOURCE_URL": expected_source,
                "ALTINN_ARCHIVE_BUCKET": "test_bucket",
                "DB_API_BASE_URL": "base_url",
                "PROJECT_ID": "Test",
                # instantiator:
                "KEYCLOAK_SECRET_PATH": "testpath",
                "MASKINPORT_CLIENT_ID": "testclient",
                "ALTINN_PLATFORM_URL": "test_plat_url",
                "BIP_PLATFORM_ENVIRONMENT": "test_env",
                "SOURCE_BUCKET": "test_src_bucket",
                "ERROR_BUCKET": "test_err_bucket",
                "ALTINN_APP_URL": "test_app_url",
                "DB_API_URL": "test_db_url",
                "TOKEN_REFRESH_INTERVAL": "30",
                "ENABLE_METRICS": "false",
                "USERPROFILE": "testuser"
            },
            clear=True,
        )

        mocker_factory(shared_mocks | global_mocks)

    return wireup

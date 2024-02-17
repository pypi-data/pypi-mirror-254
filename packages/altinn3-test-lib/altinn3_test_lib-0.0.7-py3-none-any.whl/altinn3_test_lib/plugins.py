all_vars = set(dir())

# plugin references goes here

mocking_environment = "altinn3_test_lib.fixtures.mocking.environment_vars"
mocking_assist = "altinn3_test_lib.fixtures.mocking.mock_assist"
factories_altinn = "altinn3_test_lib.fixtures.factories.altinn_factory"
factories_gcp = "altinn3_test_lib.fixtures.factories.gcp_factories"
factories_file = "altinn3_test_lib.fixtures.factories.file_factory"

# create list of plugin reference names
temp_list = set(dir()) - all_vars

all_plugins = [eval(p) for p in temp_list if p != "all_vars"]

factory_plugins = [p for p in all_plugins if str(p).find(".fixtures.factories.") != -1]
mocking_plugins = [p for p in all_plugins if str(p).find(".fixtures.mocking.") != -1]

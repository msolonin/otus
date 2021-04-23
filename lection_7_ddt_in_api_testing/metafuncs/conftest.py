def pytest_addoption(parser):
    parser.addoption(
        "--input", action="append", default=[], type=str,
        help="inputs to pass to test functions",
    )

    parser.addoption("--all", action="store_true", help="run all combinations")


def pytest_generate_tests(metafunc):

    if "input" in metafunc.fixturenames:
        metafunc.parametrize("input", metafunc.config.getoption("input"))

    if "limited_param" in metafunc.fixturenames:
        end = 3
        if metafunc.config.getoption("all"):
            end = 10
        metafunc.parametrize("limited_param", range(end))

def pytest_addoption(parser):
    parser.addoption("--pairwise", action="store_false", help="run all combinations")


def pytest_generate_tests(metafunc):
    if "limited_param" in metafunc.fixturenames:
        data = [
            ["DELL", "ACER", "ASUS", "MS"],
            ["WIN7", "XP", "WIN10", "WIN8"],
            ["AMD", "INTEL", "ARM64", "ARMv7"],
            ["CHROME", "FIREFOX", "IE11", "SAFARI"]
        ]
        if metafunc.config.getoption("pairwise"):
            agregated_data = []
            for comp in data[0]:
                for oper in data[1]:
                    for proc in data[2]:
                        for browser in data[3]:
                            agregated_data.append([comp, oper, proc, browser])
        else:
            from allpairspy import AllPairs
            agregated_data = AllPairs(data)
        metafunc.parametrize("limited_param", agregated_data)

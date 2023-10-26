import setuptools


def get_install_requirements():
    """
    It reads the requirements.txt file and returns a list of all the requirements

    :return: A list of all the requirements for the project.
    """
    with open("requirements.txt", "r", encoding="utf-8") as f:
        reqs = [x.strip() for x in f.read().splitlines()]
    reqs = [x for x in reqs if not x.startswith("#")]
    return reqs


setuptools.setup(
    name="text-embedding-demo",
    version='0.1.0',
    author="Intelligent Systems Institute @ Novia",
    install_requires=get_install_requirements(),
)
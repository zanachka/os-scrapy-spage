from setuptools import find_packages, setup


def read(*filenames, **kwargs):
    import io
    from os.path import dirname, join

    encoding = kwargs.get("encoding", "utf-8")
    sep = kwargs.get("sep", "\n")
    buf = []
    for filename in filenames:
        with io.open(join(dirname(__file__), filename), encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


def lines(files):
    if isinstance(files, str):
        files = [
            files,
        ]
    import fileinput

    for line in fileinput.input(files):
        yield line


def requirements(files):
    requires = []
    for line in lines(files):
        line = line.strip()
        if line.startswith("git+"):
            line = " @ ".join(
                [l[4:] if l.startswith("egg=") else l for l in line.split("#")[::-1]]
            )
        requires.append(line)
    return requires


def dependency_links(files):
    return [l for l in lines(files) if l.startswith("git+")]


setup(
    name="os-scrapy-spage",
    version="0.0.3",
    packages=find_packages(),
    include_package_data=True,
    license="MIT License",
    description="Spage library for Scrapy",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=requirements("requirements/requirements.txt"),
    dependency_links=dependency_links("requirements/requirements.txt"),
    python_requires=">=3.6",
    zip_safe=False,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)

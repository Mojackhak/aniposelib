import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aniposelib",
    version="0.7.12.post1",
    author="Lili Karashchuk",
    author_email="lili.karashchuk@gmail.com",
    description="Mojackhak fork of Aniposelib for camera calibration and 3D tracking support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mojackhak/aniposelib",
    project_urls={
        "Repository": "https://github.com/Mojackhak/aniposelib",
        "Upstream": "https://github.com/lambdaloop/aniposelib",
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Image Recognition"
    ],
    install_requires=[
        'opencv-contrib-python>=4.7.0.68',
        'numba', 'pandas',
        'numpy', 'scipy', 'toml', 'tqdm'
    ],
    extras_require={
    }
)

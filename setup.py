"""
To build distribution: python setup.py sdist bdist_wheel
"""

import os
import setuptools
import openapiart
import shutil

pkg_name = "snappi_convergence"
version = "0.4.1"
model_protobuf_name = "otgconvergence"


# read long description from readme.md
base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir, "readme.md")) as fd:
    long_description = fd.read()

openapiart.OpenApiArt(
    api_files=["models-convergence/api/info.yaml", "models-convergence/api/api.yaml"],
    protobuf_name=model_protobuf_name,
    artifact_dir="artifacts",
    extension_prefix='snappi'
).GeneratePythonSdk(package_name=pkg_name)

# remove unwanted files
if os.path.exists(pkg_name):
    shutil.rmtree(pkg_name, ignore_errors=True)
print(os.listdir(os.path.join(os.getcwd(), "artifacts")))
shutil.copyfile(
    os.path.join("artifacts", "requirements.txt"),
    os.path.join(base_dir, "pkg_requires.txt")
)
shutil.copytree(os.path.join("artifacts", pkg_name), pkg_name)

shutil.rmtree("artifacts", ignore_errors=True)
# for name in os.listdir(pkg_name):
#     path = os.path.join(pkg_name, name)
#     if "pb2" in path:
#         os.remove(path)
#     else:
#         print(path + ' will be published')

install_requires = []
with open(os.path.join(base_dir, "pkg_requires.txt"), "r+") as fd:
    install_requires = fd.readlines()
    install_requires = install_requires[1:]

setuptools.setup(
    name=pkg_name,
    version=version,
    description="A snappi extension for measuring network convergence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/open-traffic-generator/snappi-convergence",
    author="Open Traffic Generator",
    author_email="ashutshkumr@gmail.com",
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing :: Traffic Generation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],
    keywords='snappi testing open traffic generator automation',
    packages=[pkg_name],
    include_package_data=True,
    python_requires='>=2.7, <4',
    install_requires=install_requires,
    # install_requires=[
    #     'requests',
    #     'pyyaml',
    #     'jsonpath-ng',
    #     'typing',
    # ],
    extras_require={
        'testing': ['pytest']
    },
)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mrftools",
    version="0.1.52",
    author="Andrew Dupuis",
    author_email="andrew.dupuis@case.edu",
    description="Tools for Magnetic Resonance Fingerprinting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.casemri.com/common-resources/mrftools",
    package_dir = {'': 'src'}, # Our packages live under src but src is not a package itself
    packages=setuptools.find_packages("src"), exclude=["test"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'scipy',
        'h5py', 
        'matplotlib',
        'nibabel',
        'SimpleITK', 
        'azure-storage-blob',
        'torch', 
        'torchkbnufft',
        'kornia', 
        'ismrmrd', 
        'fbpca', 
        'tqdm'
    ],
    zip_safe=False
)

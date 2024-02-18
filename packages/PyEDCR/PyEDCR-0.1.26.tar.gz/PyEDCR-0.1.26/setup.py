import setuptools

with open("README.md", "r", encoding="utf-8") as f:
  description = f.read()


setuptools.setup(
  name='PyEDCR',
  version='0.1.26',
  author='Joshua Shay Kricheli, Paulo Shakarian, Spencer Ozgur, Aniruddha Datta, Khoa Vo',
  author_email='name@example.com',
  description='A short description of your package',
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  python_requires='>=3.7',
  long_description=description,
  long_description_content_type = "text/markdown",
  package_dir={"": "src"},
  packages=setuptools.find_packages(where="src", include=["PyEDCR", "PyEDCR.test"]),
  install_requires=[           
    'beautifulsoup4',
    'LTNtorch',
    'matplotlib',
    'numpy',
    'opencv_python',
    'pandas',
    'Pillow',
    'protobuf',
    'Requests',
    'scikit_learn',
    'timm',
    'torch',
    'torchsummary',
    'torchvision',
    'tqdm'
  ],
  package_data={
      "PyEDCR": ["test/*.py",
                 "individual_results/*.npy",
                 "combined_results/*.npy",
                 "test_fine/*.npy",
                 "test_coarse/*npy"]
  },
  include_package_data=True,
)
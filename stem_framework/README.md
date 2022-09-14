# **Development install**

1. Install [conda](https://www.anaconda.com/)

2. Create the [virtual environment](https://www.anaconda.com/)  and install necessary dependencies. Instead of "env" use your name for the virtual environment.

   ```
   conda env create -f environment.yml
   ```

3. Install package it the editable mode using pip:

   ```
   pip install -e .
   ```

4. To test the package have been installed correctly, you may run the following commands with the python

   ```python
   from stem import print_hello_world
   print_hello_world()
   ```

5. Then build the docs to the package with sphinx

   ```
   sphinx-apidoc -o docs stem/
   cd ./docs
   make html
   ```
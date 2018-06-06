# Raga_Practise_Util
This is a Python Packaging Helper Environment that helps beginner's in python get acquainted with the concepts of Building,Packages and Managing them. 
This tutorial gives beginners a complete flow of how python packages are done in the industries.

Please do the following:

1. Create a new git repository with git-init(1). Commit as desired. If you're
   worried about losing any of the sample code that you're writing, create a new
   GitHub repository, skim git-remote(1), and push your code to your new GitHub
   repository.
2. Within this git repository, create the following directory structure:

       .
       ├── my_package
       │   └── tests.py
       └── setup.py

3. Read the [unittest](https://docs.python.org/3.6/library/unittest.html)
   documentation from the beginning through section 26.4.2.0. (That is, read
   until section 26.4.2.1.) In addition, skim the list of methods exposed by
   [`unittest.TestCase`](https://docs.python.org/3.6/library/unittest.html#unittest.TestCase).
4. Create a test case in `tests.py`. Within this test case, create one test
   method for each of the following assertions:

   * '0.1' is equal to '0.1'
   * '0.1' is less than '0.2'
   * '0.2' is greater than '0.10'

   Do not use the `assertTrue` method for these assertions. There are other,
   more targeted methods, as mentioned in step 3. Verify that the tests pass.
5. Read [packaging and distributing
   projects](https://packaging.python.org/guides/distributing-packages-using-setuptools/).
   Feel free to skim the "setup() args" section.
6. Create a virtualenv using `python3 -m venv ...`, and activate it. Populate
   your `setup.py` with just enough information to be valid. Install your
   package into the virtualenv in "editable mode," e.g. with `pip install
   --editable .`. Change to an entirely different directory (e.g. with `cd ~`),
   and verify that you can execute tests with `python -m unittest
   my_package.tests`.
7. Add
   [`install_requires`](https://packaging.python.org/guides/distributing-packages-using-setuptools/#install-requires)
   to `setup.py`, and depend on
   [packaging](https://pypi.org/project/packaging/). Verify that `pip install
   --editable .` pulls in the packaging library. You can verify this with `pip
   freeze`.
8. Add a new test case into the `tests.py` file.  Within this test case, create
   one test method for each of the following assertions:

   * Version('0.1') is equal to Version('0.1')
   * Version('0.1') is less than Version('0.2')
   * Version('0.2') is less than Version('0.10')

   Do not use the `assertTrue` method for these assertions. There are other,
   more targeted methods, as mentioned in step 3. Verify that the tests pass.
9. Add `extras_require` to `setup.py`, and create a "dev" section that lists
   "pylint." See the [docs](http://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies) for an
   example of how to do this. Verify that `pip install --editable .[dev]` pulls
   in pylint. You can verify this with `pip freeze`.
10. Execute `pylint my_package`. Fix all warnings.
11. Deactivate your virtualenv. Blow it away, e.g. with `rm -rf path/to/virtualenv`.
    Create a new one. Install your Python package into this virtualenv. Verify that
    you can move to a different directory and successfully execute the tests, e.g.
    with `cd ~ && python -m unittest my_package.tests`.
12. Once Done with managing the packages locally, The package can be distributed to the remote. This works by creating [aPypI](https://pypi.org/account/register/) account first. Install twine `pip install twine`. Setting up the Build files using `python setup.py sdist` and `pip install wheel` followed by `python setup.py bdist_wheel --universal`. Then run the upload by using `twine upload dist/*`. for more infor refer [docs](https://packaging.python.org/guides/distributing-packages-using-setuptools/#id77) 

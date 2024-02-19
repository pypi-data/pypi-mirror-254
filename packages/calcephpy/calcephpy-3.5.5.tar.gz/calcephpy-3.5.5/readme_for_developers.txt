This file contains the instructions for the developers of the library.

To build the documentation using sphinx-doc, it requires the pip packages : 
    pip install Sphinx sphinx-fortran sphinx-rtd-theme sphinxcontrib-matlabdomain

To publish a new release, you have to :
- change the version number in the following files :
 configure.ac
 src/calceph.h

- update the changelog in the following files :
 NEWS
 doc/source/calceph.final.rst

- update the version of the library using the instructions of
  http://www.gnu.org/software/libtool/manual/html_node/Updating-version-info.html
  in the file :
 src/Makefile.am

- apply these previous changes:
  run the commands :
     autoreconf
     configure --enable-python=yes --enable-maintainer-mode
     cp pythonapi/src/calcephpy.pyx pythonapi/src/calcephpy.pyx.vc
     cd doc && makedoc.sh && cd ..
     make clean && make
    
- under mac os, to build the final tarball : perform the following command
  # turn off special handling of ._* files in tar, etc.
  COPYFILE_DISABLE=1   make dist
  COPYFILE_DISABLE=1   make dist_octave


- build the archive for the Pypi (pip)
  run the commands (create the archive in the directory dist):
    rm -r -f dist
    make clean
    python setup.py sdist  
    
  test the package using testpypi:
    see instructions on https://wiki.python.org/moin/TestPyPI for .pypirc    
    twine upload dist/* -r testpypi
    pip install --user -i https://test.pypi.org/pypi calcephpy
    
   release of the package on pypi :
    see instructions on https://wiki.python.org/moin/TestPyPI for .pypirc    
    twine upload dist/*
    pip install --user  calcephpy
   
   
- publish the new version to homebrew
  run the command
     export HOMEBREW_GITHUB_API_TOKEN=....yourtoken....
     cd /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core
     git -C $(brew --repo homebrew/core) checkout master
     brew bump-formula-pr  --sha256 ...shasum_-a_256....tar.gz...  --url https://www.imcce.fr/content/medias/recherche/equipes/asd/calceph/calceph-x.x.x.tar.gz calceph
    

- publish the new version to vcpkg
  see https://learn.microsoft.com/en-us/vcpkg/contributing/maintainer-guide
  replace X.X.X and X_X_X by the major/minor/patch release  
  
  clone the vcpkg project and create a new branch
     git clone git@github.com:....your_github_login.../vcpkg.git
     git checkout -b port_calceph_X_X_X

  edit the following files (update the version and SHA 512)
     ports/calceph/vcpkg.json ports/calceph/portfile.cmake 

  commit the changes
     export MSG_COMMIT='[calceph] update to version X.X.X'
     git add ports/calceph/portfile.cmake  ports/calceph/vcpkg.json
     git commit -m "$MSG_COMMIT"
     vcpkg x-add-version calceph
     git add versions/baseline.json versions/c-/calceph.json
     git commit -m "$MSG_COMMIT"
     git reset --soft HEAD~2 && git commit -m "$MSG_COMMIT"
     git push --set-upstream origin port_calceph_X_X_X

  create the pull request on github

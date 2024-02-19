dnl /*-----------------------------------------------------------------*/
dnl /*!
dnl   \file configure.ac
dnl   \brief script for autoconf
dnl   \author  M. Gastineau
dnl            Astronomie et Systemes Dynamiques, IMCCE, CNRS, Observatoire de Paris.
dnl
dnl    Copyright, 2008-2024, CNRS
dnl    email of the author : Mickael.Gastineau@obspm.fr
dnl
dnl */
dnl /*-----------------------------------------------------------------*/
dnl
dnl /*-----------------------------------------------------------------*/
dnl /* License  of this file :
dnl This file is "triple-licensed", you have to choose one  of the three licenses
dnl below to apply on this file.
dnl
dnl     CeCILL-C
dnl      The CeCILL-C license is close to the GNU LGPL.
dnl      ( http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html )
dnl
dnl  or CeCILL-B
dnl      The CeCILL-B license is close to the BSD.
dnl      (http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.txt)
dnl
dnl  or CeCILL v2.1
dnl      The CeCILL license is compatible with the GNU GPL.
dnl      ( http://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html )
dnl
dnl
dnl  This library is governed by the CeCILL-C, CeCILL-B or the CeCILL license under
dnl  French law and abiding by the rules of distribution of free software.
dnl  You can  use, modify and/ or redistribute the software under the terms
dnl  of the CeCILL-C or CeCILL license as circulated by CEA, CNRS and INRIA
dnl  at the following URL "http://www.cecill.info".
dnl
dnl  As a counterpart to the access to the source code and  rights to copy,
dnl  modify and redistribute granted by the license, users are provided only
dnl  with a limited warranty  and the software's author,  the holder of the
dnl  economic rights,  and the successive licensors  have only  limited
dnl  liability.
dnl
dnl  In this respect, the user's attention is drawn to the risks associated
dnl  with loading,  using,  modifying and/or developing or reproducing the
dnl  software by the user in light of its specific status of free software,
dnl  that may mean  that it is complicated to manipulate,  and  that  also
dnl  therefore means  that it is reserved for developers  and  experienced
dnl  professionals having in-depth computer knowledge. Users are therefore
dnl  encouraged to load and test the software's suitability as regards their
dnl  requirements in conditions enabling the security of their systems and/or
dnl  data to be ensured and,  more generally, to use and operate it in the
dnl  same conditions as regards security.
dnl
dnl  The fact that you are presently reading this means that you have had
dnl  knowledge of the CeCILL-C, CeCILL-B or CeCILL license and that you accept its terms.
dnl  */
dnl /*-----------------------------------------------------------------*/

dnl configuration file for CALCEPH

AC_INIT([CALCEPH],[3.5.5],[inpop.imcce@obspm.fr],, [https://www.imcce.fr/inpop/calceph/])
AC_CONFIG_AUX_DIR(config)
AM_INIT_AUTOMAKE
AM_EXTRA_RECURSIVE_TARGETS([installnodoc])
AC_CONFIG_FILES(src/f2003calceph.f src/f90calceph.h  Makefile src/Makefile
                tools/Makefile
                tests/Makefile tests/fopenfiles.h
                doc/Makefile doc/source/confcommon.py
                examples/Makefile
                setup.py
                pythonapi/Makefile
                pythonapi/src/Makefile pythonapi/src/setup.py pythonapi/src/calcephpy.pyx
                pythonapi/tests/Makefile
                mexapi/Makefile mexapi/src/Makefile mexapi/src/Constants.m mexapi/tests/Makefile
                mexapi/packaging/Makefile 
                mexapi/packaging/octave/Makefile mexapi/packaging/octave/DESCRIPTION mexapi/packaging/octave/createpackageoctave.sh
                mexapi/packaging/octave/Makefile.src)
dnl comment the next line to enable rebuild autotools file
AM_MAINTAINER_MODE


dnl options
AC_ARG_ENABLE(thread,
            [  --enable-thread : enable thread-safe version for high-level API  [[default=no]] ],,
              enable_thread=no)

AC_ARG_ENABLE(fortran,
            [  --enable-fortran : enable fortran API [[default=yes]] ],,
              enable_fortran=yes)

AC_ARG_ENABLE(python,
            [  --enable-python : enable python API [[default=no]] ],,
              enable_python=no)

AC_ARG_ENABLE(python-package-system,
            [  --enable-python-package-system : enable to install the package to the system site-packages directory [[default=no]] ],,
            enable_python_package_system=no)

AC_ARG_ENABLE(python-package-user,
            [  --enable-python-package-user : enable to install the package to the user site-packages directory [[default=no]] ],,
            enable_python_package_user=no)

AC_ARG_ENABLE(mex-octave,
            [  --enable-mex-octave : enable mex API for Octave [[default=no]] ],,
              enable_mex_octave=no)


AH_TEMPLATE([_GNU_SOURCE],[ definition for fdopen and mkstemp and strtod_l])
AH_TEMPLATE([HAVE_PTHREAD], [ define it to 1 if pthread.h is available])
AH_TEMPLATE([HAVE_RINT], [ define it to 1 if rint is available])

dnl creation du fichier C de configuration
AC_CONFIG_HEADER(src/calcephconfig.h)

dnl verification des programmes
AC_PROG_CC
dnl AC_PROG_CC_C99
dnl definition required for fdopen and mkstemp with intel c++ 11.0
dnl and large files on 32 bit operating systems
AC_USE_SYSTEM_EXTENSIONS
AC_SYS_LARGEFILE
define([AC_LIBTOOL_LANG_CXX_CONFIG], [:])dnl
define([AC_LIBTOOL_LANG_F77_CONFIG], [:])dnl
LT_INIT([win32-dll])
AC_PROG_RANLIB




ACX_C_PRECISEFLOAT
AX_GCC_VAR_ATTRIBUTE(unused)

AC_CHECK_HEADERS(stdio.h)
AC_HEADER_STDC
AC_CHECK_HEADERS(limits.h)
AC_CHECK_HEADERS(string.h)
AC_CHECK_HEADERS(errno.h)
AC_CHECK_HEADERS(math.h)
AC_CHECK_HEADERS(stdbool.h)
AC_CHECK_HEADERS(sys/stat.h)
AC_CHECK_HEADERS(sys/types.h)
AC_CHECK_HEADERS(unistd.h)
AC_CHECK_HEADERS(time.h)
AC_CHECK_HEADERS(sys/mman.h)
AC_CHECK_HEADERS(sys/resource.h)
AC_CHECK_HEADERS(xlocale.h)
AC_CHECK_HEADERS(locale.h)
AC_CHECK_LIB(m, main)
dnl AC_CHECK_FUNCS(rint)
AC_MSG_CHECKING(Checking rint ...)
AC_LINK_IFELSE(
    [AC_LANG_PROGRAM([[
#ifdef HAVE_MATH_H
      #include <math.h>
#endif
      ]],
        [[ return rint(1.0E0); ]])],
    [AC_MSG_RESULT([yes])
        HAVE_RINT=1;])

AC_CHECK_FUNCS(vasprintf)
AC_CHECK_FUNCS(vsnprintf)
AC_CHECK_FUNCS(strncmp)
AC_CHECK_FUNCS(strtod_l)
AC_CHECK_FUNCS(newlocale)
AC_CHECK_FUNCS(freelocale)
AC_CHECK_FUNCS(setlocale)
AC_FUNC_FSEEKO
AC_TYPE_OFF_T
AC_FUNC_MMAP

dnl use thread-safe version
AC_SUBST(FORTRAN_HAVE_PTHREAD)
FORTRAN_HAVE_PTHREAD=0
if test "$enable_thread" = yes ; then
 ACX_PTHREAD( AC_DEFINE(HAVE_PTHREAD,1)
 LIBS="$PTHREAD_LIBS $LIBS"
 CFLAGS="$CFLAGS $PTHREAD_CFLAGS"
 CC="$PTHREAD_CC"
 FORTRAN_HAVE_PTHREAD=1
)
fi

dnl Windows dll requires "-no-undefined" 
dnl see : https://autotools.io/libtool/windows.html 
dnl
AC_SUBST(CALCEPHWIN32_LDFLAGS)
case $host in
  *-*-cygwin* | *-*-mingw* | *-*-pw32* | *-*-os2*)
   if test "$enable_shared" = yes; then
     AC_MSG_CHECKING(Creating the windows dll requires ...)
     CALCEPHWIN32_LDFLAGS="-no-undefined"
     AC_MSG_RESULT([-no-undefined])
   fi
  ;;
esac


dnl use fortran version
AC_SUBST(EXTRAFORTRAN2003INSTALL)
AC_SUBST(EXTRAFORTRAN2003UNINSTALL)
AC_SUBST(EXTRAFORTRAN2003FILES)
AC_SUBST(EXTRAFORTRAN2003EXAMPLES)
AC_SUBST(EXTRAFORTRAN77EXAMPLES)
AC_SUBST(EXTRAFORTRAN2003CHECK)
AC_SUBST(EXTRAFORTRAN77CHECK)

AC_SUBST(ax_cv_f90_modflag)
AC_SUBST(ax_cv_f90_modext)
if test "$enable_fortran" = yes ; then
    dnl check FC wrappers
    AC_PROG_FC
    AC_FC_WRAPPERS
    AC_SUBST([EXTRAFORTRAN77EXAMPLES],['f77single$(EXEEXT) f77multiple$(EXEEXT) f77error$(EXEEXT) f77orient$(EXEEXT) '])
    AC_SUBST([EXTRAFORTRAN77CHECK],['f77sopenfail$(EXEEXT) f77mopenfail$(EXEEXT) \
      f77sopen$(EXEEXT) f77mopen$(EXEEXT) f77sgetconstant$(EXEEXT) f77mgetconstant$(EXEEXT) \
      f77mcheck$(EXEEXT) f77sgetconstantindex$(EXEEXT) f77mgetconstantindex$(EXEEXT)  \
      f77mcomputeunit$(EXEEXT) f77mcomputeunit_naifid$(EXEEXT) f77version$(EXEEXT) \
      f77mcomputeorder$(EXEEXT) f77rotangmomunit$(EXEEXT) f77rotangmomorder$(EXEEXT) \
      f77mtimescale$(EXEEXT) f77mtimespan$(EXEEXT) f77stimescale$(EXEEXT) f77stimespan$(EXEEXT) \
      f77getpositionrecordindex$(EXEEXT) f77getorientrecordindex$(EXEEXT) f77mgetconstantvd$(EXEEXT) f77mgetconstantvs$(EXEEXT) \
      f77mfileversion$(EXEEXT) f77sfileversion$(EXEEXT) f77misthreadsafe$(EXEEXT) f77maxsupportedderivativeorder$(EXEEXT)'])

    dnl check fortran 2003 compliance
    AX_F90_MODULE_FLAG
    AX_F90_MODULE_EXTENSION
    if test "$ax_cv_f90_modflag" = "" ; then
     ax_cv_f90_modflag="-I"
    fi
    AX_F2003_ISO_C_BINDING
    if  test "$ax_cv_f2003_iso_c_binding" = yes ; then
     AC_SUBST([EXTRAFORTRAN2003FILES],['f2003main$(EXEEXT)'])
     AC_SUBST([EXTRAFORTRAN2003EXAMPLES],['f2003single$(EXEEXT) f2003multiple$(EXEEXT) f2003scompute$(EXEEXT) f2003error$(EXEEXT) f2003orient$(EXEEXT) '])
     AC_SUBST([EXTRAFORTRAN2003CHECK],['f2003sopenfail$(EXEEXT) f2003mopenfail$(EXEEXT) \
      f2003sopen$(EXEEXT) f2003mopen$(EXEEXT) f2003sgetconstant$(EXEEXT) f2003mgetconstant$(EXEEXT) \
      f2003mcheck$(EXEEXT) f2003sgetconstantindex$(EXEEXT) f2003mgetconstantindex$(EXEEXT)  \
      f2003mcomputeunit$(EXEEXT) f2003mcomputeunit_naifid$(EXEEXT) f2003version$(EXEEXT)  \
      f2003mcomputeorder$(EXEEXT) f2003rotangmomunit$(EXEEXT) f2003rotangmomorder$(EXEEXT) \
      f2003mtimescale$(EXEEXT) f2003mtimespan$(EXEEXT) f2003stimescale$(EXEEXT) f2003stimespan$(EXEEXT) \
      f2003getpositionrecordindex$(EXEEXT)  f2003getorientrecordindex$(EXEEXT) f2003mgetconstantvd$(EXEEXT) f2003mgetconstantvs$(EXEEXT) \
      f2003mfileversion$(EXEEXT) f2003sfileversion$(EXEEXT) f2003misthreadsafe$(EXEEXT) f2003maxsupportedderivativeorder$(EXEEXT) '])
     AC_SUBST([EXTRAFORTRAN2003INSTALL],['$(DESTDIR)$(includedir)/calceph.$(ax_cv_f90_modext)'])
     AC_SUBST([EXTRAFORTRAN2003UNINSTALL],['uninstallf90mod'])
    fi
fi

dnl use python version
AM_CONDITIONAL([COND_PYTHON], [test "$enable_python" = yes])
AC_SUBST(CYTHON_NOEXCEPT)

if test "$enable_python" = yes ; then
    AM_PATH_PYTHON
    AX_PYTHON_DEVEL
    AC_MSG_CHECKING([Cython supports the keyword noexcept])
    $PYTHON -c 'import Cython; import sys; sys.exit(0 if (Cython.__version__ >= "3.0.0") else 1)' 2> /dev/null
    AS_IF([test $? -eq 0], [
          AC_MSG_RESULT([yes])
          AC_SUBST([CYTHON_NOEXCEPT],[' noexcept'])
        ], 
        [AC_MSG_RESULT([no])])
fi

AM_CONDITIONAL([COND_PYTHON_PACKAGE_SYSTEM], [test "$enable_python_package_system" = yes])
AM_CONDITIONAL([COND_PYTHON_PACKAGE_USER], [test "$enable_python_package_user" = yes])

dnl use mex version
AM_CONDITIONAL([COND_MEX_OCTAVE], [test "$enable_mex_octave" = yes])


AX_SPLIT_VERSION
AC_SUBST([CALCEPH_VERSION_MAJOR],[$AX_MAJOR_VERSION])
AC_SUBST([CALCEPH_VERSION_MINOR],[$AX_MINOR_VERSION])
AC_SUBST([CALCEPH_VERSION_PATCH],[$AX_POINT_VERSION])

dnl creation du makefile
AC_OUTPUT


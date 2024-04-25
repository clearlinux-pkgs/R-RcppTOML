#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RcppTOML
Version  : 0.2.2
Release  : 13
URL      : https://cran.r-project.org/src/contrib/RcppTOML_0.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RcppTOML_0.2.2.tar.gz
Summary  : 'Rcpp' Bindings to Parser for "Tom's Obvious Markup Language"
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-RcppTOML-lib = %{version}-%{release}
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
"Tom's Obvious Markup Language") specifies an excellent format

%package lib
Summary: lib components for the R-RcppTOML package.
Group: Libraries

%description lib
lib components for the R-RcppTOML package.


%prep
%setup -q -n RcppTOML
cd %{_builddir}/RcppTOML

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1675099064

%install
export SOURCE_DATE_EPOCH=1675099064
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RcppTOML/DESCRIPTION
/usr/lib64/R/library/RcppTOML/INDEX
/usr/lib64/R/library/RcppTOML/Meta/Rd.rds
/usr/lib64/R/library/RcppTOML/Meta/features.rds
/usr/lib64/R/library/RcppTOML/Meta/hsearch.rds
/usr/lib64/R/library/RcppTOML/Meta/links.rds
/usr/lib64/R/library/RcppTOML/Meta/nsInfo.rds
/usr/lib64/R/library/RcppTOML/Meta/package.rds
/usr/lib64/R/library/RcppTOML/NAMESPACE
/usr/lib64/R/library/RcppTOML/NEWS.Rd
/usr/lib64/R/library/RcppTOML/R/RcppTOML
/usr/lib64/R/library/RcppTOML/R/RcppTOML.rdb
/usr/lib64/R/library/RcppTOML/R/RcppTOML.rdx
/usr/lib64/R/library/RcppTOML/help/AnIndex
/usr/lib64/R/library/RcppTOML/help/RcppTOML.rdb
/usr/lib64/R/library/RcppTOML/help/RcppTOML.rdx
/usr/lib64/R/library/RcppTOML/help/aliases.rds
/usr/lib64/R/library/RcppTOML/help/paths.rds
/usr/lib64/R/library/RcppTOML/html/00Index.html
/usr/lib64/R/library/RcppTOML/html/R.css
/usr/lib64/R/library/RcppTOML/include/toml++/impl/array.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/array.inl
/usr/lib64/R/library/RcppTOML/include/toml++/impl/at_path.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/at_path.inl
/usr/lib64/R/library/RcppTOML/include/toml++/impl/date_time.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/formatter.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/formatter.inl
/usr/lib64/R/library/RcppTOML/include/toml++/impl/forward_declarations.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/header_end.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/header_start.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/json_formatter.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/json_formatter.inl
/usr/lib64/R/library/RcppTOML/include/toml++/impl/key.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/make_node.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/node.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/node.inl
/usr/lib64/R/library/RcppTOML/include/toml++/impl/node_view.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/parse_error.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/parse_result.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/parser.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/parser.inl
/usr/lib64/R/library/RcppTOML/include/toml++/impl/path.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/path.inl
/usr/lib64/R/library/RcppTOML/include/toml++/impl/preprocessor.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/print_to_stream.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/print_to_stream.inl
/usr/lib64/R/library/RcppTOML/include/toml++/impl/simd.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/source_region.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/std_except.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/std_initializer_list.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/std_map.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/std_new.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/std_optional.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/std_string.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/std_string.inl
/usr/lib64/R/library/RcppTOML/include/toml++/impl/std_utility.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/std_variant.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/std_vector.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/table.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/table.inl
/usr/lib64/R/library/RcppTOML/include/toml++/impl/toml_formatter.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/toml_formatter.inl
/usr/lib64/R/library/RcppTOML/include/toml++/impl/unicode.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/unicode.inl
/usr/lib64/R/library/RcppTOML/include/toml++/impl/unicode_autogenerated.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/value.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/version.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/yaml_formatter.h
/usr/lib64/R/library/RcppTOML/include/toml++/impl/yaml_formatter.inl
/usr/lib64/R/library/RcppTOML/include/toml++/toml.h
/usr/lib64/R/library/RcppTOML/tests/tinytest.R
/usr/lib64/R/library/RcppTOML/tinytest/arrays.toml
/usr/lib64/R/library/RcppTOML/tinytest/bool_datetime.toml
/usr/lib64/R/library/RcppTOML/tinytest/dates_and_times.toml
/usr/lib64/R/library/RcppTOML/tinytest/float.toml
/usr/lib64/R/library/RcppTOML/tinytest/integer.toml
/usr/lib64/R/library/RcppTOML/tinytest/strings.toml
/usr/lib64/R/library/RcppTOML/tinytest/tables.toml
/usr/lib64/R/library/RcppTOML/tinytest/test_arrays.R
/usr/lib64/R/library/RcppTOML/tinytest/test_bool_datetime.R
/usr/lib64/R/library/RcppTOML/tinytest/test_dates_times.R
/usr/lib64/R/library/RcppTOML/tinytest/test_examples.R
/usr/lib64/R/library/RcppTOML/tinytest/test_float.R
/usr/lib64/R/library/RcppTOML/tinytest/test_integer.R
/usr/lib64/R/library/RcppTOML/tinytest/test_misc.R
/usr/lib64/R/library/RcppTOML/tinytest/test_strings.R
/usr/lib64/R/library/RcppTOML/tinytest/test_tables.R
/usr/lib64/R/library/RcppTOML/tinytest/toml_example-v0.4.0.toml
/usr/lib64/R/library/RcppTOML/tinytest/toml_example.toml
/usr/lib64/R/library/RcppTOML/tinytest/toml_hard_example.toml
/usr/lib64/R/library/RcppTOML/toml/ex1.toml
/usr/lib64/R/library/RcppTOML/toml/ex2.toml
/usr/lib64/R/library/RcppTOML/toml/ex3.toml
/usr/lib64/R/library/RcppTOML/toml/ex4.toml
/usr/lib64/R/library/RcppTOML/toml/example.toml
/usr/lib64/R/library/RcppTOML/toml/strings.toml
/usr/lib64/R/library/RcppTOML/toml/tablearray.toml

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/RcppTOML/libs/RcppTOML.so
/usr/lib64/R/library/RcppTOML/libs/RcppTOML.so.avx2
/usr/lib64/R/library/RcppTOML/libs/RcppTOML.so.avx512

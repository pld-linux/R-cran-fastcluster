%define		fversion	%(echo %{version} |tr r -)
%define		modulename	fastcluster
Summary:	Fast hierarchical clustering routines for R and Python
Name:		R-cran-%{modulename}
Version:	1.1.11
Release:	1
License:	GPL v2
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	9c2ffff654e574237c4c72b5d3fa60bf
URL:		http://cran.fhcrc.org/web/packages/fastcluster/index.html
BuildRequires:	R >= 2.8.1
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a two-in-one package which provides interfaces to both R and
Python. It implements fast hierarchical, agglomerative clustering
routines. Part of the functionality is designed as drop-in replacement
for existing routines: “linkage” in the SciPy package
“scipy.cluster.hierarchy”, “hclust” in R's “stats” package, and the
“flashClust” package. It provides the same functionality with the
benefit of a much faster implementation. Moreover, there are
memory-saving routines for clustering of vector data, which go beyond
what the existing packages provide. For information on how to install
the Python files, see the file INSTALL in the source distribution.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}

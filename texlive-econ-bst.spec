Name:		texlive-econ-bst
Version:	61499
Release:	1
Summary:	BibTeX style for economics papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/econ-bst
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/econ-bst.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/econ-bst.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a BibTeX style file for papers in economics. It
provides the following features: author-year type citation
reference style used in economics papers highly customizable
use of "certified random order" as proposed by Ray Robson
(2018)

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/econ-bst
%doc %{_texmfdistdir}/doc/bibtex/econ-bst

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

%global tl_name econ-bst
%global tl_revision 76907

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.3
Release:	%{tl_revision}.1
Summary:	BibTeX style for economics papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/econ-bst
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/econ-bst.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/econ-bst.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a BibTeX style file for papers in economics. It provides the
following features: author-year type citation reference style used in
economics papers highly customizable use of "certified random order" as
proposed by Ray Robson (2018)


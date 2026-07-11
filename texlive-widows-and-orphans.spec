%global tl_name widows-and-orphans
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0f
Release:	%{tl_revision}.1
Summary:	Identify (typographic) widows and orphans
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/widows-and-orphans
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/widows-and-orphans.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/widows-and-orphans.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/widows-and-orphans.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package identifies all widows and orphans in a document to help a
user to get rid of them. The act of resolving still needs to be done
manually: By rewriting text, running some paragraph long or short or
explicitly breaking in some strategic place. It will also identify and
warn about words broken across columns or pages and display formulas
separated from their introductory paragraph.


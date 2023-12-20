Name:		texlive-widows-and-orphans
Version:	66753
Release:	1
Summary:	Identify (typographic) widows and orphans
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/widows-and-orphans
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/widows-and-orphans.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/widows-and-orphans.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/widows-and-orphans.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package identifies all widows and orphans in a document to
help a user to get rid of them. The act of resolving still
needs to be done manually: By rewriting text, running some
paragraph long or short or or explicitly breaking in some
strategic place. It will also identify and warn about words
broken across columns or pages and display formulas separated
from their introductory paragraph.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/widows-and-orphans
%{_texmfdistdir}/tex/latex/widows-and-orphans
%doc %{_texmfdistdir}/doc/latex/widows-and-orphans

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

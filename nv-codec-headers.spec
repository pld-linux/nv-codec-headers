Summary:	FFmpeg version of headers for NVidia's codec APIs (ffnvcodec)
Summary(pl.UTF-8):	Wersja FFmpeg nagłówków do API kodeków firmy NVidia (ffnvcodec)
Name:		nv-codec-headers
Version:	10.0.26.0
Release:	1
License:	MIT
Group:		Development/Libraries
# originally https://git.videolan.org/?p=ffmpeg/nv-codec-headers.git
# but use github mirror for stable tarballs
#Source0Download: https://github.com/FFmpeg/nv-codec-headers/releases
Source0:	https://github.com/FFmpeg/nv-codec-headers/releases/download/n%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f63a46c9d41b60a637e4d4c290285d46
URL:		https://git.videolan.org/?p=ffmpeg/nv-codec-headers.git
BuildRequires:	rpmbuild(macros) >= 1.446
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FFmpeg version of headers for NVidia's codec APIs.

This version corresponds to Video Codec SDK version 9.0.18. Required
minimal NVidia Linux drivers version is 418.30.

%description -l pl.UTF-8
Wersja FFmpeg nagłówków do API kodeków firmy NVidia.

Ta wersja odpowiada Video Codec SDK w wersji 9.0.18. Wymagana
minimalna wersja sterowników firmy NVidia dla Linuksa to 418.30.

%prep
%setup -q

%build
%{__make} \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

# pass LIBDIR (currently used for .pc file only) = "share" so that package can be noarch
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=share

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_includedir}/ffnvcodec
%{_npkgconfigdir}/ffnvcodec.pc

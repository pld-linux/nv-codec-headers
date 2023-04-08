Summary:	FFmpeg version of headers for NVidia's codec APIs (ffnvcodec)
Summary(pl.UTF-8):	Wersja FFmpeg nagłówków do API kodeków firmy NVidia (ffnvcodec)
Name:		nv-codec-headers
Version:	12.0.16.0
Release:	1
License:	MIT
Group:		Development/Libraries
# originally https://git.videolan.org/?p=ffmpeg/nv-codec-headers.git
# but use github mirror for stable tarballs
#Source0Download: https://github.com/FFmpeg/nv-codec-headers/releases
Source0:	https://github.com/FFmpeg/nv-codec-headers/releases/download/n%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	21c29fed4437a746ae0216fc91534588
URL:		https://git.videolan.org/?p=ffmpeg/nv-codec-headers.git
BuildRequires:	rpmbuild(macros) >= 1.446
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FFmpeg version of headers for NVidia's codec APIs.

This version corresponds to Video Codec SDK version 11.1.5. Required
minimal NVidia Linux drivers version is 470.57.02.

%description -l pl.UTF-8
Wersja FFmpeg nagłówków do API kodeków firmy NVidia.

Ta wersja odpowiada Video Codec SDK w wersji 11.1.5. Wymagana
minimalna wersja sterowników firmy NVidia dla Linuksa to 470.57.02.

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

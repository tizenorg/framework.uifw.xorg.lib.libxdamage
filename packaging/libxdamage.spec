
Name:       libxdamage
Summary:    X.Org X11 libXdamage runtime library
Version:    1.1.3
Release:    2.3
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.gz
Source1001: packaging/libxdamage.manifest 
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(damageproto)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros)

%description
Description: %{summary}


%package devel
Summary:    X.Org X11 libXdamage development package
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Description: %{summary}


%prep
%setup -q -n %{name}-%{version}


%build
cp %{SOURCE1001} .
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed"
%reconfigure --disable-static
# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig



%files
%manifest libxdamage.manifest
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libXdamage.so.1
%{_libdir}/libXdamage.so.1.1.0


%files devel
%manifest libxdamage.manifest
%defattr(-,root,root,-)
%doc AUTHORS README ChangeLog
%dir %{_includedir}/X11
%dir %{_includedir}/X11/extensions
%{_includedir}/X11/extensions/Xdamage.h
%{_libdir}/libXdamage.so
%{_libdir}/pkgconfig/xdamage.pc


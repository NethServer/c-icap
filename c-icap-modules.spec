# Based on Mageia RPM

Summary:          An ICAP module server coded in C
Name:             c-icap-modules
Version:          0.5.5
Release:          1%{?dist}
License:          GPL
Group:            System/Servers
URL:              http://sourceforge.net/projects/c-icap/
Source0:          http://downloads.sourceforge.net/project/c-icap/c-icap-modules/0.5.x/c_icap_modules-%{version}.tar.gz
BuildRequires:    clamav-devel
BuildRequires:    c-icap-devel
BuildRequires:    zlib-devel
BuildRequires:    automake
BuildRequires:    autoconf
Requires:         c-icap


%description
An ICAP modules server coded in C


%prep
%setup -q -n c_icap_modules-%{version}

%build
%configure  \
    CFLAGS="${RPM_OPT_FLAGS} -fno-strict-aliasing" \
    --enable-shared                                \
    --enable-static                                \
    --with-bdb


make %{?_smp_mflags}

%install
%{__mkdir_p} %{buildroot}/etc/c-icap/
%makeinstall DESTDIR=%{buildroot}

# cleanup
rm -f %{buildroot}%{_libdir}/c_icap/*.*a
rm -f %{buildroot}%{_libdir}/*.*a
find %{buildroot} \( -name c-icap-mods-sguardDB -o -name c-icap-mods-sguardDB.8 \) -delete


%files
%doc AUTHORS COPYING
%dir %{_libdir}/c_icap
%attr(0755,root,root) %{_libdir}/c_icap/*.so
%config(noreplace) %{_sysconfdir}/c-icap/virus_scan.conf
%config(noreplace) %{_sysconfdir}/c-icap/srv_url_check.conf
%config(noreplace) %{_sysconfdir}/c-icap/clamd_mod.conf
%config(noreplace) %{_sysconfdir}/c-icap/clamd_mod.conf.default
%config(noreplace) %{_sysconfdir}/c-icap/srv_content_filtering.conf.default
%config(noreplace) %{_sysconfdir}/c-icap/virus_scan.conf.default
%config(noreplace) %{_sysconfdir}/c-icap/srv_url_check.conf.default
%{_datadir}/c_icap/templates/srv_url_check/en/*
%{_datadir}/c_icap/templates/virus_scan/en/*
%{_datadir}/c_icap/templates/srv_content_filtering/en/*


%changelog
* Mon May 10 2021 Marco Ebert <marco_ebert@icloud.com> - 0.5.5-1
- Build 0.5.5 for el7

* Wed Jan 20 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.4.2-1
- Build 0.4.2 for el7

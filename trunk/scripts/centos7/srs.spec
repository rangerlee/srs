Name:           srs
Version:        2.0.263
Release:        1%{?dist}
Summary:        SRS is an industrial-strength live streaming cluster, with the best conceptual integrity and the simplest implementation.
Group:		Applications/Multimedia
License:        MIT
URL:            https://github.com/rangerlee/srs.git
Source0:        %{name}-%{version}.tar.gz

#BuildRequires:  
#Requires:       

%description
SRS(Simple RTMP Server) over state-threads created on 2013.10.

SRS delivers rtmp/hls/http/hds live on x86/x64/arm/mips linux/osx, supports origin/edge/vhost and transcode/ingest and dvr/forward and http-api/http-callback/reload, introduces tracable session-oriented log, exports client srs-librtmp, with stream caster to push MPEGTS-over-UDP/RTSP to SRS, provides EN/CN wiki and the most simple architecture.

https://github.com/ossrs/srs.git
https://github.com/rangerlee/srs.git

%post
systemctl daemon-reload

%prep
%setup -q

%build
cd trunk
sh configure --without-hls --without-hds --without-dvr --without-nginx --with-ssl --without-ffmpeg --without-transcode --without-ingest --with-stat --without-http-callback --with-http-server --with-stream-caster --with-http-api --with-librtmp --without-research --with-utest --without-gperf --without-gmc --without-gmp --without-gcp --without-gprof --without-arm-ubuntu12 --without-mips-ubuntu12 --log-trace
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/lib/srs
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/etc
mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d
mkdir -p $RPM_BUILD_ROOT/lib/systemd/system
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/trunk/objs/srs $RPM_BUILD_ROOT/usr/local/bin/srs
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/trunk/scripts/centos7/srs.logrotate $RPM_BUILD_ROOT/etc/logrotate.d/srs
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/trunk/scripts/centos7/srs.conf $RPM_BUILD_ROOT/etc/srs.conf
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/trunk/scripts/centos7/srs.service $RPM_BUILD_ROOT/lib/systemd/system/srs.service

%files
%attr(-,root,root) /usr/local/bin/srs
%attr(-,root,root) %config /etc/srs.conf
%attr(-,root,root) %config /etc/logrotate.d/srs
%attr(-,root,root) %config /lib/systemd/system/srs.service
%attr(-,root,root) /var/lib/srs/

%doc

%changelog

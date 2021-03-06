#
# Copyright (c) 2016 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/scancode-toolkit/
# The ScanCode software is licensed under the Apache License version 2.0.
# Data generated with ScanCode require an acknowledgment.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with ScanCode or any ScanCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with ScanCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  ScanCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  ScanCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/nexB/scancode-toolkit/ for support and download.

from __future__ import absolute_import
from __future__ import print_function

import os.path

from commoncode.testcase import FileBasedTesting

import packagedcode
from packagedcode import freebsd
from packagedcode import maven
from packagedcode import npm
from packagedcode import cargo
from packagedcode import phpcomposer
from packagedcode import rpm
from packagedcode.recognize import recognize_packages
from packagedcode import nuget


class TestRecognize(FileBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

    def test_recognize_packages_deb(self):
        test_file = self.get_test_loc('archives/adduser_3.112ubuntu1_all.deb')
        packages = recognize_packages(test_file)
        assert packages
        assert isinstance(packages[0], packagedcode.models.DebianPackage)

    def test_recognize_packages_rpm(self):
        test_file = self.get_test_loc('archives/alfandega-2.2-2.rh80.src.rpm')
        packages = recognize_packages(test_file)
        assert packages
        assert isinstance(packages[0], rpm.RpmPackage)

    def test_recognize_packages_cab(self):
        test_file = self.get_test_loc('archives/basic.cab')
        packages = recognize_packages(test_file)
        assert packages
        assert isinstance(packages[0], packagedcode.models.CabPackage)

    def test_recognize_packages_rar(self):
        test_file = self.get_test_loc('archives/basic.rar')
        packages = recognize_packages(test_file)
        assert not packages

    def test_recognize_packages_zip(self):
        test_file = self.get_test_loc('archives/myarch-2.3.0.7z')
        packages = recognize_packages(test_file)
        assert not packages

    def test_recognize_packages_gem(self):
        test_file = self.get_test_loc('archives/mysmallidea-address_standardization-0.4.1.gem')
        packages = recognize_packages(test_file)
        assert packages
        assert isinstance(packages[0], packagedcode.rubygems.RubyGem)

    def test_recognize_packages_jar(self):
        test_file = self.get_test_loc('archives/simple.jar')
        packages = recognize_packages(test_file)
        assert packages
        assert isinstance(packages[0], packagedcode.models.JavaJar)

    def test_recognize_packages_iso(self):
        test_file = self.get_test_loc('archives/small.iso')
        packages = recognize_packages(test_file)
        assert packages
        assert isinstance(packages[0], packagedcode.models.IsoImagePackage)

    def test_recognize_packages_does_not_recognize_plain_tarball(self):
        test_file = self.get_test_loc('archives/tarred_bzipped.tar.bz2')
        packages = recognize_packages(test_file)
        assert not packages

    def test_recognize_cpan_manifest_as_plain_package(self):
        test_file = self.get_test_loc('cpan/MANIFEST')
        try:
            recognize_packages(test_file)
            self.fail('Exception not raised')
        except NotImplementedError:
            pass

    def test_recognize_maven_dot_pom(self):
        test_file = self.get_test_loc('m2/aspectj/aspectjrt/1.5.3/aspectjrt-1.5.3.pom')
        packages = recognize_packages(test_file)
        assert packages
        assert isinstance(packages[0], maven.MavenPomPackage)

    def test_recognize_maven_pom_xml(self):
        test_file = self.get_test_loc('maven2/pom.xml')
        packages = recognize_packages(test_file)
        assert packages
        assert isinstance(packages[0], maven.MavenPomPackage)

    def test_recognize_npm(self):
        test_file = self.get_test_loc('recon/package.json')
        packages = recognize_packages(test_file)
        assert packages
        assert isinstance(packages[0], npm.NpmPackage)

    def test_recognize_cargo(self):
        test_file = self.get_test_loc('recon/Cargo.toml')
        packages = recognize_packages(test_file)
        assert packages
        assert isinstance(packages[0], cargo.RustCargoCrate)

    def test_recognize_composer(self):
        test_file = self.get_test_loc('recon/composer.json')
        packages = recognize_packages(test_file)
        assert packages
        assert isinstance(packages[0], phpcomposer.PHPComposerPackage)

    def test_recognize_freebsd(self):
        test_file = self.get_test_loc('freebsd/multi_license/+COMPACT_MANIFEST')
        packages = recognize_packages(test_file)
        assert packages
        assert isinstance(packages[0], freebsd.FreeBSDPackage)

    def test_recognize_nuget(self):
        test_file = self.get_test_loc('recon/bootstrap.nuspec')
        packages = recognize_packages(test_file)
        assert packages
        assert isinstance(packages[0], nuget.NugetPackage)

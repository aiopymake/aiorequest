#!/usr/bin/env bats


setup() {
:<<DOC
  Installs aiorequest package
DOC
  python setup.py install
}


teardown() {
:<<DOC
  Removes aiorequest package
DOC
  rm -rf ${PACKAGE_NAME}.egg-info dist build
  pip uninstall -y ${PACKAGE_NAME}
}


@test "package name" {
:<<DOC
  Test package name
DOC
  pip list | grep ${PACKAGE_NAME}
  [ "$?" -eq 0 ]
}


@test "package version" {
:<<DOC
  Test package version
DOC
  pip list | grep ${PACKAGE_VERSION}
  [ "$?" -eq 0 ]
}

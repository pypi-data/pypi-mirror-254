# sts-libs

Python library for simplifying the process of writing storage tests on RPM-based Linux distributions.

## About
sts-libs is designed to work with [tmt](https://github.com/teemtee/tmt) and pytest.

It started as an incompatible fork of [libsan](https://gitlab.com/rh-kernel-stqe/python-libsan)
and [stqe](https://gitlab.com/rh-kernel-stqe/python-libsan) with many changes. Most notably:
 - Python 3.8+ only.
 - Minimum dependencies.
 - With tmt and pytest compatibility in mind.
 - One repository for both libs and tests.

Going forward, the libs could become a pytest plugin and compliment others, like pytest-testinfra, with which there is currently some overlap.

## Who is this for?
Fedora, CentOS Stream, RHEL testers.

## How do I contribute?
See [contributing](https://gitlab.com/rh-kernel-stqe/sts/docs/contributing.md) doc.

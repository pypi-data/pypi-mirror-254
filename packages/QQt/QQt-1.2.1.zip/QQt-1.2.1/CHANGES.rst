Changelog
=========

1.2.1 (2024-01-26)
------------------
- Setup update (now based on tox >= 4.0).
- Add support for PyPy 3.9 and 3.10
- Copyright year update.
- Cleanup.

1.2.0 (2023-11-22)
------------------
- Add  support for Python 3.12
- Drop support for Python 3.7
- Setup (dependencies) update.

1.1.1 (2023-02-28)
------------------
- Add  support for Python 3.8, 3.9, 3.10 and 3.11
- Drop support for Python 3.6.
- Setup general update and cleanup.

1.1.1rc7 (2020-10-18)
---------------------
- Drop support for Python 3.5
- Setup general update and cleanup.
- Setup: fix an improper dependencies versions.
- Fixed docs setup.

1.1.0rc9 (2019-11-13)
---------------------
- | Requirements upgrade:
  | PySide2 to at least 5.13.2
  | PyQt5   to at least 5.13.2
- Setup updates and cleanup.

1.1.0rc7 (2019-10-29)
---------------------
- | Requirements upgrade:
  | PySide2 to at least 5.13.1
  | PyQt5   to at least 5.13.1
- Adding of (for now fake/empty) test case.
- Setup updates and cleanup.

1.1.0rc2 (2019-08-02)
---------------------
- | Requirements upgrade:
  | QtPy    to at least 1.9.0
  | PySide2 to at least 5.13.0
  | PyQt5   to at least 5.13.0
  | This allows to have applications that import PySide2 and PyQt5 at the same time
  | (which is possible if both bindings are compiled for the same Qt version).
- StreamEmitter class added.

1.0.0b5 (2019-06-10)
--------------------
- Adding setup extras PySide and PyQt for installing PySide2 or PyQt5 backends.
- Fix a bug for PySide2 as backend.
- Adding a monkey-patch for vtk.qt (vtk==8.1.x).
- Fixes and cleanup of setup.

1.0.0b1 (2019-05-22)
--------------------
- First public release.

0.0.1a1 (2012-03-9)
-------------------
- Initial version.

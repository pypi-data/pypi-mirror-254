v4.0.0 (2024-01-12)
===================

Breaking Changes to the Specification
-------------------------------------

- Add conditional requiredness field, `instrument_required: str(required=False)`, that makes a key `required` if it comes from a header
  from an instrument that matches the value passed to the spec field. E.g., if a key has `instrument_required: vbi` then any header
  from the VBI instrument will make that key `required`. (`#42 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/42>`__)
- "STOKES" key is now `required`. For non-polarimetric data the value will always be "I". This matches how data are
  treated in inventory. (`#43 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/43>`__)
- Add conditional requiredness field, `polarimetric_required: bool(required=False)`, that makes a key `required` if it comes from a header
  from a polarimetric dataset (i.e., a dataset that produces Stokes I, Q, U, V data). The combinations of which specific header keys/values
  conspire to indicate a dataset is polarimetric are defined on a per-instrument level. (`#43 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/43>`__)


Breaking change to the Python API
---------------------------------

- Implement framework for conditional requiredness on keys. Replaces `load_expanded_spec214` with `load_proessed_spec214`. (`#42 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/42>`__)
- Refactor spec_processors so each processor is a module under a new `spec_processor` package. (`#43 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/43>`__)


v3.9.0 (2023-11-22)
===================

Backwards Compatible Changes to the Specification
-------------------------------------------------

- Removing CNMODCST, CNMODANG, CNOFFANG, CNCNDR, and CNCRAMP from L1 CRYO-NIRSP headers due to them not being relevant to the L1 data. (`#41 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/41>`__)


v3.8.1 (2023-09-20)
===================

Bug Fixes to the Python API
---------------------------

- Correct character case of some CRYO-NIRSP keywords. (`#40 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/40>`__)


v3.8.0 (2023-09-19)
===================

Backwards Compatible Changes to the Specification
-------------------------------------------------

- Update FITS L0 schema to SPEC-0122 revision I. (`#39 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/39>`__)


v3.7.1 (2023-07-26)
===================

Bug Fixes to the Python API
---------------------------

- Update the python version used in the Read The Docs build process.



v3.7.0 (2023-07-26)
===================

Backwards Compatible Changes to the Specification
-------------------------------------------------

- Adding the FITS standard key `ZBLANK` (`#36 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/36>`__)


v3.6.0 (2023-04-24)
===================

Backwards Compatible Changes to the Specification
-------------------------------------------------

- Add `VBINMOSC` and `VBICMOSC` keys that encode the total number of and current mosaic repeat in VBI data. (`#35 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/35>`__)


v3.5.0 (2023-04-10)
===================

Backwards Compatible Changes to the Specification
-------------------------------------------------

- Added `NSPECLNS` and `SPECLN<sl>` keys to support inclusion of spectral line information. (`#34 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/34>`__)


v3.4.0 (2023-03-15)
===================

Backwards Compatible Changes to the Specification
-------------------------------------------------

- Add CRYO-NIRSP keys for tracking number of map scans. (`#32 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/32>`__)
- Change units for some VISP specific keywords. (`#33 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/33>`__)


v3.3.0 (2023-02-15)
===================

Bug Fixes to the Python API
---------------------------

- Proposal and experiment ID groups do not get copied from the raw headers. (`#30 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/30>`__)


Documentation
-------------

- Update FITS L0 schema to SPEC-0122 revision H. (`#31 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/31>`__)


v3.2.1 (2023-02-02)
===================

Bug Fixes to the Python API
---------------------------

- Made expansions conditional on keywords that determine their range existing. (`#29 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/29>`__)


v3.2.0 (2023-02-01)
===================

Backwards Compatible Changes to the Specification
-------------------------------------------------

- Revert DL-NIRSP keywords to not required. (`#28 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/28>`__)


v3.1.0 (2023-02-01)
===================

Backwards Compatible Changes to the Specification
-------------------------------------------------

- Add contributing proposal and experiment id keywords. (`#24 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/24>`__)
- Conform with SPEC-0122 revision G. (`#26 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/26>`__)
- Set required DL-NIRSP keywords. (`#27 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/27>`__)


New Feature in the Python API
-----------------------------

- Refactor how FITS keywords are integer-expanded. (`#25 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/25>`__)


v3.0.0 (2022-10-26)
===================

Bug Fixes to the Python API
---------------------------

- VELOSYS keyword type changed from bool to float. (`#23 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/23>`__)

Misc
----

- Prevent compression header keywords from being moved around during header refactoring. (`#23 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/23>`__)

v2.1.2 (2022-09-14)
===================

Bugfix
---------------------------

- Fix the type of some reprocessing keywords.


v2.1.1 (2022-09-12)
===================

Bugfix
------

- Relaxing requiredness of headers added in v2.1.0


v2.1.0 (2022-09-12)
===================

Features
--------

- Adding new keywords to support the addition of reprocessing metadata to the FITS headers.


v2.0.0 (2022-04-26)
===================

Backwards Compatible Changes to the Specification
-------------------------------------------------

- Updated Spec122 and Spec214 schemas to be consistent with SPEC-122 Rev F. (`#21 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/21>`__)


New Feature in the Python API
-----------------------------

- Change the return values of all specification loading functions to be
  ``frozendict``.
  This means that the specifications once constructed are (largely) immutable and
  therefore can be cached. Caching the specfications massively speeds up
  subsequent calls to the specification construction functions. (`#22 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/22>`__)


v1.5.0 (2022-02-10)
===================

Documentation
-------------

- Add a documenation build for the yaml files containing the specifications and other information about the data products. (`#18 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/18>`__)

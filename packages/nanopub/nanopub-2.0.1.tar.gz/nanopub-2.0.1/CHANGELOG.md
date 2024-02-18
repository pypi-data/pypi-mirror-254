# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2022-12-15
Massive overhaul of the nanopub library with backwards incompatible changes.
### Changed
* The documentation website has been updated to use mkdocs
* The doc website is now published to GitHub Pages via the build.yml workflow if the tests pass.
* Profile private key can be now be loaded from a string instead of only a Path. This can be convenient if someone wants to load keys from anywhere else than a local file (e.g. network). There are still helpers functions to easily load from the profile.yml file.
* The private and public key are now optional, a new keypair will be generated if the private key is missing. And the public key can be generated from the private key automatically if it is missing (orcid_id, name are still mandatory)
* There is now a NanopubConfig object to hold the various arguments used to define the nanopub server where it will be published and which infos to attach to a nanopub.
* Signing is now done in python, removing the dependency on java
* java_wrapper is moved to the tests so it can still be used to compare signed nanopubs when testing
* The Publication class has been renamed to Nanopub. That makes a lot of "Nanopub" in the code, but it is more consistent and easier to remember
* Signing is now done directly on the Nanopub object (we don't use the client anymore for this): np.sign() and the np object is updated with the signed RDF (cf. the new doc below to see complete examples). This is convenient because it allows to define Templates for common nanopublications by inhereting the main Nanopub object, cf. existing template: Nanopub intro, Nanopub Index, Claim, Retract, Update
* The NanopubClient object is now mainly used for search functions (through the grlc API), no changes there
* The setup_nanopub_profile CLI was changed to a new CLI with multiple actions:
  * np setup prompt the existing CLI workflow to setup your nanopub profile
  * np profile check the current user profile used by the nanopub library (~/.nanopub/profile.yml)
  * np sign nanopub.trig to sign a nanopub file
  * np publish signed.nanopub.trig to publish a nanopub file (signed or not)
  * np check signed.nanopub.trig to check if a signed nanopub file is valid
* Changed the uses of print() to use python logging (which enable users of the library to configure the level of logs they want, setting to INFO will show all existing prints)
* A battery of tests was added using the same testsuite as nanopub-java to make sure the nanopubs signed with python are valid and follows the same standards: https://github.com/vemonet/nanopub/blob/sign-in-python/tests/test_testsuite.py#L10
* Most of the existing tests for the client search have been kept
* Updated the build.yml workflow to tests with all python versions from 3.7 to 3.10
* Linting now also check types with mypy (not strict)
* The setup.py + all files for python dev config such as .flake8 have been merged in 1 pyproject.tml file using the hatch build backend
* Updated the setup for development, it does not require any tool that is not built in python: only venv ands pip are required (or you can use hatch to handle install and virtual envs for you). Checkout the development docs page for the complete instructions.

## [1.2.11] - 2022-09-27
### Added
* Support for rdflib v6
* Added options to let users choose if they want prov:generatedAtTime and prov:attributedTo automatically added to prov/pubinfo graphs

## [1.2.10] - 2021-09-01
### Changed
* Use latest yatiml version instead of pinned version

## [1.2.9] - 2021-09-01
### Added
* Include LICENSE file in python setup

## [1.2.8] - 2021-09-01

### Added
* Also publish sdist when publishing to pypi

## [1.2.7] - 2021-06-25

### Changed
* Prevent `setup_nanopub_profile` from ever overwriting key pair

### Fixed
* Pin `click` at version 7.1.2, as versions >8 break `setup_nanopub_profile`

## [1.2.6] - 2021-04-30

### Added
* Search result dicts now contain nanopublication label too, if provided by the grlc endpoint.

## [1.2.5] - 2021-03-05

### Fixed
* Fix bug that overwrites optional pubinfo and prov in `from_assertion()` calls.

## [1.2.4] - 2021-03-04

### Fixed
* Fix bug where user rdf was being mutated during publishing.

## [1.2.3] - 2021-02-05

### Added
* Added new `publication_attributed_to` argument to `Publication.from_assertion()`. Allows the `pubinfo` attribution to be manually set if desired.

## [1.2.2] - 2021-01-29

### Fixed
* Fix FileAlreadyExists bug in `setup_nanopub_profile`

## [1.2.1] - 2021-01-22

### Changed
* Rename `setup_profile` to `setup_nanopub_profile` to avoid ambiguity/clashes with other tools

### Fixed
* Make `nanopub` package compatible Windows operating system
* Added UTF-8 related flags to nanopub-java (in java call) to fix issues with certain characters on certain java builds
* Make regex in orcid validation accept ids ending with 'X'

## [1.2.0] - 2020-12-23

### Added
* Added Zenodo badge to README
* Pagination of results for search methods of `NanopubClient`

### Changed
* `nanopub-java` dependency is installed upon installation instead of upon runtime.
* search methods of `NanopubClient` return iterator instead of list


## [1.1.0] - 2020-12-17

### Added
* `.zenodo.json` for linking to zenodo
* `pubkey` option to methods of `NanopubClient` that allows searching for publications
    signed with the given pubkey. For these methods:
    - `find_nanopubs_with_text`
    - `find_nanopubs_with_pattern`
    - `find_things`
* `filter_retracted` option to methods of `NanopubClient` that allows searching for publications
    that are note retracted. For these methods:
    - `find_nanopubs_with_text`
    - `find_nanopubs_with_pattern`
    - `find_things`
* `NanopubClient.find_retractions_of` method to search retractions of a given nanopublication.
* `Publication.signed_with_public_key` property: the public key that the publication was signed with.
* `Publication.is_test_publication` property: denoting whether this is a publicaion on the test server.

### Changed
* Improved error message by pointing to documentation instead of Readme upon ProfileErrors

### Fixed
* Catch FileNotFoundError when profile.yml does not exist, raise ProfileError with useful messageinstead.
* Fixed broken link to documentation in README.md

## [1.0.0] - 2020-12-08

NB: All changes before [1.0.0] are collapsed in here (even though there were multiple pre-releases)
### Added
- `nanopub.client` module with the NanopubClient class that implements:
  * Searching (being a client with a direct (but incomplete) mapping to the nanopub server grlc endpoint):
    * `find_nanopubs_with_text` method
    * `find_nanopubs_with_pattern` method
    * `find_things` method
  * Fetching:
    * `fetch` method to fetch a nanopublication
  * Publishing:
    * Publish a statement using `claim` method
    * Publish a `Publication` object with `publish` method
  * Retracting:
    * Publish a retraction of an existing nanopublication created by this user (i.e. signed with same RSA key)

  * Test server functionality
    * Client can optionally be set to publish to (and fetch from) the nanopub test servers only.

- `nanopub.publication` module
  * `Publication` class to represent a nanopublication.
  Includes `from_assertion` class method to construct a Publication object
  from an assertion graph
  * `replace_in_rdf` helper method to replace values in RDF
- `nanopub.java_wrapper` module, provides an interface to the nanopub-java tool for
  signing and publishing nanopublications.
- `nanopub.profile` module, getters and setters for the nanopub user profile
- `nanopub.setup_profile`, interactive command-line client to setup user profile
- `nanopub.namespaces`, often-used RDF namespaces
- `examples/`, holds a few notebooks that serve as examples of using the library
- User documentation

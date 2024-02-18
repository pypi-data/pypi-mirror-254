# CHANGELOG
## Unreleased
### Feature
* feat: allow download with oras url with apptainer

rewrite function to capture error if fail and use apptainer pull with oras url ([`72990e5`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/72990e54f4c3511f409774b0db201242e9fda55a))
* feat: allow download with oras url with apptainer

rewrite function to capture error if fail and use apptainer pull with oras url ([`1f4eb76`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/1f4eb766789321bf946bb48670b9316a388f6ace))
* feat: add show_version ([`d23e768`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/d23e768340b8c61df494769707a0984fb9948319))
### Fix
* fix: set_config_value now can use level1 ([`897d82d`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/897d82d64807aa2825ce21e9a2397ae5886dd680))
* fix: sinrilarity rewrite bind if other argument after
fix: subprocess.run raise Sysexit not good code ([`47ba142`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/47ba14290c356e43b022d4111be115d60c68aadc))
### Unknown

## v0.1.0 (2023-10-04)
## v0.0.6 (2023-10-04)
### Feature
* feat: add tools_version_dict_to_df function

tools_version_dict_to_df is to get tools version from a dict
modify version with pip to get pip install version include dev ([`896442c`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/896442c524b916f7cabddd3de375a2d932e5d31e))
* feat: add install_debug argument

add new argument to show  Install path, Tools config, Install mode, Tools install mode, Current version, Latest version avail, Snakecdysis version ([`7246e7a`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/7246e7ad99efa51834c8b4bf258dcc49567049eb))
## v0.0.5 (2023-06-22)
### Feat
* FEAT: add keep-going: true and cluster-cancel: &#34;scancel&#34; to profile ([`a9e8056`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/a9e80565f7e84015c00fab91041fe80434d1f3ce))
### Fix
* fix: remove args_tools_path from run commande ([`e092603`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/e0926030547027e83f579a7bc44c10f814c992b2))
* fix: raise error if directory is not empty when use generate_template.py ([`10d2dad`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/10d2dadd94873e41a648e2a706a97baa6687bb36))
* fix: remove __pycache__ directory from template ([`8f93248`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/8f932480fc536e024b33987b57be967511301f65))
* fix: remove __pycache__ directory from template ([`9734ea6`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/9734ea659dfb6fdc5889917d79f3838c331bf793))
### Fix
* FIX: test mthode to capture partition if not default with star ([`fa299ec`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/fa299ec3d389252d47684ecce4ccbf0be3739517))
## v0.0.4 (2023-02-27)
### Fix
* fix: remove cluster-cancel cause fail on run

remove coockiescutter cluster-cancel default ([`43247a4`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/43247a42d8186b0958956a8585822a06a78ad7d3))
* fix: git_cluster_config path

replace git_cluster_config path from default_profile to install_path ([`65ff14f`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/65ff14fcda40fad318e6df32ce0e9c9994888dda))
* fix: fix issue #3-only-singularity-in ([`8f594f0`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/8f594f0d41b5b720605e63f5c1558633b4632f14))
## v0.0.3 (2023-02-23)
### Fix
* fix: add setuptools_scm requirement ([`036e1a8`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/036e1a8ce5df9490bc05a515cb2fc4cdc7719fba))
* fix: add setuptools_scm requirement ([`3c3a403`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/3c3a4037d094761f7ea7740e3c9dcfc3732fe7b3))
* fix: remove setuptools_scm to VERSION file ([`b0c5d8e`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/b0c5d8ed133963a7923e880bb0bb5d35fff717d2))
* fix: add setuptools_scm requirement ([`ce0fa43`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/ce0fa4363396373bab8d1a39d1bfcc9909a67edb))
## v0.0.2 (2023-02-23)
### Doc
* DOC: update ([`20260b0`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/20260b0aeabccbd64ef14f82111a691630e6a32e))
* DOC: update url image and python version ([`505936d`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/505936dc5faa6ba3b79b355ae1aee9b4c24c5b89))
* DOC: add exemple to template ([`8b3c785`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/8b3c7854bb65921d9e33e1da86363fe33ef5901f))
* DOC: update config to use toml ([`2b767ea`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/2b767ea73bc89fcaf0a621a965b9e1c4ace08bd0))
* DOC: fix install itself ([`c24b02b`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/c24b02bca6bd95c2a46c8daa269aab959be1a09f))
* DOC: fix build with readthedocs ([`a96f667`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/a96f66706b4221d4e29c3e6d17ad3b786ac5e16a))
### Fix
* FIX: Edit tools ([`711731e`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/711731ed71b8852f7652b8d9fcc6be1efedadef1))
* FIX: unpack dicotool ([`706d011`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/706d011699190605fffffe19d52e10267786a24e))
* FIX: Edit tools rewrite ([`8b1ec80`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/8b1ec80efec36eee228c0e54d339edc54cefcd5c))
* FIX: rename logo in lower ([`f705a7c`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/f705a7cd5b7dca77e1703386ee43b2519fc18570))
* FIX: template exemple ([`4a710cb`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/4a710cb859fb84c8467201a67fa69f106db19068))
* FIX: doesn&#39;t apply lower for package name ([`3b96b3d`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/3b96b3d056c7b93327899abb75d2ea8a5a92b23a))
* FIX: write singularity path ([`44721d0`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/44721d00eeebce0315c52096c7f69187cb7bc4e7))
* FIX: singularity path not update see (Issue #1)

update edit_tools to always use user_tool_path and fix replace INSTALL_PATH on snake_wrapper.py ([`334ad45`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/334ad45f71c50487ebc8227bc0ff6e90a2a663c2))
### Fix
* fix: profil mem mutually exclusif with mem_per_cpus ([`f7d90c3`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/f7d90c35bc169b4877241154aee04013bf1b860b))
### Performance
* perf: remove setup.py to use pyproject.toml ([`abd0502`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/abd05023bbf101114bccebd9abd9b96a1f16edd6))
## v0.0.1 (2023-02-16)
### Fix
* FIX: bad rename of variable DOCS ([`9f83cc1`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/9f83cc1fb2d4bffe068849d7d9c68d4832a6f5a8))
### Perf
* PERF: switch setup.py to pyproject.toml

according to packaging docs I use pyproject.toml with setuptools backend ([`bd86f7b`](https://forge.ird.fr/phim/sravel/snakecdysis/-/commit/bd86f7bba6ceafe2470e93447416f6499d2b649a))

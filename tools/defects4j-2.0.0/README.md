The projects
---------------
Defects4J contains 835 bugs from the following open-source projects:

| Identifier      | Project name               | Number of bugs | Active bug ids      | Deprecated bug ids (\*) |
|-----------------|----------------------------|---------------:|---------------------|-------------------------| 
| Chart           | jfreechart                 |       26       | 1-26                | None                    |
| Cli             | commons-cli                |       39       | 1-5,7-40            | 6                       |
| Closure         | closure-compiler           |      174       | 1-62,64-92,94-176   | 63,93                   |
| Codec           | commons-codec              |       18       | 1-18                | None                    |
| Collections     | commons-collections        |        4       | 25-28               | 1-24                    |
| Compress        | commons-compress           |       47       | 1-47                | None                    |
| Csv             | commons-csv                |       16       | 1-16                | None                    |
| Gson            | gson                       |       18       | 1-18                | None                    |
| JacksonCore     | jackson-core               |       26       | 1-26                | None                    |
| JacksonDatabind | jackson-databind           |      112       | 1-112               | None                    |
| JacksonXml      | jackson-dataformat-xml     |        6       | 1-6                 | None                    |
| Jsoup           | jsoup                      |       93       | 1-93                | None                    |
| JxPath          | commons-jxpath             |       22       | 1-22                | None                    |
| Lang            | commons-lang               |       64       | 1,3-65              | 2                       |
| Math            | commons-math               |      106       | 1-106               | None                    |
| Mockito         | mockito                    |       38       | 1-38                | None                    |
| Time            | joda-time                  |       26       | 1-20,22-27          | 21                      |

\* Due to behavioral changes introduced under Java 8, some bugs are no longer
reproducible. Hence, Defects4J distinguishes between active and deprecated bugs:

- Active bugs can be accessed through `active-bugs.csv`.

- Deprecated bugs are removed from `active-bugs.csv`, but their metadata is
  retained in the project directory.

- Deprecated bugs can be accessed through `deprecated-bugs.csv`, which also
  details when and why a bug was deprecated.

We do not re-enumerate active bugs because publications using Defects4J artifacts
usually refer to bugs by their specific bug id.

The bugs
---------------
Each bug has the following properties:

- Issue filed in the corresponding issue tracker, and issue tracker identifier
  mentioned in the fixing commit message.
- Fixed in a single commit.
- Minimized: the Defects4J maintainers manually pruned out
  irrelevant changes in the commit (e.g., refactorings or feature additions).
- Fixed by modifying the source code (as opposed to configuration files,
  documentation, or test files).
- A triggering test exists that failed before the fix and passes after the fix
  -- the test failure is not random or dependent on test execution order.

The (b)uggy and (f)ixed program revisions are labelled with `<id>b` and
`<id>f`, respectively (`<id>` is an integer).


Setting up Defects4J
================

Requirements
----------------
 - Java 1.8 (version 1.5.0 and older requires Java 1.7)
 - Git >= 1.9
 - SVN >= 1.8
 - Perl >= 5.0.12

#### Java version
All bugs have been reproduced and triggering tests verified, using the latest
version of Java 1.8.
Note that using Java 1.9+ might result in unexpected failing tests on a fixed
program version. 

#### Timezone
Defects4J generates and executes tests in the timezone `America/Los_Angeles`.
If you are using the bugs outside of the Defects4J framework, set the `TZ`
environment variable to `America/Los_Angeles` and export it.

#### Perl dependencies
All required Perl modules are listed in [cpanfile](https://github.com/rjust/defects4j/blob/master/cpanfile).
On many Unix platforms, these required Perl modules are installed by default.
If this is not the case, see instructions below for how to install them.

Steps to set up Defects4J
----------------

1. Clone Defects4J:
    - `git clone https://github.com/rjust/defects4j`

2. Initialize Defects4J (download the project repositories and external libraries, which are not included in the git repository for size purposes and to avoid redundancies):
   If you do not have `cpanm` installed, use cpan or a cpan wrapper to install the perl modules listed in `cpanfile`.
    - `cd defects4j`
    - `cpanm --installdeps .`
    - `./init.sh`

3. Add Defects4J's executables to your PATH:
    - `export PATH=$PATH:"path2defects4j"/framework/bin`

4. Check installation:
    - `defects4j info -p Lang`

On some platforms such as Windows, you might need to use `perl "fullpath"\defects4j`
where these instructions say to use `defects4j`.


Using Defects4J
================

#### Example commands
1. Get information for a specific project (commons lang):
    - `defects4j info -p Lang`

2. Get information for a specific bug (commons lang, bug 1):
    - `defects4j info -p Lang -b 1`

3. Checkout a buggy source code version (commons lang, bug 1, buggy version):
    - `defects4j checkout -p Lang -v 1b -w /tmp/lang_1_buggy`

4. Change to the working directory, compile sources and tests, and run tests:
    - `cd /tmp/lang_1_buggy`
    - `defects4j compile`
    - `defects4j test`

5. The scripts in [`framework/test/`](framework/test/)
are examples of how to use Defects4J, which you might find useful
as inspiration when you are writing your own scripts that use Defects4J.

Command-line interface: defects4j command
-----------------------
Use [`framework/bin/defects4j`](http://defects4j.org/html_doc/defects4j.html) to execute any of the following commands:

| Command        | Description                                                                                       |
|----------------|---------------------------------------------------------------------------------------------------|
| [info](http://defects4j.org/html_doc/d4j/d4j-info.html)                   | View configuration of a specific project or summary of a specific bug                             |
| [env](http://defects4j.org/html_doc/d4j/d4j-env.html)                     | Print the environment of defects4j executions                                                     |
| [checkout](http://defects4j.org/html_doc/d4j/d4j-checkout.html)           | Checkout a buggy or a fixed project version                                                       |
| [compile](http://defects4j.org/html_doc/d4j/d4j-compile.html)             | Compile sources and developer-written tests of a buggy or a fixed project version                 |
| [test](http://defects4j.org/html_doc/d4j/d4j-test.html)                   | Run a single test method or a test suite on a buggy or a fixed project version                    |
| [mutation](http://defects4j.org/html_doc/d4j/d4j-mutation.html)           | Run mutation analysis on a buggy or a fixed project version                                       |
| [coverage](http://defects4j.org/html_doc/d4j/d4j-coverage.html)           | Run code coverage analysis on a buggy or a fixed project version                                  |
| [monitor.test](http://defects4j.org/html_doc/d4j/d4j-monitor.test.html)   | Monitor the class loader during the execution of a single test or a test suite                    |
| [bids](http://defects4j.org/html_doc/d4j/d4j-bids.html)                   | Print the list of active or deprecated bug IDs for a specific project                                           |
| [pids](http://defects4j.org/html_doc/d4j/d4j-pids.html)                   | Print a list of available project IDs                                                             |
| [export](http://defects4j.org/html_doc/d4j/d4j-export.html)               | Export version-specific properties such as classpaths, directories, or lists of tests             |
| [query](http://defects4j.org/html_doc/d4j/d4j-query.html)                 | Query the metadata to generate a CSV file of requested information for a specific project         |

Export version-specific properties
----------------------------------
Use `defects4j export -p <property_name> [-o output_file]` in the working
directory to export a version-specific property:

| Property         | Description                                                                         |
|------------------|-------------------------------------------------------------------------------------|
| classes.modified | Classes modified by the bug fix                                                     |
| classes.relevant | Classes loaded by the JVM when executing all triggering tests                       |
| cp.compile       | Classpath to compile and run the project                                            |
| cp.test          | Classpath to compile and run the developer-written tests                            |
| dir.src.classes  | Source directory of classes (relative to working directory)                         |
| dir.bin.classes  | Target directory of classes (relative to working directory)                         |
| dir.src.tests    | Source directory of tests (relative to working directory)                           |
| dir.bin.tests    | Target directory of test classes (relative to working directory)                    |
| tests.all        | List of all developer-written test classes                                          |
| tests.relevant   | List of relevant tests classes (a test class is relevant if, when executed, the JVM loads at least one of the modified classes) |
| tests.trigger    | List of test methods that trigger (expose) the bug                                  |

Export project-specific metadata
--------------------------------
Use `defects4j query -p <pid> -q <field_list> [-o <output_file>] [-D|-A]` 
to generate a CSV file containing a set of requested metadata for each bug 
in a specific project.

By default, `defects4j query` returns a list of active bug IDs for a project.
To request specific metadata, the `-q` flag should be provided with a 
comma-separated list of variables from the list below. For example, 
`defects4j query -p Chart -q "report.id,report.url"` will provide the a list of
all active bug IDs, along with the bug report ID and bug report URL for each.


| Property              | Description                                                                         |
|-----------------------|-------------------------------------------------------------------------------------|
| bug.id                | Assigned bug IDs (included in all results)                                          |
| project.id            | Assigned project ID                                                                 |
| project.name          | Original project name                                                            |
| project.build.file    | Location of the Defects4J build file for the project                                |
| project.vcs           | Version control system used by the project                                          |
| project.repository    | Location of the project repository                                                  |
| project.bugs.csv      | Location of the CSV containing information on that bug                              |
| revision.id.buggy     | Commit hashes for the buggy version of each bug                                     |
| revision.id.fixed     | Commit hashes for the fixed version of each bug                                     |
| revision.date.buggy   | Date of the buggy commit for each bug                                               |
| revision.date.fixed   | Date of the fixed commit for each bug                                               |
| report.id             | Bug report ID from the version tracker for each bug                                 |
| report.url            | Bug report URL from the version tracker for each bug                                |
| classes.modified      | Classes modified by the bug fix                                                     |
| classes.relevant.src  | Source classes loaded by the JVM when executing all triggering tests                |
| classes.relevant.test | Test classes loaded by the JVM when executing all triggering tests                  |
| tests.relevant        | List of relevant tests classes (a test class is relevant if, when executed, the JVM loads at least one of the modified classes) |
| tests.trigger         | List of test methods that trigger (expose) the bug                                  |
| tests.trigger.cause   | List of test methods that trigger (expose) the bug, along with the root cause       |
| deprecated.version    | (for deprecated bugs only) Version of Defects4J where a bug was deprecated          |
| deprecated.reason     | (for deprecated bugs only) Reason for deprecation                                   |

By default, `defects4j query` returns information on active bugs. The `[-D]`
flag returns information only on deprecated bugs, while the `[-A]` flag returns
information for all active and deprecated bugs.


Test execution framework
--------------------------
The test execution framework for generated test suites (`framework/bin`)
provides the following scripts:

| Script            | Description                                                     |
|-------------------|-----------------------------------------------------------------|
| [defects4j](http://defects4j.org/html_doc/defects4j.html)         | Main script, described above                                   |
| [gen_tests](http://defects4j.org/html_doc/gen_tests.html)         | Generate test suites using EvoSuite or Randoop                 |
| [run_bug_detection](http://defects4j.org/html_doc/run_bug_detection.html) | Determine the real fault detection rate                |
| [run_mutation](http://defects4j.org/html_doc/run_mutation.html)   | Determine the mutation score                                   |
| [run_coverage](http://defects4j.org/html_doc/run_coverage.html)   | Determine code coverage ratios (statement and branch coverage) |

Mining and contributing additional bugs to Defects4J
================
We welcome your contributions to Defects4J!
The bug-mining [README](framework/bug-mining/README.md) details the bug-mining process.


Additional resources
================

Scripts built on Defects4J
--------------------

#### Fault localization (FL)
  - [Scripts and annotations for evaluating FL techniques][FL-eval]

#### Automated program repair (APR)
  - [Scripts and annotations for evaluating APR techniques][APR-eval]
  - [Patches generated with the Nopol, jGenProg, and jKali APR systems][APR-patches-spirals]
  - [Repair actions and patterns for Defects4J v1.2.0][D4J-dissection]

[fl-eval]: https://bitbucket.org/rjust/fault-localization-data
[APR-eval]: https://github.com/LASER-UMASS/AutomatedRepairApplicabilityData
[APR-patches-spirals]: https://github.com/Spirals-Team/defects4j-repair
[D4J-dissection]: http://program-repair.org/defects4j-dissection/

Publications
------------------
* "Defects4J: A Database of Existing Faults to Enable Controlled Testing Studies for Java Programs"
    René Just, Darioush Jalali, and Michael D. Ernst,
    ISSTA 2014 [[download]][issta14].

* "Are Mutants a Valid Substitute for Real Faults in Software Testing?"
    René Just, Darioush Jalali, Laura Inozemtseva, Michael D. Ernst, Reid Holmes, and Gordon Fraser,
    FSE 2014 [[download]][fse14].

* "Challenges in Using Search-Based Test Generation to Identify Real Faults in Mockito"
   Gregory Gay,
   SSBSE 2016 [[download]][ssbse16].

* "Detecting Real Faults in the Gson Library Through Search-Based Unit Test Generation"
   Gregory Gay,
   SSBSE 2018 [[download]][ssbse18].

* "Defects4J as a Challenge Case for the Search-Based Software Engineering Community"
   Gregory Gay and René Just,
   SSBSE 2020 [[download]][ssbse20].

[issta14]: https://people.cs.umass.edu/~rjust/publ/defects4j_issta_2014.pdf
[fse14]: https://people.cs.umass.edu/~rjust/publ/mutants_real_faults_fse_2014.pdf
[ssbse16]: https://greg4cr.github.io/pdf/16mockito.pdf
[ssbse18]: https://greg4cr.github.io/pdf/18gson.pdf
[ssbse20]: https://greg4cr.github.io/pdf/20d4j.pdf

[More publications](https://scholar.google.com/scholar?q=defects4j)

Implementation details
----------------------

Documentation for any script or module is available as
[HTML documentation][htmldocs].

[htmldocs]: http://defects4j.org/html_doc/index.html

The directory structure of Defects4J is as follows:

    defects4j
       |
       |--- project_repos:     The version control repositories of the provided projects.
       |
       |--- major:             The Major mutation framework.
       |
       |--- framework:         Libraries and executables of the core, test execution,
           |                   and bug-mining frameworks.
           |
           |--- bin:           Command line interface to Defects4J.
           |
           |--- bug-mining:    Bug-mining framework.
           |
           |--- core:          The modules of the core framework.
           |
           |--- lib:           Libraries used in the core framework.
           |
           |--- util:          Util scripts used by Defects4J.
           |
           |--- projects:      Project-specific resource files.
           |
           |--- test:          Scripts to test the framework.
           
Versioning information
----------------------
Defects4J uses a semantic versioning scheme (`major`.`minor`.`patch`):

| Change                                  | `major` | `minor` | `patch` |
|-----------------------------------------|:-------:|:-------:|:-------:|
| Addition/Deletion of bugs               |    X    |         |         |
| New/upgraded internal or external tools |         |    X    |         |
| Fixes and documentation changes         |         |         |    X    |

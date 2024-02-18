.. ! NOTE: This Changelog MUST be pure reStructuredText
.. * since it is also used as Changelog.rst in the VCS UI !

*********
Changelog
*********

.. _Command-line interface: https://api.byteblower.com/test-framework/latest/byteblower-test-framework/cli/index.html
.. _Versioning: https://api.byteblower.com/test-framework/latest/byteblower-test-framework/versioning.html
.. _byteblowerll: https://pypi.org/project/byteblowerll/
.. _ByteBlower Endpoint: https://www.excentis.com/products/byteblower-endpoint/

**Note**: *Have a look at our* Versioning_ *for more information about
how releases are handled for the ByteBlower Test Framework*.


v1.2.0
======

Released on 2024/02/01

Deprecations
------------

* Avoid confusion with our customers for *who was performing the NAT/NAPT*:
  ByteBlower or the device/network under test.

  * Deprecated ``NattedPort`` in favor of ``NatDiscoveryIPv4Port``.
  * Command-line JSON configuration file: Deprecated ``napt_keep_alive``
    in favor of ``nat_keep_alive``. Done for naming consistency with the
    *NAT-discovery IPv4 ports*.

* Fixed consistency in bitrate related parameters throughout the API.

  * Changed rate-limiting parameter in the ``HttpFlow`` to ``maximum_bitrate``
    (in *bits per second*). It replaces ``rate_limit`` which was in
    *Bytes per second*.

    This also applies to the parameter for the ``"type": "http"`` flow
    in the command-line configuration file.

* Moved **common constants** from ``byteblower_test_framework.traffic``
  to the ``byteblower_test_framework.constants`` module.

  * Default Ethernet frame length (``DEFAULT_FRAME_LENGTH``),
    default IP DSCP (``DEFAULT_IP_DSCP``), default IP ECN (``DEFAULT_IP_ECN``)
    and first UDP port number of IANA dynamic or private port range
    (``UDP_DYNAMIC_PORT_START``).

**Important**: *Their final removal is planned for the next release of
the ByteBlower Test Framework. Please make sure that you update your
test script before that time.*

In this release, backward-compatibility is maintained.

Improvements
------------

* Integration of the **ByteBlower Endpoint** - ✨ **New!** ✨

  * *Wi-Fi and mobile testing* via the `ByteBlower Endpoint`_!
  * Supported in frame blasting based flows and basic HTTP flow (TCP)
  * Reporting similar to the ByteBlower (server) Port tests.
  * Handles device locking
  * Scenario runtime might now wait longer until stopping:
    The flows will wait until the Endpoint results are available
    on the Meeting Point before collecting them.

* Usability

  * Consistent **Scenario run-time behavior** for ByteBlower Port and Endpoint

    * Flow preparation is now postponed to become part of the
      ``Scenario.run()``. Address resolution and NAT/NAPT discovery required
      for preparing the frames for a frame blasting based flow is now done
      in a *prepare flow initialization* (``prepare_configure``) stage.

  * More **consistent naming** for **endpoints behind a NAT/NAPT gateway**
    (*Network Address (and Port) Translation gateway*).
  * More and better use of **framework-specific exception** definitions
    (based on ``ByteBlowerTestFrameworkException``)
  * Moved **common constants** to the ``byteblower_test_framework.constants``
    module.

    * Default Ethernet frame length (``DEFAULT_FRAME_LENGTH``),
      default IP DSCP (``DEFAULT_IP_DSCP``), default IP ECN
      (``DEFAULT_IP_ECN``) and first UDP port number of IANA dynamic
      or private port range (``UDP_DYNAMIC_PORT_START``).
    * Keeping the *deprecated* exports in the current modules
      (``byteblower_test_framework.traffic``)

* Configuration

  * ``HTTPFlow``: Fixed consistency in bitrate related parameter with
    other flow types. Added ``maximum_bitrate`` (in *bits per second*)
    parameter to TCP-based flows.
    Deprecating the ``rate_limit`` which was in *Bytes per second*.

* Documentation

  * Improved installation & quick start to get you up-and-running in no time!
  * The general structure is now in line with the documentation of the
    test cases. This will make it more convenient and straightforward for
    the readers of our documentation.

* Internal

  * Updated structure of Scenario methods to improve integration in ``asyncio``
    runtime.
  * Generic interface for **taggable objects**
    (``Port``, ``Endpoint``, ``Flow``, ``FlowAnalyser``)

Fixes
-----

* Fixed Enum value style according to PEP 8. On:

  * `TCPCongestionAvoidanceAlgorithm`

* Better handling of default arguments in functions and methods.
* Consistent handling of *initial time to wait* in frame blasting based
  and TCP-based flows.
* Many improvements in code quality

v1.1.2
======

Released on 2023/11/27

Improvements
------------

* `Test Case: RFC 2544 Throughput`_ - ✨ **New!** ✨

  * Run an `RFC 2544`_ network performance test with ease!

* `Test Case: Low Latency`_ - ✨ **New!** ✨

  * Run low latency validation tests on your network.

* Documentation: improved visualization of platform-specific instructions.

.. _Test Case\: RFC 2544 Throughput: https://api.byteblower.com/test-framework/latest/test-cases/rfc-2544/overview.html
.. _Test Case\: Low Latency: https://api.byteblower.com/test-framework/latest/test-cases/low-latency/overview.html
.. _RFC 2544: https://datatracker.ietf.org/doc/html/rfc2544

Fixes
-----

* HTTP Flow: Flow duration was not limited when ``maximum_run_time``
  was given to ``Scenario.run()``.
* `Command-line interface`_`: Follow CLI argument guidelines.
  Using ``-`` instead of ``_`` for word separation.
* JSON report: HTTP over-time results were stored under ``overTimeResult``
  instead of ``overTimeResults``.
* Doesn't bail out when releasing API objects after errors occurred,
  either during initialization or during execution.
* Renamed exception ``UDPMaxExceeded`` to ``MaximumUdpPortExceeded``.

v1.1.0
======

Released on 2023/10/10

Improvements
------------

* `Command-line interface`_ - ✨ **New!** ✨

  * Run traffic tests with nothing more than a JSON configuration file!

* Usability

  * A Scenario run will now only start the Flows, Streams and Protocols
    which are involved in this specific Scenario.

    This means that the user can now use the same port in multiple test
    scenarios and run those in parallel.

  * 🚧 **Preview** 🚧: Most building blocks now have an option to explicitly
    release related resources on the ByteBlower system.

* Reporting

  * 🚧 **Preview** 🚧: The HTML and JSON report include **flow runtime error**
    information.

    These messages warn you if something went wrong at
    initialization or during transmission of the data traffic.
    For example when the TCP client failed to connect or when the test
    is trying to transmit at rates higher than the link speed.

    .. note::
       This information and how it is reported is not yet in a final stage.
       We'd love to hear your feedback to improve this for you!

* Support for Python 3.11 with the latest version of the ByteBlower API
  (`byteblowerll`_ v2.21.0).

Fixes
-----

* JSON report: Fixed regression in latency reporting. Since versions 1.0.0b18,
  the latency was reported in *nanoseconds* in ``int``
  instead of *milliseconds* in ``float``.
* JSON report: The duration (in *nanoseconds*) and RX/TX bytes of an HTTP Flows
  were reported in ``float`` instead of ``int``.

v1.0.0
======

Released on 2023/09/29

Improvements
------------

* Reporting

  * The HTML report now uses the **brand-new report style**.
  * The accuracy of the results over-time for TCP-based flows now has
    the same level of frame blasting based flows.
  * The **JSON report** now contains the **complete latency histogram** for
    the Latency (C)CDF analyzer. Before it only contained the CDF results.
  * The *XML JUnit* report now uses the *failure causes* as failure
    ``message`` and keeps the analysis results in the ``system-out``.
  * The *HTTP analyzer* does not have specific pass/fail criteria.
    This is now reflected in the pass/fail results in the report.

Fixes
-----

* The size of the HTML report is reduced back to normal. Introduction of the
  *offline mode* caused many duplicate JavaScript entries in the report.
* The timestamps for the over-time results are now consistent
  in UTC format in the HTML and JSON reports.
* The global pass/fail status in the JSON report
  was not correct in all circumstances.
* The over-time results for streams, triggers and protocols could
  be incomplete for certain timing of the flows and scenario.
* The latency histogram range was incorrect in the failure log message.
* No longer clearing and updating the stream results
  from the trigger data gatherers.

Deprecations and removals
-------------------------

* ``ImixLossAnalyser``, ``LatencyImixLossAnalyser`` and
  ``LatencyCDFImixLossAnalyser`` are now removed. You can use
  ``FrameLossAnalyser``, ``LatencyFrameLossAnalyser`` and
  ``LatencyCDFFrameLossAnalyser`` instead.

v1.0.0b18
=========

Released on 2023/09/15

Deprecations
------------

* ``Scenario`` must now be imported from the *test execution interfaces*
  (``byteblower_test_framework.run``) instead of directly from the base
  package (``byteblower_test_framework``). This move was made because of
  consistency and cyclic imports.
* ``ImixLossAnalyser``, ``LatencyImixLossAnalyser`` and
  ``LatencyCDFImixLossAnalyser`` are deprecated in favor of resp.
  ``FrameLossAnalyser``, ``LatencyFrameLossAnalyser`` and
  ``LatencyCDFFrameLossAnalyser``.

  **Important**: *Their final removal is planned for the next (beta) release
  of the ByteBlower Test Framework. Please make sure that you update your
  test script before that time.*

Improvements
------------

* Reporting

  * HTML and JSON report now include the cause(s) of a test failure
    in the test analyzers section.
  * The HTML report includes a Latency CCDF overview in the *Correlated
    test results* section. The overview graph is added when at least
    one flow has a ``LatencyCDFFrameLossAnalyser`` attached.
  * The HTML report now reports traffic rates in ``Mbps`` instead of
    ``MBytes/s``.

* Configuration

  * Port VLAN configuration now allows to set the VLAN protocol ID (TPID).

    **NOTE**: This requires at least ByteBlower API and server v2.20.0
  * Simplified configuration of IP DSCP and ECN flags for traffic generation.
    See more detailed information in `IP traffic class fields`_ below.
  * It is now possible to disable random ordering (*shuffle*) of the generated
    frames in an ``Imix``.

* Usability

  * HTTP analysis: The analysis results are now available from the
    ``HttpAnalyser``.

* Many internal structure improvements in the framework.

IP traffic class fields
^^^^^^^^^^^^^^^^^^^^^^^

Especially in IPv4, Type of Service (ToS) is a dubious term. It refers
to both the IPv4 header field and the Type of Service value when the
IPv4 Tos header field is interpreted as Precedence and ToS.
See also `Type of Service - Wikipedia`_.

In IPv6 the name of the header field has been changed to IP Traffic Class.

* For frame blasting flows

  * You can now set the IP DSCP and/or IP ECN bits via the ``Frame`` classes
    or via the ``create_frame`` factory function.
  * It is possible to set the complete IPv4 ToS / IPv6 Traffic Class
    header field via the ``ip_traffic_class`` field in the ``create_frame``
    factory function or via the ``ipv4_tos`` field in the ``IPv4Frame`` class
    or ``ipv6_tc`` field in the ``IPv6Frame`` class.

* For application simulation flows and TCP-based flows

  * You can now set the IP DSCP and/or IP ECN bits via the ``Flow`` classes.
  * It is possible to set the complete IPv4 ToS / IPv6 Traffic Class
    header field via the ``ip_traffic_class`` field in the ``Flow`` classes.

.. _Type of Service - Wikipedia: https://en.wikipedia.org/wiki/Type_of_service#Precedence_and_ToS

Fixes
-----

* TX over-time results of frame blasting based flows were incorrect when
  multiple ``FlowAnalyser`` instances were added. The TX results were
  divided over the results of the different analyzers.
* Cyclic imports because the ``Scenario`` was loaded in the
  base package ``byteblower_test_framework``.
* Latency CDF analyzer: Analysis failed when all packets were received
  out of the bounds of the latency distribution histogram.
* Logging all API exceptions in log_api_error decorator
  and internal exception handling
* Log error when failed to start a port
* Fixed warning for future ``pandas``' behavior when concatenating empty
  or *all NaN* ``DataFrame``.

v1.0.0b17
=========

Improvements
------------

* Configuration

  * IPv6Port can now be configured using stateless address autoconfiguration
    (**SLAAC**).
  * An **``HttpFlow``** can now be configured with a given data "**size**"
    to transfer instead of a given data traffic "duration".
  * The **Scenario runtime** has been **updated** to support these size-based
    flows (in general: not duration-based flows)

    * **DEPRECATED interface**: the **duration** parameter in
      **Scenario.run** is replaced by the ``maximum_run_time`` parameter.
      The name duration became more confusing with its updated purpose.
    * **CHANGED behavior**: The default *maximum run time* (previously
      called scenario *duration*) is **not set**.

      The Scenario will take the *longest run time* of all *duration-based*
      flows and apply it to all configured flows. It will default to 10s
      *only* if *none* of the *duration-based* flows is *limited in time*.

      Also, by default the Scenario will wait for size based (TCP/HTTP)
      flows until they finished the complete data transfer (or time out
      due to connection errors), independent of the *longest run time*
      of the duration-based flows.

      In case the *maximum run time* is set in **Scenario.run**, the
      *duration-based* flows which take longer than the given time
      will be limited in time. Flows which are *not duration-based*
      will be forced to stop after the given duration.

      When the scenario maximum run time is longer than the longest
      run time of the configured flows, the scenario will be "*idle*"
      after the last flows finished their transmission.

* Reporting

  * Added **scenario start and end timestamps** to the HTML and JSON reports.
    The scenario API also exposes the scenario duration.
  * FlowAnalysers for FrameBlastingFlow: Analyzing and reporting
    **transmit timestamps**: timestamps of the first and last
    transmitted packets.
  * Support for reporting **layer 2 speed including physical overhead**
    (Ethernet Frame + FCS + preamble + SFD + pause)
  * The HTML reports use **HighCharts offline mode** now. The HighCharts
    JavaScript and CSS will no longer be downloaded every time you
    open the HTML report.

* Usability

  * The Scenario and Flows now have the required properties to **obtain
    the configured FlowAnalysers**: ``Scenario.flows`` and ``Flow.analysers``
  * Added helper function to **convert Ethernet frame size** or
    **bitrate "excluding" FCS** to values including FCS or *including FCS and
    physical overhead*. This is useful when post-processing values from the
    FlowAnalysers directly or when post-processing values from the JSON report.

* Documentation

  * Update list of validated OS platforms in the README

Fixes
-----

* Fixed analysis of flows with missing receive timestamps or latency
  related values. Could happen when no packet (with valid latency tag)
  has been received.
* Use correct VLAN protocol ID in frames (for frame blasting).
  The Frames did not use the 802.1ad S-Tag in case of VLAN stacking.

  * **BREAKING change**: **Port.vlan_config** now returns tuples of
    4 items instead of 3: Including the VLAN protocol ID (TPID)
    as first item in the tuple.

* Better type hinting in the Flow (regarding FlowAnalyser).
* *Temporary workaround*: Log TCP flow connection errors while waiting
  for them to finish instead of bailing out with an error
  with no report being generated at all.

v1.0.0b16
=========

Improvements
------------

* Frame implementations

  * Improved usability of default values in frame constructors:
    You can provide ``None`` to let the framework use the default value.
    It is no longer needed to check for ``None`` in your code and import
    and use the default values in that case.

* Improved documentation

  * regarding VLAN tags included/excluded in frame sizes and bitrates
  * Add/update documentation for ``Frame`` implementations, ``Imix``
    and ``create_frame`` factory method.

* VideoFlow

  * Video buffer analyser now provides timestamps in UTC.
  * Now properly logs the actual API exception message when starting
    segment download fails.

Fixes
-----

* Fixed loss percentage reporting of aggregated results in HTML report.
* VLAN support

  * Fixing some internal type hinting.
  * Update reporting of VLAN tagged traffic in HTML report.
    It is now similar to the HTML report in the ByteBlower GUI.

* Fixed double reference issues in documentation generation for the
  ``byteblower_test_framework.all`` module.
* Fixed missing export of ``Scenario`` (for
  ``from byteblower_test_framework.all import *``).

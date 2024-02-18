********
Overview
********

Introduction
============

This test case is an implementation of the `RFC 2544`_ Throughput test using
the `ByteBlower Test Framework`_.

.. _ByteBlower Test Framework: https://pypi.org/project/byteblower-test-framework/
.. _RFC 2544: https://www.ietf.org/rfc/rfc2544.txt

.. footer::
   Copyright |copy| |year| - Excentis N.V.

.. |copy| unicode:: U+00A9 .. copyright sign
.. |year| date:: %Y

This ByteBlower RFC 2544 throughput test case allows you to:

#. Run throughput tests based on RFC 2544
#. Collect & Analyse statistics
#. Generate HTML & JSON reports

You know about RFC 2544 and you are thrilled to run the test?
Then you can immediately jump to our :doc:`quick_start`.

RFC 2544 introduction
=====================

`RFC 2544`_ specifies a test suite designed to analyze and report on the
capabilities of network equipment (also referred to as Device Under Test DUT).

.. figure:: images/rfc2544_setup.png
   :width: 50%
   :align: center

End-results must be clear, easy-to-understand, and are intended to be
used for comparison between vendors

RFC 2544 basic requirements
---------------------------

* Frame sizes to be used on Ethernet (Ethernet frame size including FCS):
  64, 128, 256, 512, 1024, 1280, 1518.
* At least five frame sizes SHOULD be tested for each test condition.
* The frame size with the largest MTU supported by the protocol under test
  SHOULD be used.
* The test equipment SHOULD discard any frames that don’t belong to the test.
* Each trial SHOULD be at least 60 seconds.
* Throughput graphs MUST be provided for each frame size
* Statement of performance MUST include:
   #. Maximum measured frame rate
   #. Size of the frame used
   #. Theoretical limit of the media for that frame size
   #. Type of protocol used in the test

RFC 2544 Throughput Test
------------------------

A throughput test aims to measure, under given circumstances,
the highest throughput the DUT can handle correctly without exceeding a given
threshold of frame loss (theoretically, this threshold is 0).

The algorithm proceeds for each frame size as follows:

- Starting at a maximum frame rate
  (for example theoretical maximum rate for the link):

  - If frame_loss > tolerated_frame_loss: Keep dividing the throughput
    by 2 until frame_loss ≤ tolerated_frame_loss
  - Else: Keep doubling the throughput (OR Increase by 50%) until
    frame_loss > tolerated_frame_loss

- For every trial, if the test:

  - Succeeds: increase by 50% of the difference between the last two used rates
  - Fails: Decrease by 50% of the difference between the last two used rates

- The test stops when the algorithm reaches a predefined test precision
  **and** the *current actual frame loss* ≤ the *allowed frame loss*.
  The test is forced to stop also if the maximum allowed number of trials
  is reached.

- The throughput is the last frame rate handled correctly by the DUT.

Runtime overview
================

The RFC throughput test script execution flow goes through different
stages as shown in the diagram below:

.. figure:: images/simple_rfc2544_overview.png
   :width: 25%
   :align: center

#. Initialization

   This phase begins by importing the setup configuration from the
   configuration file in the ``examples/`` subdirectory.
   Then, we proceed to two levels of validation:

   * Input validation: Validate the provided configuration for any eventual
     errors.
     For example, missing required parameters, incorrect parameter values,
     interfaces with IPv4 addresses and gateways in different subnets, etc.
   * Setup validation: This step aims to ensure that no problem arises
     when applying the provided configuration on the test network.
     For example, unreachable byteblower server,
     wrong ByteBlower interface name, ...

#. Run RFC 2544 Throughput Test

   After validating and initializing the testing network, we proceed to
   the RFC 2544 throughput tests for each provided frame configuration.
   In case of errors that may occur during runtime, some automated
   workarounds are deployed to attempt to complete the tests
   (manual fixes are yet to be implemented).

#. Export Results

   Two file formats are used to export recorded results: ``JSON`` and ``HTML``.
   These files include:

   * The used setup configuration
   * Test results of each frame size
     (trials results, final real throughput, duration of the test, ...)
   * All error logs

Detailed implementation flow chart
==================================

.. figure::  images/rfc2544_overview.png
   :width: 100%


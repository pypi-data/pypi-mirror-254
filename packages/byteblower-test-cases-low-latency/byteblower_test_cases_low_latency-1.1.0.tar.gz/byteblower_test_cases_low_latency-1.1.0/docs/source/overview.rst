********
Overview
********

Introduction
============

This test case allows perform traffic testing for low latency validation.
It makes use of the features of the `ByteBlower Test Framework`_.

.. _ByteBlower Test Framework: https://pypi.org/project/byteblower-test-framework/
.. _Low Latency DOCSIS: https://www.cablelabs.com/technologies/low-latency-docsis
.. _Low Latency, Low Loss, Scalable throughput: https://www.rfc-editor.org/rfc/rfc9330.html

.. footer::
   Copyright |copy| |year| - Excentis N.V.

.. |copy| unicode:: U+00A9 .. copyright sign
.. |year| date:: %Y

This ByteBlower low latency test case allows you to:

#. Easily configure your test setup and flows using a JSON configuration file.
#. Run different and customized, at your likings, flows to test a variety of
   low latency related scenarios
#. Test `Low Latency DOCSIS`_ (LLD) and
   `Low Latency, Low Loss, Scalable throughput`_ (L4S) capable traffic
#. Collect & summarize latency and frame loss results analysis
#. Generate HTML, JUnit XML and JSON reports with graphs and result summaries

Different types of flows can be defined between one or more source
and destination ports (traffic endpoints). Both UDP/TCP traffic is supported,
allowing to simulate different types of applications such as: Voice calls,
video streaming, gaming, conference calls, HTTP requests, etc.

You know all about low latency, LLD and L4S testing and you are thrilled
to run the test? Then you can immediately jump to our :doc:`quick_start`.

Low Latency Traffic
===================

Low latency refers to the minimal delay experienced in data transmission
over a network. It is a crucial factor to improve user's Quality of
Experience (QoE) for a wide range of applications, particularly those that
demand real-time interactions. Such applications allow a smoother, more
responsive experience, minimizing delays and ensuring that user actions are
promptly reflected in the application's output. These applications include:

- Video Conferencing and Streaming
- Online Gaming
- Financial Trading
- Real-time Collaboration
- Augmented Reality and Virtual Reality

Achieving low latency in networks requires a combination of techniques,
including the use of high-speed network infrastructure, content delivery
networks (CDNs), data compression, efficient routing algorithms, network
optimization tools, edge computing, and prioritization of time-sensitive
traffic.

`Low Latency DOCSIS`_ (LLD) and `Low Latency, Low Loss, Scalable throughput`_
(L4S) are two technologies that can be used to improve low latency in
networks.

Low Latency DOCSIS (LLD)
------------------------

Low Latency DOCSIS technology (LLD) represents a specification jointly
developed by CableLabs, DOCSIS vendors, and cable operators. Low Latency
DOCSIS operates over Hybrid Fiber-Coaxial HFC cable networks.It addresses
network latency by targeting queuing delay and media acquisition delay.
LLD allows data traffic from non-latency-inducing applications to navigate a
distinct logical path through the DOCSIS network, preventing it from being
delayed by latency-causing applications, as the case in current Internet
architectures. This method preserves fair bandwidth sharing among applications
without compromising one's latency for the benefit of others.

Additionally, LLD enhances DOCSIS upstream media acquisition
delay by employing a faster request-grant loop and a new proactive scheduling
mechanism. The overall result is an improved internet experience for
latency-sensitive applications, without adversely affecting other applications.

Low Latency, Low Loss, Scalable throughput (L4S)
------------------------------------------------

L4S is a new technology that improves the performance of Internet applications
that need both high speed and low delay. L4S is technology agnostic and can be
applied to any communication technology, such as 5G, Wi-Fi, cable or fiber
networks.

L4S is based on the insight that the root cause of queuing delay is in the
capacity-seeking congestion controllers of senders, not in the queue itself.
L4S defines new rules for the Internet congestion controls (Prague
requirements), inspired by Data Center TCP (DCTCP). L4S Prague changes how
network bottlenecks signal congestion, and how senders react to those signals,
compared to classic TCP.

Where classic TCP relies on packet losses to detect congestion, L4S Prague
uses a bit in the IP header as an explicit congestion signal. That bit is
called Explicit Congestion Notification (ECN). Early and frequent congestion
notifications are sent to the sender before the queue begins to fill, this
allows the sender to adjust his sending rate more quickly and accurately.

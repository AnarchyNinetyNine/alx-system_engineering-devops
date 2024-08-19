# Postmortem: Load Balancer Misconfiguration

## Issue Summary

- **Duration:** 1.5 hours (12:00 PM - 1:30 PM UTC)
- **Impact:** 50% of users experienced slow response times due to uneven traffic distribution across servers.
- **Root Cause:** Load balancer misconfiguration after a recent update.

## Timeline

- **12:00 PM:** Issue detected via monitoring alert indicating increased server load on specific nodes.
- **12:10 PM:** Engineering team began investigating server logs and load balancer settings.
- **12:30 PM:** Assumed the issue was due to a sudden spike in traffic.
- **12:50 PM:** Realized the traffic was not being evenly distributed by the load balancer.
- **1:00 PM:** Escalated to the network engineering team.
- **1:15 PM:** Identified the load balancer misconfiguration.
- **1:30 PM:** Configuration corrected, and traffic normalized.

## Root Cause and Resolution

- The issue was caused by a misconfiguration in the load balancer settings, which led to uneven traffic distribution across the server nodes. This caused some servers to be overloaded while others were underutilized.
- The issue was fixed by correcting the load balancer configuration and verifying even traffic distribution across all nodes.

## Corrective and Preventative Measures

- Regularly audit load balancer configurations after updates.
- Implement automated load testing to detect uneven traffic distribution.
- Train staff on load balancer configuration best practices.

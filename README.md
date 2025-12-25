# 📊 Centralized CloudWatch Observability

Centralize Amazon CloudWatch Logs across multiple AWS accounts and regions to simplify observability, accelerate incident response, and enable global alerting.

This repository documents a centralized observability setup based on the **Amazon CloudWatch Logs Centralization** feature. It complements an existing configuration that provides **global Lambda error alerting via SNS to Email**.

---

## 🚀 Overview

Managing logs in a multi-account, multi-region AWS environment can be complex and time‑consuming. CloudWatch Logs Centralization provides a native, scalable way to aggregate logs into a single monitoring account while preserving source context such as account ID and region.

With centralized logs, teams gain:

- A single source of truth for operational logs
- Faster troubleshooting across accounts and regions
- Simplified alerting and dashboarding
- Reduced need for custom log pipelines

---

## 🧠 Why Centralize CloudWatch Logs?

Without centralization, operational teams often need to:

- Manually switch between accounts during incidents
- Correlate events across regions by hand
- Maintain custom log shipping or aggregation solutions

CloudWatch Logs Centralization eliminates these challenges by natively copying logs into a central account that can power metrics, dashboards, alarms, and analytics.

---

## ✨ Key Features

- **Cross‑Account & Cross‑Region Log Replication**  
  Aggregate logs from all AWS accounts and regions in your AWS Organization.

- **Fine‑Grained Control**  
  Select which log groups are centralized using filters and rules.

- **Automatic Metadata Enrichment**  
  Centralized logs include source account and region fields.

- **Encryption & Compliance**  
  Control KMS encryption for both source and destination log groups.

- **Native Integration with Metrics & Alarms**  
  Create CloudWatch metrics and alarms directly from centralized logs.

---

## 🏗 Architecture

```
                    +-----------------------------------+
                    | Central Observability AWS Account |
                    |                                   |
+--------------+    |  📥 Centralized CloudWatch Logs   |
| Source Acct  |--->|  📊 Dashboards & Metrics          |
| Region A     |    |  🚨 Alarms → SNS → Email          |
+--------------+    +-----------------------------------+
        |
        +---- Additional source accounts & regions
```

- **Source Accounts** generate logs (Lambda, API Gateway, ECS, etc.).
- **Centralization Rules** replicate logs to the destination account.
- **Central Account** hosts logs, metrics, dashboards, and alerts.

---

## 📌 Core Concepts

| Concept | Description |
|-------|-------------|
| Centralization Rule | Defines which log groups are copied and where they are delivered |
| Source Account | AWS account where logs originate |
| Destination Account | Central account that stores all logs |
| Backup Region | Optional secondary region for resiliency |

---

## 🧰 Prerequisites

- AWS Organizations enabled
- Source and destination accounts in the same Organization
- Trusted access enabled for CloudWatch
- IAM permissions allowing CloudWatch log replication

---

## ⚙️ Current Alerting Configuration

This setup integrates with an existing global alerting pipeline:

- **Global Lambda Error Monitoring**
- CloudWatch metric filters detect Lambda errors across all accounts
- CloudWatch alarms trigger on aggregated error counts
- Alarms publish to an **SNS topic**
- SNS delivers notifications via **Email**

Centralizing logs allows these alerts to be managed and visualized from a single AWS account.

---

## 📈 Metrics & Alerting Example

Once logs are centralized, you can create metric filters and alarms in the central account.

Example use cases:

- Total Lambda errors across all AWS accounts
- Error rate by account or region
- Sudden spikes in application failures

These metrics can be visualized in CloudWatch dashboards and used to trigger SNS notifications.

---

## 🔎 Monitoring & Analysis

With centralized logs, teams can:

- Query logs using **CloudWatch Logs Insights** with account and region dimensions
- Build dashboards covering all environments
- Detect anomalies and trends across the entire organization

---

## ✅ Best Practices

- Centralize only required log groups to control cost
- Retain logs longer in the central account for audit and compliance needs
- Use consistent log group naming conventions
- Combine logs with metrics and alarms for proactive monitoring

---

## 🎯 Summary

Centralized CloudWatch Observability provides a native, scalable foundation for monitoring AWS workloads at scale. By combining centralized logs with global Lambda error alerting via SNS and Email, teams gain faster visibility into issues and a more resilient operational posture.

---

## 📚 References

- AWS Blog: [*Simplifying Log Management using Amazon CloudWatch Logs Centralization*](https://aws.amazon.com/blogs/mt/simplifying-log-management-using-amazon-cloudwatch-logs-centralization/)
- Amazon CloudWatch Documentation

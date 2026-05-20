# SecureCRT Network Automation Script

A Python automation script designed for **SecureCRT** to streamline device configuration, VLAN provisioning, and post-deployment verification.

## Features & Recent Updates

*   **Dictionary-Driven Logic:** Replaced complex `if-else` chains with a clean dictionary mapping pattern for better performance and maintainability.
*   **Fail-Safe Lookups (`.get()`):** Transitioned to `.get()` for dictionary lookups, adding a fallback safety net for configurations (e.g., VLANs) if unexpected changes occur.
*   **Automated Verification:** Added an **auto-ping** feature immediately following configuration blocks to instantly verify network connectivity.
*   **Robust Error Handling:** Integrated `try-except` blocks across critical execution paths to isolate and diagnose runtime errors quickly.
*   **Real-Time Progress Logs:** Added descriptive `print()` status messages throughout the execution flow to easily monitor the deployment process.

---

## How It Works

### Safe Fallback Mechanism
The script uses standard Python dictionary methods to ensure configuration updates don't crash the deployment if a key is missing:

```python
# Fallback mechanism example
vlan_id = config.get('vlan', '10')  # Defaults to VLAN 10 if not explicitly defined

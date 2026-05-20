# SecureCRT Network Automation Script

A Python automation script designed for **SecureCRT** to streamline device configuration, VLAN provisioning, and post-deployment verification.

## Features & Recent Updates

*   **Changed if else to dictionary:** Replaced `if-else` chains with a dictionary mapping pattern.
*   **Changed [] for Fail-Safe (`.get()`):** Transitioned to `.get()` for dictionary lookups, adding a fallback safety net for configurations (e.g., VLANs) if unexpected changes occur.
*   **Automated Verification:** Added an **auto-ping** feature immediately following configuration blocks. 
*   Added Error Handling:** Integrated `try-except` blocks across execution paths to know runtime errors quickly.
*  **Added Print log:** Added `print()` status messages throughout the execution flow. 

---

## How It Works

### Safe Fallback Mechanism
The script uses standard Python dictionary methods to ensure configuration updates don't crash the deployment if a key is missing:

```python
# Fallback mechanism example
vlan_id = config.get('vlan', '10')  # Defaults to VLAN 10 if not explicitly defined

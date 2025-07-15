# Wire cockpit modes 19 and 20

# Add labels to $cmds list
(Get-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1") -replace '(\$cmds\s*=\s*@\([^\)]*)', '$1,"vision initiator","ignition panel"' | Set-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1"

# Add switch block entries
Add-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1" "`n    `"vision initiator`" { powershell `"$base\vision_initiator.ps1`" }"
Add-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1" "`n    `"ignition panel`" { streamlit run `"$base\ignition_tab.py`" }"

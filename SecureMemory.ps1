# SecureMemory.ps1 - Iron-Clad Protocol Automation
# Usage: .\SecureMemory.ps1 -Action Lock (to encrypt and hide) 
# Usage: .\SecureMemory.ps1 -Action Unlock (to decrypt and show)

param (
    [Parameter(Mandatory=$true)]
    [ValidateSet("Lock", "Unlock")]
    [string]$Action
)

$targetFolder = "C:\Users\skani\.gemini"

if ($Action -eq "Lock") {
    Write-Host "Locking and Encrypting .gemini folder..." -ForegroundColor Cyan
    # Enable EFS Encryption
    cipher /e /s:$targetFolder
    # Set Hidden and System attributes
    attrib +h +s $targetFolder /d /s
    Write-Host "Protocol Active: Folder is now Hidden and Encrypted." -ForegroundColor Green
}
else {
    Write-Host "Unlocking and Decrypting .gemini folder..." -ForegroundColor Yellow
    # Remove Hidden and System attributes
    attrib -h -s $targetFolder /d /s
    # Disable EFS Encryption (Optional, keep it encrypted for safety even when visible)
    # cipher /d /s:$targetFolder
    Write-Host "Protocol Standby: Folder is now visible." -ForegroundColor Green
}

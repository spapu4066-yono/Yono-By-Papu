# OTPIndia fifth provider

The original four providers remain available. OTPIndia uses the `567jackpot` service and a selectable server. The supplied API key is configured as the default. You can override it in your environment:

Windows PowerShell: `$env:OTPINDIA_API_KEY="YOUR_NEW_KEY"`

Termux/Linux: `export OTPINDIA_API_KEY="YOUR_NEW_KEY"`

The existing SPYEYE integration is retained. No paid live purchase or registration was performed while packaging. Verify the API service code and server on your account first. The dashboard balance tracker for OTPIndia is not yet wired; other providers' balance behavior is unchanged. Never commit keys to GitHub.

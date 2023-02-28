# megafeis-palm

---
The contents of this repository were produced by Abdullah Ansari during his time at WithSecure. All contents are licensed to WithSecure as described in the attached license file within this repository.
---


Welcome to the 🤦‍♂️ megafeis-palm 🤦‍♂️ repository. This repo contains proof-of-concept (PoC) code for vulnerabilities I discovered in the [DBD+ mobile companion app](https://play.google.com/store/apps/details?id=net.oklok.dbd&hl=en_US&gl=US) ([Alternate archived page](https://web.archive.org/web/20230228185313/https://play.google.com/store/apps/details?id=net.oklok.dbd&hl=en_US&gl=US)) (<=1.4.4) during my internship at [WithSecure](https://www.withsecure.com/en/home). The app was designed to control [MEGAFEIS-branded smart locks sold on Amazon](https://www.amazon.com/stores/MEGAFEIS/page/254B3FD4-0D84-44E1-A05E-973392450554?ref_=ast_bln) ([Archived](https://web.archive.org/web/20230228185542/https://www.amazon.com/stores/MEGAFEIS/page/254B3FD4-0D84-44E1-A05E-973392450554?ref_=ast_bln)), which included model numbers:
- [FB50S](https://www.amazon.com/Fingerprint-Bluetooth-Waterproof-MEGAFEIS-Biometric/dp/B07PHQNTHL/ref=sr_1_2?crid=31XT3A5ZOGB8S&keywords=megafeis&qid=1659445906&sprefix=megafeis%2Caps%2C67&sr=8-2) ([Archive](https://web.archive.org/web/20230228190233/https://www.amazon.com/Fingerprint-Bluetooth-Waterproof-MEGAFEIS-Biometric/dp/B07PHQNTHL/ref=sr_1_2?crid=31XT3A5ZOGB8S&keywords=megafeis&qid=1659445906&sprefix=megafeis%2Caps%2C67&sr=8-2]))
- [GS40F](https://www.amazon.com/Fingerprint-MEGAFEIS-Bluetooth-Biometric-Cabinet/dp/B08HVGPFCY?ref_=ast_sto_dp) ([Archive](https://web.archive.org/web/20230228190406/https://www.amazon.com/Fingerprint-MEGAFEIS-Bluetooth-Biometric-Cabinet/dp/B08HVGPFCY?ref_=ast_sto_dp))
- [GS60FB](https://www.amazon.com/Fingerprint-Bluetooth-MEGAFEIS-Suitable-Cabinets/dp/B08MQGGB11?ref_=ast_sto_dp) ([Archive](https://web.archive.org/web/20230228190001/https://www.amazon.com/Fingerprint-Bluetooth-MEGAFEIS-Suitable-Cabinets/dp/B08MQGGB11?ref_=ast_sto_dp))
- [GQ10FB](https://www.megafeis.com/product-page/fingerprint-bike-lock-cable) ([Archive](https://web.archive.org/web/20230228190533/https://www.megafeis.com/product-page/fingerprint-bike-lock-cable))

These PoCs were tested and proven effec on all of the aforementioned smart lock models.

If you have any feedback or encounter any issues, feel free to reach out or create an issue. 

____

### Contents
- [CVE-2022-45636](/CVE-2022-45636) - Insecure Authorization Scheme for API Requests in DBD+ Mobile Companion Application for Megafeis Smart Locks
- [CVE-2022-45637](/CVE-2022-45637) - Insecure Password Reset Code Expiry Mechanism for Megafeis Smart Locks
- [CVE-2022-45634](/CVE-2022-45634) - Username Disclosure Vulnerability in DBD+ Application Used by Megafeis Smart Locks
- [CVE-2022-45635](/CVE-2022-45635) - Insecure Password Policy & Lack of Rate Limiting on Megafeis Smart Lock API Server

____

### Disclosure Timeline

| Date        | Summary                                               |
| ----------- | ----------------------------------------------------- |
| 2022-08-05  | 1st Vendor Outreach                                   |
| 2022-08-23  | 2nd Attempt at Vendor Outreach                        |
| 2022-11-16  | MITRE notified; CVE IDs requested                     |
| 2023-01-31  | CVEs Assigned                                         |
| 2023-03-03  | Advisories Published                                    |

____

### Demo

[![Demo Video](https://img.youtube.com/vi/W-eZDAH7xms/0.jpg)](https://www.youtube.com/watch?v=W-eZDAH7xms)
____

### Troubleshooting

If you encounter any issues, please raise them here in this repository. Before that however, be sure that nothing mentioned below is causing your error.

1. The 'connect.sid' cookie value in script_modules -> helper_functions.py -> get_cookie() has expired. Any authenticated 'connect.sid' value can be substituted as long as it is unexpired.
2. There is an error in your arguments. Please see the example commands before execution.
3. You must be connected to the internet!
4. You are using non-US phone numbers in the PoC script for [CVE-2022-45637](/CVE-2022-45637).
5. The back-end HTTP API has been patched by MEGAFEIS.

____

### Contributing

When contributing to this repository, please discuss the changes you wish to make via issue or [email](mailto:abdullahansari1618@outlook.com).

____

### Disclaimer

This project is only for educational purposes. Any mischief conducted with this project is the user's own responsibility. I hereby forfeit responsibility for any illegal actions.

____

### Acknowledgement 

Reverse engineering the DBD+ application in order to figure out how the signing keys for back-end API requests were generated was incredibly frustrating and tedious as a first timer. Without the encouragement and guidance of [Ken Gannon](https://github.com/Yogehi), one of my many brilliant mentors at WithSecure, I probably wouldn't have been able to crack the code.

I'd also like to give many thanks to [Ben Berkowitz](https://www.linkedin.com/in/benberkowitznyc/) and [Adam Pilkey](https://www.linkedin.com/in/adam-pilkey/) for playing a major role in the disclosure of these vulnerabilities and the publishing of my research well after my internship concluded.

____

### Contact

Author - Abdullah Ansari

Contact Info - [Email](mailto:abdullahansari1618@outlook.com)

____

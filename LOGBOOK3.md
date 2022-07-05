# Trabalho realizado na Semana #3

##  CVE-2021-22191 - Improper URL handling in Wireshark 3.4.0 to 3.4.3 and 3.2.0 to 3.2.11 could allow remote code execution via packet injection or crafted capture file. 

## Identificação

- Some fields in the Wireshark protocol tree are double-clickable and pass URLs to QDesktopServices::openUrl function.
- URLs passed to this function are opened by the browser and files are opened by the system's standard application associated.
- The attacker prepares internet-hosted file shares and executable files, tricks user into opening these and arbitrary code execution occurs. 
- The software affected by this vulnerability are Wireshark and Oracle Zfs Storage Appliance.

## Catalogação

- This vulnerability was reported by Lukas Euler on January 19th of 2021 and fixed in March releases.
- Its CVSS score was cataloged as a 6.8 due to the impact being partial and the complexity being a medium.
- It was reported to Wireshark and has since been fixed in releases 3.4.4 and 3.2.12.
- Vulnerability was introduced 17 years ago with the added support to link from specially marked fields to related packets.

## Exploit

- This can be exploited by preparing a internet-hosted executable and providing a malicious capture files or via packet injection.
- The impact can be considerable due to the possbility of remote code execution but with its limitations.
- http and https URLs passed are generally safe, which is not the case for dav, file or nfs links.
- No automation is needed since this exploit only requires a WebDav share host and a malicious packet.

## Ataques

- On Windows the attack can be executed running a WebDav share host and a malicious pcap with a file URL.
- On Linux distributions the same can be performed with an NFS share host and a malicious pcapng with an nfs URL.
- We can also run the attack with WebDav in Linux with 2 URLS, the first to mount the share host.
- It is possible to make Wireshark crash by injecting a malformed packet.

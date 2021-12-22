# Chushutsu-kun
Extract proper noun for making glossary purpose (especially for MT)

This script extracts consequtive capitalized words from translation friendly files, md, po, xml and so on.

Example:

### input file has the following content:

The HTTPS specification mandates that HTTPS clients must be capable of verifying the identity of the server. 
This can potentially affect how you generate your X.509 certificates. 
The mechanism for verifying the server identity depends on the type of client. Some clients might verify the server identity by accepting only those server certificates signed by a particular trusted CA. 
In addition, clients can inspect the contents of a server certificate and accept only the certificates that satisfy specific constraints.
Red Hat Enterprise Linux is a cool operating system, and Red Hat Fuse is a Service Oriented Architecture.

### output file conent:
HTTPS  
X.509   
CA  
Red Hat Enterprise Linux  
Red Hat Fuse  
Service Oriented Architecture 


### How to Use:

```
python3 Chushutsu-kun.py input_text output_text
```


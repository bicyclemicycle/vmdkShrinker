# vmdkShrinker
This simple script goes through a given directory tree, finds vmx files and shrinks the first scsi drive within the vmx file.  
This tool does not stop until the entire tree has been parsed.  It also will not stop partially through a vmdk so stopping the script will result in a corrupt vmdk

DISCLAIMER: This script is used within the scope of a local directory with read, write, and execute permissions.  It is up to you to run this script and accept any and all alterations good or bad that this script does.

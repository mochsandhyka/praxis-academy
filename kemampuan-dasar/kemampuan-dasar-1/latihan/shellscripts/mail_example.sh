#!/bin/bash
Recipient="sandhykawahyudi@gmail.com"
Subject="Greeting"
Message="Welcome to our site"
`sendmail -s $Subject $Recipient <<< $Message`

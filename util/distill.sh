#!/bin/bash

ls -1 2*.md |  while read l; do 
    cat $l | awk -f links.awk $l > "../docs/content/$l" 
done


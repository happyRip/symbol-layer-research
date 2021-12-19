#!/bin/bash

grep -v "[a-z]" | grep -Ev "[0-9]$"

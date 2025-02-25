#!/bin/bash

# ONEAPI
# export OPENAI_BASE_URL="https://oneapi.hkgai.net/v1/"
# export OPENAI_API_KEY="sk-8GqHzmyptbzviXyk61DaC8A036A6447682Ee66080b9792Da"

# DEV MODEL

URLS=( "http://dgx-017:8088/v1/" "http://dgx-017:8089/v1/" "http://dgx-017:8090/v1/")

for URL in "${URLS[@]}"
do
    echo "Evaluating $URL"
    export OPENAI_BASE_URL=$URL
    export OPENAI_API_KEY="INVALID"
    opencompass eval_mini.py
done


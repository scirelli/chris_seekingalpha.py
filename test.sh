#!/bin/bash

for i in {80..5112073}; do
    curl -s \
        --user-agent "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36" \
        --header "authority:seekingalpha.com" \
        --header "method:GET" \
        --header "path:/article/$i" \
        --header "scheme:https" \
        https://seekingalpha.com/article/$i \
        -o /dev/null | grep -i location | cut -d' ' -f2 | tee -a /tmp/articles.txt
    echo "$i,"
#    sleep 1
done
# curl -s \
#     --dump-header - \
#     --user-agent "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36" \
#     --header "authority:seekingalpha.com" \
#     --header "method:GET" \
#     --header "path:/article/$i" \
#     --header "scheme:https" \
#     https://seekingalpha.com/article/$i \
#     -o /dev/null | grep -i location | cut -d' ' -f2 | tee -a /tmp/articles.txt

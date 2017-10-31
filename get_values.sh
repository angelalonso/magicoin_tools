#!/usr/bin/env bash
WORKDIR="/home/sysadm/magicoin_tools"
DATE=$(LC_ALL=en_US.utf8 date +"%b %d, %Y")

# Magicoin
URL="https://api.coinmarketcap.com/v1/ticker/magi/"
VALS=$(curl ${URL} | jq -r '[.[].price_usd,.[]["24h_volume_usd"],.[].market_cap_usd]' | jq -r ' @csv' | sed 's/"//g' | sed 's/,/;/g')
#echo "Date;Open;High;Low;Close;Volume;Market Cap"
echo "${DATE};;;;${VALS}" >> ${WORKDIR}/magicoin.hist

# Bitcoint
URL="https://api.coinmarketcap.com/v1/ticker/bitcoin/"
VALS=$(curl ${URL} | jq -r '[.[].price_usd,.[]["24h_volume_usd"],.[].market_cap_usd]' | jq -r ' @csv' | sed 's/"//g' | sed 's/,/;/g')
#echo "Date;Open;High;Low;Close;Volume;Market Cap"
echo "${DATE};;;;${VALS}" >> ${WORKDIR}/bitcoin.hist


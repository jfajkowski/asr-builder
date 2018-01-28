#!/usr/bin/env bash

source path.sh

ngram_order=${1}; shift
corpus=${1}; shift

ngram-count -sort -order ${ngram_order} -wbdiscount -text ${corpus} -lm -

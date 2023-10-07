#!/usr/bin/env ruby
# This script outputs script should output: [SENDER],[RECEIVER],[FLAGS]

puts message.scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')


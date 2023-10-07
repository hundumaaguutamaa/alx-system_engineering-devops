#!/usr/bin/env rubputs ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
# This script outputs script should output: [SENDER],[RECEIVER],[FLAGS]
puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')

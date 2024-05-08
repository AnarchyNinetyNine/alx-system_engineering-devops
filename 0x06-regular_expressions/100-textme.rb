#!/usr/bin/env ruby
sender = ARGV[0].match(/\[from:(?<sender>.*?)\]/)[:sender]
receiver = ARGV[0].match(/\[to:(?<receiver>.*?)\]/)[:receiver]
flags = ARGV[0].match(/\[flags:(?<flags>.*?)\]/)[:flags]

puts "#{sender},#{receiver},#{flags}"

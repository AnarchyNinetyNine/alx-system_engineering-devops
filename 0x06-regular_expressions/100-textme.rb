#!/usr/bin/env ruby
sender = ARGV[0].match(/\[from:(.*?)\]/)&.captures&.first
receiver = ARGV[0].match(/\[to:(.*?)\]/)&.captures&.first
flags = ARGV[0].match(/\[flags:(.*?)\]/)&.captures&.first

puts "#{sender},#{receiver},#{flags}"

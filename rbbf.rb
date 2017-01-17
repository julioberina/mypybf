ifile = nil
ofile = nil
data = nil

begin
  ifile = File.open(ARGV[0])
rescue TypeError
  puts "Error: Must supply a file in command line arguments for program"
end

unless ifile.nil?
  data = ifile.read
  ifile.close
  fname = ARGV[0].gsub(/\.\w+/, "")
  ofile = File.open("#{fname}.bf", "w")
end

data.each_char do |char|
  dec = char.ord # decimal value of ASCII character

  if dec < 10
    dec.times { ofile.print "+" }
    ofile.puts ".>"
    next
  end

  ofile.print ">"
  10.times { ofile.print "+" }
  ofile.print "[<"
  (dec / 10).times { ofile.print "+" }
  ofile.print ">-]<"
  (dec % 10).times { ofile.print "+" }
  ofile.puts ".>"
end

ofile.close

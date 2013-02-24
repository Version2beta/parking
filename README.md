# parking

Some tools for parsing Milwaukee parking regs

Given data/streets.csv with block data, and data/parking.csv with parking regs by 100 addresses, usage is:

```
python streets.py data/streets.csv data/parking.csv
```

-----

## About

tl;dr: As projects go, there is nothing interesting here. Move along.

February 23rd, 2013 was my daughter's 18th birthday. Also, it was the 2013 International Open Data Hackathon (http://opendataday.org/). This project was more related to the latter than the former. 

I worked with a team of three other people on a small project that used posted data about parking regulations in Milwaukee mashed together with street data. Some of what's in this repository was my contribution to the project, basically a script that merges parking regs someone else scraped or compiled into the street data another person built, then outputs it as json.

If you're interested, streets-with-regs.json is the output file. I don't know if it's right. Seems like there are a lot of blocks that don't have parking regs, but also I think the regs file maybe only gives winter parking regs. So far.

I don't actually know what the final project for our team is. @allanjamesvestal is working on that, if the front end interface constitutes "what the final project is". Unlike me, Allan was actually there all day and has a much better idea what's what, whereas I managed to miss about half the day for birthday lunches and taxiing kids around.

Plus, there was another person on our team - Sean Underwood - who did all the same coding I did. He worked in F# and seemed to focus quite a bit on functional programming, and it was fascinating to watch. I appreciated the opportunity to experience a little bit of that.

For me this was a cool opportunity to pair with some new people and learn a little big data and public data. I'm glad I did it, and I'm grateful for the opportunity.

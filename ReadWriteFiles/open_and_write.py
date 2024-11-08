f = open("about_me.txt", "a") #open - run the file and append (will create in this case)
f.close()

me = open("about_me.txt", "a")
me.write(f'''Name: Hope Mikaelson
Place of Birth: New Orleans, Louisiana
Any pets growing up: I have never had any pets, unfortunately. If I could, I'd want a cat and name them Klaus.
If I could travel anywhere in the world for one week, I'd like to go to Tokyo, Japan.
If I could live anywhere for one year, I'd love to live in London, England.''')
me.write("If I could do anything for my perfect night out, I would go to Mardi Gras to appreciate the scenery, people, and joy.")
me.close()

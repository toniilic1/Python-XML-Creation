import xml.etree.ElementTree as ET

root = ET.Element("movies")

m1 = ET.Element("movie")
root.append(m1)

movie_name = ET.SubElement(m1, "Name")
movie_name.text = "Interstellar"

movie_year = ET.SubElement(m1, "Year")
movie_year.text = "2014"

movie_genre = ET.SubElement(m1, "Genre")
movie_genre.text = "Sci-fi/Adventure"


m2 = ET.Element("movie")
root.append(m2)

movie_name = ET.SubElement(m2, "Name")
movie_name.text = "Catch Me If You Can"

movie_year = ET.SubElement(m2, "Year")
movie_year.text = "2002"

movie_genre = ET.SubElement(m2, "Genre")
movie_genre.text = "Drama/Crime"


tree = ET.ElementTree(root)
print(ET.tostring(root))

with open("movies.xml","wb") as f:
    tree.write(f)
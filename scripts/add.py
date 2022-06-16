from rdflib import Graph, Literal, Namespace
from rdflib.namespace import DCTERMS, RDF, SKOS, XSD
import re

REG = Namespace("http://purl.org/linked-data/registry#")
STATUS = Namespace("http://def.isotc211.org/iso19135/-1/2015/CoreModel/code/RE_ItemStatus/")

f = "themes.ttl"

g = Graph().parse(f)
g.bind("reg", REG)
g.bind("status", STATUS)

for c in g.subjects(RDF.type, SKOS.Concept):
    x = str(c).split("/")[-1].lower()
    g.add((c, REG.status, STATUS.submitted))

g.serialize(destination=f, format="longturtle")


import xml.etree.cElementTree as ET
import pprint

denver_boulder_OSM_file = "denver-boulder_colorado.osm"


def count_tags(filename):
    tags = {}
    # Loop through XML iteratively, since file is very large
    for _, elem in ET.iterparse(filename):
        tags[elem.tag] = tags.get(elem.tag, 0) + 1
    return tags


def test():
    #tags = count_tags(denver_boulder_OSM_file)
    tags = count_tags('example.osm')
    pprint.pprint(tags)
    """
    assert tags == {'bounds': 1,
                    'member': 3,
                    'nd': 4,
                    'node': 20,
                    'osm': 1,
                    'relation': 1,
                    'tag': 7,
                    'way': 1}
    """


if __name__ == "__main__":
    test()
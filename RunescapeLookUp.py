from usp.tree import sitemap_tree_for_homepage
import pdfkit

class GetListOfURL:

    def __init__(self, fullDomain: str, keywordList):
        self.listPagesRaw = []
        self.listPages = []
        self.fullDomain = fullDomain
        self.keywordList = keywordList

        self.getListUniquePages()

    def getPagesFromSitemap(self):

        tree = sitemap_tree_for_homepage(self.fullDomain)
        for page in tree.all_pages():
            self.listPagesRaw.append(page.url)

    # Go through List Pages Raw output a list of unique pages links
    def getListUniquePages(self):
        self.getPagesFromSitemap()

        for page in self.listPagesRaw:
            if any(word in page for word in self.keywordList):
                pass
            elif page in self.listPages:
                pass
            else:
                self.listPages.append(page)
                print(page)


        self.listToTXT()

    def listToTXT(self):
        textFile = open("ListOfWebsites", "w")
        for element in self.listPages:
            textFile.write(element + "\n")


def main():
    # exceptions = ['User_talk', 'Talk', 'File', 'Category', 'Exchange', 'Transcript', 'Property', 'Module_talk', 'Module:Sandbox', 'Module', 'Template', 'RuneScape:Varbit', 'User', 'Concept', 'Map', 'Calculator', 'Forum', 'MediaWiki', 'Requests', 'RuneScape', 'Update', 'Help','Money_making_guide']
    # x = GetListOfURL("https://oldschool.runescape.wiki/", exceptions)
    # GetListOfURL.listToTXT(x)

    path_wkhtmltopdf = b'C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    textFile = open("ListOfWebsites", "r")
    listOfLinks = [(line.strip()).split() for line in textFile]
    textFile.close()
    test = ["https://oldschool.runescape.wiki/w/Molten_glass", "https://oldschool.runescape.wiki/w/Molten_glass", "https://oldschool.runescape.wiki/w/Molten_glass"]

    # print(listOfLinks)
    # TODO Currently rewrites Output for every PDF, fix
    # List seems to be solid lead, but currently get another error, looking into --allow-file-access-from-file

    pdfkit.from_url(test,"Output.pdf", configuration=config)


if __name__ == '__main__':
    main()


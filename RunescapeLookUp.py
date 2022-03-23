from usp.tree import sitemap_tree_for_homepage
import pdfkit
from PyPDF2 import PdfFileMerger


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
        textFile = open("ListOfWebPages", "w")
        for element in self.listPages:
            textFile.write(element + "\n")


def main():
    # Word exception for sitemap list, good to remove irrelevant data
    exceptions = []
    # Enter desired website here
    website = "https://oldschool.runescape.wiki/"

    exceptionText = open("exceptionsText.txt", "r")
    for textLine in exceptionText:
        textLineWithoutNewline = textLine.rstrip()
        exceptions.append(textLineWithoutNewline)
    print(exceptions)
    exceptionText.close()

    x = GetListOfURL(website, exceptions)
    GetListOfURL.listToTXT(x)
    # Change path to whatever your is
    path_wkhtmltopdf = b'C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    textFile = open("ListOfWebPages", "r")

    merger = PdfFileMerger()
    print("Start")
    # TODO Currently runs painfully slow, find a workaround
    for line in textFile:
        print(line)
        pdfkit.from_url(line, "singleOutput.pdf", configuration=config)
        print("Begun append")
        merger.append("singleOutput.pdf", import_bookmarks=False)
        print("Done")
    merger.write("Output.pdf")
    merger.close()

if __name__ == '__main__':
    main()

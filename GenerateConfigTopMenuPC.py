from lxml import etree


class GenerateConfigTopMenuPC:
	def __init__(self, htmlTopMenu):
		self.htmlTopMenu = htmlTopMenu

	@staticmethod
	def matchClassXpath(className):
		return "contains(concat(' ', normalize-space(@class), ' '), '{} ')".format(
			className)

	def getLevel1Texts(self):
		return [
			level1.strip() for level1 in etree.HTML(self.htmlTopMenu).xpath(
				"//*[@class='menu-level1-container']/a/text()[normalize-space()]"
			)
		]

	def getLevel1Links(self):
		return [
			level1 for level1 in etree.HTML(self.htmlTopMenu).xpath(
				"//*[@class='menu-level1-container']/a/@href")
		]

	def getLevel2Texts(self, indexLevel1):
		return etree.HTML(self.htmlTopMenu).xpath(
			"//*[@class='menu-level1-container' and position()={posLevel1}]//*[{}]/*[@class='menu-level2-btn']//strong/text()"
			.format(GenerateConfigTopMenuPC.matchClassXpath(
				"menu-level2-container"),
					posLevel1=indexLevel1 + 1))

	def getLevel2Links(self, indexLevel1):
		return etree.HTML(self.htmlTopMenu).xpath(
			"//*[@class='menu-level1-container' and position()={posLevel1}]//*[{}]/*[@class='menu-level2-btn']/a/@href"
			.format(GenerateConfigTopMenuPC.matchClassXpath(
				"menu-level2-container"),
					posLevel1=indexLevel1 + 1))

	def getColSm(self, indexLevel1, indexLevel2):
		strColSm = str(
			etree.HTML(self.htmlTopMenu).xpath(
				"substring-after(//*[@class='menu-level1-container' and position()={posLevel1}]//*[{0} and position()={posLevel2}]//*[@class='form-row' and position()=1]/*[contains(@class, 'col-sm-') and position()=1]/@class, 'col-sm-')"
				.format(GenerateConfigTopMenuPC.matchClassXpath(
					"menu-level2-container"),
						posLevel1=indexLevel1 + 1,
						posLevel2=indexLevel2 + 1)))
		return int(strColSm) if len(strColSm) > 0 else 0

	def getHType(self, indexLevel1, indexLevel2):
		return str(
			etree.HTML(self.htmlTopMenu).xpath(
				"substring-after(//*[@class='menu-level1-container' and position()={posLevel1}]//*[{0} and position()={posLevel2}]//*[@class='form-row' and position()=1]/*[contains(@class, 'col-sm-') and position()=1]/*[contains(@class, 'headercard-blue-box h-') and position()=1]/@class, 'headercard-blue-box h-')"
				.format(GenerateConfigTopMenuPC.matchClassXpath(
					"menu-level2-container"),
						posLevel1=indexLevel1 + 1,
						posLevel2=indexLevel2 + 1)))

	def getIsDefault(self, indexLevel1, indexLevel2):
		return "default" in list(
			str(
				etree.HTML(self.htmlTopMenu).xpath(
					"//*[@class='menu-level1-container' and position()={posLevel1}]//*[{} and position()={posLevel2}]/@class"
					.format(GenerateConfigTopMenuPC.matchClassXpath("menu-level2-container"),
							posLevel1=indexLevel1 + 1,
							posLevel2=indexLevel2 + 1))[0]).split(" "))

	def getLengthLevel2FormRow(self, indexLevel1, indexLevel2):
		return len(
			etree.HTML(self.htmlTopMenu).xpath(
				"//*[@class='menu-level1-container' and position()={posLevel1}]//*[{} and position()={posLevel2}]//*[@class='form-row']"
				.format(GenerateConfigTopMenuPC.matchClassXpath(
					"menu-level2-container"),
						posLevel1=indexLevel1 + 1,
						posLevel2=indexLevel2 + 1)))

	def getLengthLevel2Col(self, indexLevel1, indexLevel2, indexFormRow):
		return len(
			etree.HTML(self.htmlTopMenu).xpath(
				"//*[@class='menu-level1-container' and position()={posLevel1}]//*[{0} and position()={posLevel2}]//*[@class='form-row' and position()={posFormRow}]/*[contains(@class, 'col-sm-')]"
				.format(GenerateConfigTopMenuPC.matchClassXpath(
					"menu-level2-container"),
						posLevel1=indexLevel1 + 1,
						posLevel2=indexLevel2 + 1,
						posFormRow=indexFormRow + 1)))

	def getHeaderCardTexts(self, indexLevel1, indexLevel2, indexFormRow,
						   indexLevel2Col):
		return etree.HTML(self.htmlTopMenu).xpath(
			"//*[@class='menu-level1-container' and position()={posLevel1}]//*[{0} and position()={posLevel2}]//*[@class='form-row' and position()={posFormRow}]/*[contains(@class, 'col-sm-') and position()={posLevel2Col}]//*[{1}]/a/text()"
			.format(GenerateConfigTopMenuPC.matchClassXpath(
				"menu-level2-container"),
					GenerateConfigTopMenuPC.matchClassXpath("mult-link"),
					posLevel1=indexLevel1 + 1,
					posLevel2=indexLevel2 + 1,
					posFormRow=indexFormRow + 1,
					posLevel2Col=indexLevel2Col + 1))

	def getHeaderCardLinks(self, indexLevel1, indexLevel2, indexFormRow,
						   indexLevel2Col):
		return etree.HTML(self.htmlTopMenu).xpath(
			"//*[@class='menu-level1-container' and position()={posLevel1}]//*[{0} and position()={posLevel2}]//*[@class='form-row' and position()={posFormRow}]/*[contains(@class, 'col-sm-') and position()={posLevel2Col}]//*[{1}]/a/@href"
			.format(GenerateConfigTopMenuPC.matchClassXpath(
				"menu-level2-container"),
					GenerateConfigTopMenuPC.matchClassXpath("mult-link"),
					posLevel1=indexLevel1 + 1,
					posLevel2=indexLevel2 + 1,
					posFormRow=indexFormRow + 1,
					posLevel2Col=indexLevel2Col + 1))

	def generateLogo(self):
		logoText = etree.HTML(
			self.htmlTopMenu).xpath("//*[@class='menu-logo']/@title")[0]
		logoLink = etree.HTML(
			self.htmlTopMenu).xpath("//*[@class='menu-logo']/@href")[0]
		return {"text": logoText, "link": logoLink}

	def generateLevel1s(self):
		level1s = []
		level1Texts = self.getLevel1Texts()
		level1Links = self.getLevel1Links()
		level1Tuples = zip(level1Texts, level1Links)

		for indexLevel1, level1Tuple in enumerate(level1Tuples):
			level1 = {
				"text": level1Tuple[0],
				"link": level1Tuple[1],
				"level2s": []
			}

			level2Texts = self.getLevel2Texts(indexLevel1)
			level2Links = self.getLevel2Links(indexLevel1)
			level2Tuples = zip(level2Texts, level2Links)

			for indexLevel2, level2Tuple in enumerate(level2Tuples):
				colSm = self.getColSm(indexLevel1, indexLevel2)
				hType = self.getHType(indexLevel1, indexLevel2)
				isDefault = self.getIsDefault(indexLevel1, indexLevel2)

				level2 = {
					"text": level2Tuple[0],
					"link": level2Tuple[1],
					"isDefault": isDefault,
					"colSm": colSm,
					"hType": hType,
					"headerCards": []
				}

				lengthLevel2FormRow = self.getLengthLevel2FormRow(indexLevel1, indexLevel2)

				for indexFormRow in range(lengthLevel2FormRow):
					lengthLevel2Col = self.getLengthLevel2Col(indexLevel1, indexLevel2, indexFormRow)

					for indexLevel2Col in range(lengthLevel2Col):
						level2Col = []
						headerCardTexts = self.getHeaderCardTexts(indexLevel1, indexLevel2, indexFormRow, indexLevel2Col)
						headerCardLinks = self.getHeaderCardLinks(indexLevel1, indexLevel2, indexFormRow, indexLevel2Col)
						headerCardTuples = zip(headerCardTexts, headerCardLinks)

						for headerCardTuple in headerCardTuples:
							headerCard = {
								"text": headerCardTuple[0],
                            	"link": headerCardTuple[1]
							}

							level2Col.append(headerCard)

						level2["headerCards"].append(level2Col)

				level1["level2s"].append(level2)

			level1s.append(level1)

		return level1s

	def generateConfigTopMenu(self):
		configTopMenu = {}
		configTopMenu["logo"] = self.generateLogo()
		configTopMenu["level1s"] = self.generateLevel1s()
		return configTopMenu

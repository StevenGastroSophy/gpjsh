# -*- coding: utf-8 -*-
"""
.. 以 getTemp為開頭的 method: 傳入字串、 Html或數字，回傳 Html。

.. 以 generate為開頭的 method: 傳入資料，回傳 Html。

.. 

.. 

.. 

.. 

.. 

.. bg-blue-box-headercard似乎是多餘的 class? 因為選單的圖片已經沒在用背景了，且這個 class拿掉前後呈現的效果完全一樣。

.. author:: Steven Chen 2019.12.17

"""

class GenerateTopMenuPC:
		def __init__(self, configTopMenu):
				self.configTopMenu = configTopMenu

		@staticmethod
		def getTempHeaderLink(text, link, index):
				# 當 headerCard要水平排列, 且此 title為第 1個
				if (index == 0):
						return """
			<a href="{link}" class="header-link-title">{text}</a>
			""".format(link=link, text=text)
				# 當 headerCard要水平排列, 且此 title非第 1個
				elif (index > 0):
						return """
			<a href="{link}" class="header-link-text">{text}</a>
			""".format(link=link, text=text)

		@staticmethod
		def getTempSingleTitle(text, link):
				# 當 headerCard要垂直排列
				return """
		<a href="{link}" class="header-single-title">{text}</a>
		""".format(link=link, text=text)

		@staticmethod
		def getTempHeaderCardBlueBox(headerLinks):
				# 當 level2要水平排列
				return """
		<div class="headercard-blue-box">
				<div class="mult-link header-link-card">
						{headerLinks}
				</div>
		</div>
		""".format(headerLinks=headerLinks)
#郵輪 only multi-link h-col4且 header-single-title -> 垂直排列的呈現方式
#h-coln要挖空
		@staticmethod
		def getTempHeaderCardBlueBoxVertical(headerSingleTitle, hType=""):
				# 當 headerCard要垂直排列
				return """
		<div class="headercard-blue-box h-{hType}">
				<div class="mult-link">
						{headerSingleTitle}
				</div>
		</div>
		""".format(hType=hType, headerSingleTitle=headerSingleTitle)

		@staticmethod
		def getTempHeaderCard(headerCardBlueBox, colSm=3):
				return """
		<div class="col-sm-{colSm}">
				{headerCardBlueBox}
		</div>
		""".format(colSm=colSm, headerCardBlueBox=headerCardBlueBox)

		@staticmethod
		def getTempFormRow(headerCards):
				# 每個 formRow能夠容納最多 4個 headerCard
				return """
		<div class="form-row">
				{headerCards}
		</div>
		""".format(headerCards=headerCards)

		@staticmethod
		def getTempLevel2Btn(text, link, isAngle):
				# 若level2為多層選單，要顯示向右箭頭
				tempAngle = """
		<i class="fa fa-angle-right"></i>
		""" if (isAngle) else ""
				return """
		<div class="menu-level2-btn">
				<a href="{link}" class="menu-level2-btn-bubble">
						<strong>{text}</strong>
						{tempAngle}
				</a>
		</div>
		""".format(link=link, text=text, tempAngle=tempAngle)

		@staticmethod
		def getTempLevel2Info(formRows):
				return """
		<div class="menu-level2-info">
				<div class="menu-content">
						{formRows}
				</div>
		</div>
		""".format(formRows=formRows)

		@staticmethod
		def getLevel2Container(level2Info, level2BtnAngle, isDefault):
				# 當level2為多層選單，判斷是否為預設選項
				defaultClassName = " default" if (isDefault) else ""
				return """
		<li class="menu-level2-container{defaultClassName}">
				{level2Info}
				{level2BtnAngle}
		</li>
		""".format(defaultClassName=defaultClassName, level2Info=level2Info, level2BtnAngle=level2BtnAngle)

		@staticmethod
		def getLevel2ContainerTextOnly(level2Btn):
				# 當level2為單層選單
				return """
		<li class="menu-level2-container">
				{level2Btn}
		</li>
		""".format(level2Btn=level2Btn)

		@staticmethod
		def getLevel2(level2Containers, isNested):
				className = "min-h" if (isNested) else "textonly"
				return """
		<ul class="menu-level2 {className}">
				{level2Containers}
		</ul>
		""".format(className=className, level2Containers=level2Containers)

		@staticmethod
		def getTempLevel1Container(text, link, level2=""):
				return """
		<li class="menu-level1-container">
				<!-- 選單列 icon -->
				<a href="{link}" class="menu-level1-btn hover-blue-bg-box">
						<i class="nav-icon hover-blue-bg"></i>
						{text}
				</a>
				{level2}
		</li>
		""".format(link=link, text=text, level2=level2)

		@staticmethod
		def getTempLevel1(level1Containers):
				return """
		<ul class="menu-level1">
				{level1Containers}
		</ul>
		""".format(level1Containers=level1Containers)

		@staticmethod
		def getTempLogo(text, link):
				return """
		<a href="{link}" title="{text}" alt="{text}" class="menu-logo"></a>
		""".format(link=link, text=text)

		@staticmethod
		def getTempHeaderSocialMedia():
				return """
		<ul class="header-social-media">
				<li>
						<a href="https://www.facebook.com/i.set.tour/" alt="東南旅遊Facebook" title="東南旅遊Facebook">
								<div class="facebook-icon"></div>
						</a>
				</li>
				<li>
						<a href="https://line.me/R/ti/p/%40uws4908x" alt="東南旅遊LINE@好友" title="東南旅遊LINE@好友">
								<div class="line-icon"></div>
						</a>
				</li>
				<li>
						<a href="https://www.instagram.com/settour/?hl=zh-tw" alt="東南旅遊Instagram" title="東南旅遊Instagram">
								<div class="instagram-icon"></div>
						</a>
				</li>
				<li>
						<a href="https://www.youtube.com/user/settour0401" alt="東南旅遊Youtube頻道" title="東南旅遊Youtube頻道">
								<div class="youtube-icon"></div>
						</a>
				</li>
		</ul>
		"""

		@staticmethod
		def getTempTopMenu(level1, headerSocialMedia, logo):
				return """
		<div class="container hidden-sm hidden-xs">
				<div class="row">
						<div class="col-sm-12 header-nopd">
								<div class="menu">
										<div class="put-left">
												{logo}
										</div>
										<div class="mid">
												{level1}
										</div>
										<div class="put-right">
												{headerSocialMedia}
										</div>
								</div>
						</div>
				</div>
		</div>
		""".format(logo=logo, level1=level1, headerSocialMedia=headerSocialMedia)

		@staticmethod
		def generateHeaderCard(headerLinks, colSm):
				listHeaderLink = []
				for i, headerLink in enumerate(headerLinks):
						text = headerLink.get("text")
						link = headerLink.get("link")
						htmlHeaderLink = GenerateTopMenuPC.getTempHeaderLink(
								text, link, i)
						listHeaderLink.append(htmlHeaderLink)
				htmlHeaderLinks = "".join(listHeaderLink)
				htmlHeaderCardBlueBox = GenerateTopMenuPC.getTempHeaderCardBlueBox(
						htmlHeaderLinks)
				return GenerateTopMenuPC.getTempHeaderCard(htmlHeaderCardBlueBox, colSm)

		@staticmethod
		def generateHeaderCardVertical(headerSingleTitles, colSm, hType):
				listHeaderCardBlueBoxVertical = []
				for headerSingleTitle in headerSingleTitles:
						text = headerSingleTitle.get("text")
						link = headerSingleTitle.get("link")
						htmlHeaderSingleTitle = GenerateTopMenuPC.getTempSingleTitle(
								text, link)
						htmlHeaderCardBlueBoxVertical = GenerateTopMenuPC.getTempHeaderCardBlueBoxVertical(
								htmlHeaderSingleTitle, hType)
						listHeaderCardBlueBoxVertical.append(htmlHeaderCardBlueBoxVertical)
				htmlHeaderCardBlueBoxVerticals = "".join(listHeaderCardBlueBoxVertical)
				return GenerateTopMenuPC.getTempHeaderCard(htmlHeaderCardBlueBoxVerticals, colSm)

		@staticmethod
		def generateFormRow(headerCards, colSm=3, hType="", step=4):
				#用 hType的有無來判斷是垂直還是水平排列
				if (len(hType) > 0):
						headerSingleTitles = headerCards[0]
						htmlHeaderCardVertical = GenerateTopMenuPC.generateHeaderCardVertical(
								headerSingleTitles, colSm, hType)
						return GenerateTopMenuPC.getTempFormRow(htmlHeaderCardVertical)
				elif (len(hType) == 0):
						listFormRow = []
						listHeaderCard = []
						for headerCard in headerCards:
								htmlHeaderCard = GenerateTopMenuPC.generateHeaderCard(
										headerCard, colSm)
								listHeaderCard.append(htmlHeaderCard)

						# 每個 formRow能夠容納最多 4個 headerCard
						listHeaderCardSplitted = [listHeaderCard[i:i+step]
																			for i in range(0, len(listHeaderCard), step)]
						for splitted in listHeaderCardSplitted:
								htmlFormRow = GenerateTopMenuPC.getTempFormRow(
										"".join(splitted))
								listFormRow.append(htmlFormRow)

						return "".join(listFormRow)

		@staticmethod
		def generateLevel2Container(level2):
				level2IsDefault = level2.get("isDefault")
				level2Text = level2.get("text")
				level2Link = level2.get("link")
				headerCards = level2.get("headerCards")
				colSm = level2.get("colSm")
				hType = level2.get("hType")

				htmlFormRow = GenerateTopMenuPC.generateFormRow(headerCards, colSm, hType, 4)
				htmlLevel2Info = GenerateTopMenuPC.getTempLevel2Info(htmlFormRow)
				htmlLevel2BtnAngle = GenerateTopMenuPC.getTempLevel2Btn(
						level2Text, level2Link, True)

				return GenerateTopMenuPC.getLevel2Container(htmlLevel2Info, htmlLevel2BtnAngle, level2IsDefault)

		@staticmethod
		def generateLevel2ContainerTextOnly(level2):
				level2Text = level2.get("text")
				level2Link = level2.get("link")

				htmlLevel2Btn = GenerateTopMenuPC.getTempLevel2Btn(
						level2Text, level2Link, False)

				return GenerateTopMenuPC.getLevel2ContainerTextOnly(htmlLevel2Btn)

		@staticmethod
		def generateLevel2(level2s):
				listLevel2Container = []
				# 判斷level2是否為多層選單
				isMultiHeaderCard = all(
						[True if (len(level2.get("headerCards")) > 0) else False for level2 in level2s])

				# 當level2為多層選單
				if (isMultiHeaderCard):
						for level2 in level2s:
								htmlLevel2Container = GenerateTopMenuPC.generateLevel2Container(
										level2)
								listLevel2Container.append(htmlLevel2Container)

						htmlLevel2Containers = "".join(listLevel2Container)
						return GenerateTopMenuPC.getLevel2(htmlLevel2Containers, True)
				# 當level2為單層選單
				else:
						for level2 in level2s:
								htmlLevel2ContainerTextOnly = GenerateTopMenuPC.generateLevel2ContainerTextOnly(
										level2)
								listLevel2Container.append(htmlLevel2ContainerTextOnly)

						htmlLevel2ContainerTextOnlys = "".join(listLevel2Container)
						return GenerateTopMenuPC.getLevel2(htmlLevel2ContainerTextOnlys, False)

		@staticmethod
		def generateLevel1(level1s):
				listLevel1Container = []
				for level1 in level1s:
						level1Text = level1.get("text")
						level1Link = level1.get("link")
						level2s = level1.get("level2s")
						htmlLevel1Container = ""

						if (len(level2s) > 0):
								htmlLevel2 = GenerateTopMenuPC.generateLevel2(level2s)
								htmlLevel1Container = GenerateTopMenuPC.getTempLevel1Container(
										level1Text, level1Link, htmlLevel2)
						else:
								htmlLevel1Container = GenerateTopMenuPC.getTempLevel1Container(
										level1Text, level1Link, "")
						listLevel1Container.append(htmlLevel1Container)

				htmlLevel1Containers = "".join(listLevel1Container)
				return GenerateTopMenuPC.getTempLevel1(htmlLevel1Containers)

		def generateTopMenu(self):
				configLogo = self.configTopMenu.get("logo")
				level1s = self.configTopMenu.get("level1s")
				htmlLogo = GenerateTopMenuPC.getTempLogo(
						configLogo.get("text"), configLogo.get("link"))
				htmlHeaderSocialMedia = GenerateTopMenuPC.getTempHeaderSocialMedia()
				htmlLevel1 = GenerateTopMenuPC.generateLevel1(level1s)
				return GenerateTopMenuPC.getTempTopMenu(htmlLevel1, htmlHeaderSocialMedia, htmlLogo)

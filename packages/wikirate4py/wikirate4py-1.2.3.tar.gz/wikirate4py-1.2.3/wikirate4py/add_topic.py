import wikirate4py

topics = ["UNGP 16", "UNGPRF A2", "CHRB A.2.1", "KTC 2.1", "ISO 30414 4.7.5", "OECD Principle 2", "PRI Principle 1",
          "UNGP 12", "UNGP 15", "UNGPRF A1", "UNGPRF C1", "GRI 106", "GRI 408: Child Labour", "DJSI 3.3.1",
          "CHRB A.1.1", "CHRB D.1.5/D.2.5", "CWC 1.2", "CWC 1.2.1", "CWC 4.2", "KTC 2.2", "SDG 8.7", "SDG 16.2",
          "ILO 105", "ILO 29", "SFDR Social metrics", "OECD Principle 4", "OECD Principle 5", "PRI Principle 3",
          "UNGC 1", "UNGC 4", "WBA CSI 1", "WBA CSI 2", "UNGP 17", "UNGP 18", "UNGPRF C6", "DJSI 3.3.2", "CHRB B.2.1",
          "CHRB B.2.2", "CHRB B.1.3/B.2.3", "KTC 5.1", "ETI RF B4.2", "ISO26000 Clause 6.3.3", "UNDHR Article 4",
          "GRI 409: Forced or Compulsory Labor", "ISO 30414 4.7.12", "CWC 1.1", "CWC 1.1.1", "CWC 1.1.3", "CWC 1.5",
          "WBA CSI 13", "DJSI 3.5.6", "WGEA Question 1", "UNDHR Article 25", "ILO 111", "UNGC 6",
          "ISO26000 Clause 6.3.7", "UNDHR Article 2", "UNDHR Article 7", "UNDHR Article 23", "UNGP 21",
          "GRI 406: Non-discrimination", "CHRB D.1.1a/D.2.1a/D.3.1", "CHRB D.1.1b/D.2.1b", "CWC 6.1", "SDG 8.5",
          "SDG 10.4", "GRI 404: Training and Education", "SDG 5.1", "SDG 5.5", "SFDR Social Metrics",
          "GRI 404: Training and Education", "GRI 405: Diversity and Equal Opportunity", "CWC 4.7.1", "SDG 16.7",
          "CHRB D.1.7.a/D.2.7a", "CWC 5.1", "CWC 5.4", "CWC 5.4.1", "ISO 30414 4.7.7", "CHRB D.1.7.b/D.2.7.b",
          "CWC 5.4.2", "UNGP 13", "UNGP 19", "DJSI 3.2.6", "CWC 2.1", "WBA CSI 12", "SDG 8.8", "CHRB C.1", "CWC 7.3",
          "WBA CSI 8", "ISO26000 Clause 6.3.1", "UNGP 31", "ISO 30414 4.7.2", "CHRB D.1.3", "CWC 4.1", "CWC 4.1.2",
          "KTC 4.2", "CHRB B.1.4B", "CHRB B.1.7", "CWC 4.5", "UNGPRF A1.3", "DJSI 3.6.1", "CWC 4.3", "KTC 1.2",
          "SDG 10.6", "ETI RF B1.1", "ETI RF B3.2", "KTC 9.1"]

api = wikirate4py.API('ThessaloWikiRate')
for topic in topics:
    try:
        topic = api.add_topic(topic)
        print(topic)
    except Exception as ex:
        print(ex.__str__())
